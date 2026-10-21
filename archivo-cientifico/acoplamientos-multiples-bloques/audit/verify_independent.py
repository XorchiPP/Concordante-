#!/usr/bin/env python3
"""Independent exact matrix audit. Does not import the author's implementation."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
checks=0

def ck(x):
    global checks
    checks+=1
    if not x: raise AssertionError(checks)

def matrix(sizes, weights):
    states=list(product(*(range(m) for m in sizes)))
    index={x:i for i,x in enumerate(states)}
    a=[[F(0) for y in states] for x in states]
    # Enumerate actual reset outcomes, including no-change outcomes.
    for S,w in weights.items():
        active=[i for i in range(len(sizes)) if S&(1<<i)]
        outcomes=list(product(*(range(sizes[i]) for i in active)))
        for row,x in enumerate(states):
            a[row][row]-=w
            for vals in outcomes:
                y=list(x)
                for i,v in zip(active,vals):y[i]=v
                a[row][index[tuple(y)]]+=w/len(outcomes)
    return states,a

def markov(a):return all(sum(row)==0 and all(v>=0 for j,v in enumerate(row) if i!=j) for i,row in enumerate(a))
def connected(a):
    seen={0}; todo=[0]
    while todo:
        i=todo.pop()
        for j,v in enumerate(a[i]):
            if i!=j and v>0 and j not in seen: seen.add(j);todo.append(j)
    return len(seen)==len(a)
def solve(a,b):
    a=[[F(x) for x in row]+[F(y)] for row,y in zip(a,b)]
    for j in range(len(a)):
        p=next(i for i in range(j,len(a)) if a[i][j])
        a[j],a[p]=a[p],a[j]
        v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(len(a)):
            if i!=j:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]
def quotient(states,a,project,target_states,target):
    idx={x:i for i,x in enumerate(target_states)}
    fibers=[[] for x in target_states]
    for j,x in enumerate(states):fibers[idx[project(x)]].append(j)
    for i,x in enumerate(states):
        row=target[idx[project(x)]]
        ck(all(sum(a[i][j] for j in fiber)==row[z] for z,fiber in enumerate(fibers)))

def spectral(states,a):
    rates={}
    for char in states:
        vec=[(-1)**sum((u&v).bit_count() for u,v in zip(char,x)) for x in states]
        eig=sum(v*z for v,z in zip(a[0],vec))
        ck(all(sum(v*z for v,z in zip(row,vec))==eig*vec[i] for i,row in enumerate(a)))
        support=sum(1<<i for i,v in enumerate(char) if v)
        if support in rates:ck(rates[support]==-eig)
        rates[support]=-eig
    return rates

P={3:F(1,2),5:F(1,2),6:F(1,2)}
Q={1:F(1,2),2:F(1,2),4:F(1,2),7:F(1,2)}
# Invert independently by Gaussian elimination, using actual matrix spectra.
for k in range(1,5):
    masks=list(range(1,1<<k))
    for weights in [{s:F(s==t) for s in masks} for t in masks]+[{s:F((-1)**s,3) for s in masks}]:
        states,a=matrix([2]*k,weights)
        rates=spectral(states,a)
        recovered=solve([[int(bool(j&s)) for s in masks] for j in masks],[rates[j] for j in masks])
        ck(recovered==[weights[s] for s in masks])

for sizes in product([2,4],repeat=3):
    for weights in (P,Q):
        states,a=matrix(sizes,weights)
        ck(markov(a));ck(connected(a));ck(all(a[i][j]==a[j][i] for i in range(len(a)) for j in range(len(a))))
        rates=spectral(states,a)
        ck(min(v for s,v in rates.items() if s)==1)
        ck(rates[7]==(F(3,2) if weights==P else F(2)))
        for pair in ((0,1),(0,2),(1,2)):
            ts,ta=matrix([sizes[i] for i in pair],{1:F(1,2),2:F(1,2),3:F(1,2)})
            quotient(states,a,lambda x:tuple(x[i] for i in pair),ts,ta)
# Simultaneous nontrivial quotient in ALL three coordinates, all 3^3 choices.
for weights in (P,Q):
    states,a=matrix([4,4,4],weights);ts,ta=matrix([2,2,2],weights)
    for rows in product([1,2,3],repeat=3):
        quotient(states,a,lambda x:tuple((r&v).bit_count()%2 for r,v in zip(rows,x)),ts,ta)
# Degenerate boundaries: empty generator and exactly one live block.
for weights,expected in [({},False),({1:F(1)},False),({7:F(1)},True)]:
    states,a=matrix([2,2,2],weights);ck(markov(a));ck(connected(a)==expected)
# Gluing constraints independently solved from seven linear observations.
# Observations are unary rates, pair common intensities, triple reset intensity.
masks=list(range(1,8))
obs=[[int(s&i==i) for s in masks] for i in [1,2,4,3,5,6,7]]
grid=0
for c in product([F(0),F(1,2),F(1)],repeat=3):
    for theta in product([F(0),F(1,2),F(1)],repeat=3):
        for t in [F(-1,2),F(0),F(1,2),F(1),F(3,2)]:
            weights=solve(obs,list(c)+list(theta)+[t])
            lower=max(F(0),theta[0]+theta[1]-c[0],theta[0]+theta[2]-c[1],theta[1]+theta[2]-c[2])
            ck(all(w>=0 for w in weights)==(lower<=t<=min(theta)));grid+=1
# Important scope control: the 'impossible' universal data DO glue at binary size.
finite={1:F(-1),3:F(1),5:F(1)}
states,a=matrix([2,2,2],finite);ck(markov(a));ck(connected(a))
for pair,weights in [((0,1),{3:F(1)}),((0,2),{3:F(1)}),((1,2),{1:F(1),2:F(1)})]:
    ts,ta=matrix([2,2],weights)
    quotient(states,a,lambda x:tuple(x[i] for i in pair),ts,ta)
_,bad=matrix([2,4,4],finite);ck(not markov(bad));ck(bad[0][16]==F(-1,4))
root=Path(__file__).resolve().parent.parent
out={'status':'PASS','assertions':checks,'method':'Direct reset outcome enumeration, full rational matrices, Gaussian elimination; no author code imported','compatibility_grid_cases':grid,'simultaneous_quotients':54,'finite_obstruction_control':'Universal-incompatible pair data glue at (2,2,2), fail at (2,4,4)','scope':'Finite checks support but do not prove the universal theorem','inputs_sha256':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in ['REPORT.md','verify_multiblock.py']}}
print(json.dumps(out,indent=2,sort_keys=True))
Path(__file__).with_name('independent_certificate.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
