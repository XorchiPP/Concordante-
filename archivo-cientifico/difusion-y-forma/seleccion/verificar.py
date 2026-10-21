#!/usr/bin/env python3
"""comparación de geometrías: spectral dimension vs. curvature/degree selection.

Original Concordante research continuation, (c) 2026 Xorch.
This is an internal mathematical/computational certificate, not a physics proof.
Requires: numpy, scipy, networkx. Reproducible and deterministic.
"""
from __future__ import annotations
from collections import deque
from hashlib import sha256
from itertools import product
from math import cos, pi
from pathlib import Path
import csv
import json
import numpy as np
import networkx as nx
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parent
TIMES = [0.05, 0.1, 0.25, 0.5, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 24, 32, 48]


def neighbors_generators(kind):
    if kind == 'cycle': return [(1,)]
    if kind == 'triangle2': return [(1,0), (0,1), (1,1)]
    if kind == 'cube3': return [(1,0,0), (0,1,0), (0,0,1)]
    raise ValueError(kind)


def graph(kind, m):
    """Coordinates specify input compatibility, not a pre-installed metric."""
    dirs = neighbors_generators(kind)
    d = len(dirs[0]); vertices = list(product(range(m), repeat=d))
    adj = {x:set() for x in vertices}
    for x in vertices:
        for g in dirs:
            y = tuple((a+b)%m for a,b in zip(x,g))
            if y == x: continue
            adj[x].add(y)
            adj[y].add(x)
    return adj


def edge_set(adj):
    return {tuple(sorted((u,v))) for u,ns in adj.items() for v in ns}


def spectrum_fourier(kind,m):
    angle=2*pi*np.arange(m)/m
    a=2-2*np.cos(angle)
    if kind=='cycle': return a
    if kind=='triangle2':
        p=angle[:,None];q=angle[None,:]
        return (6-2*np.cos(p)-2*np.cos(q)-2*np.cos(p+q)).ravel()
    if kind=='cube3': return (a[:,None,None]+a[None,:,None]+a[None,None,:]).ravel()
    raise ValueError(kind)


def spectrum_numeric(adj):
    verts=list(adj); lookup={v:i for i,v in enumerate(verts)}
    L=np.zeros((len(verts),len(verts)),dtype=float)
    for v,ns in adj.items():
        i=lookup[v];L[i,i]=len(ns)
        for u in ns:L[i,lookup[u]]=-1
    return np.linalg.eigvalsh(L)


def heat_stats(lam,t):
    # subtract min eigenvalue for numerical stability
    weights=np.exp(-t*(lam-np.min(lam)))
    mean_lam=np.dot(lam,weights)/weights.sum()
    k_trace=np.exp(-t*np.min(lam))*weights.sum()
    return {'heat_trace':float(k_trace),'normalized_return':float(k_trace/len(lam)),
            'spectral_dimension':float(2*t*mean_lam)}


def distances_to(adj,src):
    dist={src:0};q=deque([src])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in dist:dist[y]=dist[x]+1;q.append(y)
    return dist


def kappa(adj, x, y):
    """Ollivier curvature, idleness=0, cost=shortest-path metric."""
    px=sorted(adj[x]); py=sorted(adj[y]); na=len(px);nb=len(py)
    D={z:distances_to(adj,z) for z in px}
    cost=np.array([D[u][v] for u in px for v in py],dtype=float)
    constraints=np.zeros((na+nb,na*nb),dtype=float)
    for i in range(na):constraints[i,i*nb:(i+1)*nb]=1
    for j in range(nb):constraints[na+j,j::nb]=1
    res=linprog(cost,A_eq=constraints,b_eq=[1/na]*na+[1/nb]*nb,
               bounds=(0,None),method='highs',options={'dual_feasibility_tolerance':1e-9})
    assert res.success,(x,y,res.message)
    return float(1-res.fun)


def kappa_all(adj):
    return np.array([kappa(adj,x,y) for x,y in sorted(edge_set(adj))])


def coarse_graph(adj):
    m = max(v[0] for v in adj)+1
    assert m%2==0
    mapped = lambda u:tuple(k//2 for k in u)
    projected={mapped(v):set() for v in adj}
    for (u,v) in edge_set(adj):
        U,V=mapped(u),mapped(v)
        if U!=V:
            projected[U].add(V)
            projected[V].add(U)
    return projected


def as_adjacency(nxg):
    return {v:set(nxg[v]) for v in nxg.nodes}


def experiment():
    data={
       'status':'PASS_INTERNAL_VERIFICATION',
       'version':'comparación de geometrías',
       'date':'2026-10-21',
       'provenance':'Concordante original research continuation; includes previously known mathematics',
       'copyright':'Concordante Lab · Xorch. © 2026. Todos los derechos reservados.',
       'conventions':{'laplacian':'combinatorial D-A','time':'continuous diffusion time',
                      'ricci':'Ollivier, idleness 0, neighbor-uniform measures, shortest-path ground metric',
                      'edge_weight':'1'},
       'tests':{}, 'spectral':{}, 'coarse':{}, 'curvature':{},'guards':[]
    }
    # Exact transform diagonalization independently verified against matrix eigenvalues.
    checks={}
    for kind,m in [('cycle',11),('triangle2',8),('cube3',5)]:
        A=graph(kind,m)
        direct=spectrum_numeric(A)
        analytic=np.sort(spectrum_fourier(kind,m))
        err=float(np.max(abs(direct-analytic)))
        assert err<1e-10,(kind,err)
        checks[kind]={'m':m,'vertices':len(A),'max_eigenspectrum_abs_error':err}
    data['tests']['independent_eigenvalue_checks']=checks

    # All graph families same size; triangular 2D and cubic 3D even have same degree and |E|.
    comparison=[('cycle',4096,1),('triangle2',64,2),('cube3',16,3)]
    for kind,m,d in comparison:
        lam=spectrum_fourier(kind,m)
        adj=graph(kind,m)
        n=len(adj);E=len(edge_set(adj)); deg={len(ns) for ns in adj.values()}
        assert len(deg)==1
        stats={str(t):heat_stats(lam,t) for t in TIMES}
        plateau={str(t):stats[str(t)]['spectral_dimension'] for t in [4,5,6,8]}
        data['spectral'][kind]={'n':n,'m':m,'dimension_of_periodic_generator':d,
                               'degree':next(iter(deg)),'edges':E,
                               'plateau_4_8':plateau,'by_time':stats}
        assert n==4096
        assert max(abs(x-d) for x in plateau.values())<0.12,(kind,plateau)
    assert all(data['spectral'][k]['edges']==12288 for k in ['triangle2','cube3'])
    assert all(data['spectral'][k]['degree']==6 for k in ['triangle2','cube3'])

    # Collapse blocks b=2. Exact output adjacency, not a spectral-clustering approximation.
    for kind,m in [('cycle',64),('triangle2',64),('cube3',16)]:
        before=graph(kind,m)
        after=coarse_graph(before)
        truth=graph(kind,m//2)
        assert after==truth,(kind,len(edge_set(after)^edge_set(truth)))
        data['coarse'][kind]={'input_n':len(before),'output_n':len(after),
            'input_m':m,'output_m':m//2,'is_exact_same_lattice_family':True,
            'd_s_at_t6_after':heat_stats(spectrum_fourier(kind,m//2),6)['spectral_dimension'],
            'd_s_at_t6_before':heat_stats(spectrum_fourier(kind,m),6)['spectral_dimension']}

    # Exact zero Ollivier curvature is detected numerically on all edge direction types.
    for kind,m in [('cycle',4096),('triangle2',64),('cube3',16)]:
        adj=graph(kind,m)
        x=(0,)*len(next(iter(adj)))
        cases=[]
        for g in neighbors_generators(kind):
            y=tuple((a+b)%m for a,b in zip(x,g))
            kap=kappa(adj,x,y)
            cases.append({'displacement':g,'wasserstein_W1':1-kap,'kappa':kap})
            assert abs(kap)<1e-8,(kind,kap)
        data['curvature'][kind]={'tested_generator_edge_types':cases,
                                'all_edges_zero_by_translation_and_point_symmetries':True,
                                'sum_kappa':0.0}
    # Finite, fixed-n comparison: naive signed action doesn't select flat graphs.
    small={
        'cycle10':nx.cycle_graph(10),
        'petersen10':nx.petersen_graph(),
        'complete10':nx.complete_graph(10)
    }
    for name,raw in small.items():
        values=kappa_all(as_adjacency(raw))
        data['curvature'][name]={'vertices':raw.number_of_nodes(),
            'edges':raw.number_of_edges(),'curvature_min':float(values.min()),
            'curvature_max':float(values.max()),'signed_action_sum':float(sum(values))}
    assert abs(data['curvature']['cycle10']['signed_action_sum'])<1e-9
    assert abs(data['curvature']['petersen10']['signed_action_sum']+5)<1e-9
    assert abs(data['curvature']['complete10']['signed_action_sum']-40)<1e-9

    # At fixed n=64 and degree 6, a random regular compatibility graph can beat
    # the curvature action of a flat triangular torus without exhibiting a 2D/3D plateau.
    data['curvature']['same_n64_degree6_random_controls']={}
    for seed in [3,7,19]:
        g=nx.random_regular_graph(6,64,seed=seed)
        adj=as_adjacency(g)
        ric=kappa_all(adj)
        ds6=heat_stats(spectrum_numeric(adj),6)['spectral_dimension']
        sumric=float(sum(ric))
        assert sumric < -70,(seed,sumric)
        assert ds6<0.01,(seed,ds6)
        data['curvature']['same_n64_degree6_random_controls'][str(seed)]={
            'n':64,'degree':6,'edges':192,'signed_action_sum':sumric,
            'mean_edge_curvature':float(np.mean(ric)),
            'spectral_dimension_at_t6':ds6,
            'graph_random_seed':seed}
    flat64=graph('triangle2',8)
    flatric=kappa_all(flat64)
    assert max(abs(flatric)) < 1e-9
    data['curvature']['same_n64_degree6_flat_triangular_control']={
        'n':64,'degree':6,'edges':192,
        'signed_action_sum':float(sum(flatric)),
        'spectral_dimension_at_t6':heat_stats(spectrum_fourier('triangle2',8),6)['spectral_dimension']}

    # Normalized vs combinatorial Laplacian for fixed-regular graphs changes diffusion time scale.
    for kind in ['triangle2','cube3']:
        lam=spectrum_fourier(kind, data['spectral'][kind]['m'])
        k=data['spectral'][kind]['degree'];t=6.0
        normalized=heat_stats(lam/k,t)['spectral_dimension']
        rescaled=heat_stats(lam,t/k)['spectral_dimension']
        assert abs(normalized-rescaled)<1e-12
        data['tests']['operator_normalization_'+kind]={'d_s_normalized_at_t6':normalized,
            'd_s_combinatorial_at_t1':rescaled, 'equal_by_exact_rescaling':True}

    data['guards']=[
       'No graph ensemble, variational measure or renormalization dynamics has been selected.',
       'Equal idleness-0 Ollivier curvature and equal size/degree do not fix spectral dimension.',
       'Coarse contraction reduces m without selecting spatial dimension.',
       'Finite graphs have spectral dimension approaching zero in both t limits.',
       'Cubic torus graph has spectral dimension near 3 but its unfilled clique complex is 1D.',
       'Graph Laplacian generator is canonical only after choosing a diffusion convention.',
       'Not empirical evidence for 3+1 spacetime or quantum gravity.'
    ]
    data['tests']['n10_Petersen_wins_signed_action_over_cycle_and_complete']=True
    return data


def write_data(data):
    path=ROOT/'certificado_historico.json'
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    with (ROOT/'dimension_espectral.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['time','cycle_n4096','triangular_torus_n4096','cubic_torus_n4096'])
        for t in TIMES:
            w.writerow([t]+[data['spectral'][k]['by_time'][str(t)]['spectral_dimension']
                               for k in ['cycle','triangle2','cube3']])
    print('PASS: numerical spectra, 2-block coarse quotients, curvature LP, finite-scale dimensions')
    print('Plateau at t=6:',{k:round(data['spectral'][k]['plateau_4_8']['6'],6) for k in ['cycle','triangle2','cube3']})
    print('Zero curvature 2D/3D:', data['curvature']['triangle2']['sum_kappa'],data['curvature']['cube3']['sum_kappa'])
    print('Petersen vs cycle/complete actions:', {k:v['signed_action_sum'] for k,v in data['curvature'].items() if k in ['cycle10','petersen10','complete10']})

if __name__=='__main__':
    write_data(experiment())
