# Atlas exacto de sistemas de raíces finitos

Entrega pública de Concordante Lab, 21 de octubre de 2026. La publicación de este recurso computacional puede coexistir con artículos posteriores según su política editorial. Antes de someterlo a una revista se revisarán su política de preprints, anonimato y embargos. La reserva de material responde a conflictos concretos o ambigüedades relevantes. La aceptación de un artículo depende de la revista y su evaluación.

## Alcance

El programa construye modelos de coordenadas exactas para A1–A8, B2–B8, C2–C8, D4–D8, E6, E7, E8, F4, G2, H3 y H4: 34 instancias finitas. Opera sobre racionales y Q(phi), con phi²=phi+1. H3 y H4 son no cristalográficos. Las etiquetas son notación matemática estándar.

Verifica cierre por reflexión para cada pareja de raíces en cada modelo mediante pares enteros que codifican 2v en Z[phi]. Las pruebas secundarias sobre la implementación racional más lenta muestrean normales en los sistemas grandes. Los tests de métrica y equivariancia también usan muestras. La comprobación cristalográfica negativa termina al encontrar un contraejemplo; no implica recorrer todas las parejas de los casos negativos.

Esta entrega reproduce cálculos exactos en los 34 modelos finitos enumerados, dentro de la teoría clásica de sistemas de raíces. El comprobador rápido de cierre presupone coordenadas semienteras en Z[phi] y normas racionales positivas; las entradas deben satisfacer esas hipótesis. Un conjunto vacío daría cierre verdadero por vacuidad: usar aquí únicamente los modelos no vacíos enumerados.

## Reproducir

Requiere Python moderno con biblioteca estándar; probado con la versión registrada en REVIEW.md. No necesita red, paquetes externos, cuentas ni instalaciones. Desde esta carpeta:

    PYTHONHASHSEED=123 PYTHONDONTWRITEBYTECODE=1 python -m unittest -v test_root_atlas_exact.py
    PYTHONDONTWRITEBYTECODE=1 python reproduce_report.py > exact_report.json

La primera orden reproduce 11 tests. La segunda genera el informe finito con las 34 instancias. tests.log conserva la salida de la ejecución de preparación; la duración no es determinista. SHA256SUMS.txt identifica los bytes de esta entrega.

## Archivos

- root_atlas_exact.py: constructores y verificadores exactos; cálculo ilustrativo de una reflexión y sus invariantes.
- test_root_atlas_exact.py: pruebas de regresión, cardinalidades, antipodalidad, reflexión, métrica, Cartan y control negativo.
- reproduce_report.py y exact_report.json: generador e informe reproducido.
- tests.log: ejecución de los tests del candidato.
- REVIEW.md: estado y límites de la revisión.

## Procedencia y derechos

Concordante Lab · © 2026. Todos los derechos reservados. Versión para consulta pública, 21 de octubre de 2026; estado científico: informe computacional exacto finito.

La consulta pública no conceden por sí mismas licencia de redistribución, adaptación, explotación comercial ni entrenamiento de sistemas. No se adopta una licencia nueva. Los materiales de terceros conservan sus derechos. Véase RIGHTS.md.

Referencia de terminología y teoría estándar: Pavel Etingof, *Lie Groups and Lie Algebras I*, MIT 18.745, otoño de 2020, Lecture 21: Root Systems. [Recurso oficial MIT OpenCourseWare](https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/resources/mit18_745_f20_lec21_pdf/). [Colección oficial de apuntes](https://ocw.mit.edu/courses/18-745-lie-groups-and-lie-algebras-i-fall-2020/resources/lecture-notes/). Consultados el 21 de octubre de 2026. Se enlaza la fuente; no se redistribuye su texto. La referencia aporta terminología y teoría estándar; la implementación y el tratamiento de H3/H4 corresponden al código de este expediente.

La versión íntegra del expediente y su trazabilidad se conservan para preparación posterior. El código mantiene una estructura de resultado de reflexión con dos campos de estado no evaluados; son metadatos y no modifican el cálculo. Sus nombres se generalizaron consistentemente sin eliminar funcionalidades.

## Límites matemáticos adicionales

El espacio del sistema es span(Phi), no necesariamente todo el espacio de coordenadas: A_n se representa en dimensión ambiente n+1; E6 y E7 en ocho coordenadas; H3 en cuatro coordenadas sobre Q(phi). Los tests no comprueban explícitamente rango, irreducibilidad, marco simple ni el axioma de sistema reducido. antipodal_lines cuenta parejas {v,-v}; por sí solo no descarta otros múltiplos colineales. Los cocientes 2 y 3 para F4/G2 se refieren a normas al cuadrado, no a longitudes.

Las dos rutas aritméticas comparten el generador de coordenadas: ofrecen un contraste de la aritmética sobre esa entrada común. Las verificaciones cubren exclusivamente los modelos y propiedades descritos arriba.
