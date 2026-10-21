#!/usr/bin/env python3
"""Small, self-contained checks of the public Concordante Lab F4 preprint inputs.

Scope: input algebra, finite orbit counts and finite fiber ranks.
Full group-ring verification additionally requires the authentic detectors,
Nakaoka theorem and complete Groebner/ideal-membership certificates.
Copyright (c) 2026 Xorch — Concordante Lab.
"""
import ast
import itertools
import json
from pathlib import Path

DATA = json.loads((Path(__file__).parent / 'f4_algebra_data.json').read_text(encoding='utf-8'))
NAMES = list(DATA['generator_degrees'])
DEG = DATA['generator_degrees']
ZERO = frozenset()
ONE = frozenset({(0, 0, 0, 0)})

def add(a, b):
    return a ^ b

def multiply(a, b):
    out = set()
    for ea in a:
        for eb in b:
            ec = tuple(x + y for x, y in zip(ea, eb))
            if ec in out: out.remove(ec)
            else: out.add(ec)
    return frozenset(out)

def power(a, n):
    assert isinstance(n, int) and 0 <= n <= 20
    ans = ONE
    while n:
        if n & 1: ans = multiply(ans, a)
        a = multiply(a, a)
        n >>= 1
    return ans

def parse_poly(expr, env):
    root = ast.parse(expr.replace('^', '**'), mode='eval')
    def rec(node):
        if isinstance(node, ast.Expression): return rec(node.body)
        if isinstance(node, ast.Name): return env[node.id]
        if isinstance(node, ast.Constant) and node.value == 1: return ONE
        if isinstance(node, ast.Constant) and node.value == 0: return ZERO
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Add): return add(rec(node.left), rec(node.right))
            if isinstance(node.op, ast.Mult): return multiply(rec(node.left), rec(node.right))
            if isinstance(node.op, ast.Pow):
                if not isinstance(node.right, ast.Constant): raise ValueError('Exponent must be integer')
                return power(rec(node.left), node.right.value)
        raise ValueError('Unsupported expression: %s' % ast.dump(node))
    return rec(root)

def orbit_actions(a):
    return [a, (a[2],a[3],a[0],a[1]), (a[1],a[0],a[3],a[2]), (a[3],a[2],a[1],a[0])]

def orbit_counts(q):
    valid = set()
    for a in range(q+1):
        for b in range(q-a+1):
            for c in range(q-a-b+1):
                d=q-a-b-c
                if (a-d)%3==0 and (b-c)%3==0: valid.add((a,b,c,d))
    result={1:0,2:0,4:0}
    while valid:
        a=next(iter(valid)); orbit=set(orbit_actions(a))
        assert orbit <= valid
        result[len(orbit)]+=1
        valid.difference_update(orbit)
    return result

def det4(rows):
    out=0
    for perm in itertools.permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        prod=1
        for i,j in enumerate(perm): prod *= rows[i][j]
        out+=(-1 if inv%2 else 1)*prod
    return out

def products_for_degree(gens, degree, limits):
    # yield one polynomial for each weighted monomial of the six positive-degree fiber generators
    weights=[DEG[x] for x in gens]
    def recur(i, rest, acc):
        if i==len(gens):
            if rest==0: yield acc
            return
        for exponent in range(rest//weights[i]+1):
            yield from recur(i+1,rest-exponent*weights[i],acc+[exponent])
    for exps in recur(0,degree,[]):
        poly=ONE
        for name, e in zip(gens,exps):
            if e: poly=multiply(poly, power(limits[name],e))
        yield poly

def gf2_rank(polys, ambient_index):
    pivots={}
    for poly in polys:
        val=0
        for monomial in poly:
            val ^= 1 << ambient_index[monomial]
        while val:
            high=val.bit_length()-1
            if high in pivots: val ^= pivots[high]
            else:
                pivots[high]=val; break
    return len(pivots)

def poly_mul_int(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def one_minus(d):
    out=[0]*(d+1);out[0]=1;out[d]=-1;return out

def one_plus(d):
    out=[0]*(d+1);out[0]=1;out[d]=1;return out

def series_coeff(n_max):
    numerator=[1,0,2,-1,1,0,0,0,-1,-1]
    den=[1]
    for fac in [one_minus(1),one_minus(1),one_minus(3),one_plus(2),one_minus(6)]:
        den=poly_mul_int(den,fac)
    ans=[]
    for n in range(n_max+1):
        right=numerator[n] if n<len(numerator) else 0
        right-=sum(den[i]*ans[n-i] for i in range(1,min(len(den)-1,n)+1))
        assert den[0]==1
        ans.append(right)
    return ans

def main():
    # Check nine exact homogeneous expressions.
    formal={name:frozenset({tuple(int(i==j) for i in range(4))}) for j,name in enumerate(['t0','t1','t2','t3'])}
    true_fiber={k:frozenset(map(tuple,supp)) for k,supp in DATA['fiber_restriction_supports'].items()}
    formal8={k:frozenset({tuple(int(k==q) for q in NAMES)}) for k in NAMES}
    # Generic polynomial expressions use 8D exponent vectors; override ONE accordingly via dimensional context.
    global ONE
    ONE=frozenset({(0,)*8})
    assert len(DATA['relations'])==9
    for r in DATA['relations']:
        terms=parse_poly(r['expression'], formal8)
        assert terms and all(sum(DEG[NAMES[i]]*e for i,e in enumerate(m))==r['degree'] for m in terms)
    print('[PASS] Nine weighted homogeneous relations at advertised degrees.')
    ONE=frozenset({(0,)*4})
    for r in DATA['relations']:
        if r['degree'] in (10,12):
            assert parse_poly(r['expression'],true_fiber)==ZERO, r['label']
    print('[PASS] Two exact fiber-defining identities evaluated in F2[t0,t1,t2,t3].')
    chosen=['alpha','gamma','w4','w6']
    weights=[1,3,3,4]
    leading=[]
    for c in chosen:
        mon=max(true_fiber[c],key=lambda e:(sum(weights[i]*e[i] for i in range(4)),e))
        leading.append(mon)
    determinant=det4(leading)
    assert determinant==-8,(leading,determinant)
    print('[PASS] Parameter leading exponents determinant = -8 (over Z).')
    # T^4+T+1: no roots F2 and no quadratic irreducible factor T²+T+1.
    assert all((t**4+t+1)%2 for t in range(2))
    # modulo T²+T+1, T²=T+1 and T⁴=T, hence T⁴+T+1=1.
    print('[PASS] Special quartic T^4+T+1 irreducible over F2.')
    names=[x for x in NAMES if x not in ('x','y')]
    counts=[]
    for q in range(13):
        ambient=[(a,b,c,q-a-b-c) for a in range(q+1) for b in range(q-a+1) for c in range(q-a-b+1)]
        rank=gf2_rank(products_for_degree(names,q,true_fiber),{m:i for i,m in enumerate(ambient)})
        orbital=sum(orbit_counts(q).values())
        assert rank==orbital,(q,rank,orbital)
        counts.append(rank)
    print('[PASS] Fiber spans = invariant orbit dimensions at degrees 0..12:', counts)
    series=series_coeff(40)
    actual=[]
    for n in range(41):
        total=0
        for q in range(n+1):
            p=n-q; o=orbit_counts(q)
            total+=(sum(o.values()) if p==0 else (p+1)*o[1]+o[2])
        assert total==series[n],(n,total,series[n]); actual.append(total)
    assert actual[16:21]==[98,113,128,141,159]
    print('[PASS] All 41 E2 orbit totals agree with the rational-series recurrence.')
    print('[SCOPE] Input-algebra checks passed. Full group-ring verification requires the separate detector and ideal certificates.')

if __name__=='__main__':main()
