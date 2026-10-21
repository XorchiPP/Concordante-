#!/usr/bin/env python3
"""Independent exact audit of two-block convolution generators.
No import of the author's verifier, no numerical eigensolver, no third-party packages.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib, json

HERE = Path(__file__).resolve().parent
counts = {}
def check(key, value):
    assert value, key
    counts[key] = counts.get(key, 0) + 1

def rates(n, m, a, b, g):
    M, N = 1 << n, 1 << m
    return {(u,v): (g if u and v else a if u else b)
            for u in range(M) for v in range(N) if u or v}

def connected(n, m, q):
    seen, todo = {(0,0)}, [(0,0)]
    moves = [z for z, value in q.items() if value > 0]
    while todo:
        x, y = todo.pop()
        for u, v in moves:
            z = x ^ u, y ^ v
            if z not in seen:
                seen.add(z); todo.append(z)
    return len(seen) == (1 << (n+m))

def char(a, x):
    return -1 if (a & x).bit_count() % 2 else 1

# Generate from the definition, not from the proposed c,d,theta parameterization.
# All 4^3 invariant nonnegative rate triples for each 1 <= n,m <= 3.
for n, m in product(range(1,4), repeat=2):
    M, N = 1 << n, 1 << m
    for a, b, g in product(map(F, range(4)), repeat=3):
        q = rates(n,m,a,b,g)
        c = M*(a+(N-1)*g)
        d = N*(b+(M-1)*g)
        theta = M*N*g
        check('parameter_recovery', a == (c*N-theta*(N-1))/(M*N)
              and b == (d*M-theta*(M-1))/(M*N) and g == theta/(M*N))
        check('finite_positivity_interval', 0 <= theta <= min(c*N/F(N-1),d*M/F(M-1)))
        for u in range(1,M):
            check('first_marginal_rates', sum(q[(u,v)] for v in range(N)) == c/M)
        for v in range(1,N):
            check('second_marginal_rates', sum(q[(u,v)] for u in range(M)) == d/N)
        for p, r in product(range(M), range(N)):
            eigenvalue = sum(value*(char(p,u)*char(r,v)-1) for (u,v), value in q.items())
            predicted = -(c+d-theta) if p and r else -c if p else -d if r else F(0)
            check('fourier_spectrum', eigenvalue == predicted)
        irreducible = connected(n,m,q)
        check('irreducibility_criterion', irreducible == (c > 0 and d > 0 and theta < c+d))
        check('unique_positive_marginal_exception',
              (c > 0 and d > 0 and not irreducible) ==
              (M == N == 2 and c == d and c > 0 and theta == 2*c))

# Enumerate every surjective linear map F_2^n -> F_2^k for 1 <= k <= n <= 3.
def apply_linear(columns, x):
    y = 0
    for i, column in enumerate(columns):
        if (x >> i) & 1:
            y ^= column
    return y

maps = []
for n in range(1,4):
    for k in range(1,n+1):
        for cols in product(range(1<<k), repeat=n):
            images = [apply_linear(cols,x) for x in range(1<<n)]
            if len(set(images)) == 1<<k:
                maps.append((n,k,images))
check('single_block_surjection_count', len(maps) == 227)
quotients = 0
for first, second in product(maps, repeat=2):
    n,k,p = first; m,l,r = second
    M,N,K,H = 1<<n,1<<m,1<<k,1<<l
    for c,d,theta in ((2,3,0),(2,3,1),(2,3,2)):
        # Rates are integers divided by MN. Sum integer numerators directly.
        a = c*N-theta*(N-1); b = d*M-theta*(M-1); g=theta
        push = {(u,v): 0 for u in range(K) for v in range(H) if u or v}
        for u,v in product(range(M),range(N)):
            target=p[u],r[v]
            if target != (0,0):
                push[target] += g if u and v else a if u else b
        for (u,v), value in push.items():
            expected = theta if u and v else c*H-theta*(H-1) if u else d*K-theta*(K-1)
            check('separated_quotient_rate_identity', value*K*H == expected*M*N)
        quotients += 1
check('paired_surjections_count', len(maps)**2 == 51529)

# Decisive finite excess: connected binary coupling, not extendible to (1,2).
c=d=F(1); theta=F(3,2)
a=b=F(1,8); g=F(3,8)
q=rates(1,1,a,b,g)
check('finite_excess_valid_and_irreducible', connected(1,1,q) and theta > min(c,d))
check('finite_excess_marginals', a+g == c/2 and b+g == d/2)
lift_a=(c*4-theta*3)/(2*4)
check('finite_excess_lift_negative', lift_a == F(-1,16))
# Maximal finite boundary can stay irreducible once a block has dimension >= 2.
check('finite_joint_only_higher_dim_irreducible', connected(2,2,rates(2,2,F(0),F(0),F(1,12))))
check('binary_joint_only_reducible', not connected(1,1,rates(1,1,F(0),F(0),F(1,2))))

out={
    'status':'PASS',
    'arithmetic':'Python integers and fractions.Fraction only',
    'rate_triples_tested':9*4**3,
    'dimension_range':'1 <= n,m <= 3',
    'linear_surjections_per_block':len(maps),
    'paired_surjections':len(maps)**2,
    'coherent_parameter_samples':[[2,3,0],[2,3,1],[2,3,2]],
    'quotient_parameter_cases':quotients,
    'checks_by_type':counts,
    'total_assertions':sum(counts.values()),
    'finite_excess':{'n':1,'m':1,'c':'1','d':'1','theta':'3/2',
                    'rates':['1/8','1/8','3/8'],'lift_1_2_axis_rate':'-1/16'},
    'scope':'Finite calculations corroborate the separate symbolic proof; no claim of computational proof in all dimensions.',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(HERE/'audit_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
