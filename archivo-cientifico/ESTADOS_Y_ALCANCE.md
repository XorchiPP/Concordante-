# Política de estados y alcance científico

> **EDICIÓN PÚBLICA PARCIAL. Política editorial · 21 de octubre de 2026.** Describe cómo se clasifican las entregas. No certifica por sí sola resultados particulares, no modifica licencias y no concede autorizaciones adicionales.

## 1. Separar afirmación, evidencia y disponibilidad

No se utilizará una única etiqueta «resuelto» o «publicado» para mezclar preguntas diferentes. Cada ficha tendrá al menos cuatro campos independientes:

- **Estado de la afirmación:** qué se ha establecido y bajo qué hipótesis.
- **Estado de la evidencia:** qué archivos existen, qué pruebas se revisaron y qué cálculos se ejecutaron.
- **Estado de publicación:** borrador privado, preparado para publicación o publicado con enlace verificable.
- **Estado de versión:** vigente para su alcance, corregido o sustituido por una versión identificada.

«Publicado» no significa «demostrado». «PASS» no significa automáticamente «teorema global». «No detectado» no significa «inexistente» fuera del dominio comprobado.

## 2. Estados de las afirmaciones

### Resultado demostrado bajo hipótesis explícitas

Se ofrece un enunciado preciso con su demostración y dependencias. Se distinguirán:

- **Prueba contenida en el expediente:** los pasos necesarios están disponibles, con las referencias que se usan.
- **Conclusión condicionada:** depende de una premisa adicional, identificación, certificado externo o resultado todavía no verificado en el expediente. Esa condición debe aparecer junto al enunciado, no solo en una nota final.

Todos los teoremas tienen hipótesis. La etiqueta «condicionado» se usa para destacar una dependencia relevante que no debe confundirse con una comprobación propia. Se consignará si la prueba solo fue leída, auditada internamente o revisada por un tercero. La palabra «independiente» requiere explicar qué se reconstruyó y qué entradas o álgebra se compartieron.

### Cálculo o certificado computacional

Resultado obtenido mediante un procedimiento definido. Debe indicar entradas, algoritmo, dominio exhaustivo o muestra, aritmética, versión del código y criterio de aceptación.

- **Reportado:** el expediente o su autor afirma el resultado; esta edición no acredita haber ejecutado el programa.
- **Reproducido:** consta una ejecución del código y entradas identificados, con salidas conservadas y comprobación del criterio declarado.
- **Reproducido por una ruta distinta:** se documentan las diferencias de implementación y las dependencias compartidas. No se llamará independiente a una repetición del mismo cálculo solo por haberse ejecutado en otro equipo.

Los intervalos rigurosos, aritmética exacta y certificados de cobertura se distinguirán de estimaciones de coma flotante. Una tabla finita no demuestra por sí sola una afirmación en todos los grados o para todos los parámetros.

### Conjetura o pregunta abierta

Afirmación propuesta sin demostración suficiente, o pregunta cuyo resultado se desconoce. Se presentarán evidencia favorable, objeciones, contraejemplos descartados correctamente y condiciones bajo las cuales podría fallar. Una conjetura no se convertirá en resultado por repetición entre documentos.

### Interpretación física

Lectura física de una construcción matemática. Debe separar definición del modelo, correspondencia propuesta, parámetros ajustados, observables y predicciones contrastables. Un resultado matemático exacto no establece por sí solo que el modelo describa la naturaleza. Una coincidencia numérica o una analogía no cuenta como derivación física.

### Refutado o resultado negativo

Una afirmación queda refutada en el alcance indicado por un contraejemplo o argumento válido. Se conservarán la afirmación original, el contraejemplo y el dominio afectado. Un teorema de imposibilidad bajo ciertas hipótesis no es una prohibición universal fuera de ellas. Un error de implementación no refuta automáticamente la afirmación matemática.

### Corregido o superado

Una versión fue corregida, ampliada o sustituida. Se indicará cuál y por qué. «Superado» no significa necesariamente falso: puede tratarse de un caso particular absorbido por un resultado más general. La versión histórica se conserva contextualizada cuando pueda publicarse sin exponer información reservada.

## 3. Reproducibilidad mínima

Para declarar un expediente computacional reproducible deben estar disponibles:

1. Enunciado, hipótesis y dominio probado.
2. Código fuente y datos de entrada necesarios, o un procedimiento determinista para reconstruirlos.
3. Instrucción de ejecución, versiones de dependencias, recursos aproximados y semillas si hay aleatoriedad.
4. Salidas relevantes, registros de ejecución y criterio verificable de éxito o fallo.
5. Manifiesto de archivos con hashes y versión exacta del corte.
6. Explicación del vínculo entre la salida y la afirmación matemática.

Si falta un elemento necesario, se marcará **reproducibilidad incompleta** y se identificará la pieza concreta. Un manifiesto sin los archivos no completa una entrega. Un hash identifica bytes; no demuestra corrección matemática. Si los archivos fueron saneados, se recalcularán sus hashes y se documentará el alcance de la transformación sin revelar lo retirado.

No se exigirá ejecutar servicios de pago ni acceder a credenciales privadas para consultar la evidencia pública. Cuando un resultado dependa de software no disponible libremente, se declarará esa limitación y se publicarán los artefactos permitidos; no se fingirá una alternativa ya verificada.

## 4. Procedencia y dependencias

Cada expediente conservará un identificador público estable y neutral, fecha, versión, lista de archivos, referencias y relación con resultados previos. Se usarán títulos naturales o matemáticos, sin apodos ni códigos internos. La equivalencia con los identificadores originales se mantendrá solo en el registro privado. La procedencia privada podrá documentarse en un registro reservado; el público recibirá una referencia de versión y evidencia accesible, no enlaces que exijan acceso al laboratorio como único respaldo.

Para fuentes externas se indicarán título, autoría bibliográfica pertinente, versión y localización pública legítima del resultado utilizado. Se citarán las hipótesis exactas y se explicará la traducción de notación cuando sea necesaria. No se redistribuirán textos, imágenes o programas de terceros sin condiciones que lo permitan. La bibliografía científica no se sustituirá por atribuciones imprecisas.

Las correcciones se propagarán a las fichas dependientes: una dependencia refutada o modificada obliga a revisar el estado de las conclusiones que la utilizan.

## 5. Privacidad y separación de copias

La publicación se prepara como copia separada. No se importarán automáticamente el historial del repositorio privado, conversaciones completas, carpetas personales, solicitudes de financiación, documentación administrativa, credenciales o datos de terceros ajenos al contenido científico.

También se revisarán metadatos de documentos, nombres de archivo, rutas locales, comentarios, registros, salidas de notebooks, enlaces privados y archivos comprimidos. Un archivo comprimido se revisa por su contenido, no solo por su nombre. La presencia de una ruta o enlace interno no prueba por sí sola una filtración de secretos, pero requiere decidir si pertenece a la versión pública.

La presentación utilizará la marca Concordante Lab, sin incorporar datos de contacto personales. Los avisos de derechos existentes y las atribuciones de terceros no se eliminarán ni sustituirán automáticamente. Si una pieza requiere resolver esa tensión, queda pendiente de revisión editorial específica; no se inventará una autorización.

## 6. Publicación por lotes

Antes de anunciar un lote como publicado:

- Comprobar que el inventario corresponde a los archivos realmente entregados.
- Revisar privacidad, condiciones de terceros, estados científicos y enlaces.
- Fijar versión y hashes de los archivos finales.
- Verificar que los enlaces públicos y las descargas funcionan sin acceso privado.
- Enumerar los faltantes y evitar expresiones como «archivo completo» si aún hay familias no incorporadas.

Las versiones antiguas, refutaciones y fallos se publican con contexto y enlaces a las correcciones. No se presentarán como conclusiones vigentes ni se ocultarán únicamente por ser resultados negativos.

## 7. Compatibilidad editorial antes de abrir

La autorización de apertura busca preservar posibilidades de publicación científica posterior. No se afirmará que cualquier difusión previa es compatible con cualquier revista, ni se exigirá elegir una revista para cada dato, programa o resultado antes de abrirlo. La apertura general puede apoyarse en vías editoriales compatibles comprobadas, sin convertirlas en promesas de aceptación.

Como referencias, las políticas de [Cambridge sobre preprints](https://www.cambridge.org/core/open-research/preprint-policy) y de [SIAM Journal on Matrix Analysis and Applications](https://epubs.siam.org/simax/editorial-policy), consultadas el 21 de octubre de 2026, muestran vías compatibles con difusión previa bajo sus respectivas condiciones. No acreditan compatibilidad con todos los destinos ni elección de alguno por parte del proyecto.

Si un manuscrito tiene revista objetivo, contrato, embargo o restricción editorial conocida, se comprobará la política específica y se conservará su fuente y fecha. Las piezas con conflicto concreto o una situación editorial ambigua se mantendrán pendientes hasta resolverla. La mera ausencia de revista objetivo no constituye ese conflicto. Una etiqueta de «borrador» o un aviso de derechos no resuelve por sí solo una restricción. No se confundirá acceso de lectura con cesión de derechos.

## 8. Derechos y límites de esta política

Esta política organiza evidencia y lectura; no concede licencias nuevas ni cambia los [avisos de licencia y derechos](../LICENCIA_Y_DERECHOS.md). Abrir el acceso de lectura y otorgar derechos de reutilización son decisiones distintas.

La revisión editorial de un lote no constituye arbitraje académico, validación empírica, promoción a un canon ni cierre de las preguntas abiertas del programa.
