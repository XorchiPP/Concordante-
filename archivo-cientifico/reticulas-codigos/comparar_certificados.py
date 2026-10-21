#!/usr/bin/env python3
"""Comparación exacta de resultados. Concordante Lab · Xorch · © 2026."""
import json
from pathlib import Path
import sys
root=Path(__file__).resolve().parent
historical=json.loads((root/'certificado_historico.json').read_text())
actual=json.loads((Path(sys.argv[1]) if len(sys.argv)>1 else root/'certificado_reproducido.json').read_text())
assert actual==historical, 'Los resultados difieren'
print('PASS: igualdad exacta de todos los campos del certificado acotado')
