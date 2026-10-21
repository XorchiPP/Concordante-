#!/usr/bin/env python3
"""Deliberately separate *toy* descent, not a Beal/Shukla Route B solution.
F=Q, M=Q(sqrt(2)), conic X^2-2Y^2=-W^2 has point (1,1,1).
The 2-cochain and its 3-coboundary are explicit for G=C2 x C2.
"""
from fractions import Fraction as Q
import itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
ONE=(Q(1),Q(0)); U=(Q(1),Q(1)); V=(Q(1),Q(-1)); ZERO=(Q(0),Q(0))
def multiply(a,b):return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def inverse(a):
    n=a[0]**2-2*a[1]**2
    assert n!=0
    return (a[0]/n,-a[1]/n)
def div(a,b):return multiply(a,inverse(b))
def ga(g,a):return (a[0],(-1 if g[0] else 1)*a[1])
def xor(a,b):return tuple(x^y for x,y in zip(a,b))
GG=list(itertools.product(range(2),repeat=2))
assert multiply(U,V)==(Q(-1),Q(0)) and 1**2-2*1**2==-1
assert ga((1,0),U)==V
def e(g):return U if g[0] else ONE
def epsilon(g,h):return U if g[0] and h[0] else ONE
def partial_e(g,h):return div(multiply(e(g),ga(g,e(h))),e(xor(g,h)))
def E_direct(g,h):return (Q(-1),Q(0)) if g[0] and h[0] else ONE
def partial_epsilon(g,h,k):
    return div(multiply(ga(g,epsilon(h,k)),epsilon(g,xor(h,k))),multiply(epsilon(xor(g,h),k),epsilon(g,h)))
def eta_direct(g,h,k):return div(V,U) if g[0] and h[0] and k[0] else ONE
assert all(partial_e(g,h)==E_direct(g,h) for g,h in itertools.product(GG,repeat=2))
assert all(partial_epsilon(g,h,k)==eta_direct(g,h,k) for g,h,k in itertools.product(GG,repeat=3))
# 2-cocycle identity, with nontrivial action, all 64 group triples
assert all(multiply(ga(g,E_direct(h,k)),E_direct(g,xor(h,k))) ==
           multiply(E_direct(g,h),E_direct(xor(g,h),k)) for g,h,k in itertools.product(GG,repeat=3))
# 3-cocycle identity, all 256 group quadruples
assert all(multiply(multiply(ga(g,eta_direct(h,k,l)),eta_direct(g,xor(h,k),l)),eta_direct(g,h,k)) ==
           multiply(eta_direct(xor(g,h),k,l),eta_direct(g,h,xor(k,l)))
           for g,h,k,l in itertools.product(GG,repeat=4))
# One deliberately modified 3-cocycle point is detected immediately
mutated={(g,h,k):eta_direct(g,h,k) for g,h,k in itertools.product(GG,repeat=3)}
mutated[(GG[3],GG[3],GG[3])]=ONE
assert mutated[(GG[3],GG[3],GG[3])]!=partial_epsilon(GG[3],GG[3],GG[3])
result={
 'id':'quadratic_conic_example','status':'PASS_TOY_CONIC_AND_COBOUNDARY_CHECKS_NOT_BEAL_ARITHMETIC_COMPARISON',
 'F':'Q','M':'Q(sqrt(2))','number_field_degree_over_Q':2,
 'conic':'X^2 - 2Y^2 = - W^2','point':{'X':1,'Y':1,'W':1},
 'U':'1+sqrt(2)','V':'1-sqrt(2)','N_M_over_F_U':-1,
 'G':'C2 x C2, first factor acts on sqrt(2) by conjugation',
 'e':'e(g)=U if first bit is 1, else 1',
 'epsilon':'epsilon(g,h)=U if both first bits are 1, else 1',
 'partial_e_matches_E_direct_pairs':16,'E_twisted_2cocycle_triples':64,
 'partial_epsilon_matches_eta_direct_triples':64,'eta_twisted_3cocycle_quadruples':256,
 'nontrivial_eta_triples':sum(eta_direct(g,h,k)!=ONE for g,h,k in itertools.product(GG,repeat=3)),
 'single_point_mutation_detected':True,
 'independence':'NONE: the toy direct eta is defined using the same U as its epsilon cochain',
 'scope':'Validates arithmetic plumbing in a 2-dimensional number field and Galois action, NOT Shukla Lemma 4.4.1 or Proposition 4.4.4, not the original degree-330 field, and not ARITHMETIC_COMPARISON.',
 'ARITHMETIC_COMPARISON_status':'OPEN','Cassels_Tate':'UNKNOWN'
}
(P/'resultado_conica.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:result[k] for k in ('status','partial_e_matches_E_direct_pairs','partial_epsilon_matches_eta_direct_triples','eta_twisted_3cocycle_quadruples','ARITHMETIC_COMPARISON_status')},ensure_ascii=False))

