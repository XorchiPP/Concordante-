#!/usr/bin/env python3
"""Compatibility relations and graph geometry.
Concordante Lab · Xorch · © 2026. All rights reserved.
Finite computations with explicit mathematical selection assumptions.
"""
from math import log2, cos, pi
import json
import numpy as np


def graph_from_edges(n, edges):
    E = {tuple(sorted((int(u), int(v)))) for u, v in edges if u != v}
    assert all(0 <= u < n and 0 <= v < n for u, v in E)
    adj = [set() for _ in range(n)]
    for u, v in E:
        adj[u].add(v)
        adj[v].add(u)
    return adj, sorted(E)


def cycle(m):
    return graph_from_edges(m, ((i, (i+1) % m) for i in range(m)))


def triangular_torus(m):
    # Coordinates generate the INPUT relation only. All measurements use adj.
    E = []
    for a in range(m):
        for b in range(m):
            u = a*m+b
            for da, db in ((1, 0), (0, 1), (1, 1)):
                v = ((a+da) % m)*m + ((b+db) % m)
                E.append((u, v))
    return graph_from_edges(m*m, E)


def balls(adj, start, max_r):
    seen = {start}
    frontier = {start}
    sizes = [1]
    for r in range(1, max_r+1):
        frontier = set().union(*(adj[x] for x in frontier)) - seen
        seen |= frontier
        sizes.append(len(seen))
    return sizes


def tri_and_k4(adj):
    n = len(adj)
    triangles=[]
    k4=[]
    for i in range(n):
        for j in adj[i]:
            if j <= i: continue
            for k in (adj[i] & adj[j]):
                if k <= j: continue
                triangles.append((i,j,k))
                for l in (adj[i] & adj[j] & adj[k]):
                    if l > k: k4.append((i,j,k,l))
    return sorted(triangles), sorted(k4)


def gf2_rank(masks):
    pivot = {}
    for z in masks:
        while z:
            i = z.bit_length()-1
            if i in pivot: z ^= pivot[i]
            else:
                pivot[i] = z
                break
    return len(pivot)


def homology_mod2(adj, edges):
    n = len(adj)
    ts, k4=tri_and_k4(adj)
    edge_id={e:idx for idx,e in enumerate(edges)}
    # Boundary1: each edge has two endpoint bits.
    boundary1=[(1<<u)^(1<<v) for u,v in edges]
    r1=gf2_rank(boundary1)
    boundary2=[]
    for i,j,k in ts:
        mask=0
        for e in ((i,j),(i,k),(j,k)):
            mask ^= (1<<edge_id[e])
        boundary2.append(mask)
    r2=gf2_rank(boundary2)
    # For the examples, max clique size = 3, hence C3=0.
    assert len(k4)==0, 'Higher chains present: adjust b2 formula'
    assert len(adj) - r1==1, 'Graphs must be connected'
    return {'vertices':n,'edges':len(edges),'triangles':len(ts),'four_cliques':len(k4),
            'rank_boundary_1':r1,'rank_boundary_2':r2,
            'betti_F2':[n-r1,len(edges)-r1-r2,len(ts)-r2]}


def laplacian(adj):
    n=len(adj)
    mat=np.zeros((n,n))
    for i,N in enumerate(adj):
        mat[i,i]=len(N)
        for j in N: mat[i,j]=-1
    return mat


def heat_and_unitary_test(adj, t=0.67):
    L=laplacian(adj)
    evals, vecs=np.linalg.eigh(L)
    P=(vecs*np.exp(-t*evals))@vecs.T
    U=(vecs*np.exp(-1j*t*evals))@vecs.T
    tol=3e-11
    errors={
        'laplacian_min_eigenvalue':float(evals[0]),
        'laplacian_max_eigenvalue':float(evals[-1]),
        'heat_row_sum_error':float(np.max(abs(P.sum(axis=1)-1))),
        'heat_column_sum_error':float(np.max(abs(P.sum(axis=0)-1))),
        'heat_min_entry':float(P.min()),
        'unitarity_error':float(np.max(abs(U.conj().T@U-np.eye(len(adj)))))
    }
    assert evals[0]>-tol
    assert errors['heat_row_sum_error']<tol
    assert errors['heat_column_sum_error']<tol
    assert errors['heat_min_entry']>-tol
    assert errors['unitarity_error']<tol
    return errors


def unitary_nonuniqueness():
    adj,_=graph_from_edges(3,[(0,1),(1,2)])
    L=laplacian(adj)
    D=np.diag([len(N) for N in adj]);A=D-L
    def evolved(H):
        w,v=np.linalg.eigh(H)
        U=(v*np.exp(-1j*w))@v.T
        return [float(abs(z)**2) for z in U[:,0]]
    pL=evolved(L)
    pA=evolved(A)
    assert max(abs(a-b) for a,b in zip(pL,pA))>0.01
    return {'initial':0,'t':1,'H_equals_L':pL,'H_equals_A':pA,
            'max_difference':max(abs(a-b) for a,b in zip(pL,pA))}


def reverses_edge_under_automorphism(adj, permutation, u, v):
    n = len(adj)
    p = [permutation(i) for i in range(n)]
    assert sorted(p) == list(range(n)), 'Not a permutation'
    assert all({p[j] for j in adj[i]} == adj[p[i]] for i in range(n))
    assert p[u] == v and p[v] == u
    return True


def topological_gauge_counts(h):
    independent_graph_loops = h['edges'] - h['vertices'] + 1
    independent_flat_loops = independent_graph_loops - h['rank_boundary_2']
    assert independent_flat_loops == h['betti_F2'][1]
    return {'U1_unconstrained_edge_connections_mod_gauge_dim': independent_graph_loops,
            'independent_triangle_flatness_conditions':h['rank_boundary_2'],
            'U1_flat_connections_mod_gauge_dim_if_torsion_free': independent_flat_loops}


def experiment():
    c11,E11=cycle(11)
    t11,Et11=triangular_torus(11)
    hc=homology_mod2(c11,E11)
    ht=homology_mod2(t11,Et11)
    vc=balls(c11,0,4)
    vt=balls(t11,0,4)
    assert vc == [1,3,5,7,9], vc
    assert vt == [1,7,19,37,61], vt
    assert hc['betti_F2']==[1,1,0]
    assert ht['betti_F2']==[1,2,1]
    assert (ht['vertices'],ht['edges'],ht['triangles'],ht['four_cliques'])==(121,363,242,0)
    C101,_=cycle(101)
    T101,_=triangular_torus(101)
    vC101=balls(C101,0,20)
    vT101=balls(T101,0,20)
    for r in (5,10,20):
        assert vC101[r] == 2*r+1
        assert vT101[r] == 1+3*r*(r+1)
    doubling={
        str(r):{'cycle_101':log2(vC101[2*r]/vC101[r]),
                'triangular_torus_101':log2(vT101[2*r]/vT101[r])}
        for r in (5,10)
    }
    assert reverses_edge_under_automorphism(c11,lambda v:(1-v)%11,0,1)
    assert reverses_edge_under_automorphism(t11,
           lambda v:((1-v//11)%11)*11+((-v%11)%11),0,11)
    heat=heat_and_unitary_test(c11)
    heat2=heat_and_unitary_test(t11)
    # Fourier-mode spectrum of C11 agrees with the combinatorial Laplacian.
    spectrum=np.linalg.eigvalsh(laplacian(c11))
    expected=sorted(2-2*cos(2*pi*k/11) for k in range(11))
    assert np.max(abs(spectrum-expected))<1e-11
    return {'status':'PASS_INTERNAL_COMPUTATIONAL_CHECKS',
            'model':'finite connected symmetric binary compatibility',
            'cycle11':dict(hc,balls_r_0_4=vc,operators=heat,gauge_counts=topological_gauge_counts(hc),edge_reversal_symmetry=True),
            'triangular_torus11':dict(ht,balls_r_0_4=vt,operators=heat2,gauge_counts=topological_gauge_counts(ht),edge_reversal_symmetry=True),
            'doubling_scale_101':doubling,
            'nonunique_quantum_dynamics_path3':unitary_nonuniqueness(),
            'guards':['internal computations only','known graph theory constructions',
                      'physical selection requires additional hypotheses','no unique dimension for arbitrary relation',
                      'gauge phases and time orientation require selection assumptions']}

if __name__=='__main__':
    print(json.dumps(experiment(),ensure_ascii=False,sort_keys=True,indent=2))
