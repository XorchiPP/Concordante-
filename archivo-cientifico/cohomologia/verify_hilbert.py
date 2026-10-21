#!/usr/bin/env python3
"""Independent integer Taylor-lcm Hilbert series verifier for the 46 leading terms.
Groebner-leading terms are exported from Wolfram GroebnerBasis (modulus 2,
DegreeReverseLexicographic, fixed variable order). Independently validate them
with verify_buchberger.py; this script covers the integer Hilbert identity.
© 2026 Xorch — Concordante Lab. Public computational companion.
"""
import json,hashlib
from pathlib import Path
from collections import defaultdict
from itertools import zip_longest
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'relations.json'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()=='130743859b2e3b2d18642811c8615bea74212187a3da722cb8bdeb5e86703103'

RAW=(ROOT/'groebner_leads.hex').read_text().strip()
assert len(RAW)==46*8,(len(RAW),'expected 46 monomials of eight exponents')
LEADS=[tuple(int(x,16) for x in RAW[i:i+8]) for i in range(0,len(RAW),8)]
assert len(set(LEADS))==46
assert not any(all(a<=b for a,b in zip(LEADS[i],LEADS[j])) for i in range(46) for j in range(46) if i!=j),'leading monomials not minimal'
WEIGHTS=(1,1,2,3,4,5,6,6)
# Taylor lcm-lattice numerator: at step m, replace C by C - lcm(m,C).
states={(0,)*8:1};sizes=[]
for m in LEADS:
    nxt=states.copy()
    for e,c in states.items():
        new=tuple(max(a,b) for a,b in zip(e,m))
        nxt[new]=nxt.get(new,0)-c
        if nxt[new]==0:del nxt[new]
    states=nxt;sizes.append(len(states))
assert len(states)==852
num=defaultdict(int)
for e,c in states.items():num[sum(a*b for a,b in zip(e,WEIGHTS))]+=c
ncoef=[num[i] for i in range(1+max(num))]
while ncoef and ncoef[-1]==0:ncoef.pop()
assert len(ncoef)==25

def mul(a,b):
    result=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):result[i+j]+=x*y
    return result

def trim(a):
    while a and a[-1]==0:a.pop()
    return a

def sub(a,b):return trim([x-y for x,y in zip_longest(a,b,fillvalue=0)])

def fac(n,s=-1):
    arr=[0]*(n+1);arr[0]=1;arr[n]=s;return arr
DA=[1]
for w in WEIGHTS:DA=mul(DA,fac(w))
DG=[1]
for f in [fac(1),fac(1),fac(3),fac(2,1),fac(6)]:DG=mul(DG,f)
NG=[1,0,2,-1,1,0,0,0,-1,-1]
difference=sub(mul(ncoef,DG),mul(NG,DA))
assert difference==[],('Hilbert discrepancy',next((i,c) for i,c in enumerate(difference) if c!=0))

# The exact rational identity is certified over Z[t] by crossing denominators.
result={'id':'hilbert-replay','result':'PASS','state':'PUBLIC_REPLAY',
'copyright':'© 2026 Xorch — Concordante Lab.',
'group':'G=(F2^2 tensor F2^2) rtimes (S3 x S3)',
'input_source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
'leading_source':'Wolfram GroebnerBasis (Modulus->2, DegreeReverseLexicographic) as separate CAS input; independent Buchberger replay is supplied in verify_buchberger.py',
'number_original_relations':9,'groebner_lead_count':46,'lcm_lattice_nonzero_states':len(states),
'first_46_lcm_state_counts':sizes,'leading_exponents':LEADS,'lcm_numerator_dense':ncoef,
'polynomial_ring_denominator_factors':[f'1-t^{w}' for w in WEIGHTS],
'global_cohomology_numerator_dense':NG,'global_cohomology_denominator_factors':['1-t','1-t','1-t^3','1+t^2','1-t^6'],
'exact_cross_multiplication_difference':difference,
'exact_hilbert_series_identity':True,
'scope':'Exact Hilbert identity of the exported initial ideal; full ring theorem requires authenticated global classes and both ideal containments',
'verification_stage':'Hilbert calculation companion to the conditional all-degree manuscript'}
(ROOT/'hilbert_certificate.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS: 46 Groebner leading monomials, 852 nonzero lcm states')
print('Numerator:',ncoef)
print('Exact identity H(A/I_exported)=P_G: TRUE (cross product zero)')
print('Scope: exact initial-ideal Hilbert identity; authenticate both ideal containments for A/J.')
