#!/usr/bin/env python3
"""Independent GF(2) Buchberger criterion replay of CAS Groebner support data.
This verifies that the 46 exported polynomials form a Groebner basis of THEIR ideal
and that the 9 source equations reduce to zero. Reverse ideal inclusion J⊇(GB)
requires the original CAS replay or explicit membership witnesses.
© 2026 Xorch — Concordante Lab. Public computational companion.
"""
import json,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent
from hashlib import sha256
SRC_PATH=R/'relations.json'
assert sha256(SRC_PATH.read_bytes()).hexdigest()=='130743859b2e3b2d18642811c8615bea74212187a3da722cb8bdeb5e86703103'
SRC=json.loads(SRC_PATH.read_text())
NAMES=SRC['variables']; WEIGHTS=(1,1,2,3,4,5,6,6)

def grevkey(e):return (sum(e),)+tuple(-x for x in reversed(e))
def divides(a,b):return all(x<=y for x,y in zip(a,b))
def shiftpoly(poly,d):return {tuple(x+y for x,y in zip(m,d)) for m in poly}
def xor(a,b):return a.symmetric_difference(b) if False else a^b

def parseterm(token):
    e=[0]*8
    for sub in token.strip().split('*'):
        k=sub.strip().split('^'); i=NAMES.index(k[0]);e[i]+=int(k[1]) if len(k)>1 else 1
    return tuple(e)

def fromexpr(s):
    terms=set()
    for part in s.split(' + '):
        e=parseterm(part)
        if e in terms:terms.remove(e)
        else:terms.add(e)
    return terms
source=[fromexpr(x) for xs in SRC['relations_by_degree'].values() for x in xs]
enc=(R/'groebner_supports.hex').read_text(encoding='utf-8-sig').strip().split(';')
assert len(enc)==46
G=[]
for k,s in enumerate(enc):
    assert len(s)%8==0
    E={tuple(int(x,16) for x in s[i:i+8]) for i in range(0,len(s),8)}
    assert len(E)==len(s)//8
    assert len({sum(u*v for u,v in zip(m,WEIGHTS)) for m in E})==1
    G.append(E)
lead=[max(g,key=grevkey) for g in G]
raw=(R/'groebner_leads.hex').read_text().strip()
assert ''.join(''.join(f'{a:x}' for a in m) for m in lead)==raw
assert not any(divides(lead[i],lead[j]) for i in range(len(G))for j in range(len(G))if i!=j)

# Modulo-2 term-set normal form with an explicit fixed monomial order.
sortedbasis=sorted(zip(lead,G),key=lambda item:grevkey(item[0]),reverse=True)
def normalform(z):
    z=set(z);r=set();steps=0
    while z:
        m=max(z,key=grevkey)
        for lm,g in sortedbasis:
            if divides(lm,m):
                offset=tuple(x-y for x,y in zip(m,lm))
                # m cancels with the leading term in shifted g
                z.symmetric_difference_update(shiftpoly(g,offset))
                break
        else:
            z.remove(m);r.add(m)
        steps+=1
    return r,steps

start=time.perf_counter();input_reductions=[]
for i,f in enumerate(source):
    remainder,n=normalform(f)
    assert not remainder,(i,'source relation not implied by 46 GB equations',remainder)
    input_reductions.append(n)
print('PASS: 9 original relations reduce to zero; 46 leading terms minimal',flush=True)

# Buchberger criterion: all S-pairs reduce to zero. Product criterion skips coprime pairs.
raw_pairs=0;product_pairs=0;tested=0;steps_total=0;max_steps=0
for i in range(len(G)):
    for j in range(i+1,len(G)):
        raw_pairs+=1
        a,b=lead[i],lead[j]
        if all(min(x,y)==0 for x,y in zip(a,b)):
            product_pairs+=1
            continue
        lcm=tuple(max(x,y) for x,y in zip(a,b))
        sa=shiftpoly(G[i],tuple(x-y for x,y in zip(lcm,a)))
        sb=shiftpoly(G[j],tuple(x-y for x,y in zip(lcm,b)))
        s=sa^sb
        remainder,steps=normalform(s)
        assert not remainder,(i,j,'S polynomial did not reduce to zero',len(remainder),remainder)
        tested+=1;steps_total+=steps;max_steps=max(max_steps,steps)
        if tested%100==0:print('S-pair zero',tested,'elapsed_sec',round(time.perf_counter()-start,2),flush=True)

res={'id':'buchberger-replay','result':'PASS','copyright':'© 2026 Xorch — Concordante Lab.',
'original_relations':9,'groebner_full_polynomials':len(G),'groebner_full_monomial_count':sum(map(len,G)),
'groebner_source_relation_reductions':input_reductions,'total_pairs':raw_pairs,
'coprime_pairs_product_criterion':product_pairs,'s_polynomials_reduced_exactly':tested,
'normalform_monomial_steps_total':steps_total,'normalform_max_steps':max_steps,
'method':'independent pure Python GF(2) term-set normal forms and S polynomial calculations',
'scope':'Reverse ideal containment requires original CAS replay or explicit membership certificates.'}
(R/'buchberger_certificate.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print('PASS independent Buchberger verification:',len(G),'polynomials;',tested,'nontrivial S-pairs;',product_pairs,'product criterion; elapsed',round(time.perf_counter()-start,3),'sec',flush=True)
