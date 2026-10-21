#!/usr/bin/env python3
"""Independent F2 ideal-membership checker. Python standard library only.
Does not import or execute the witness-search implementation.
Hex format: semicolon-separated polynomials; eight hex digits per monomial,
one nonnegative exponent per variable, in the declared variable order.
"""
import argparse
from collections import Counter
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re

VARIABLES = ['x', 'y', 'alpha', 'gamma', 'w4', 'w5', 'w6', 'Theta']
WEIGHTS = [1, 1, 2, 3, 4, 5, 6, 6]
EXPECTED_HASHES = {
    'groebner_supports.hex': '550dfeb94726e42de31395b90b51da3018955025d2a75881ca5270383fe1de6d',
    'relations.json': '130743859b2e3b2d18642811c8615bea74212187a3da722cb8bdeb5e86703103',
}

class InvalidCertificate(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise InvalidCertificate(message)

def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate JSON key: ' + key)
        result[key] = value
    return result

def load_json(raw):
    return json.loads(raw, object_pairs_hook=no_duplicate_keys)

def degree(m):
    return sum(a * w for a, w in zip(m, WEIGHTS))

def parity(terms):
    return frozenset(m for m, count in Counter(terms).items() if count % 2)

def parse_relation(expression):
    require(isinstance(expression, str) and expression.strip(), 'empty relation')
    monomials = []
    for summand in expression.split('+'):
        powers = [0] * 8
        for factor in summand.strip().split('*'):
            factor = factor.strip()
            if factor == '1':
                continue
            match = re.fullmatch(r'([A-Za-z][A-Za-z0-9]*)(?:\^([0-9]+))?', factor)
            require(match is not None, 'invalid relation token: ' + factor)
            name, exponent = match.groups()
            require(name in VARIABLES, 'unknown variable: ' + name)
            powers[VARIABLES.index(name)] += int(exponent) if exponent else 1
        monomials.append(tuple(powers))
    return parity(monomials)

def parse_targets(raw):
    text = raw.decode('ascii').strip()
    chunks = text.split(';')
    require(len(chunks) == 46, 'target population must be 46')
    result = []
    for index, chunk in enumerate(chunks):
        require(re.fullmatch('[0-9a-fA-F]+', chunk) is not None and len(chunk) % 8 == 0,
                f'invalid hex encoding at target {index}')
        terms = [tuple(int(c, 16) for c in chunk[i:i+8]) for i in range(0, len(chunk), 8)]
        require(len(set(terms)) == len(terms), f'duplicate encoded support at target {index}')
        result.append(frozenset(terms))
    require(len(set(result)) == 46, 'duplicate target polynomials')
    return result

def verify(certificate, raw_inputs, trusted_hashes=None, verbose=False):
    trusted_hashes = EXPECTED_HASHES if trusted_hashes is None else trusted_hashes
    require(certificate['field'] == 'F2', 'wrong field')
    require(certificate['variables'] == VARIABLES, 'wrong certificate variable order')
    require(certificate['weights'] == WEIGHTS, 'wrong certificate weights')
    require(certificate['relation_order'] == 'relations_by_degree JSON insertion order, then array order', 'wrong relation ordering declaration')
    require(certificate['input_sha256'] == trusted_hashes, 'certificate hash manifest mismatch')
    for name, digest in trusted_hashes.items():
        require(sha256(raw_inputs[name]).hexdigest() == digest, 'input hash mismatch: ' + name)
    relation_data = load_json(raw_inputs['relations.json'])
    require(relation_data['variables'] == VARIABLES, 'wrong input variable order')
    require(relation_data['variable_degrees'] == WEIGHTS, 'wrong input weights')
    require(relation_data['number_minimal_homogeneous_relations'] == 9, 'wrong relation count metadata')
    relations, relation_degrees = [], []
    for key, expressions in relation_data['relations_by_degree'].items():
        require(re.fullmatch('[0-9]+', key) is not None and isinstance(expressions, list), 'invalid relation group')
        d = int(key)
        for expression in expressions:
            relation = parse_relation(expression)
            require(relation and {degree(m) for m in relation} == {d}, 'inhomogeneous or zero relation')
            relations.append(relation)
            relation_degrees.append(d)
    require(len(relations) == 9, 'relation population must be 9')
    targets = parse_targets(raw_inputs['groebner_supports.hex'])
    witnesses = certificate['witnesses']
    require(isinstance(witnesses, list) and len(witnesses) == 46, 'witness population must be 46')
    seen, term_count, expansion_count = set(), 0, 0
    for witness in witnesses:
        i, d, terms = witness['target_index'], witness['weighted_degree'], witness['terms']
        require(type(i) is int and 0 <= i < 46 and i not in seen, 'invalid or duplicate target index')
        seen.add(i)
        require(type(d) is int and d >= 0, 'invalid target degree')
        require({degree(m) for m in targets[i]} == {d}, f'inhomogeneous target {i}')
        require(isinstance(terms, list) and terms, 'empty witness terms')
        expanded = Counter()
        for term in terms:
            r, multiplier = term['relation_index'], term['multiplier_exponents']
            require(type(r) is int and 0 <= r < 9, 'invalid relation index')
            require(isinstance(multiplier, list) and len(multiplier) == 8 and
                    all(type(n) is int and n >= 0 for n in multiplier), 'invalid multiplier exponents')
            require(degree(multiplier) + relation_degrees[r] == d, f'inhomogeneous witness term for target {i}')
            for monomial in relations[r]:
                expanded[tuple(a+b for a, b in zip(multiplier, monomial))] += 1
                expansion_count += 1
            term_count += 1
        actual = frozenset(m for m, count in expanded.items() if count % 2)
        require(actual == targets[i], f'exact polynomial equality failed at target {i}; symmetric difference has {len(actual ^ targets[i])} terms')
        if verbose:
            print(f'PASS target {i:02d}: degree={d}, witness_terms={len(terms)}, support={len(actual)}')
    require(seen == set(range(46)), 'target index coverage incomplete')
    return {'equalities': len(seen), 'relations': len(relations), 'witness_terms': term_count,
            'expanded_monomials_before_cancellation': expansion_count,
            'target_degree_min': min(degree(next(iter(p))) for p in targets),
            'target_degree_max': max(degree(next(iter(p))) for p in targets)}

def negative_tests(original, raw):
    tests = []
    def reject(label, mutate, refresh=False):
        cert, data = deepcopy(original), dict(raw)
        mutate(cert, data)
        hashes = EXPECTED_HASHES
        if refresh:
            hashes = {name: sha256(value).hexdigest() for name, value in data.items()}
            cert['input_sha256'] = hashes.copy()
        try:
            verify(cert, data, hashes)
        except (InvalidCertificate, ValueError, KeyError, TypeError) as error:
            print(f'PASS negative {label}: rejected ({error})')
            tests.append(label)
        else:
            raise RuntimeError('negative test wrongly accepted: ' + label)
    reject('changed input bytes / hash', lambda c, d: d.__setitem__('relations.json', d['relations.json'] + b' '))
    reject('changed certificate hash', lambda c, d: c['input_sha256'].__setitem__('relations.json', '0'*64))
    reject('missing witness', lambda c, d: c['witnesses'].pop())
    reject('duplicate target index', lambda c, d: c['witnesses'][1].__setitem__('target_index', 0))
    reject('out of range relation', lambda c, d: c['witnesses'][0]['terms'][0].__setitem__('relation_index', 9))
    reject('negative exponent', lambda c, d: c['witnesses'][0]['terms'][0]['multiplier_exponents'].__setitem__(0, -1))
    reject('incorrect multiplier dimension', lambda c, d: c['witnesses'][0]['terms'][0]['multiplier_exponents'].pop())
    reject('incorrect degree', lambda c, d: c['witnesses'][0].__setitem__('weighted_degree', 5))
    reject('same degree wrong relation / equality', lambda c, d: c['witnesses'][0]['terms'][0].__setitem__('relation_index', 2))
    reject('drop nontrivial witness term / equality', lambda c, d: c['witnesses'][2]['terms'].pop())
    reject('same degree changed target / equality', lambda c, d: d.__setitem__('groebner_supports.hex', d['groebner_supports.hex'].replace(b'01010000', b'10010000', 1)), True)
    reject('same degree changed relation / equality', lambda c, d: d.__setitem__('relations.json', d['relations.json'].replace(b'y*gamma', b'x*gamma', 1)), True)
    reject('inhomogeneous input relation', lambda c, d: d.__setitem__('relations.json', d['relations.json'].replace(b'y*gamma', b'y*alpha', 1)), True)
    reject('malformed hex input', lambda c, d: d.__setitem__('groebner_supports.hex', b'Z' + d['groebner_supports.hex'][1:]), True)
    reject('duplicate JSON key', lambda c, d: d.__setitem__('relations.json', d['relations.json'].replace(b'{', b'{"variables": [],', 1)), True)
    return len(tests)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    root = args.directory
    cert_raw = (root / 'membership_witness.json').read_bytes()
    certificate = load_json(cert_raw)
    inputs = {name: (root/'inputs'/name).read_bytes() for name in EXPECTED_HASHES}
    print('Independent standard-library direct expansion / Counter parity verification')
    print('Witness SHA256:', sha256(cert_raw).hexdigest())
    for name, digest in EXPECTED_HASHES.items():
        print('Frozen input SHA256:', name, digest)
    result = verify(certificate, inputs, verbose=True)
    print('SUMMARY:', json.dumps(result, sort_keys=True))
    print('NEGATIVE TESTS PASSED:', negative_tests(certificate, inputs))
    # Ensure in-memory mutations did not alter the originals.
    require((root/'membership_witness.json').read_bytes() == cert_raw, 'original witness changed')
    require(all((root/'inputs'/name).read_bytes() == raw for name, raw in inputs.items()), 'original inputs changed')
    print('PASS original files unchanged; all 46 exact equalities verified.')

if __name__ == '__main__':
    main()
