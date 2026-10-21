#!/usr/bin/env python3
"""Exact bounded checks; stdlib only. No universal claim follows from test counts."""
from fractions import Fraction as F
from itertools import product
from math import prod
import json, sys
from pathlib import Path
N=0

def check(v):
    global N
    N+=1
    assert v, N

def rate(lam,J): return sum((v for S,v in lam.items() if S&J),F(0))
def invert(r,k):
    full=(1<<k)-1
    fun={T:r[full]-r[full^T] for T in range(full+1)}
    return {S:sum(((-1)**(S.bit_count()-T.bit_count())*fun[T] for T in range(full+1) if T&S==T),F(0)) for S in range(1,full+1)}
def support(x): return sum(1<<i for i,a in enumerate(x) if a)
def q(lam,M,z):
    T=support(z)
    return sum((v/F(prod(M[i] for i in range(len(M)) if S>>i&1)) for S,v in lam.items() if T&S==T),F(0)) if T else F(0)
def rates(lam,M): return {z:q(lam,M,z) for z in product(*(range(m) for m in M)) if any(z)}
def chars(lam,M):
    qs=rates(lam,M)
    for a in product(*(range(m) for m in M)):
        eig=sum((v*((-1)**sum((x&y).bit_count() for x,y in zip(a,z))-1) for z,v in qs.items()),F(0))
        check(eig==-rate(lam,support(a)))
def marg(qs,B):
    out={}
    for z,v in qs.items():
        w=tuple(z[i] for i in B)
        if any(w):out[w]=out.get(w,F(0))+v
    return out

def triple(c,th,t):
    return {1:c[0]-th[0]-th[1]+t,2:c[1]-th[0]-th[2]+t,4:c[2]-th[1]-th[2]+t,3:th[0]-t,5:th[1]-t,6:th[2]-t,7:t}
def limits(c,th): return max(F(0),th[0]+th[1]-c[0],th[0]+th[2]-c[1],th[1]+th[2]-c[2]),min(th)
def lin(rows,x):return sum(((r&x).bit_count()%2)<<i for i,r in enumerate(rows))
def surjections(n,r):
    return [rows for rows in product(range(1<<n),repeat=r) if len({lin(rows,x) for x in range(1<<n)})==1<<r]

for k in range(1,5):
    full=(1<<k)-1
    families=[{S:F(S==chosen) for S in range(1,full+1)} for chosen in range(1,full+1)]
    families += [{S:F((S*7)%5,3) for S in range(1,full+1)}, {S:F((-1)**S,2) for S in range(1,full+1)}]
    for lam in families:
        r={J:rate(lam,J) for J in range(full+1)}
        check(invert(r,k)==lam)
        chars(lam,[2]*k)
        if all(v>=0 for v in lam.values()):check(all(v>=0 for v in rates(lam,[2]*k).values()))
P=triple([F(1)]*3,[F(1,2)]*3,F(0))
Q=triple([F(1)]*3,[F(1,2)]*3,F(1,2))
for M in product([2,4],repeat=3):
    for lam in [P,Q]:
        chars(lam,M)
        check(min(rate(lam,J) for J in range(1,8))==1)
        qs=rates(lam,M)
        check(all(v>=0 for v in qs.values()))
        # Positive nonzero total off-diagonal rate; full matrix audit is separate.
        check(sum(qs.values())>0)
    for B in [(0,1),(0,2),(1,2)]:check(marg(rates(P,M),B)==marg(rates(Q,M),B))
    for lam,t in [(P,F(0)),(Q,F(1,2))]:
        check(sum(v for z,v in rates(lam,M).items() if all(z))==t*prod(F(m-1,m) for m in M))
check(rate(P,7)==F(3,2));check(rate(Q,7)==2)
for lam,a,b,c in [(P,F(1,4),F(1,8),F(0)),(Q,F(5,16),F(1,16),F(1,16))]:
    for z,v in rates(lam,[2]*3).items():check(v=={1:a,2:b,3:c}[support(z).bit_count()])
quotient_counts={}
for n,r in [(2,1),(3,1),(3,2)]:
    maps=surjections(n,r);quotient_counts[f'{n}->{r}']=len(maps)
    check(len(maps)=={(2,1):3,(3,1):7,(3,2):42}[(n,r)])
    for pos in range(3):
        M=[2]*3;M[pos]=1<<n
        dest=[2]*3;dest[pos]=1<<r
        for lam in [P,Q]:
            qs=rates(lam,M)
            for rows in maps:
                pushed={}
                for z,v in qs.items():
                    w=list(z);w[pos]=lin(rows,w[pos]);w=tuple(w)
                    if any(w):pushed[w]=pushed.get(w,F(0))+v
                check(pushed==rates(lam,dest))
# Complete 5^3 theta grid, 3^3 c grid, and 7 t values, including impossible data.
grid=0
for c in product([F(0),F(1,2),F(1)],repeat=3):
    for th in product([F(0),F(1,4),F(1,2),F(3,4),F(1)],repeat=3):
        low,high=limits(c,th)
        for t in [F(-1,4),F(0),F(1,4),F(1,2),F(3,4),F(1),F(5,4)]:
            lam=triple(c,th,t)
            check(all(v>=0 for v in lam.values())==(low<=t<=high));grid+=1
            check([rate(lam,1<<i) for i in range(3)]==list(c))
            check([lam[S]+lam[7] for S in [3,5,6]]==list(th))
            check(rate(lam,7)==sum(c)-sum(th)+t)
check(limits([F(1)]*3,[F(1),F(1),F(0)])==(F(1),F(0)))
# Negative universal coefficient can be hidden at one finite size.
neg={1:F(-1,8),2:F(-1,8),4:F(-1,8),3:F(0),5:F(0),6:F(0),7:F(1)}
check(all(v>=0 for v in rates(neg,[2,2,2]).values()))
check(q(neg,[2,8,8],(1,0,0))==F(-7,128))
finite_glue={1:F(-1),2:F(0),4:F(0),3:F(1),5:F(1),6:F(0),7:F(0)}
check(all(v>=0 for v in rates(finite_glue,[2,2,2]).values()))
check(q(finite_glue,[2,4,4],(1,0,0))==F(-1,4))
result={'status':'PASS','arithmetic':'fractions.Fraction','assertions':N,'quotient_map_counts':quotient_counts,'theta_grid_cases':grid,'k_range':[1,4],'triple_dimension_vectors':8,'P_binary_rates':{'single':'1/4','pair':'1/8','triple':'0'},'Q_binary_rates':{'single':'5/16','pair':'1/16','triple':'1/16'},'P_triple_decay':'3/2','Q_triple_decay':'2','common_gap':'1','universal_proof':'REPORT.md sections 2-4; finite checks do not prove universality','external_dependencies':[]}
text=json.dumps(result,indent=2,sort_keys=True)+'\n'
Path(__file__).with_name('certificate.json').write_text(text)
print(text,end='')
