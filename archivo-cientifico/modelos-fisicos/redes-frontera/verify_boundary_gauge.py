#!/usr/bin/env python3
"""Exact, standard-library replay of two boundary-realization counterexamples.

No floating point, external calls, external writes, or sampling-based proof.
The general identity is proved in REPORT.md. This file checks its hypotheses
and exact rational consequences for the two displayed networks.
"""
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def scale(a, c):
    return [[c*x for x in row] for row in a]


def sub(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def inv(a):
    n = len(a)
    z = [list(row)+ir for row, ir in zip(a, eye(n))]
    for j in range(n):
        p = next(i for i in range(j, n) if z[i][j])
        z[j], z[p] = z[p], z[j]
        pivot = z[j][j]
        z[j] = [x/pivot for x in z[j]]
        for i in range(n):
            if i != j:
                c = z[i][j]
                z[i] = [x-c*y for x, y in zip(z[i], z[j])]
    return [row[n:] for row in z]


def det(a):
    n = len(a)
    z = [list(row) for row in a]
    result = F(1)
    for j in range(n):
        rows = [i for i in range(j, n) if z[i][j]]
        if not rows:
            return F(0)
        p = rows[0]
        if p != j:
            z[j], z[p] = z[p], z[j]
            result = -result
        pivot = z[j][j]
        result *= pivot
        for i in range(j+1, n):
            c = z[i][j]/pivot
            z[i] = [x-c*y for x, y in zip(z[i], z[j])]
    return result


def diag(values):
    return [[F(values[i]) if i == j else F(0) for j in range(len(values))]
            for i in range(len(values))]


def laplace(n, edges):
    a = [[F(0) for j in range(n)] for i in range(n)]
    for i, j, c in edges:
        c = F(c)
        a[i][i] += c
        a[j][j] += c
        a[i][j] -= c
        a[j][i] -= c
    return a


def transfer(l, m, boundary, s):
    interior = [i for i in range(len(l)) if i not in boundary]
    a = sub(l, boundary, boundary)
    c = sub(l, boundary, interior)
    k = sub(l, interior, interior)
    mi = sub(m, interior, interior)
    return add(a, scale(mm(mm(c, inv(add(k, scale(mi, F(s))))), transpose(c)), -1))


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, list):
        return [serial(x) for x in value]
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    return value


CHECKS = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    CHECKS.append(name)


def certify(name, l, masses, s):
    n = len(l)
    boundary, interior = [0, 1], [2, 3, 4]
    m = diag(masses)
    mi = sub(m, interior, interior)
    t = eye(n)
    for i in range(3):
        for j in range(3):
            t[i+2][j+2] = s[i][j]
    l2 = mm(mm(transpose(t), l), t)
    check(name+': M-isometry', mm(mm(transpose(s), mi), s) == mi)
    check(name+': fixes constant', mm(s, [[F(1)]]*3) == [[F(1)]]*3)
    check(name+': full M-isometry', mm(mm(transpose(t), m), t) == m)
    for label, x in [('A', l), ('B', l2)]:
        check(name+': '+label+' symmetric', x == transpose(x))
        check(name+': '+label+' zero row sums', all(sum(row) == 0 for row in x))
        check(name+': '+label+' complete positive conductances',
              all(x[i][j] < 0 for i in range(n) for j in range(i+1, n)))
    check(name+': networks differ', l != l2)
    check(name+': no vertex permutation identifies networks',
          not any(all(l[i][j] == l2[p[i]][p[j]] for i in range(n) for j in range(n))
                  for p in permutations(range(n))))
    check(name+': boundary principal block identical', sub(l, boundary, boundary) == sub(l2, boundary, boundary))
    q = scale(mm(inv(m), l), -1)
    q2 = scale(mm(inv(m), l2), -1)
    check(name+': generators similar', q2 == mm(mm(inv(t), q), t))
    pi = [[F(x, sum(masses)) for x in masses]]
    check(name+': both stationary measures', mm(pi, q) == mm(pi, q2) == [[F(0)]*n])
    check(name+': detailed balance both',
          all(masses[i]*x[i][j] == masses[j]*x[j][i]
              for x in [q, q2] for i in range(n) for j in range(n)))
    check(name+': same directed rate ratios',
          all(q[i][j]/q[j][i] == q2[i][j]/q2[j][i] == F(masses[j], masses[i])
              for i in range(n) for j in range(i+1, n)))
    activity = -sum(pi[0][i]*q[i][i] for i in range(n))
    activity2 = -sum(pi[0][i]*q2[i][i] for i in range(n))
    check(name+': same stationary activity (extra checked condition)', activity == activity2)
    obs_minors = []
    for label, x in [('A', l), ('B', l2)]:
        c = sub(x, boundary, interior)
        a = mm(inv(mi), sub(x, interior, interior))
        o = c+mm(c, a)+mm(mm(c, a), a)
        minor = det(o[:3])
        check(name+': '+label+' full interior observability', minor != 0)
        obs_minors.append(minor)
    readings = []
    for freq in [F(0), F(1, 3), F(1), F(2), F(11, 7)]:
        r1, r2 = transfer(l, m, boundary, freq), transfer(l2, m, boundary, freq)
        check(name+': exact boundary sample '+str(freq), r1 == r2)
        readings.append({'s': freq, 'transfer': r1})
    power1, power2 = eye(n), eye(n)
    for exponent in range(11):
        check(name+': boundary generator moment '+str(exponent),
              sub(power1, boundary, boundary) == sub(power2, boundary, boundary))
        power1, power2 = mm(power1, q), mm(power2, q2)
    dc1, dc2 = transfer(l, m, [0, 1, 2], 0), transfer(l2, m, [0, 1, 2], 0)
    check(name+': third boundary distinguishes DC', dc1[2][2] != dc2[2][2])
    check(name+': internal impulse distinguishes at first time derivative', q[0][2] != q2[0][2])
    return {'L_A': l, 'L_B': l2, 'M': m, 'S': s, 'T': t,
            'Q_A': q, 'Q_B': q2, 'boundary': boundary, 'interior': interior,
            'stationary_measure': pi[0], 'stationary_activity': activity,
            'observability_minors': obs_minors, 'frequency_checks': readings,
            'third_boundary_DC_current_at_2': [dc1[2][2], dc2[2][2]],
            'third_boundary_DC_difference_A_minus_B': dc1[2][2]-dc2[2][2],
            'internal_impulse_derivative_at_0': [q[0][2], q2[0][2]]}


def main():
    uniform = laplace(5, [(0,1,5),(0,2,6),(0,3,5),(0,4,4),(1,2,4),
                         (1,3,7),(1,4,5),(2,3,5),(2,4,6),(3,4,4)])
    su = scale(mat([[6,-2,3],[-2,3,6],[3,6,-2]]), F(1,7))
    distinct = mat([[38,-2,-14,-4,-18],[-2,26,-6,-8,-10],
                    [-14,-6,48,-12,-16],[-4,-8,-12,44,-20],[-18,-10,-16,-20,64]])
    sd = mat([['3/4','2/3','-5/12'],['1/2','-1/3','5/6'],['-1/4','2/3','7/12']])
    result = {'schema':'concordante-boundary-gauge-exact-v1', 'arithmetic':'Fraction; zero tolerance',
              'primary_distinct_capacities': certify('distinct', distinct, [1,2,3,4,5], sd),
              'secondary_uniform_capacities': certify('uniform', uniform, [1,1,1,1,1], su),
              'scope':'Two exact witnesses. General identities are justified algebraically in REPORT.md.',
              'nonclaims':['No physical gravity.', 'No empirical observation.', 'No universal identification theorem.',
                           'No equality of ordinary Laplacian spectra for distinct capacities.',
                           'No generic preservation of stationary activity by every M-isometry.']}
    result['checks'] = CHECKS
    result['check_count'] = len(CHECKS)
    result['status'] = 'PASS_EXACT_WITNESSES'
    output = Path(__file__).with_name('certificate.json')
    output.write_text(json.dumps(serial(result), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status':result['status'],'check_count':len(CHECKS),'output':output.name}))


if __name__ == '__main__':
    main()
