#!/usr/bin/env python3
"""Exact finite controls; universal proof in REPORT.md.
Matrix helpers adapted from the pinned predecessor; no external imports.
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



CHECKS=[]
def check(name,value):
    if not value: raise AssertionError(name)
    CHECKS.append(name)

M=diag([1,2,3,4,5]); mi=sub(M,[2,3,4],[2,3,4])
L=mat([[20,-2,-4,-6,-8],[-2,26,-6,-8,-10],[-4,-6,37,-12,-15],[-6,-8,-12,46,-20],[-8,-10,-15,-20,53]])
S=mat([[1,0,0],[0,F(-1,9),F(10,9)],[0,F(8,9),F(1,9)]])
T=eye(5)
for i in range(3):
 for j in range(3): T[i+2][j+2]=S[i][j]
Lt=mm(mm(transpose(T),L),T)
check('capacity_isometry',mm(mm(transpose(S),mi),S)==mi)
check('constant_fixed',mm(S,[[F(1)]]*3)==[[F(1)]]*3)
check('marked_e2_fixed',mm(S,[[F(1)],[F(0)],[F(0)]])==[[F(1)],[F(0)],[F(0)]])
check('involution',mm(S,S)==eye(3))
check('distinct_networks',Lt!=L)
check('weighted_nonisomorphism_by_degrees',sorted(L[i][i] for i in range(5))!=sorted(Lt[i][i] for i in range(5)))
A=[];C=[];minor=[]
for name,l in [('original',L),('transformed',Lt)]:
 check(name+'_symmetric',l==transpose(l))
 check(name+'_zero_rows',all(sum(row)==0 for row in l))
 check(name+'_all_positive_edges',all(l[i][j]<0 for i in range(5) for j in range(i+1,5)))
 check(name+'_min_edge_2',min(-l[i][j] for i in range(5) for j in range(i+1,5))==2)
 c=sub(l,[0,1],[2,3,4]);a=mm(inv(mi),sub(l,[2,3,4],[2,3,4]));o=c+mm(c,a)+mm(mm(c,a),a)
 minor.append(det(o[:3]));check(name+'_observable',minor[-1]!=0);A.append(a);C.append(c)
check('minor_values',minor==[F(8,15),F(-8,15)])
for boundary in [[0,1],[0,1,2]]:
 for s in [0,F(1,3),1,7,100]:
  check('transfer_B'+str(boundary)+'_s'+str(s),transfer(L,M,boundary,s)==transfer(Lt,M,boundary,s))
# Exact all-function hypotheses were certified above. These finite moments audit implementations.
p=[[F(1)],[F(0)],[F(0)]];left=C[0];right=C[1]
for k in range(12):
 check('prepared_e2_moment_'+str(k),mm(left,p)==mm(right,p))
 left=mm(left,A[0]);right=mm(right,A[1])
check('e3_discriminator',C[0][0][1]-C[1][0][1]==F(4,9))
check('expanded_B0123_discriminator',sub(L,[0,1,2,3],[0,1,2,3])!=sub(Lt,[0,1,2,3],[0,1,2,3]))
# Constant + two nodal preparations span all interiors.
check('two_marks_span',det(mat([[1,1,0],[1,0,1],[1,0,0]]))!=0)
# Conservation identity reconstructs the unprepared response from Lambda:
# C(D+sM)^-1 M 1 = -Lambda(s)1_B/s.
for s in [F(1,3),F(1),F(7)]:
 d=sub(L,[2,3,4],[2,3,4]);h=mm(mm(C[0],inv(add(d,scale(mi,s)))),mi)
 lhs=mm(h,[[F(1)]]*3);rhs=scale(mm(transfer(L,M,[0,1],s),[[F(1)]]*2),-1/s)
 check('conservation_preparation_identity_'+str(s),lhs==rhs)
# Algebraic reconstruction from exact Markov coefficients through order n.
k=[C[0]]
for r in range(3): k.append(mm(k[-1],A[0]))
o=sum(k[:3],[]);oplus=sum(k[1:4],[])
ahat=mm(inv(o[:3]),oplus[:3])
check('reconstruct_A_from_markov_coefficients',ahat==A[0])
check('reconstruct_D_from_A',mm(mi,ahat)==sub(L,[2,3,4],[2,3,4]))
cert={'status':'PASS','checks':CHECKS,'count':len(CHECKS),'arithmetic':'fractions.Fraction; zero tolerance','edition':'interior-marks-2026-10-21','M':M,'L':L,'L_tilde':Lt,'S':S,'observability_minors':minor,'e3_initial_current_difference':F(4,9),'traces':[sum(L[i][i] for i in range(5)),sum(Lt[i][i] for i in range(5))],'functional_identity_basis':'Proved gauge identities, not sampling. See REPORT.md.'}
Path(__file__).with_name('certificate.json').write_text(json.dumps(serial(cert),ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(CHECKS),'observable_minors':serial(minor),'e3_difference':'4/9'},sort_keys=True))
