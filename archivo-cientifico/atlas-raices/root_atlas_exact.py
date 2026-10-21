"""Exact finite root-system atlas over Q(phi), phi^2 = phi + 1.

H3/H4 are non-crystallographic finite reflection systems.
Includes a reflection example with explicit unevaluated metadata.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product
import re
from typing import Iterable


@dataclass(frozen=True)
class QPhi:
    """Exact a + b*phi, with phi^2 = phi + 1."""
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', Fraction(self.a))
        object.__setattr__(self, 'b', Fraction(self.b))

    @staticmethod
    def of(v: QPhi | int | Fraction) -> QPhi:
        return v if isinstance(v, QPhi) else QPhi(Fraction(v))

    def __add__(self, rhs):
        x = self.of(rhs)
        return QPhi(self.a + x.a, self.b + x.b)

    __radd__ = __add__

    def __neg__(self):
        return QPhi(-self.a, -self.b)

    def __sub__(self, rhs):
        return self + (-self.of(rhs))

    def __rsub__(self, lhs):
        return self.of(lhs) - self

    def __mul__(self, rhs):
        x = self.of(rhs)
        return QPhi(self.a*x.a + self.b*x.b,
                    self.a*x.b + self.b*x.a + self.b*x.b)

    __rmul__ = __mul__

    def conjugate(self):
        # phi' = 1 - phi
        return QPhi(self.a+self.b, -self.b)

    def __truediv__(self, rhs):
        x = self.of(rhs)
        if x == QPhi():
            raise ZeroDivisionError
        norm = x.a*x.a + x.a*x.b - x.b*x.b
        c = x.conjugate()
        return self*c*(Fraction(1)/norm)

    def __rtruediv__(self, lhs):
        return self.of(lhs)/self

    def is_integer(self) -> bool:
        return self.b == 0 and self.a.denominator == 1

    def __str__(self):
        return f'({self.a}+{self.b}phi)'


ZERO, ONE, HALF, PHI = QPhi(), QPhi(1), QPhi(Fraction(1,2)), QPhi(0,1)
V = tuple[QPhi, ...]


def vec(coords: Iterable[QPhi | int | Fraction]) -> V:
    return tuple(QPhi.of(x) for x in coords)


def dot(a: V, b: V) -> QPhi:
    if len(a) != len(b):
        raise ValueError('dimension mismatch')
    return sum((x*y for x,y in zip(a,b)), ZERO)


def reflect(v: V, alpha: V) -> V:
    if len(v) != len(alpha):
        raise ValueError('dimension mismatch')
    denom = dot(alpha, alpha)
    if denom == ZERO:
        raise ValueError('zero reflection normal')
    k = 2*dot(v,alpha)/denom
    return tuple(v_i-k*a_i for v_i,a_i in zip(v,alpha))


def cartan_pair(beta: V, alpha: V) -> QPhi:
    """2(beta,alpha)/(alpha,alpha); alpha is the coroot denominator."""
    return 2*dot(beta,alpha)/dot(alpha,alpha)


def basis(i: int, n: int) -> V:
    return vec(int(j==i) for j in range(n))


def sign_roots(n: int, include_axes: bool, include_pairs: bool, axes_scale=1):
    roots = set()
    if include_axes:
        for i in range(n):
            for s in (-1,1):
                roots.add(vec(s*axes_scale*int(j==i) for j in range(n)))
    if include_pairs:
        for i,j in combinations(range(n),2):
            for s,t in product((-1,1),repeat=2):
                roots.add(vec(s*int(k==i)+t*int(k==j) for k in range(n)))
    return roots


def even_permutations(seq):
    for p in permutations(range(len(seq))):
        inversions = sum(p[i]>p[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
        if inversions%2==0:
            yield tuple(seq[i] for i in p)


def root_atlas(name: str) -> frozenset[V]:
    """Classical A_n/B_n/C_n/D_n (n<=8), E6/7/8, F4, G2, H3/4."""
    roots: set[V] = set()
    family = re.fullmatch(r'([ABCD])([0-9]+)',name)
    if family:
        typ, rank = family.group(1), int(family.group(2))
        if not (1 <= rank <= 8) or (typ in ('B','C') and rank < 2) or (typ=='D' and rank<4):
            raise ValueError('supported ranks: 1<=A<=8, 2<=B,C<=8, 4<=D<=8')
        if typ=='A':
            n=rank+1
            for i in range(n):
                for j in range(n):
                    if i!=j:
                        roots.add(tuple(basis(i,n)[k]-basis(j,n)[k] for k in range(n)))
        elif typ=='B':
            roots=sign_roots(rank,True,True)
        elif typ=='C':
            roots=sign_roots(rank,True,True,axes_scale=2)
        else:
            roots=sign_roots(rank,False,True)
    elif name=='F4':
        roots = sign_roots(4, True, True)
        for signs in product((-1,1),repeat=4):
            roots.add(vec(Fraction(s,2) for s in signs))
    elif name=='G2':
        for i in range(3):
            for j in range(3):
                if i!=j:
                    roots.add(tuple(basis(i,3)[k]-basis(j,3)[k] for k in range(3)))
        for i in range(3):
            roots.add(vec(2*int(k==i)-int(k!=i) for k in range(3)))
            roots.add(vec(-2*int(k==i)+int(k!=i) for k in range(3)))
    elif name in {'E6','E7','E8'}:
        roots = sign_roots(8, False, True)
        for signs in product((-1,1),repeat=8):
            if sum(s<0 for s in signs)%2==0:
                roots.add(vec(Fraction(s,2) for s in signs))
        if name in {'E6','E7'}:
            a=tuple(basis(0,8)[k]-basis(1,8)[k] for k in range(8))
            roots={v for v in roots if dot(v,a)==ZERO}
        if name=='E6':
            b=tuple(basis(1,8)[k]-basis(2,8)[k] for k in range(8))
            roots={v for v in roots if dot(v,b)==ZERO}
    elif name in {'H3','H4'}:
        roots = sign_roots(4, True, False)
        for signs in product((-1,1),repeat=4):
            roots.add(vec(Fraction(s,2) for s in signs))
        abc=(ZERO, HALF, PHI/2, (PHI-ONE)/2)
        for positions in even_permutations(abc):
            nz=[i for i,x in enumerate(positions) if x!=ZERO]
            for signs in product((-1,1),repeat=3):
                v=list(positions)
                for i,s in zip(nz,signs):
                    v[i]=v[i]*s
                roots.add(tuple(v))
        if name=='H3':
            roots={v for v in roots if v[0]==ZERO}
    else:
        raise KeyError(name)
    return frozenset(roots)


def antipodal_lines(roots: frozenset[V]) -> int:
    if any(tuple(-x for x in v) not in roots for v in roots):
        raise AssertionError('roots must be antipodal')
    return len(roots)//2


def reflection_closed(roots: frozenset[V], normals: Iterable[V] | None = None) -> bool:
    for alpha in (roots if normals is None else normals):
        for beta in roots:
            if reflect(beta,alpha) not in roots:
                return False
    return True


def crystallographic(roots: frozenset[V], normals: Iterable[V] | None = None) -> bool:
    for alpha in (roots if normals is None else normals):
        for beta in roots:
            if not cartan_pair(beta,alpha).is_integer():
                return False
    return True


def length_shells(roots: frozenset[V]) -> dict[QPhi,int]:
    result = {}
    for v in roots:
        n = dot(v,v)
        result[n] = result.get(n,0)+1
    return result


def failure_certificate(roots: frozenset[V]) -> tuple[V,V,QPhi] | None:
    for alpha in roots:
        for beta in roots:
            c=cartan_pair(beta,alpha)
            if not c.is_integer():
                return (beta,alpha,c)
    return None

@dataclass(frozen=True)
class RootMoveEvidence:
    """A mathematical readout; never grants permission to act."""
    system: str
    alpha: V
    before: V
    after: V
    metric_preserved: bool
    atlas_preserved: bool
    certificate: str = 'EXACT_LOCAL_COORDINATE_CHECK'
    semantic_transport: str = 'NOT_TESTED'
    action_eligibility: str = 'NOT_EVALUATED'
    authority: str = 'NOT_EVALUATED'


def preview_root_move(system: str, alpha: V, before: V) -> RootMoveEvidence:
    """Propose s_alpha(before); only math is verified, never agent policy."""
    roots = root_atlas(system)
    if alpha not in roots or before not in roots:
        raise ValueError('alpha and before must be roots of the selected atlas')
    after = reflect(before,alpha)
    return RootMoveEvidence(
        system=system, alpha=alpha, before=before, after=after,
        metric_preserved=(dot(after,after)==dot(before,before)),
        atlas_preserved=(after in roots),
    )


def _encoded_phi_vectors(roots: frozenset[V]):
    """Represent 2*v over Z[phi]. Atlas coordinates have half-integer parts."""
    result = set()
    for v in roots:
        encoded = []
        for x in v:
            aa, bb = 2*x.a, 2*x.b
            if aa.denominator != 1 or bb.denominator != 1:
                raise ValueError('expected coordinates in (1/2)Z[phi]')
            encoded.append((int(aa), int(bb)))
        result.add(tuple(encoded))
    return result


def _mul_zphi(x: tuple[int,int], y: tuple[int,int]) -> tuple[int,int]:
    a,b = x
    c,d = y
    return (a*c+b*d, a*d+b*c+b*d)


def _dot_zphi(x,y) -> tuple[int,int]:
    aa=bb=0
    for u,v in zip(x,y):
        a,b=_mul_zphi(u,v)
        aa+=a
        bb+=b
    return aa,bb


def reflection_closed_full_exact(roots: frozenset[V]) -> bool:
    """Exhaustive exact check for ALL normals and ALL roots via Z[phi].

    Each atlas is half-integral over Z[phi] and all Cartan pairs lie in
    Z[phi]. This is an independent, integer-only cross-check of reflect().
    """
    r=_encoded_phi_vectors(roots)
    for alpha in r:
        na,nb=_dot_zphi(alpha,alpha)
        if na<=0 or nb!=0:
            raise ValueError('expected rational positive squared norm')
        for beta in r:
            da,db=_dot_zphi(beta,alpha)
            ka,ra=divmod(2*da,na)
            kb,rb=divmod(2*db,na)
            if ra!=0 or rb!=0:
                return False
            moved=[]
            for (va,vb),(aa,ab) in zip(beta,alpha):
                pa,pb=_mul_zphi((ka,kb),(aa,ab))
                moved.append((va-pa,vb-pb))
            if tuple(moved) not in r:
                return False
    return True


def crystallographic_full_exact(roots: frozenset[V]) -> bool:
    """All pairs: Cartan coefficients integral iff each phi part vanishes."""
    r=_encoded_phi_vectors(roots)
    for alpha in r:
        na,nb=_dot_zphi(alpha,alpha)
        if na<=0 or nb!=0:
            raise ValueError('expected rational positive squared norm')
        for beta in r:
            da,db=_dot_zphi(beta,alpha)
            if (2*da)%na or db:
                return False
    return True
