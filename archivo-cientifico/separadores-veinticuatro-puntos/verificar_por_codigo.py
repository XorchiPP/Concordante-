#!/usr/bin/env python3
"""Separadores por octadas: comprobación exacta.
Concordante Lab · Xorch · © 2026. Todos los derechos reservados.
Entradas reducidas a los campos utilizados, con hashes de esta edición.
"""
from pathlib import Path
from collections import defaultdict, Counter
from hashlib import sha256
from itertools import combinations, permutations
import json
from math import lcm

HERE=Path(__file__).resolve().parent
F3=HERE/'octadas_entrada.json'
F4=HERE/'testigo_entrada.json'
C5=HERE/'certificado_reproducido.json'
A5=HERE/'atlas_separadores.json'
M24=244823040
CHECK={}
def require(name,truth):
    CHECK[name]=bool(truth)
    if not truth:raise AssertionError(name)
def msk(s):return int(s,16)
def coords(m):return frozenset(i for i in range(24) if m & (1<<i))
def signs(rows):return [tuple(1 if i in r else 0 for r in rows) for i in range(24)]
def overlap(rows):return dict(sorted(Counter(len(a&b) for a,b in combinations(rows,2)).items()))
def hd(rows):return tuple(Counter(sum(z) for z in signs(rows)).get(w,0) for w in range(7))
def permorder(p):
    remaining=set(range(6));o=1
    while remaining:
        i=next(iter(remaining));j=i;n=0
        while j in remaining:
            remaining.remove(j);j=p[j];n+=1
        o=lcm(o,n)
    return o

def gf2basis(words):
    basis={}
    for x in words:
        z=x
        while z:
            k=z.bit_length()-1
            if k not in basis:basis[k]=z;break
            z ^= basis[k]
    return tuple(basis[k] for k in sorted(basis,reverse=True))
def gen_code(bs):
    a=[0]
    for w in bs:
        a.extend([x^w for x in a])
    return set(a)
def transport_word(word,pi):
    # intentionally use generators rather than direct 759-octad image checks
    b=0
    for i in range(24):
        if word & (1<<i):b|=(1<<pi[i])
    return b

def sym_size(rows,genbasis,code):
    pts=signs(rows)
    if len(set(pts))!=24:return 0,[]
    idx={v:i for i,v in enumerate(pts)}
    lift=[];possible=0
    for pi in permutations(range(6)):
        t=[tuple(p[pi.index(k)] for k in range(6)) for p in pts]
        if any(v not in idx for v in t):continue
        possible+=1
        im=[idx[z] for z in t]
        if all(transport_word(w,im) in code for w in genbasis):lift.append((pi,im))
    return possible,lift

def all_completions(rows,slot,octsets):
    base=rows[:slot]+rows[slot+1:]
    cls=defaultdict(list)
    for idx,b in enumerate(signs(base)):cls[b].append(idx)
    if max(len(t) for t in cls.values())>2:return set()
    twins=[frozenset(pts) for pts in cls.values() if len(pts)==2]
    return {oct for oct in octsets if oct not in base and all(len(oct&t)==1 for t in twins)}

def main():
    source=json.loads(F3.read_text()); pre=json.loads(F4.read_text()); cert=json.loads(C5.read_text());atlas=json.loads(A5.read_text())
    oct_masks=[msk(s) for s in source['octad_masks_759']]
    octsets={coords(z) for z in oct_masks}
    require('frozen_octad_sha',sha256(F3.read_bytes()).hexdigest()==cert['inherited_sha256']['octadas_entrada'])
    require('frozen_reader_sha',sha256(F4.read_bytes()).hexdigest()==cert['inherited_sha256']['testigo_entrada'])
    require('759_octads_unique_supports',len(octsets)==759)
    basis=gf2basis(oct_masks)
    require('12_binary_basis_vectors',len(basis)==12)
    code=gen_code(basis)
    require('4096_words_full_code',len(code)==4096)
    require('octad_layer_reconstructed',set(oct_masks)=={x for x in code if x.bit_count()==8})
    witness=[coords(msk(v)) for v in pre['axis_characters']['six_witness_hex']]
    require('separador_base_all_24_distinct',len(set(signs(witness)))==24)
    complets=[all_completions(witness,slot,octsets) for slot in range(6)]
    require('local_completion_counts_independent',[len(a) for a in complets]==[4,12,24,4,12,32])
    nbr={(slot, o) for slot,poss in enumerate(complets) for o in poss if o!=witness[slot]}
    require('all_82_direct_one_step_solutions',len(nbr)==82)
    # Exact transitive group classification from 6-bit row actions and full code basis
    reps=cert['local_orbit_types']+cert['cyclic_reader_types']
    require('certified_13_representatives',len(reps)==13)
    labels=set();orbit_sizes=[];stable={};critical=[]
    for r in reps:
        rows=[coords(msk(v)) for v in r['octads_hex']]
        require('six_valid_masks_'+r['id'],len(set(rows))==6 and all(v in octsets for v in rows))
        p=signs(rows);require('distinct24_'+r['id'],len(set(p))==24)
        hist=hd(rows);pair=overlap(rows)
        require('weight_histogram_'+r['id'],list(hist)==r['weight_histogram'])
        require('pair_intersections_'+r['id'],{str(k):v for k,v in pair.items()}==r['pair_intersections'])
        poss,autos=sym_size(rows,basis,code)
        require('stabilizer_order_'+r['id'],len(autos)==r['m24_stabilizer_order'])
        require('orbit_size_'+r['id'],M24//len(autos)==r['m24_orbit_size'])
        critical_bits=[0]*6
        for u,v in combinations(p,2):
            diff=[i for i in range(6) if u[i]!=v[i]]
            if len(diff)==1:critical_bits[diff[0]]+=1
        require('critical_bits_'+r['id'],critical_bits==r['critical_pairs_per_bit'] and all(x>0 for x in critical_bits))
        sig=(hist,tuple(sorted(pair.items())),len(autos))
        require('no_colliding_M24_orbit_invariants_'+r['id'],sig not in labels)
        labels.add(sig); orbit_sizes.append(M24//len(autos));stable[r['id']]=len(autos)
    require('13_distinct_orbits_independently',len(labels)==13)
    require('orbit_lower_bound_2489034240',sum(orbit_sizes)==2489034240)
    require('cyclic_order_six_two',list(stable.values())[-2:]==[6,6])
    # Group C6: the induced column permutation yields 4 cycles of length six.
    row=[coords(msk(v)) for v in cert['cyclic_reader_types'][0]['octads_hex']]
    _,automorph=sym_size(row,basis,code)
    pi,im=next((a,b) for a,b in automorph if permorder(a)==6)
    seen=set();cycles=[]
    for i in range(24):
        if i in seen:continue
        cyc=[];k=i
        while k not in seen:
            seen.add(k);cyc.append(k);k=im[k]
        cycles.append(cyc)
    require('C6_independent_four_cyclic_orbits',[len(x) for x in cycles]==[6]*4)
    require('C6_all_reader_intersections_two',overlap(row)=={2:15})
    # Input certificates claim local orbit type counts and two symmetry types.
    info={'audit':'separadores_octadas independent direct point sets + generated full 4096-word code',
          'checks_passed':len(CHECK),'checks':CHECK,
          'base_code_dimension':12,'base_code_size':len(code),
          'one_swap_completions':[len(x) for x in complets],
          'M24_orbit_type_counts':dict(Counter(stable.values())),
          'certified_distinct_orbits':len(labels),
          'distinct_six_reader_lower_bound':sum(orbit_sizes),
          'symmetric_C6_orbit_sizes':[len(x) for x in cycles],
          'symmetric_reader_intersections':overlap(row)}
    (HERE/'certificado_alternativo.json').write_text(json.dumps(info,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
    print('separadores_octadas INDEPENDENT',len(CHECK),'PASS, 13 M24-orbits, >= 2489034240 readouts')

if __name__=='__main__':main()
