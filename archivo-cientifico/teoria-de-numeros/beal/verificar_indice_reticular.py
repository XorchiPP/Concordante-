#!/usr/bin/env python3
"""Exact finite witness extracted from the historical notation audit.
No access to the historical dataset; no claim to recheck its occurrence there.
Python standard library only. Concordante Lab · Xorch, 2026.
"""
import itertools
import json
from pathlib import Path

def det5(rows):
    out = 0
    for perm in itertools.permutations(range(5)):
        inversions = sum(perm[i] > perm[j] for i in range(5) for j in range(i+1, 5))
        product = 1
        for i, j in enumerate(perm):
            product *= rows[i][j]
        out += -product if inversions % 2 else product
    return out

rows = [[-1,-1,1,0,0],[-1,0,-1,1,0],[-1,0,0,-1,1],[-1,1,-1,-1,-1],[0,-1,-1,0,1]]
assert det5(rows) == 11
assert all(sum((j+1)*row[j] for j in range(5)) % 11 == 0 for row in rows)
mutation = [row[:] for row in rows]
mutation[0][0] += 1
assert det5(mutation) != 11
assert sum((j+1)*mutation[0][j] for j in range(5)) % 11 != 0
result = {
    'status':'PASS_EXACT_FINITE_LATTICE_WITNESS',
    'rows':rows,'determinant':det5(rows),'rank':5,'index':11,
    'phase_map_coefficients':[1,2,3,4,5],
    'surjectivity_witness':[1,0,0,0,0],
    'proof':'The phase map is onto Z/11 because its first coefficient is 1. The row lattice is contained in its kernel; both have index 11 in Z^5, hence they coincide.',
    'negative_control_detected':True,
    'scope':'Only this explicit matrix and phase kernel. Does not recheck historical 5103 symbols, occurrence of rows in that dataset, nor all multiplicative relations of a number field.',
    'arithmetic_comparison':'OPEN','Cassels_Tate':'UNKNOWN','Beal_proof':False
}
Path(__file__).with_name('resultado_indice_reticular.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
