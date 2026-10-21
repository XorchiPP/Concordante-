#!/usr/bin/env python3
"""Exact integer two-port presentation and mathematical certificates.
Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Frozen strict family: six eligible edge-exchange valves on wired 3x3.
Relaxed family: same seven-site directed core, two one-way ports with one
internal arc per port-core neighbor and remaining arcs to sink.
Column-emitter convention D[target, source] < 0.
"""
import json,itertools,math
from collections import Counter
from pathlib import Path
from sympy import Matrix,eye,ones
from sympy.polys.domains import ZZ
from sympy.matrices.normalforms import smith_normal_form
ROOT=Path(__file__).parent
PORTS=(0,8)
CORE=(1,2,3,4,5,6,7)
CORE_VALVES=((2,1),(6,7))
STRICT_PORT_VALVES=((0,1),(0,3),(8,5),(8,7))
CANDIDATE_INTERNAL=((2,1),(2,5),(6,3),(6,7))


def base_grid():
 d=4*eye(9)
 for u in range(9):
  for v in range(9):
   if abs(u//3-v//3)+abs(u%3-v%3)==1:d[v,u]=-1
 return d

def valve(d,u,v):
 d=d.copy();d[v,u]-=1;d[u,v]+=1;return d

def core_matrix(subset=CORE_VALVES):
 a=base_grid().extract(CORE,CORE)
 for u,v in subset:
  i,j=CORE.index(u),CORE.index(v)
  a[j,i]-=1;a[i,j]+=1
 return a

def coupling(weight):
 return Matrix([weight if v in (1,3) else 0 for v in CORE]),Matrix([weight if v in (5,7) else 0 for v in CORE])

def assemble(a, b, core, outward):
 d=Matrix.zeros(9)
 for u in PORTS:d[u,u]=4
 for i,u in enumerate(CORE):
  for j,v in enumerate(CORE):d[u,v]=core[i,j]
 for p,coeff in [(0,a),(8,b)]:
  for i,v in enumerate(CORE):
   if outward:d[v,p]-=coeff[i]
   else:d[p,v]-=coeff[i]
 return d

def snf(d):
 return [abs(int(x)) for x in smith_normal_form(d,domain=ZZ).diagonal() if abs(int(x))>1]

def index(d,extra):
 matrix=d.row_join(Matrix.hstack(*extra))
 return abs(int(math.prod(int(z) for z in smith_normal_form(matrix,domain=ZZ).diagonal())))

def order(d,v):
 x=d.inv()*v
 return math.lcm(*[int(z.q) for z in x])

def mod2_nullity(d):
 arr=[[int(d[i,j])&1 for j in range(d.cols)] for i in range(d.rows)]
 rank=0
 for j in range(d.cols):
  found=next((i for i in range(rank,d.rows) if arr[i][j]),None)
  if found is None:continue
  arr[found],arr[rank]=arr[rank],arr[found]
  for i in range(d.rows):
   if i!=rank and arr[i][j]:arr[i]=[x^y for x,y in zip(arr[i],arr[rank])]
  rank+=1
 return d.cols-rank

def sink_budgets(d):return [sum(int(d[i,j]) for i in range(d.rows)) for j in range(d.cols)]

def source_support_reaches(d,beta):
 seen={i for i,x in enumerate(beta) if x>0}
 pending=list(seen)
 while pending:
  u=pending.pop()
  for v in range(d.rows):
   if v!=u and d[v,u]<0 and v not in seen:seen.add(v);pending.append(v)
 return len(seen)==d.rows

def script(d):
 sig=Matrix([1]*d.rows)
 for _ in range(1000):
  beta=d*sig
  if min(beta)>=0:
   assert source_support_reaches(d,list(beta))
   return [int(x) for x in sig],[int(x) for x in beta]
  sig[next(i for i,x in enumerate(beta) if x<0)]+=1
 raise ValueError('No short positive burning script')

def val_mask(flag):return 'outward' if flag else 'inward'

def build_cases():
 a_core=core_matrix()
 a,b=coupling(2);c,d=coupling(1)
 cases=[]
 for name,va,vb,outer,strict in [('SP',a,b,True,True),('SQ',a,b,False,True),('RP',c,d,True,False),('RQ',c,d,False,False)]:
  matrix=assemble(va,vb,a_core,outer)
  sig,beta=script(matrix)
  cases.append(dict(id=len(cases),name=name,contract='six_valve_exchange' if strict else 'relaxed_directed_port',direction=val_mask(outer),matrix=[[int(matrix[i,j]) for j in range(9)] for i in range(9)],script=sig,burn=beta,sink=sink_budgets(matrix)))
 return a_core,cases

def main():
 checks={}
 def passed(name,x):
  if not x:raise AssertionError(name)
  checks[name]=True
 A,cases=build_cases()
 a,b=coupling(2);ar,br=coupling(1)
 net={c['name']:Matrix(c['matrix']) for c in cases}
 base=base_grid()
 for k,edges in [('SP',STRICT_PORT_VALVES+CORE_VALVES),('SQ',tuple((v,u) for u,v in STRICT_PORT_VALVES)+CORE_VALVES)]:
  p=base.copy()
  for u,v in edges:p=valve(p,u,v)
  passed(k+'_literally_six_edge_exchange_valves',p==net[k])
 for c in cases:
  name=c['name'];d=net[name]
  passed(name+'_threshold_four',all(d[i,i]==4 for i in range(9)))
  passed(name+'_nonnegative_sink',min(c['sink'])>=0)
  passed(name+'_directed_offdiagonal',all(d[i,j]<=0 for i in range(9) for j in range(9) if i!=j))
  passed(name+'_dissipative',d.det()>0)
  passed(name+'_script_nonnegative',min(c['burn'])>=0)
  passed(name+'_script_reaches_all',source_support_reaches(d,c['burn']))
  passed(name+'_same_core',d.extract(CORE,CORE)==A)
  passed(name+'_ports_scc_singletons',all(d[i,j]==0 for i in PORTS for j in PORTS if i!=j))
 passed('core_asymmetric',A!=A.T)
 passed('core_det_10440',A.det()==10440)
 passed('core_smith_Z3_Z3480',snf(A)==[3,3480])
 passed('core_outdegree_cap',list(ones(1,7)*A)==[3,1,2,0,2,1,3])
 passed('all_four_det_same',all(d.det()==167040 for d in net.values()))
 passed('strict_group_snf',snf(net['SP'])==snf(net['SQ'])==[2,12,6960])
 passed('relaxed_group_snf',snf(net['RP'])==snf(net['RQ'])==[12,13920])
 passed('nonisomorphic_groups_mod2',all(mod2_nullity(net[x])==3 for x in ('SP','SQ')) and all(mod2_nullity(net[x])==2 for x in ('RP','RQ')))
 passed('strict_internal_arcs24',all(36-sum(sink_budgets(net[x]))==24 for x in ('SP','SQ')))
 passed('relaxed_internal_arcs20',all(36-sum(sink_budgets(net[x]))==20 for x in ('RP','RQ')))
 out_data={}
 for prefix,va,vb in [('strict',a,b),('relaxed',ar,br)]:
  r0=order(A,va);r8=order(A,vb)
  idx=index(A,[va,vb]);h=10440//idx
  p=net['SP' if prefix=='strict' else 'RP'];q=net['SQ' if prefix=='strict' else 'RQ']
  bigidx=index(p,[eye(9)[:,0],eye(9)[:,8]])
  smallidx=index(q,[eye(9)[:,0],eye(9)[:,8]])
  periods=(order(p,eye(9)[:,0]),order(p,eye(9)[:,8]));in_periods=(order(q,eye(9)[:,0]),order(q,eye(9)[:,8]))
  passed(prefix+'_port_periods_out',periods==(4*r0,4*r8))
  passed(prefix+'_port_periods_in',in_periods==(4,4))
  passed(prefix+'_mark_subgroup_index_out',bigidx==idx)
  passed(prefix+'_mark_subgroup_index_in',smallidx==10440)
  passed(prefix+'_port_marked_subgroup_order',167040//bigidx==16*h)
  passed(prefix+'_coupling_order_equal',r0==r8)
  out_data[prefix]={
    'core_couplings':{'port0':[int(z) for z in va], 'port8':[int(z) for z in vb]},
    'coupling_order':{'port0':r0,'port8':r8},
    'joint_coupling_subgroup_order':h,'core_coupling_lattice_index':idx,
    'single_mark_period':{'port0':periods[0],'port8':periods[1]},
    'single_mark_orbits':{'port0':167040//periods[0],'port8':167040//periods[1]},
    'joint_marked_subgroup_order':167040//bigidx,
    'joint_marked_orbits':bigidx,
    'inward_single_mark_period':{'port0':4,'port8':4},
    'inward_joint_marked_orbits':smallidx,
    'group_smith':snf(p),
    'port0_full_period_odometer':[int(z) for z in (periods[0]*p.inv()[:,0])],
    'port8_full_period_odometer':[int(z) for z in (periods[1]*p.inv()[:,8])],
    'core_inverse_port0':[str(z) for z in A.inv()*va],
    'core_inverse_port8':[str(z) for z in A.inv()*vb],
    'core_extended_matrix_lattice_smith':[abs(int(z)) for z in smith_normal_form(A.row_join(va).row_join(vb),domain=ZZ).diagonal()]
  }
 passed('strict_1740_orders',out_data['strict']['coupling_order']=={'port0':1740,'port8':1740})
 passed('strict_5220_joint',out_data['strict']['joint_coupling_subgroup_order']==5220)
 passed('strict_two_orbits',out_data['strict']['joint_marked_orbits']==2)
 passed('relaxed_3480_orders',out_data['relaxed']['coupling_order']=={'port0':3480,'port8':3480})
 passed('relaxed_10440_joint',out_data['relaxed']['joint_coupling_subgroup_order']==10440)
 passed('relaxed_transitive',out_data['relaxed']['joint_marked_orbits']==1)
 passed('relaxed_minimal_two_marked_generators',len(snf(net['RP']))==2 and out_data['relaxed']['joint_marked_orbits']==1)
 # Finite obstruction within the original strict opposite-corner exchange-valve subfamily:
 parity=[]
 for size in range(5):
  for subset in itertools.combinations(CANDIDATE_INTERNAL,size):
   mat=core_matrix(subset)
   pa=assemble(a,b,mat,True);qa=assemble(a,b,mat,False)
   good=min(sink_budgets(pa))>=0 and min(sink_budgets(qa))>=0
   passed('legal_'+str(subset),good)
   kdet=int(mat.det());i=index(mat,[a,b]);sizeH=kdet//i
   passed('strict_parity_obstruction_'+str(subset),kdet%2==0 and i%2==0)
   parity.append({'third_or_more_internal_valves':[list(x) for x in subset],'core_det':kdet,'core_smith':snf(mat),'generated_core_subgroup':sizeH,'index':i})
 passed('all_16_strict_core_variant_subsets',len(parity)==16)
 witness=Matrix([3,1,1,1,3,0,0,0,0]);e0=eye(9)[:,0]
 witness_states={}
 expected_loss={'SP':0,'SQ':4,'RP':2,'RQ':4}
 for name,d in net.items():
  after=witness+e0-d*e0
  passed('witness_'+name+'_stable',all(0<=z<4 for z in after))
  loss=sum(sink_budgets(d)[i]*int(e0[i]) for i in range(9))
  passed('witness_'+name+'_loss',loss==expected_loss[name])
  witness_states[name]={'after':[int(z) for z in after],'sink_loss':loss,'odometer':[1]+[0]*8}
 certificate={
  'id':'dinamica_dos_puertos','status':'EXACT_TWO_PORT_ORBIT_LATTICE_PASS',
  'base':'wired 3x3 9-site column-emitter threshold four',
  'core_original_labels':list(CORE),
  'core_valves':[list(x) for x in CORE_VALVES],
  'core_matrix':[[int(A[i,j]) for j in range(7)] for i in range(7)],
  'core_det':int(A.det()),'core_smith':snf(A),
  'case_names':['SP','SQ','RP','RQ'],
  'all_four_recurrence_cardinality':167040,
  'recurrence_identity':'Rec(SP)=Rec(SQ)=Rec(RP)=Rec(RQ)= {0,1,2,3}_{0} x {0,1,2,3}_{8} x Rec(A); Speer SCC decomposition',
  'strict_six_valve_sets':{'SP':[list(x) for x in STRICT_PORT_VALVES+CORE_VALVES],'SQ':[list(x) for x in tuple((v,u) for u,v in STRICT_PORT_VALVES)+CORE_VALVES]},
  'strict_vs_relaxed_sink_arc_count':{'strict':12,'relaxed':16},
  'strict_vs_relaxed_internal_arc_count':{'strict':24,'relaxed':20},
  'cases':cases,'group_data':out_data,
  'strict_16_core_variants':parity,
  'witness_add_at_corner0':{'recurrent_input':[int(z) for z in witness], 'state_code':855,'network_observations':witness_states},
  'checks':checks,'passed':len(checks),
  'external_attribution':'Speer SCC recurrence theorem, Smith normal form / finite abelian group presentations are standard',
  'scope':'Finite directed sandpile calculations; SCC factorization and finite group actions use classical theory'
 }
 (ROOT/'certificado_reproducido.json').write_text(json.dumps(certificate,indent=2,ensure_ascii=False)+'\n')
 with (ROOT/'casos.txt').open('w') as f:
  f.write('4\n')
  for x in cases:f.write(' '.join(map(str,[*sum(x['matrix'],[]),*x['script'],*x['burn']]))+'\n')
 print('EXACT_TWO_PORT_ORBIT_LATTICE_PASS',len(checks))
 print(json.dumps({'core_det':10440,'SNF':snf(A),'full_det':167040,'strict':{k:out_data['strict'][k] for k in ['coupling_order','joint_coupling_subgroup_order','joint_marked_orbits','single_mark_period','single_mark_orbits','group_smith']},'relaxed':{k:out_data['relaxed'][k] for k in ['coupling_order','joint_coupling_subgroup_order','joint_marked_orbits','single_mark_period','single_mark_orbits','group_smith']}},indent=2))

if __name__=='__main__':main()
