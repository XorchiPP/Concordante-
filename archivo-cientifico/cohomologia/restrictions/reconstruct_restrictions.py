#!/usr/bin/env python3
"""Finite replay of reconstructed detector restrictions.
Concordante Lab / Xorch.
Scope: polynomial reconstruction and finite compatibility checks;
global realization of the eight classes remains an external hypothesis.
Adapted by selecting existing blocks from the archived verifier.
"""
from __future__ import annotations
import csv, hashlib, itertools, json, math
from pathlib import Path
P=Path(__file__).resolve().parent
SRC=P/'inputs'
COPYRIGHT='© 2026 Xorch — Concordante Lab. Todos los derechos reservados.'
RANKS=(4,3,3,3,3,3)
SYMS=('x','y','alpha','gamma','w4','w5','w6','Theta')
DEG=(1,1,2,3,4,5,6,6)
# SHA256 of the normalized inputs in this edition.
PINS={'basis_degree10.csv': 'ed950a296bcffa00d27746e0423ce077f4e3fa65f81a4e2e5a6da591ede5da83', 'basis_degree11.csv': 'df1519a21cdb7d785a047e525bf52fd3c8bf2b3c02f3f24b41b2b75e3f1a3fa7', 'basis_degree12.csv': 'd6c5426112b274c262f0183149a32ab8430f46b864dcec5b589b473b8d5b7bc8', 'detector_subgroups.json': 'b2a25ed46e5dffc992f6a03ec7404fb4368ca4411ecfb049058ebd73440850a9', 'group_permutations.csv': 'c919c9317e3cb81591fbcb0e89979a36aed10af4293864fce1cbdef92b35478f', 'lhs_modules.csv': 'a9f75b70dacc6754d3d374757913597b43b6ae996ce173d07ac5488baf43be52'}
PINS['manuscript_fiber.json']='5654a28989afb9020b4e21988e9e126dc4b7b758e2957a7265cded4c2606ffb6'
for name,sha in PINS.items():
 assert hashlib.sha256((SRC/name).read_bytes()).hexdigest()==sha,(name,'sha256 mismatch')

def csvrows(path):
 with path.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def outcsv(name,header,lines):
 with (P/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.writer(f);w.writerow(header);w.writerows(lines)
def exps(r,d):return tuple(a for a in itertools.product(range(d+1),repeat=r)if sum(a)==d)
def blocks(v,d):
 out=[];offset=0
 for r in RANKS:
  n=len(exps(r,d));out.append((v>>offset)&((1<<n)-1));offset+=n
 assert v>>offset==0
 return out
def pbits(v,r,d):return {e for i,e in enumerate(exps(r,d))if (v>>i)&1}
def pvec(a,r,d):
 idx={v:i for i,v in enumerate(exps(r,d))}
 assert all(len(z)==r and sum(z)==d for z in a)
 return sum(1<<idx[x]for x in a)
def pmul(a,b):
 out=set()
 for x in a:
  for y in b:
   v=tuple(i+j for i,j in zip(x,y))
   if v in out:out.remove(v)
   else:out.add(v)
 return out
def pplus(*polys):
 out=set()
 for a in polys:out.symmetric_difference_update(a)
 return out
def ppow(a,k,r):
 out={(0,)*r}
 while k:
  if k&1:out=pmul(out,a)
  a=pmul(a,a);k>>=1
 return out
def divide(a,b):
 if not b:return None if not a else None
 out=set();left=set(a);lead=max(b)
 while left:
  t=max(left)
  if any(i<j for i,j in zip(t,lead)):raise AssertionError(('non-divisible',t,lead))
  x=tuple(i-j for i,j in zip(t,lead))
  out.add(x);left.symmetric_difference_update({tuple(i+j for i,j in zip(x,y))for y in b})
 assert pmul(out,b)==a
 return out
def frobroot(a,m):
 assert all(all(i%m==0 for i in e)for e in a)
 return {tuple(i//m for i in e)for e in a}
def sq(a,i):
 out=set()
 for e in a:
  for f in itertools.product(*(range(min(i,k)+1)for k in e)):
   if sum(f)!=i or any((math.comb(k,j)&1)==0 for k,j in zip(e,f)):continue
   z=tuple(k+j for k,j in zip(e,f))
   if z in out:out.remove(z)
   else:out.add(z)
 return out
def vec(polys,d):
 mask=0;offset=0
 for r,a in zip(RANKS,polys):
  mask |= pvec(a,r,d)<<offset; offset+=len(exps(r,d))
 return mask
def rank(cols):
 piv={}
 for v in cols:
  while v:
   b=v.bit_length()-1
   if b in piv:v^=piv[b]
   else:piv[b]=v;break
 return len(piv)
def eliminate(cols):
 piv={};kernel=[];ind=[]
 for j,v in enumerate(cols):
  w=v;c=1<<j
  while w:
   k=w.bit_length()-1
   if k in piv:w^=piv[k][0];c^=piv[k][1]
   else:piv[k]=(w,c);ind.append(j);break
  if not w:kernel.append(c)
 return len(piv),kernel,ind
def decoder(cols):
 piv={}
 for j,v in enumerate(cols):
  w=v;c=1<<j
  while w:
   k=w.bit_length()-1
   if k in piv:w^=piv[k][0];c^=piv[k][1]
   else:piv[k]=(w,c);break
  else:raise AssertionError('dependent target basis')
 def run(v):
  c=0
  while v:
   k=v.bit_length()-1
   if k not in piv:raise AssertionError('target not in known span')
   v^=piv[k][0];c^=piv[k][1]
  return c
 return run
def table(d):
 rows=csvrows(SRC/f'basis_degree{d}.csv')
 vals=[int(r['joint_restriction_hex'],16)for r in rows]
 assert len(vals)=={10:39,11:48,12:57}[d] and rank(vals)==len(vals)
 return rows,vals
TAB={d:table(d)for d in (10,11,12)}

def generator_reconstruction():
 # Reconstruct low-degree polynomial restrictions by *injective Frobenius* in a polynomial domain,
 # exact division by nonzero w6, and unique linear forms with the certified 10th power.
 lookup={d:{r['class_expression']:[pbits(b,rk,d)for rk,b in zip(RANKS,blocks(v,d))]
   for r,v in zip(*TAB[d])}for d in TAB}
 gens={name:[frobroot(poly,m) for poly in lookup[degree][src]]
       for name,src,degree,m in [('w5','w5^2',10,2),('w6','w6^2',12,2),('Theta','Theta^2',12,2),('gamma','gamma^4',12,4)]}
 for sym in ('x','y'):
  gens[sym]=[]
  for rk,pol in zip(RANKS,lookup[10][sym+'^10']):
   candidates=[]
   for mask in range(1<<rk):
    line={tuple(int(j==i)for j in range(rk))for i in range(rk)if(mask>>i)&1}
    if ppow(line,10,rk)==pol:candidates.append(line)
   assert len(candidates)==1,(sym,'line not unique')
   gens[sym].append(candidates[0])
 gens['w4']=[divide(a,b)for a,b in zip(lookup[10]['w4*w6'],gens['w6'])]
 aq=[divide(a,b) for a,b in zip(lookup[10]['alpha^2*w6'],gens['w6'])]
 assert all(z is not None for z in aq+gens['w4'])
 gens['alpha']=[frobroot(a,2)for a in aq]
 for i in range(6):
  assert sq(gens['alpha'][i],1)==gens['gamma'][i]
  assert not pmul(gens['alpha'][i],gens['y'][i])
 return gens
GENS=generator_reconstruction()
def monomials(d,i=0,z=()):
 if i==8:
  if d==0:yield z
  return
 for k in range(d//DEG[i]+1):yield from monomials(d-k*DEG[i],i+1,z+(k,))
def expression(e):return '*'.join(s+(f'^{k}'if k>1 else '') for s,k in zip(SYMS,e)if k)or'1'
def evaluate(e):
 polys=[]
 for j,rk in enumerate(RANKS):
  a={(0,)*rk}
  for s,k in zip(SYMS,e):
   if k:a=pmul(a,ppow(GENS[s][j],k,rk))
  polys.append(a)
 return polys
# Verify the 144 original independent basis columns, not just total ranks.
for d in (10,11,12):
 for row,mask in zip(*TAB[d]):
  exp=tuple(int(row['power_'+s])for s in SYMS)
  assert vec(evaluate(exp),d)==mask,('basis mismatch',d,row['class_expression'])

WEIGHTS=((1,1),(1,2),(2,1),(2,2))
def transform(e,a,b):
 dest=[0]*4
 for j,(u,v)in enumerate(WEIGHTS):
  new=((3-u if a else u),(3-v if b else v))
  dest[WEIGHTS.index(new)]=e[j]
 return tuple(dest)
def orb(q):
 fixed=set()
 for e in exps(4,q):
  if sum(e[i]*WEIGHTS[i][0]for i in range(4))%3==0 and sum(e[i]*WEIGHTS[i][1]for i in range(4))%3==0:fixed.add(e)
 D=len(fixed);counts={1:0,2:0,4:0}
 while fixed:
  e=next(iter(fixed));o={transform(e,a,b)for a in (0,1)for b in (0,1)}
  assert o<=fixed
  counts[len(o)]+=1;fixed-=o
 return D,counts[1],counts[2],counts[4]
def even_closed(k):
 a=int(k%2==0)
 r0=(2*k)%3
 F=(k-r0)//3+1 if k>=r0 else 0
 b=F+(k+1-3*a)//2
 assert (k+1-3*a)%2==0
 D,oa,ob,oc=orb(2*k)
 c=(D-a-2*b)//4
 assert (a,b,c)==(oa,ob,oc)
 return a,b,c,F
O={q:orb(q)for q in range(14)}
for q in range(0,14,2):even_closed(q//2)
def hp(p,q):
 D,a,b,c=O[q]
 return a+b+c if p==0 else (p+1)*a+b
for q in range(13):
 rec=csvrows(SRC/'lhs_modules.csv')[q]
 assert int(rec['q_fiber'])==q and int(rec['C3xC3_fixed_dim'])==O[q][0]
 h=list(map(int,rec['H0_to_H12_q'].split()))
 assert [hp(i,q)for i in range(len(h))]==h
E2={n:[hp(p,n-p)for p in range(n+1)]for n in (10,11,12,13)}
assert E2[11]==[11,5,0,6,0,4,0,9,0,1,0,12]
assert E2[12]==[17,0,5,0,7,0,4,0,10,0,1,0,13]
assert E2[13]==[15,7,0,5,0,8,0,4,0,11,0,1,0,14]

# Direct check of the section Q0 <= G, using original 576 12-point permutations.
ROOK=csvrows(SRC/'group_permutations.csv')
GP={tuple(map(int,r['g_permutation12'].split())):r for r in ROOK}
assert len(GP)==576
v4={(0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0)}
N={g for g,r in GP.items()if r['plane_swap']=='0' and tuple(map(int,r['row_perm4'].split())) in v4 and tuple(map(int,r['column_perm4'].split()))in v4}
Q={g for g,r in GP.items()if tuple(map(int,r['row_perm4'].split()))[0]==0 and tuple(map(int,r['column_perm4'].split()))[0]==0}
def compose(a,b):return tuple(a[b[i]]for i in range(len(a)))
assert (len(N),len(Q),len(N&Q))==(16,36,1)
assert len({compose(n,q)for n in N for q in Q})==576
assert all(compose(a,b)in Q for a in Q for b in Q)
assert all(compose(a,b)in N for a in N for b in N)


# Compare Stiefel–Whitney restrictions for the supplied 12-point permutation action.
C09=json.loads((SRC/'detector_subgroups.json').read_text())

def permw(E):
 gg=[tuple(map(int,g.split()))for g in E['basis_G_elements']];r=len(gg)
 group={0:tuple(range(12))}
 for j,g in enumerate(gg):
  for k,h in list(group.items()):group[k|(1<<j)]=compose(h,g)
 assert len(group)==len(set(group.values()))==2**r
 unseen=set(range(12));orbit_sizes=[];W=[{(0,)*r}]+[set()for _ in range(12)]
 while unseen:
  x=min(unseen);orbit={g[x]for g in group.values()};unseen-=orbit;orbit_sizes.append(len(orbit))
  stab=[k for k,g in group.items()if g[x]==x]
  chars=[c for c in range(1<<r)if all((c&k).bit_count()%2==0 for k in stab)]
  assert len(chars)==len(orbit)
  for c in chars:
   line={tuple(int(j==t)for j in range(r))for t in range(r)if (c>>t)&1}
   for j in range(12,0,-1):W[j].symmetric_difference_update(pmul(W[j-1],line))
 return W,orbit_sizes
Ws=[];orbs=[]
for j,E in enumerate(C09['sylow2']['E_conjugacy_examples']):
 W,ob=permw(E);Ws.append(W);orbs.append(ob)
 assert W[1]==GENS['x'][j]
 assert W[2]==pplus(GENS['alpha'][j],pmul(GENS['x'][j],GENS['y'][j]))
 assert all(W[k]==GENS['w'+str(k)][j]for k in [4,5,6])
 assert all(not W[k]for k in [10,11,12])

# Compare the normal-fiber convention with the already published manuscript data.
reference=json.loads((SRC/'manuscript_fiber.json').read_text())
assert all({tuple(e) for e in reference[name]}==GENS[name][0] for name in SYMS)
export={'generator_degrees':dict(zip(SYMS,DEG)),
 'detector_ranks':list(RANKS),
 'supports':{name:[sorted(map(list,a)) for a in GENS[name]] for name in SYMS},
 'scope':'Reconstructed restrictions; global realization remains a stated dependency'}
(P/'generator_restrictions.json').write_text(json.dumps(export,indent=2)+'\n')
result={'result':'PASS','basis_columns_rechecked':sum(len(TAB[d][0]) for d in TAB),
 'basis_degrees':[10,11,12], 'group_section_orders':[len(N),len(Q),len(N&Q)],
 'fiber_matches_manuscript':True,'detectors':6,
 'sw_comparisons':'w1=x, w2=alpha+xy, w4/w5/w6 match reconstructed restrictions',
 'scope':'Finite polynomial and group-action checks; global realization and reverse ideal containment remain separate dependencies'}
(P/'reconstruction_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
