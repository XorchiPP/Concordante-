# Reconstrucción de redes mediante marcas nodales

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Edición pública del 21 de octubre de 2026, a partir de un informe y auditoría del 16 de octubre de 2026.

## Qué demuestra y qué no

Se estudian redes finitas conexas con nodos etiquetados, frontera no vacía, capacidades diagonales positivas conocidas e iguales para las dos redes y modelo interior observable. Se dispone de la transferencia de frontera completa para todas las frecuencias positivas y de respuestas temporales completas a preparaciones nodales conocidas, con el mismo reloj y unidades.

Bajo este contrato, la ambigüedad se clasifica por isometrías de capacidad que fijan el vector constante y las preparaciones, restringidas a transformaciones que conserven un Laplaciano físicamente admisible. Con n≥1 nodos interiores, n−1 marcas nodales bastan (cero para n=1; n=0 fuera de esta fórmula); la cota es óptima en peor caso, no una necesidad para cada red. El informe incluye prueba general autocontenida, reconstrucción exacta y un testigo racional de cinco nodos que permanece indistinguible con una marca.

El grupo algebraico residual no coincide necesariamente con toda la clase de redes admisibles. Preparar un nodo y abrirlo como frontera son protocolos distintos. Sin observabilidad, n−1 preparaciones pueden no identificar la red. La cota no cuenta muestras temporales, precisión, coste experimental ni señales arbitrarias. No hay garantía de estabilidad ante ruido, disponibilidad experimental de las preparaciones, igualdad de actividad estacionaria, prioridad bibliográfica ni deducción gravitatoria.

## Documentos y reproducción

- REPORT.md: hipótesis, pruebas condicionadas, reconstrucción, testigo y límites.
- audit/AUDIT.md: auditoría algebraica histórica y alcance de sus verificaciones.
- verify_marks.py y certificate.json: verificador principal e informe racional exacto.
- audit/verify_independent.py y audit/independent_certificate.json: implementación separada que reconstruye el ejemplo y verifica identidades polinómicas.
- main_stdout.txt, main_stderr.txt, audit/stdout.txt y audit/stderr.txt: salidas de la nueva ejecución de los derivados.
- SHA256SUMS.txt: integridad de los archivos de esta edición, no certificado de verdad científica.

Python 3.12.14 con biblioteca estándar. Sin instalaciones, red ni cuentas. Desde esta carpeta:

    sha256sum -c SHA256SUMS.txt
    python verify_marks.py
    python audit/verify_independent.py

Los programas escriben certificados en sus respectivas carpetas. La nueva ejecución vuelve a comprobar los derivados; no crea una segunda demostración independiente por repetir código. El principal incluye muestras finitas de frecuencias y momentos. El independiente comprueba identidades racionales funcionales para el testigo de cinco nodos mediante determinantes polinómicos y multiplicación cruzada, además de 42 instancias construidas para n=2,3,4,5. Ninguna rejilla sustituye la prueba para todo n.

## Fuentes y derechos

El razonamiento algebraico es autocontenido. Los ayudantes matriciales del verificador principal proceden de un antecedente propio del proyecto; aquí se incluyen íntegros y no requieren importarlo. El segundo verificador no importa el principal ni sus certificados. Antecedente, originales y trazabilidad se conservan completos en custodia privada y siguen pendientes de preparación editorial separada. No se afirma una revisión exhaustiva de literatura ni prioridad externa.

Presentación por marca y alias conforme a elección editorial. RIGHTS.md conserva la reserva de derechos sin transferir titularidad ni conceder una licencia nueva. La preparación de este recurso no exige una revista ya elegida; cualquier conflicto concreto de embargo, anonimato o publicación previa debe revisarse antes de la difusión correspondiente, sin prometer compatibilidad universal.
