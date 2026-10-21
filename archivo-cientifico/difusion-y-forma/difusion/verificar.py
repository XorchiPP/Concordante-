#!/usr/bin/env python3
"""difusión a escala finita / Freudenthal flag torus, heat RG and selection falsifiers.
Concordante Lab · Xorch. © 2026. Todos los derechos reservados..  Research only, not a physical law.
Run: python verificar.py   Dependencies: numpy, scipy, networkx, matplotlib.
"""
from __future__ import annotations
import csv, itertools, json, math, hashlib
from pathlib import Path
from collections import Counter, defaultdict
import numpy as np
import networkx as nx
from scipy.optimize import linprog

ROOT=Path(__file__).resolve().parent
DIRECTIONS={
    'cycle1':[(1,)],
    'tri2':[(1,0),(0,1),(1,1)],
    'cube3':[(1,0,0),(0,1,0),(0,0,1)],
    'flag3':[v for v in itertools.product((0,1),repeat=3) if any(v)]
}

def graph(family, m):
    dirs=DIRECTIONS[family]; d=len(dirs[0]); vertices=list(itertools.product(range(m), repeat=d))
    adj={x:set() for x in vertices}
    for x in vertices:
        for g in dirs:
            y=tuple((x[j]+g[j])%m for j in range(d));adj[x].add(y);adj[y].add(x)
    for x in adj:adj[x].discard(x)
    return adj

def spectrum(family,m):
    a=2*np.pi*np.arange(m)/m
    if family=='cycle1':return 2-2*np.cos(a)
    if family=='cube3':
        return ((2-2*np.cos(a))[:,None,None]+(2-2*np.cos(a))[None,:,None]+(2-2*np.cos(a))[None,None,:]).ravel()
    if family=='tri2':
        p,q=np.meshgrid(a,a,indexing='ij')
        return (6-2*(np.cos(p)+np.cos(q)+np.cos(p+q))).ravel()
    if family=='flag3':
        p,q,r=np.meshgrid(a,a,a,indexing='ij')
        return (14-2*(np.cos(p)+np.cos(q)+np.cos(r)+np.cos(p+q)+np.cos(p+r)+np.cos(q+r)+np.cos(p+q+r))).ravel()
    raise ValueError(family)

def trace_ds(lam,t):
    w=np.exp(-t*lam); k=float(np.sum(w));ds=float(2*t*np.dot(lam,w)/k)
    return k,ds

def nxgraph(adj):
    g=nx.Graph();g.add_nodes_from(adj)
    g.add_edges_from((u,v) for u, neighbors in adj.items() for v in neighbors)
    return g

def clique_data(adj):
    cliques=list(nx.enumerate_all_cliques(nxgraph(adj)))
    groups={}
    for c in cliques:groups.setdefault(len(c)-1,[]).append(tuple(sorted(c)))
    assert max(groups)==3
    ranks={}
    for k in range(1,4):
        index={v:i for i,v in enumerate(groups[k-1])};base={}
        for c in groups[k]:
            col=0
            for face in itertools.combinations(c,k):col ^=1 << index[face]
            while col:
                pivot=col.bit_length()-1
                if pivot in base:col ^=base[pivot]
                else:base[pivot]=col;break
        ranks[k]=len(base)
    betti=[len(groups[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(4)]
    return groups,ranks,betti

def verify_vertex_link(groups,root=(0,0,0)):
    # In a 3-complex, vertices/edges/triangles of the 2D link correspond
    # to edges/triangles/tetrahedra through root, with root removed.
    link=[[] for _ in range(3)]
    for k in (1,2,3):
        link[k-1]=[tuple(v for v in simplex if v!=root)
                   for simplex in groups[k] if root in simplex]
    assert [len(x) for x in link]==[14,36,24]
    lverts=set(v for t in link[0] for v in t)
    ledges=[tuple(sorted(x)) for x in link[1]]
    ltris=[tuple(sorted(x)) for x in link[2]]
    assert len(set(lverts))==14 and len(set(ledges))==36 and len(set(ltris))==24
    ef=Counter(e for tr in ltris for e in itertools.combinations(tr,2))
    assert set(ef)==set(ledges) and set(ef.values())=={2}
    lgraph=nx.Graph();lgraph.add_nodes_from(lverts);lgraph.add_edges_from(ledges)
    assert nx.is_connected(lgraph)
    # In each vertex link inside the link, each link vertex has a connected
    # cycle of incident triangles (checks the 2-manifold condition).
    for v in lverts:
        around=nx.Graph()
        for tri in ltris:
            if v in tri:
                other=[u for u in tri if u!=v];around.add_edge(other[0],other[1])
        assert nx.is_connected(around) and all(deg==2 for _,deg in around.degree())
    assert 14-36+24==2
    return {'f_vector':[14,36,24], 'euler':2,'edge_face_incidence':2,
            'connected':True,'surface_link':'S2 by compact connected surface classification'}

def waterstein_curvature(adj, src, dst):
    from collections import deque
    def dist(start):
        seen={start:0};queue=deque([start])
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if v not in seen:seen[v]=seen[u]+1;queue.append(v)
        return seen
    a=sorted(adj[src]);b=sorted(adj[dst]);na=len(a);nb=len(b)
    distances=[dist(x) for x in a]
    c=np.array([distances[i][b[j]] for i in range(na) for j in range(nb)],dtype=float)
    A=np.zeros((na+nb,na*nb))
    for i in range(na):A[i,i*nb:(i+1)*nb]=1
    for j in range(nb):A[na+j,j::nb]=1
    opt=linprog(c,A_eq=A,b_eq=[1/na]*na+[1/nb]*nb,bounds=(0,None),method='highs')
    assert opt.success
    return 1-float(opt.fun)

def random_ensemble(n=64,degree=6,count=80, seedoffset=0):
    ds_lams=[]
    for seed in range(seedoffset,seedoffset+count):
        G=nx.random_regular_graph(degree,n,seed=seed)
        assert nx.is_connected(G)
        L=degree*np.eye(n)-nx.to_numpy_array(G)
        ds_lams.append(np.linalg.eigvalsh(L))
    return ds_lams

def compute():
    result={'id':'difusión a escala finita','date':'2026-10-21','author':'Xorch','status':'INTERNAL_VERIFIED_NO_CANON',
        'copyright':'Concordante Lab · Xorch. © 2026. Todos los derechos reservados.',
        'methods':'Fourier Laplacian / mod-2 incidence boundary ranks / transport LP / seeded regular graph controls',
        'prior_work':['comparación de geometrías','relaciones de compatibilidad','estudio previo de dimensión y escala','estudio previo de entropía y resolución'],
        'D1':{},'D2':{},'D3':{},'D4':{},'tests':{}}
    a16=spectrum('cube3',16);a8=spectrum('cube3',8)
    rows=[]
    for t in [6,12,24,48]:
        kf,df=trace_ds(a16,t);kc,dc=trace_ds(a8,t/4)
        rows.append({'fine_heat_time':t,'coarse_heat_time':t/4,'fine_ds':df,'coarse_ds':dc,'difference':dc-df,
                     'fine_trace':kf,'coarse_trace':kc})
    result['D1']['physical_time_comparison']=rows
    l16=2-2*np.cos(2*np.pi/16);l8=2-2*np.cos(2*np.pi/8)
    result['D1']['nonexact_lowest_mode']={'fine_lambda':float(l16),'coarse_lambda':float(l8),'ratio':float(l8/l16)}
    assert abs(l8/l16-4)>0.01
    assert abs(rows[0]['difference']-0.3449146834822243)<1e-10
    result['D1']['K_at_t0']={'fine':4096,'coarse':512}
    result['D1']['cannot_have_full_trace_identity']=True
    # n4096 degree6 matched pair. Same derivative order 0,1,2; triangle motif enters third.
    g2=spectrum('tri2',64);g3=spectrum('cube3',16)
    for degree in (0,1,2):
        assert abs(sum(g2**degree)-sum(g3**degree))<1e-7
    n=4096;E=12288;T2=2*E//3
    assert abs((sum(g2**3)-sum(g3**3))+6*T2)<1e-6
    spectra=[]
    for t in [0.01,0.05,0.1,0.25,0.5,1,2,4,6,10,16,24,48]:
        a,b=trace_ds(g2,t),trace_ds(g3,t)
        spectra.append({'t':t,'Lambda':t**(-0.5),'trace_2D':a[0],'trace_3D':b[0],
                        'difference_2D_minus_3D':a[0]-b[0], 'ds_2D':a[1],'ds_3D':b[1]})
        assert a[0]>b[0]
    result['D2']={'spectral_action':'Tr exp(-t L), t=1/Lambda^2, graph heat trace (not automatically a Connes spectral triple)',
        'scan':spectra,'triangles_2D':T2,'triangles_3D':0,
        'small_t_difference_leading_coefficient':float(T2),
        'explanation':'Delta K = 8192 t^3 + O(t^4), since trace A^3 is 6 times triangle count; not a proof that K2>K3 for every positive t.',
        'Lambda_minimization':'K(t) grows with Lambda and 1<=K<=N, so optimizing cutoff alone is degenerate.'}
    # small N64 sampled ensemble fixed (N, degree, edges); not a phase transition/thermodynamic limit.
    n=64;Gtri=spectrum('tri2',8);Gcube=spectrum('cube3',4)
    pool=random_ensemble(count=80)
    sample_t=[]
    for t in [0.1,0.25,0.5,1,2,3,4]:
        h=np.array([trace_ds(x,t)[0] for x in pool]);ds=np.array([trace_ds(x,t)[1] for x in pool])
        item={'t':t,'triangle_K':trace_ds(Gtri,t)[0],'cube_K':trace_ds(Gcube,t)[0],
              'random_K_min':float(h.min()),'random_K_median':float(np.median(h)),
              'random_K_max':float(h.max()),'random_ds_min':float(ds.min()),
              'random_ds_median':float(np.median(ds)),'random_ds_max':float(ds.max()),
              'fraction_random_K_lt_cube':float(np.mean(h<trace_ds(Gcube,t)[0]))}
        sample_t.append(item)
    assert sample_t[3]['fraction_random_K_lt_cube']==1
    # Sampling-library Boltzmann weights (not counting graphs with true entropy multiplicities)
    lib=[Gtri,Gcube]+pool
    K=np.array([trace_ds(x,1)[0] for x in lib]);
    beta_scan=[]
    for beta in [0,1,5,10,30,100]:
        ex=-beta*K;ex-=ex.max();p=np.exp(ex);p/=p.sum()
        entropy=float(-sum(x*np.log(x) for x in p if x>0))
        beta_scan.append({'beta':beta,'P_triangle':float(p[0]),'P_cube':float(p[1]),
                          'P_random_pool':float(sum(p[2:])), 'effective_number_states_Shannon':float(np.exp(entropy))})
    result['D3']={'kind':'finite sampled library / diagnostic only, no thermodynamic ensemble or fixed point',
        'n':64,'degree':6,'edge_count':192,'seed_list':list(range(80)),'random_samples':80,
        'action_K_time':1,'probe':sample_t,'Boltzmann_reweighting':beta_scan,
        'warning':'A single d_s(t) close to 3 on a random regular graph does not establish a 3D plateau or manifold.'}
    # Freudenthal periodic 3D flag triangulation on 5^3 vertices.
    G=graph('flag3',5);groups,ranks,betti=clique_data(G)
    f=[len(groups[i]) for i in range(4)]
    assert f==[125,875,1500,750] and betti==[1,3,3,1] and [ranks[i] for i in range(1,4)]==[124,748,749]
    link=verify_vertex_link(groups)
    kappas=[];origin=(0,0,0)
    for delta in DIRECTIONS['flag3']:
        curvature=waterstein_curvature(G,origin,delta)
        kappas.append({'edge_direction':delta,'curvature_idleness0':curvature})
        assert abs(curvature)<1e-9
    low=np.zeros((3,3))
    for delta in DIRECTIONS['flag3']:
        v=np.array(delta);low+=np.outer(v,v)
    assert np.all(np.linalg.eigvalsh(low)>0)
    result['D4']={'family':'periodic Freudenthal-Kuhn flag 3-torus',
          'm':5,'n':125,'degree':14,'f_vector':f,'mod2_boundary_ranks':[ranks[i] for i in range(1,4)],
          'mod2_betti':betti,'Euler':sum((-1)**i*f[i] for i in range(4)),
          'vertex_link':link,'Ollivier_idleness0_edge_orbits':kappas,
          'quadratic_form_Q':low.astype(int).tolist(),
          'f_vector_general_m_ge5':['m^3','7m^3','12m^3','6m^3'],
          'fairness_guard':'Genuine 3-manifold comparator, but 14-regular versus triangular 2-torus 6-regular; not same E.',
          'topological_basis':'all vertex links S2; f and mod2 homology match 3-torus; periodic cube triangulation supplies homeomorphism'}
    result['D4']['flag_spectral']={}
    for m in [8,12,16,24]:
        l=spectrum('flag3',m)
        result['D4']['flag_spectral'][str(m)]={'n':len(l),
           'ds_at_t':{str(t):trace_ds(l,t)[1] for t in [0.25,0.5,1,2,3,4,5,6]}}
    # Verify Fourier formula against independently assembled Laplacian on small instance.
    for fam,m in [('tri2',6),('cube3',5),('flag3',5)]:
        adj=graph(fam,m);num=np.sort(np.linalg.eigvalsh(nx.laplacian_matrix(nxgraph(adj)).toarray()))
        ana=np.sort(spectrum(fam,m));err=float(np.max(abs(num-ana)))
        assert err<1e-10,(fam,err)
        result['tests'][fam+'_Fourier_against_numerical_diagonalization']=err
    result['tests']['all_internal_checks']='PASS'
    return result

def create_chart(data):
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(8.8,5.2))
    t=np.linspace(0.08,12,241)
    for family,m,label in [('tri2',64,'2D triangular torus (64²)'),('cube3',16,'3D cubic graph (16³)'),('flag3',16,'3D flag torus (16³)'),('flag3',24,'3D flag torus (24³)')]:
        lam=spectrum(family,m)
        ds=[trace_ds(lam,q)[1] for q in t]
        ax.plot(t,ds,label=label)
    ax.set_xlabel('Graph diffusion time t')
    ax.set_ylabel('Spectral dimension d_s(t)')
    ax.set_xlim(0,12);ax.set_ylim(0,5)
    ax.grid(True,alpha=.25);ax.legend(loc='upper right',fontsize=8)
    ax.set_title('difusión a escala finita | Finite-scale spectral dimension')
    fig.tight_layout();fig.savefig(ROOT/'perfiles_espectrales.png',dpi=150)
    plt.close(fig)
    fig,ax=plt.subplots(figsize=(8.8,5.1))
    t=np.geomspace(0.15,75,251);fine=spectrum('cube3',16);coarse=spectrum('cube3',8)
    ax.semilogx(t,[trace_ds(fine,x)[1] for x in t],label='Fine 16³, a=1: t=t_phys')
    ax.semilogx(t,[trace_ds(coarse,x/4)[1] for x in t],label='Coarse 8³, a=2: t=t_phys/4')
    ax.set_xlabel('Matched physical diffusion time t_phys')
    ax.set_ylabel('Spectral dimension d_s')
    ax.grid(True,alpha=.25);ax.legend(fontsize=8)
    ax.set_title('D1: Coarse-graining time match: curves do not coincide exactly')
    fig.tight_layout();fig.savefig(ROOT/'tiempo_emparejado.png',dpi=150);plt.close(fig)

def write_data(data):
    (ROOT/'certificado_historico.json').write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
    with (ROOT/'resultados.csv').open('w',encoding='utf8',newline='') as f:
        w=csv.writer(f);w.writerow(['source','t','series','value'])
        for x in data['D2']['scan']:
            for k in ['trace_2D','trace_3D','difference_2D_minus_3D','ds_2D','ds_3D']:w.writerow(['D2',x['t'],k,x[k]])
        for x in data['D1']['physical_time_comparison']:
            for k in ['fine_ds','coarse_ds','difference']:w.writerow(['D1',x['fine_heat_time'],k,x[k]])
        for x in data['D3']['probe']:
            for k in ['triangle_K','cube_K','random_K_min','random_K_median','random_K_max','random_ds_median']:
                w.writerow(['D3',x['t'],k,x[k]])
        for m,entry in data['D4']['flag_spectral'].items():
            for t,v in entry['ds_at_t'].items():w.writerow(['D4',t,'flag3_m'+m,v])
    create_chart(data)
    paths=[ROOT/x for x in ['verificar.py','certificado_historico.json','resultados.csv','perfiles_espectrales.png','tiempo_emparejado.png']]
    lines=[hashlib.sha256(x.read_bytes()).hexdigest()+'  '+x.name for x in paths]
    (ROOT/'HASHES_EJECUCION.txt').write_text('\n'.join(lines)+'\n',encoding='utf8')
    print('PASS internal verification')
    print('D1',[(x['fine_heat_time'],round(x['fine_ds'],6),round(x['coarse_ds'],6)) for x in data['D1']['physical_time_comparison']])
    print('D2',[(x['t'],round(x['difference_2D_minus_3D'],4)) for x in data['D2']['scan']])
    print('D3',data['D3']['probe'][3])
    print('D4',data['D4']['f_vector'],data['D4']['mod2_betti'],data['D4']['vertex_link'])

if __name__=='__main__':write_data(compute())
