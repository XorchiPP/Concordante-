#!/usr/bin/env python3
"""Control acotado de entrada Golay y comparación de resultados.
Concordante Lab · Xorch · © 2026. Todos los derechos reservados.
"""
from pathlib import Path
from collections import Counter
import json
p=Path(__file__).resolve().parent
# Presentación cíclica del antecedente: g=x^11+x^9+x^7+x^6+x^5+x+1.
g=sum(1<<j for j in (11,9,7,6,5,1,0))
words=[0]
for j in range(12):words += [w^(g<<j) for w in words]
code={w|((w.bit_count()%2)<<23) for w in words}
assert len(code)==4096
assert Counter(w.bit_count() for w in code)=={0:1,8:759,12:2576,16:759,24:1}
source=json.loads((p/'octadas_entrada.json').read_text())
assert {int(h,16) for h in source['octad_masks_759']}=={w for w in code if w.bit_count()==8}
assert sum(sorted(w.bit_count() for w in range(32))[:24])==49
for historic,current in [('certificado_historico.json','certificado_reproducido.json'),('certificado_alternativo_historico.json','certificado_alternativo.json'),('atlas_historico.json','atlas_separadores.json')]:
 assert json.loads((p/historic).read_text())==json.loads((p/current).read_text()),current
print('PASS: 4096 palabras, 759 octadas, cota 49>40, tres comparaciones JSON exactas')
