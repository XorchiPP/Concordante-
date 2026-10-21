#!/usr/bin/env python3
"""Independent rational audit; no import of the author's verifier or certificate.
Polynomial transfer identities are checked by determinants in Q[s], not samples.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations
from pathlib import Path
import json, hashlib

def matrix(n,m=None): return [[Q(0) for _ in range(n if m is None else m)] for _ in range(n)]
def identity(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def transpose(a): return [list(c) for c in zip(*a)]
def mul(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def block(a,ii,jj): return [[a[i][j] for j in jj] for i in ii]
def congruence(a,t): return mul(transpose(t),mul(a,t))
def rank(a):
    a=[r[:] for r in a]; row=0
    for col in range(len(a[0])):
        p=next((i for i in range(row,len(a)) if a[i][col]),None)
        if p is None: continue
        a[row],a[p]=a[p],a[row]
        x=a[row][col]; a[row]=[v/x for v in a[row]]
        for i in range(row+1,len(a)):
            x=a[i][col]; a[i]=[v-x*w for v,w in zip(a[i],a[row])]
        row+=1
        if row==len(a):break
    return row

def norm(p):
    p=list(map(Q,p))
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p)
def plus(p,q):return norm([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def times(p,q):
    r=[Q(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return norm(r)
def minus(p):return tuple(-v for v in p)
def determinant(a):
    n=len(a); z=(Q(0),)
    for p in permutations(range(n)):
        parity=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=(Q((-1)**parity),)
        for i in range(n):term=times(term,a[i][p[i]])
        z=plus(z,term)
    return z

def transfer_polynomials(l,m,b):
    hidden=[i for i in range(len(l)) if i not in b]
    k=[[(l[i][j],m[i] if i==j else Q(0)) for j in hidden] for i in hidden]
    den=determinant(k); nums=[]
    for i in b:
        row=[]
        for j in b:
            # Block determinant equals det(K)*(L_ij-C_i K^-1 C_j^T).
            bordered=[r+[(l[h][j],)] for h,r in zip(hidden,k)]
            bordered.append([(l[i][h],) for h in hidden]+[(l[i][j],)])
            row.append(determinant(bordered))
        nums.append(row)
    return nums,den

def transfer_equal(l,r,m,b):
    p,d=transfer_polynomials(l,m,b);q,e=transfer_polynomials(r,m,b)
    return all(times(p[i][j],e)==times(q[i][j],d) for i in range(len(b)) for j in range(len(b)))

def laplacian(m,extra):
    n=len(m);l=matrix(n)
    for i,j in combinations(range(n),2):
        w=m[i]*m[j]+extra.get((i,j),Q(0))
        l[i][i]+=w;l[j][j]+=w;l[i][j]-=w;l[j][i]-=w
    return l

def reflection(m,a,b):
    w=[Q(0)]*len(m);w[a]=m[b];w[b]=-m[a]
    d=sum(m[i]*w[i]**2 for i in range(len(m)))
    return [[Q(i==j)-2*w[i]*w[j]*m[j]/d for j in range(len(m))] for i in range(len(m))]
def observation(l,m):
    ii=list(range(2,len(m)));c=block(l,[0,1],ii)
    a=[[l[i][j]/m[i] for j in ii] for i in ii];stack=[]
    for _ in ii:stack+=c;c=mul(c,a)
    return rank(stack)
def valid(l):return l==transpose(l) and all(sum(r)==0 for r in l) and all(l[i][j]<0 for i,j in combinations(range(len(l)),2))
checks=[]
def check(label,test):
    assert test,label
    checks.append(label)

m=list(map(Q,[1,2,3,4,5]));l=laplacian(m,{(0,2):Q(1),(0,3):Q(2),(0,4):Q(3)})
t=reflection(m,3,4);r=congruence(l,t)
check('K5 physical complete Laplacians',valid(l) and valid(r))
check('K5 observable both',observation(l,m)==observation(r,m)==3)
check('K5 fixed e2',all(t[i][2]==Q(i==2) for i in range(5)))
check('K5 rational transfer original boundary',transfer_equal(l,r,m,[0,1]))
check('K5 rational transfer expanded boundary',transfer_equal(l,r,m,[0,1,2]))
check('K5 rational transfer second extra boundary differs',not transfer_equal(l,r,m,[0,1,2,3]))
check('K5 initial e3 discriminates by 4/9',l[0][3]-r[0][3]==Q(4,9))
check('K5 printed transformed entries',[r[0][3],r[0][4],r[3][3],r[3][4],r[4][4]]==list(map(Q,['-58/9','-68/9','3758/81','-1616/81','4253/81'])))
# Laplace transform of preparation e2 is C(D+sM)^-1 M e2.
# Compare full numerator polynomials using a block determinant with lower-right 0.
def prepared(l,m,j):
    ii=[2,3,4];k=[[(l[i][h],m[i] if i==h else Q(0)) for h in ii] for i in ii]
    den=determinant(k); nums=[]
    for b in [0,1]:
        a=[row+[(m[i] if i==j else Q(0),)] for i,row in zip(ii,k)]
        a.append([(l[b][i],) for i in ii]+[(Q(0),)])
        nums.append(minus(determinant(a)))
    return nums,den
p,d=prepared(l,m,2);q,e=prepared(r,m,2)
check('K5 all-time preparation via rational Laplace identity',all(times(a,e)==times(b,d) for a,b in zip(p,q)))
# Exhaustive marked subsets within n=2..5, one constructive alternative per subset.
instances=0
for n in range(2,6):
    m=list(map(Q,range(1,n+3)));ii=list(range(2,n+2));base=laplacian(m,{})
    E=matrix(n+2)
    for pos,i in enumerate(ii):
        w=m[i]*(pos+1);E[0][0]+=w;E[i][i]+=w;E[0][i]-=w;E[i][0]-=w
    # One common positive epsilon for ALL hidden pairs, hence all marked subsets.
    transforms={pair:reflection(m,*pair) for pair in combinations(ii,2)}
    Es={pair:congruence(E,t) for pair,t in transforms.items()}
    K=max(abs(e[i][j]) for e in Es.values() for i,j in combinations(range(n+2),2))
    c=min(m[i]*m[j] for i,j in combinations(range(n+2),2));eps=c/(2*(1+K))
    l=[[base[i][j]+eps*E[i][j] for j in range(n+2)] for i in range(n+2)]
    for k in range(n-1):
        for J in combinations(ii,k):
            remaining=[i for i in ii if i not in J];t=transforms[tuple(remaining[:2])];r=congruence(l,t)
            M=[[m[i] if i==j else Q(0) for j in range(n+2)] for i in range(n+2)]
            check(f'n={n},J={J}: isometry, fixed boundary and marks',congruence(M,t)==M and all(sum(row)==1 for row in t) and all(t[i][j]==Q(i==j) for i in range(n+2) for j in [0,1]+list(J)))
            check(f'n={n},J={J}: positive distinct observable pair',valid(l) and valid(r) and l!=r and observation(l,m)==observation(r,m)==n)
            instances+=1
# Necessary hypothesis: same Lambda and one nodal preparation, but not identifiable
# when n=2 observability fails. Boundary expansion DOES distinguish this pair.
def invisible(a):return [[Q(2),Q(-1),Q(-1)],[Q(-1),1+a,-a],[Q(-1),-a,1+a]]
a,b=invisible(Q(1)),invisible(Q(2));m=[Q(1)]*3
check('without observability Lambda identical',transfer_equal(a,b,m,[0]))
check('without observability opening marked node distinguishes',not transfer_equal(a,b,m,[0,1]))
c=[[Q(-1),Q(-1)]]
check('without observability C A=C both, hence C exp(-tA)e1=-exp(-t)',mul(c,block(a,[1,2],[1,2]))==mul(c,block(b,[1,2],[1,2]))==c)
check('without observability spectra differ by traces',a[1][1]+a[2][2]!=b[1][1]+b[2][2])
root=Path(__file__).resolve().parent.parent
out={'status':'PASS','checks':len(checks),'constructed_subset_instances':instances,'finite_range':'all J with |J|<=n-2 for n=2,3,4,5; one constructive pair per J','K5_transfer_method':'exact polynomial determinants over Q[s] and cross multiplication','universal_proof':'separate human-readable audit and REPORT.md; not inferred from finite tests','source_sha256':{name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in ['REPORT.md','verify_marks.py']},'labels':checks}
Path(__file__).with_name('independent_certificate.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='labels'},ensure_ascii=False))
