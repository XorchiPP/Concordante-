# Realizaciones reversibles indistinguibles en frontera

Resultado: dos redes ponderadas no isomorfas, capacidades conocidas y distintas,
ningún modo interior oscuro, y exactamente la misma respuesta dinámica completa
en dos vértices. Comparten además medida reversible y actividad estacionaria.

- Informe y prueba: [REPORT.md](REPORT.md)
- Verificador Python estándar: [verify_boundary_gauge.py](verify_boundary_gauge.py)
- Certificado: [certificate.json](certificate.json), 74 comprobaciones exactas
- Auditoría independiente: [audit/AUDITORIA_MATEMATICA.md](audit/AUDITORIA_MATEMATICA.md)

Reproducir: `python3 verify_boundary_gauge.py`.

Para reproducir también la auditoría simbólica se requiere SymPy 1.14.0
(registrado en `requirements_audit.txt`). Con esa dependencia disponible,
`sh replay.sh` ejecuta ambas baterías y comprueba los hashes. No instala software.

Las redes se distinguen si el vértice 2 se añade a la frontera. La observabilidad
de estados no equivale a identificar las conductancias. El aporte es un resultado algebraico finito con testigos exactos. La conexión gravitatoria y la prioridad histórica quedan abiertas.

© 2026 Xorch — Concordante Lab. Derechos reservados.
