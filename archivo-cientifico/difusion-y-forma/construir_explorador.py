#!/usr/bin/env python3
"""Construye el explorador español con las series históricas incluidas.
Concordante Lab · Xorch. © 2026. Todos los derechos reservados.
"""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
data=json.loads((root/'datos_explorador.json').read_text())
assert len(data['times'])==200 and all(len(s['d'])==200 for s in data['series'])
encoded=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</',r'<\/')
text=(root/'plantilla_explorador.html').read_text().replace('__DATOS__',encoded)
(root/'explorador.html').write_text(text,encoding='utf-8')
print('Explorador construido a partir de 5 series históricas de 200 puntos.')
