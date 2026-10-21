#!/usr/bin/env python3
"""Exact F2 polynomial membership witness search. No external dependencies."""
import json,hashlib,time,resource,heapq,sys
from pathlib import Path
R=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
start=time.monotonic()
raw=(R/'inputs/relations.json').read_bytes(); enc=(R/'inputs/groebner_supports.hex').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='130743859b2e3b2d18642811c8615bea74212187a3da722cb8bdeb5e86703103'
assert hashlib.sha256(enc).hexdigest()=='550dfeb94726e42de31395b90b51da3018955025d2a75881ca5270383fe1de6d'
src=json.loads(raw); names=src['variables']; weights=src['variable_degrees']; zero=(0,)*8
assert names==['x','y','alpha','gamma','w4','w5','w6','Theta'] and weights==[1,1,2,3,4,5,6,6]
def parse(s):
 p=set()
 for term in s.split('+'):
  m=[0]*8
  for factor in term.strip().split('*'):
   a,*b=factor.strip().split('^');m[names.index(a)]+=int(b[0]) if b else 1
  m=tuple(m);p.symmetric_difference_update([m])
 return p
def degree(m):return sum(a*b for a,b in zip(m,weights))
def key(m):return (sum(m),)+tuple(-a for a in m[::-1])
def shift(p,m):return {tuple(a+b for a,b in zip(t,m)) for t in p}
def shiftw(w,m):return {(i,tuple(a+b for a,b in zip(t,m))) for i,t in w}
def divides(a,b):return all(x<=y for x,y in zip(a,b))
F=[]
for d,ss in src['relations_by_degree'].items():
 for s in ss:
  f=parse(s);assert {degree(m) for m in f}=={int(d)};F.append(f)
G=[]
for s in enc.decode('utf-8-sig').strip().split(';'):
 p={tuple(int(c,16) for c in s[k:k+8]) for k in range(0,len(s),8)}
 assert len(s)%8==0 and len(p)==len(s)//8 and len({degree(m) for m in p})==1
 G.append(p)
assert len(F)==9 and len(G)==46
B=[]; L=[]; W=[];pairs=[]
def reduce(p,w):
 p=set(p);w=set(w);r=set()
 while p:
  m=max(p,key=key)
  for i,l in enumerate(L):
   if divides(l,m):
    delta=tuple(a-b for a,b in zip(m,l));p^=shift(B[i],delta);w^=shiftw(W[i],delta);break
  else:p.remove(m);r.add(m)
 return r,w
def add(p,w):
 n=len(B);l=max(p,key=key)
 for i,a in enumerate(L):
  if any(min(x,y) for x,y in zip(a,l)):
   lc=tuple(max(x,y) for x,y in zip(a,l));heapq.heappush(pairs,(sum(lc),key(lc),i,n,lc))
 B.append(p);L.append(l);W.append(w)
for i,f in enumerate(F):
 p,w=reduce(f,{(i,zero)})
 if p:add(p,w)
pending=set(range(46));answers={};steps=0
while True:
 for i in sorted(pending):
  p,w=reduce(G[i],set())
  if not p:answers[i]=w
 pending-=answers.keys()
 print('basis',len(B),'pending',len(pending),'pairs',len(pairs),'seconds',round(time.monotonic()-start,3),flush=True)
 if not pending:break
 if not pairs:raise RuntimeError(('membership unresolved',sorted(pending)))
 # Each batch adds one basis polynomial, or consumes all remaining zero pairs.
 while pairs:
  _,_,i,j,lc=heapq.heappop(pairs);steps+=1
  a=tuple(x-y for x,y in zip(lc,L[i]));b=tuple(x-y for x,y in zip(lc,L[j]))
  p,w=reduce(shift(B[i],a)^shift(B[j],b),shiftw(W[i],a)^shiftw(W[j],b))
  if p:add(p,w);break
out={'field':'F2','variables':names,'weights':weights,'relation_order':'relations_by_degree JSON insertion order, then array order','input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'inputs').iterdir()},'assertion_tested':'Each of 46 frozen support polynomials equals the specified F2 sum of monomial multiples of the nine relations.','witnesses':[{'target_index':i,'weighted_degree':degree(next(iter(G[i]))),'terms':[{'relation_index':j,'multiplier_exponents':list(m)} for j,m in sorted(answers[i])]} for i in range(46)],'search':{'seconds':time.monotonic()-start,'basis_size':len(B),'pairs_processed':steps,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'python':sys.version}}
(R/'membership_witness.json').write_text(json.dumps(out,indent=2)+'\n')
print('SUCCESS',out['search'], 'witness terms',sum(len(w) for w in answers.values()),flush=True)
