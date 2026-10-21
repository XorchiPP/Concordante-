#!/usr/bin/env python3
"""Comprueba fórmulas y datos de esta edición, sin ejecutar los experimentos completos.
Concordante Lab · Xorch. © 2026. Todos los derechos reservados.
Dependencia: NumPy. Sin red. Diagonalizaciones máximas de 125 por 125.
"""
import ast, json, itertools, re
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parent
# Se extraen exclusivamente las tres funciones puras ya inspeccionadas.
tree=ast.parse((root/'difusion/verificar.py').read_text())
selected=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'graph','spectrum','trace_ds'}]
assert len(selected)==3
ns={'np':np,'itertools':itertools,'DIRECTIONS':{'tri2':[(1,0),(0,1),(1,1)],'cube3':[(1,0,0),(0,1,0),(0,0,1)],'flag3':[v for v in itertools.product((0,1),repeat=3) if any(v)]}}
exec(compile(ast.Module(body=selected,type_ignores=[]),'funciones_inspeccionadas','exec'),ns)
errors={}
for family,m in [('tri2',6),('cube3',5),('flag3',5)]:
 adj=ns['graph'](family,m);vertices=list(adj);idx={v:i for i,v in enumerate(vertices)};L=np.zeros((len(adj),len(adj)))
 for v,neighbors in adj.items():
  L[idx[v],idx[v]]=len(neighbors)
  for u in neighbors:L[idx[v],idx[u]]=-1
 err=float(np.max(abs(np.linalg.eigvalsh(L)-np.sort(ns['spectrum'](family,m)))))
 assert err<1e-10
 errors[family]=err
view=json.loads((root/'datos_explorador.json').read_text())
# Mismos 200 tiempos geométricos originales, antes del redondeo de presentación.
times=np.geomspace(.06,80,200); assert np.max(abs(times-np.array(view['times'])))<5.1e-9
max_series_error=0.0
for s,(family,m,factor) in zip(view['series'],[('tri2',64,1),('cube3',16,1),('flag3',16,1),('flag3',24,1),('cube3',8,.25)]):
 lam=ns['spectrum'](family,m)
 values=[ns['trace_ds'](lam,float(t)*factor)[1] for t in times]
 err=float(np.max(abs(np.array(values)-s['d'])))
 assert err<5.1e-8
 max_series_error=max(max_series_error,err)
cert=json.loads((root/'difusion/certificado_historico.json').read_text())
assert cert['D4']['f_vector']==[125,875,1500,750]
assert cert['D4']['mod2_betti']==[1,3,3,1]
assert cert['D2']['triangles_2D']==8192 and cert['D2']['triangles_3D']==0
assert cert['D3']['random_samples']==80
for row in cert['D1']['physical_time_comparison']:
 assert row['coarse_heat_time']==row['fine_heat_time']/4
 for key,m,t in [('fine_ds',16,row['fine_heat_time']),('coarse_ds',8,row['coarse_heat_time'])]:
  assert abs(ns['trace_ds'](ns['spectrum']('cube3',m),t)[1]-row[key])<1e-10
html=(root/'explorador.html').read_text(); embedded=json.loads(re.search(r'const DATA=(.*?);\n',html).group(1));assert embedded==view
# Inspección estática adicional de superficies de red; SVG namespace no es una petición.
for pattern in [r'\bfetch\s*\(',r'XMLHttpRequest',r'WebSocket',r'sendBeacon',r'<script[^>]+src=',r'<iframe',r'@import',r'url\s*\(',r'localStorage',r'document\.cookie']:
 assert not re.search(pattern,html,re.I),pattern
assert 'lang="es"' in html
result={'estado':'PASS','espectros_pequenos_error_maximo':errors,'series_historicas_puntos_comprobados':1000,'series_error_redondeo_maximo':max_series_error,'tiempo_emparejado_filas':4,'certificados':'Comprobación de campos seleccionados; homología, transportes LP y muestra aleatoria conservados como evidencia histórica.','alcance':'Funciones Fourier y ensamblaje de matrices pequeños; edición HTML y coherencia de datos. No se ejecutaron los experimentos completos.'}
(root/'comprobacion_edicion.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
