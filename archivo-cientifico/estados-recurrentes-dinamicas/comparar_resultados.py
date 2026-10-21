#!/usr/bin/env python3
"""Comparación exacta. Concordante Lab · Xorch · © 2026."""
from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
assert json.loads((p/'certificado_historico.json').read_text())==json.loads((p/'certificado_reproducido.json').read_text())
assert (p/'casos_historicos.txt').read_bytes()==(p/'casos.txt').read_bytes()
a=(p/'recurrencia_fifo.bin').read_bytes();b=(p/'recurrencia_lotes.bin').read_bytes()
assert a==b and len(a)==131072
assert hashlib.sha256(a).hexdigest()=='d9f36fb21df7aa427e04bfeba4cf67097093d1a9767f3a8007f211ccf9e4b4ce'
blocks=[a[i*32768:(i+1)*32768] for i in range(4)]
assert all(t==blocks[0] for t in blocks)
assert all(sum(v.bit_count() for v in t)==167040 for t in blocks)
assert all((t[855>>3]>>(855&7))&1 for t in blocks)
print('PASS: certificado y matrices históricos iguales; dos censos iguales al hash histórico; cuatro bloques idénticos de167040 estados; testigo855 recurrente')
