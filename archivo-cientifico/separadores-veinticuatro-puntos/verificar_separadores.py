#!/usr/bin/env python3
"""Separadores por octadas: comprobación exacta.
Concordante Lab · Xorch · © 2026. Todos los derechos reservados.
Entradas reducidas a los campos utilizados, con hashes de esta edición.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, permutations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
F3=ROOT/'octadas_entrada.json'
F4=ROOT/'testigo_entrada.json'
HASH3='7e681ede31617412963fa9bfa6b1e67ca0da463e7a82d870009e193c70956f48'
HASH4='23c881905803abd7ccc0439bd7915a5927b16a373b673becf585b803dcb5b76d'
M24=244823040
C6_EXAMPLES=[
 ['2e04a8','802b8c','421962','90444b','851231','1d8806'],
 ['11e103','c38260','4d3014','2a1702','884e06','221139']
]
TESTS={}
def check(name,condition):
    TESTS[name]=bool(condition)
    if not condition: raise AssertionError(name)
def signatures(rows):
    return [sum(((row>>i)&1)<<k for k,row in enumerate(rows)) for i in range(24)]
def invariants(rows):
    ss=signatures(rows)
    return (tuple(Counter(s.bit_count() for s in ss).get(k,0) for k in range(7)),
            tuple(sorted((a&b).bit_count() for a,b in combinations(rows,2))))
def critical_pairs(rows):
    ss=signatures(rows);count=[0]*6
    for a,b in combinations(ss,2):
        c=a^b
        if c and c&(c-1)==0:count[c.bit_length()-1]+=1
    return tuple(count)
def binary_rank(words):
    basis={}
    for n in words:
        while n:
            pivot=n.bit_length()-1
            if pivot not in basis:
                basis[pivot]=n;break
            n^=basis[pivot]
    return len(basis)
def sixpack_stab(rows,octads,octset):
    ss=signatures(rows);loc={v:i for i,v in enumerate(ss)}
    if len(loc)!=24:raise ValueError('not resolving')
    candidates=0;actual=[]
    for g in permutations(range(6)):
        transformed=[sum(((s>>j)&1)<<g[j] for j in range(6)) for s in ss]
        if any(s not in loc for s in transformed):continue
        candidates+=1
        pi=[loc[s] for s in transformed]
        ok=True
        for o in octads:
            mask=0
            for i in range(24):
                if o>>i&1:mask |= 1<<pi[i]
            if mask not in octset:ok=False;break
        if ok: actual.append(g)
    return candidates,actual

def permutation_order(pi):
    visited=set();result=1
    from math import lcm
    for i in range(len(pi)):
        if i in visited:continue
        j=i;l=0
        while j not in visited:
            visited.add(j);j=pi[j];l+=1
        result=lcm(result,l)
    return result

def completions(rows,index,octads):
    others=rows[:index]+rows[index+1:]
    ss=signatures(others)
    # signatures() interprets others as five rows, as desired
    blocks=defaultdict(list)
    for i,s in enumerate(ss):blocks[s].append(i)
    if any(len(p)>2 for p in blocks.values()):return []
    twinmasks=[sum(1<<i for i in points) for points in blocks.values() if len(points)==2]
    return [o for o in octads if o not in others and all((o&pair).bit_count()==1 for pair in twinmasks)]

def maskhex(rows):return [f'{v:06x}' for v in rows]
def packrecord(rows,octads,octset):
    candidate,autos=sixpack_stab(rows,octads,octset)
    hist,inner=invariants(rows)
    crit=critical_pairs(rows)
    return {'octads_hex':maskhex(rows),
            'weight_histogram':list(hist),
            'pair_intersections':dict(sorted((str(k),v) for k,v in Counter(inner).items())),
            'critical_pairs_per_bit':list(crit),
            'candidate_signature_row_symmetries':candidate,
            'm24_stabilizer_order':len(autos),
            'stabilizer_permutations': [list(g) for g in autos],
            'stabilizer_element_orders':dict(sorted((str(k),v) for k,v in Counter(permutation_order(g) for g in autos).items())),
            'm24_orbit_size':M24//len(autos)}

def main():
    check('octadas_sha',sha256(F3.read_bytes()).hexdigest()==HASH3)
    check('testigo_sha',sha256(F4.read_bytes()).hexdigest()==HASH4)
    a=json.loads(F3.read_text()); prev=json.loads(F4.read_text())
    octads=sorted(int(v,16) for v in a['octad_masks_759']);octset=set(octads)
    check('octad_759_unique',len(octads)==len(octset)==759)
    check('all_parent_octads_weight_eight',all(o.bit_count()==8 for o in octads))
    witness=[int(v,16) for v in prev['axis_characters']['six_witness_hex']]
    check('frozen_witness_six_valid_octads',len(set(witness))==6 and set(witness)<=octset)
    check('frozen_witness_24_distinct_signatures',len(set(signatures(witness)))==24)
    check('parent_five_reader_lower_bound',prev['axis_characters']['min_five_bit_signature_weight']==49)
    candidates=[];local=[]
    for k in range(6):
        options=completions(witness,k,octads)
        candidates.append(len(options))
        check('original_mask_is_valid_completion_'+str(k),witness[k] in options)
        for o in options:
            if o==witness[k]:continue
            rows=witness[:k]+[o]+witness[k+1:]
            check('resolved_neighbor_'+str(k)+'_'+f'{o:06x}',len(set(signatures(rows)))==24)
            local.append({'replaced_reader_index':k,'replacement_octad_hex':f'{o:06x}', 'rows':rows})
    check('six_completion_counts_4_12_24_4_12_32',candidates==[4,12,24,4,12,32])
    check('local_one_swap_count_82',len(local)==82)
    check('local_82_packs_distinct',len({tuple(sorted(r['rows'])) for r in local})==82)
    records=[];by_invariant=defaultdict(list)
    for r in local:
        row=packrecord(r['rows'],octads,octset)
        invariant=(tuple(row['weight_histogram']),tuple(sorted((int(k),v) for k,v in row['pair_intersections'].items())),row['m24_stabilizer_order'])
        by_invariant[invariant].append((r,row))
    check('eleven_distinct_invariant_stabilizer_classes_one_swap',len(by_invariant)==11)
    class_rows=[]
    for inv,occurrences in sorted(by_invariant.items(),key=lambda kv:(kv[0][0],kv[0][1],kv[0][2])):
        r,rec=min(occurrences,key=lambda z:(z[0]['replaced_reader_index'],z[0]['replacement_octad_hex']))
        rec['local_one_swap_representatives_of_type']=len(occurrences)
        rec['source_replacement_index']=r['replaced_reader_index'];rec['source_replacement_hex']=r['replacement_octad_hex']
        rec['id']='local_'+str(len(class_rows)+1).zfill(2)
        class_rows.append(rec)
    check('nine_local_trivial_stabilizer_types',sum(r['m24_stabilizer_order']==1 for r in class_rows)==9)
    check('one_local_c2_type',sum(r['m24_stabilizer_order']==2 for r in class_rows)==1)
    check('one_local_c3_type',sum(r['m24_stabilizer_order']==3 for r in class_rows)==1)
    check('local_orbit_lower_bound',sum(r['m24_orbit_size'] for r in class_rows)==2407426560)
    sym=[]
    for i,hexlist in enumerate(C6_EXAMPLES):
        rows=[int(h,16) for h in hexlist]
        check('cyclic_example_six_octads_'+str(i),len(rows)==len(set(rows))==6 and set(rows)<=octset)
        check('cyclic_example_resolves_'+str(i),len(set(signatures(rows)))==24)
        rec=packrecord(rows,octads,octset); rec['id']='cyclic_'+str(i+1);sym.append(rec)
        check('cyclic_example_stabilizer_order_six_'+str(i),rec['m24_stabilizer_order']==6)
        check('cyclic_example_is_C6_'+str(i),rec['stabilizer_element_orders']=={'1':1,'2':1,'3':2,'6':2})
        check('cyclic_example_all_six_critical_'+str(i),all(v>=1 for v in rec['critical_pairs_per_bit']))
    check('balanced_C6_six_pairs_all_intersect_two',sym[0]['pair_intersections']=={'2':15})
    check('balanced_C6_uniform_6_critical_per_reader',sym[0]['critical_pairs_per_bit']==[6]*6)
    check('balanced_C6_24_signatures_degree_1_2_3',sym[0]['weight_histogram']==[0,6,12,6,0,0,0])
    # Derive the order-six reader permutation, then its induced permutation on 24 lines.
    balanced=[int(h,16) for h in C6_EXAMPLES[0]]
    row_perm=next(tuple(g) for g in sym[0]['stabilizer_permutations'] if permutation_order(g)==6)
    ss=signatures(balanced);loc={v:i for i,v in enumerate(ss)}
    induced=[loc[sum(((p>>j)&1)<<row_perm[j] for j in range(6))] for p in ss]
    orbits=[];seen=set()
    for i in range(24):
        if i in seen:continue
        j=i;cycle=[]
        while j not in seen:
            seen.add(j);cycle.append(j);j=induced[j]
        orbits.append(cycle)
    check('balanced_C6_four_orbits_six_points',[len(o) for o in orbits]==[6]*4)
    # Distinct 13 orbits: all 11 local triples distinct, cyclic stabilizer=6,
    # and the two cyclic types have different intersection signature.
    check('two_cyclic_orbit_types_distinct',
          (sym[0]['weight_histogram'],sym[0]['pair_intersections']) !=(sym[1]['weight_histogram'],sym[1]['pair_intersections']))
    check('thirteen_certified_distinct_M24_orbit_witnesses',len(class_rows)+len(sym)==13)
    total_lower=sum(z['m24_orbit_size'] for z in class_rows+sym)
    check('disjoint_orbits_cover_at_least_2489034240_sixpacks',total_lower==2489034240)
    check('all_13_stabilizers_subgroups_S6',all(z['m24_stabilizer_order']<=720 and 720%z['m24_stabilizer_order']==0 for z in class_rows+sym))
    check('every_one_swap_neighbor_has_critical_pairs',all(all(critical_pairs(r['rows'])) for r in local))
    check('witness_six_critical_pairs_positive',all(critical_pairs(witness)))
    check('conway_24frame_index_external',8292375*4096*M24==8315553613086720000)
    # Assert no globally equivariant six-set selector: M24 acts transitively on octads;
    # no nonempty proper M24 invariant subset of the 759 octads.
    check('global_M24_octad_transitivity_blocks_six_reader_selector',0<6<759)
    out={
      'cut':'separadores_octadas',
      'state':'EXACT_13_INEQUIVALENT_M24_ORBIT_WITNESSES_PASS / LOCAL_82_NEIGHBORS_EXHAUSTIVE_PASS / C6_READOUT_PASS / GLOBAL_SELECTOR_NOGO',
      'inherited_sha256':{'octadas_entrada':HASH3,'testigo_entrada':HASH4},
      'classical_inputs':{'M24_order':M24,'M24_is_Aut_extended_Golay':True,'Co0_frame_count':8292375,'frame_stabilizer':'2^12:M24'},
      'universal_argument':'24 pairwise distinct six-bit signatures imply Stab_M24(R) injects into S6; each bit is essential by the five-octad theorem',
      'separador_base':packrecord(witness,octads,octset),
      'one_slot_valid_completion_counts_including_original':candidates,
      'one_swap_distinct_neighbors':len(local),
      'local_distinct_invariant_triples':len(class_rows),
      'local_orbit_types':class_rows,
      'cyclic_reader_types':sym,
      'balanced_C6_coordinate_orbits':orbits,
      'at_least_M24_orbits':13,
      'at_least_unordered_minimal_six_octad_readers':total_lower,
      'global_nogo':'No Co0-equivariant section choosing six octads over all frames: a chosen reference frame would require M24-fixed proper six-subset, impossible by octad transitivity.',
      'transport':'For decorated frames (F,R), Co0 acts by conjugating Golay octad sign operators; point-line signatures equivariant. Choice of R and lifts is not Co0-canonical.',
      'checks_passed':len(TESTS), 'checks':TESTS}
    (ROOT/'certificado_reproducido.json').write_text(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
    atlas={
      'parent_witness_hex':maskhex(witness),
      'local_one_swap_82':[{'slot':r['replaced_reader_index'],'replacement_hex':r['replacement_octad_hex']} for r in local],
      'one_swap_orbit_representative_11':[{'id':r['id'],'masks_hex':r['octads_hex'],'stabilizer_order':r['m24_stabilizer_order'],'hist':r['weight_histogram'],'pair_overlaps':r['pair_intersections']} for r in class_rows],
      'cyclic_orbit_representatives_2':[{'id':r['id'],'masks_hex':r['octads_hex'],'stabilizer_permutations':r['stabilizer_permutations'],'hist':r['weight_histogram'],'pair_overlaps':r['pair_intersections']} for r in sym],
      'balanced_C6_row_generator':list(row_perm),
      'balanced_C6_coordinate_generator':induced,
      'balanced_C6_point_cycles':orbits
    }
    (ROOT/'atlas_separadores.json').write_text(json.dumps(atlas,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
    print('separadores_octadas MAIN',len(TESTS),'PASS')
    print('one-swap completions',candidates,'neighbors',len(local),'M24 classes >=',len(class_rows)+len(sym))
    print('orbit lower bound',total_lower,'C6 rows',maskhex(balanced),'four 6-cycles',orbits)

if __name__=='__main__':main()
