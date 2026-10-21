# Concordante Lab · Archivo científico

> **EDICIÓN PÚBLICA PARCIAL.** Diez entregas, 21 de octubre de 2026: geometría, expedientes reproducibles y áreas documentales con alcance definido. Los originales de trabajo permanecen privados.

Concordante Lab reúne investigación matemática, computacional y exploraciones de interpretación física. Este archivo está pensado para mostrar el trabajo completo: resultados, hipótesis, programas, pruebas, límites, correcciones y rutas que no funcionaron. Cada afirmación conserva su estado científico y el tipo de revisión recibido.

## Estado de esta edición

- **Alcance:** códigos, retículas y vecinos primos, acoplamientos de múltiples bloques, fundamentos relacionales, cohomología módulo dos, geometría y álgebras en cuatro dimensiones, tres expedientes reproducibles y primeras entregas acotadas de teoría de números, modelos e interpretación física y preguntas abiertas, con índice y política editorial. El resto del programa se incorporará por etapas.
- **Material científico acumulado:** códigos y retículas, acoplamientos de múltiples bloques, relaciones de compatibilidad y geometría de grafos, cohomología condicionada con verificaciones algebraicas, simetrías y álgebras en cuatro dimensiones, atlas de raíces, acoplamientos por dos bloques, reconstrucción de redes, documentos y cálculos autónomos de teoría de números, modelos e interpretación física, y preguntas abiertas.
- **Fecha de la entrega:** 21 de octubre de 2026.
- **Publicación:** diez entregas parciales; el catálogo distingue lo incorporado y lo pendiente.
- **Originales de trabajo:** permanecen privados. La copia pública no debe incluir su historial Git, conversaciones, datos personales o documentación administrativa.

Los materiales previos conservan su estado propio y cada ampliación describe la revisión recibida.

## Cómo leer el archivo

Cada entrada deberá indicar por separado:

1. Qué afirma y bajo qué hipótesis.
2. Qué evidencia existe y qué revisión recibió realmente.
3. Qué versión se consulta y si tiene correcciones posteriores.
4. Qué archivos se pueden descargar y si bastan para reproducir el cálculo.
5. Qué continúa abierto.

La [política de estados y alcance](ESTADOS_Y_ALCANCE.md) define estas etiquetas. Un resultado puede ser matemáticamente válido bajo sus hipótesis y seguir sin reproducirse de manera independiente. Un documento publicado también puede contener una conjetura abierta.

## Recorrido de lectura

El hilo principal pregunta: **¿qué podemos conocer de una red a partir de su forma y de su respuesta?** Este es un orden para leer; las dependencias matemáticas se declaran dentro de cada trabajo.

### 1. Qué construimos

[Fundamentos y relaciones](fundamentos-relaciones/README.md): puntos, conexiones, distancia y operadores. La selección de una relación y una dinámica concreta acompaña las construcciones como pregunta abierta.

### 2. Qué propiedades tiene: cuatro ramas paralelas

- **Geometría y simetría:** [atlas de raíces](atlas-raices/README.md) y [simetrías y álgebras en cuatro dimensiones](simetrias-cuatro-dimensiones/README.md).
- **Teoría de números:** [estructuras algebraicas, comparación aritmética y descenso](teoria-de-numeros/README.md), con sus hipótesis y pendientes técnicos.
- **Retículas y empaquetamientos:** [códigos, retículas y vecinos primos](reticulas-codigos/README.md); [distinguir 24 puntos con seis conjuntos de ocho](separadores-veinticuatro-puntos/README.md).
- **Cohomología y obstrucciones:** [manuscrito y restricciones](cohomologia/README.md), con [igualdad de ideales verificada](cohomologia/ideal-membership/README.md) y realización global de clases condicionada.

Las cuatro ramas comparten herramientas y referencias cruzadas; cada una tiene entrada propia.

### 3. Cómo cambia

[Difusión y forma](difusion-y-forma/README.md) → [reconstrucción de redes](redes-observables/README.md) → [acoplamientos de dos bloques](acoplamientos-dos-bloques/README.md) y [múltiples bloques](acoplamientos-multiples-bloques/README.md). Como comparación adicional, [mismos estados recurrentes, distintas dinámicas](estados-recurrentes-dinamicas/README.md). Las flechas indican una secuencia de lectura; cada resultado conserva su contrato propio.

### 4. Qué puede explicar

[Modelos e interpretación física](modelos-fisicos/README.md): magnitudes, parámetros y propuestas de contraste. La selección física, las unidades, el límite continuo y las mediciones independientes se distinguen de los resultados matemáticos.

**Ejemplo conductor:** construir las redes periódicas triangular 64×64 y cúbica 16³; comprobar sus 4096 puntos, 12288 enlaces y seis vecinos; distinguirlas por 8192 frente a cero triángulos; comparar el regreso medio bajo la misma regla de difusión. Una aplicación física añade qué se mide, sus unidades y el experimento de contraste.

**Preguntas abiertas y correcciones, transversales:** la [agenda](preguntas-abiertas/README.md) acompaña los pendientes de cada trabajo. **Cómo se obtuvo y comprobó:** cada expediente enlaza pruebas, código, datos, salidas y hashes; la [política de estados](ESTADOS_Y_ALCANCE.md) explica el tipo de evidencia.

## Compatibilidad con publicaciones posteriores

La apertura busca conservar posibilidades de publicación científica posterior. Datos, código y resultados pueden difundirse antes de elegir revista: existen vías editoriales compatibles con la difusión previa, como muestran las políticas de [Cambridge](https://www.cambridge.org/core/open-research/preprint-policy) y [SIAM Journal on Matrix Analysis and Applications](https://epubs.siam.org/simax/editorial-policy), consultadas el 21 de octubre de 2026. Cada revista aplica condiciones específicas y la elección de destino permanece separada de esta apertura. Si un manuscrito tiene destino previsto, compromisos o restricciones editoriales conocidos, se comprobarán específicamente. Se reservarán las piezas con conflicto concreto o una situación editorial ambigua pendiente de resolver. No se enviarán manuscritos ni se aceptarán condiciones editoriales como parte automática de esta apertura.

## Incorporación por etapas

1. **Inventario y protección.** Identificar familias y versiones; separar datos personales, administrativos, secretos y materiales de terceros no redistribuibles. Resolver duplicados sin borrar el historial científico relevante.
2. **Catálogo trazable.** Crear las fichas y enlazar solo evidencias públicas realmente disponibles. Marcar lo pendiente sin presentarlo como descargable.
3. **Expedientes completos.** Incorporar por familias informes, pruebas, código, entradas, salidas y hashes, con instrucciones y límites explícitos. Los intentos fallidos también se incluyen cuando sean publicables y estén contextualizados.
4. **Material pesado e histórico.** Añadir paquetes por versión y archivos históricos saneados, sin importar automáticamente el historial privado ni los permisos de sus carpetas.
5. **Navegación y mantenimiento.** Conectar el archivo con las explicaciones y experiencias visuales; actualizar el catálogo cuando se verifique una nueva entrega o corrección.

Las etapas organizan el trabajo; no restringen el objetivo de cobertura completa de la investigación publicable. Ningún lote se anunciará como incorporado antes de comprobar sus archivos y acceso público. Los huecos se declararán.

## Fuentes, descargas y derechos

Las referencias bibliográficas apuntarán a la publicación original o a una versión pública legítima. Los resultados propios incluirán evidencia pública suficiente para entender su alcance. Un enlace privado a Drive o al laboratorio no será la única evidencia de una afirmación pública.

La lectura pública no equivale a una nueva licencia de reutilización. Se mantienen los avisos vigentes de [licencia y derechos](../LICENCIA_Y_DERECHOS.md); este índice no añade permisos de redistribución, adaptación, explotación comercial o sublicencia. Los materiales de terceros conservan sus condiciones propias.

## Relación con la presentación visual

La entrada visual y la biblioteca explicativa pueden enlazar este archivo sin convertir todos los expedientes técnicos en pantallas de navegación. El archivo debe permitir descargar y comprobar; la experiencia visual debe permitir descubrir y comprender. Ninguno sustituye las pruebas ni el registro de límites.

## Historial de entregas

### Lotes publicados

- [Atlas exacto de sistemas de raíces finitos](atlas-raices/README.md): 34 modelos finitos y comprobación exacta de cierre por reflexión; límites y revisión en el expediente.
- [Acoplamientos proyectivos por dos bloques](acoplamientos-dos-bloques/README.md): pruebas algebraicas bajo hipótesis explícitas, cálculo exacto acotado y auditoría adjunta.
- [Reconstrucción de redes mediante marcas nodales](redes-observables/README.md): identificación exacta bajo observabilidad, capacidades positivas conocidas e iguales y datos completos; n−1 marcas para n≥1, óptimo en peor caso. La estabilidad ante ruido queda pendiente.

### Áreas incorporadas en la tercera entrega

- [Teoría de números](teoria-de-numeros/README.md): argumentos condicionados, fe de erratas, dos cálculos autónomos reproducidos y resultados históricos no reejecutados. Beal y Birch–Swinnerton-Dyer permanecen abiertos; faltan las entradas masivas y el cálculo Cassels–Tate indicado.
- [Modelos e interpretación física](modelos-fisicos/README.md): documentos de modelos, hipótesis, cálculos y criterios de contraste físico.
- [Preguntas abiertas](preguntas-abiertas/README.md): problemas transversales y obligaciones de prueba o contraste pendientes.

La primera entrega contiene atlas y acoplamientos de dos bloques; la segunda, redes; la tercera abre las tres áreas anteriores; la cuarta añade [Simetrías y álgebras en cuatro dimensiones](simetrias-cuatro-dimensiones/README.md), con cálculo exacto y prueba de completación mínima. La quinta incorpora fundamentos relacionales y cohomología módulo dos. La sexta añade códigos, retículas y vecinos primos, junto con acoplamientos de múltiples bloques. La séptima incorpora separadores de 24 puntos mediante octadas del código de Golay. La octava añade cuatro redes con los mismos estados recurrentes y distintas dinámicas de adición. La novena incorpora difusión en grafos y un suplemento de restricciones cohomológicas. La décima demuestra la igualdad de los dos ideales de relaciones mediante identidades explícitas. Los diez cortes son del 21 de octubre de 2026. El resto del archivo sigue pendiente de preparación y revisión.

### Áreas incorporadas en la quinta entrega

- [Relaciones de compatibilidad y geometría de grafos](fundamentos-relaciones/README.md): construcciones métricas y operadores bajo hipótesis explícitas, ejemplos finitos reproducidos y problemas de selección de relación, transporte y dinámica.
- [Cohomología módulo dos del cociente central de W(F4)](cohomologia/README.md): manuscrito completo de un teorema de anillo condicionado y comprobaciones algebraicas reproducidas; la igualdad de ideales está verificada y la autenticación de clases globales y certificados adicionales conserva su estado explícito en el expediente.

### Ampliaciones de la sexta entrega

- [Códigos, retículas y vecinos primos](reticulas-codigos/README.md): pruebas de mínimos de Construction A, corte binario y límites de vecinos primos, con 17.459 comprobaciones exactas; hipótesis y expedientes pendientes en el informe.
- [Acoplamientos de múltiples bloques](acoplamientos-multiples-bloques/README.md): clasificación universal para un número fijo de bloques y dimensiones sin cota bajo cocientes separados y reloj común, compatibilidad triple y controles exactos reproducidos.

### Ampliación de la séptima entrega

- [Distinguir 24 puntos con seis conjuntos de ocho](separadores-veinticuatro-puntos/README.md): prueba del mínimo de seis octadas, censo de 82 vecinos por una sustitución y trece órbitas certificadas como cota inferior; entradas completas y dos verificadores reproducibles. La clasificación global de órbitas permanece abierta.

### Ampliación de la octava entrega

- [Mismos estados recurrentes, distintas dinámicas](estados-recurrentes-dinamicas/README.md): cuatro redes dirigidas de nueve vértices comparten exactamente 167.040 configuraciones recurrentes, con grupos críticos y acciones de adición distintos. Pruebas, matrices, censos completos, órbitas y datos binarios reproducibles distinguen los contratos estricto y relajado.

### Ampliaciones de la novena entrega

- [Mismos conteos, distinta difusión](difusion-y-forma/README.md): comparación de geometrías con observables locales compartidos, datos históricos y comprobaciones parciales reproducidas. Incluye un [explorador descargable en español](difusion-y-forma/explorador.html) con cinco series de difusión tabuladas.
- [Restricciones sobre seis detectores](cohomologia/restrictions/README.md): reconstrucción finita de soportes y cotejo de 144 columnas. Amplía la evidencia disponible del manuscrito condicionado; la realización global de clases conserva sus dependencias; la décima entrega resuelve por separado la igualdad de ideales.

### Ampliación de la décima entrega

- [Igualdad exacta de los ideales de relaciones](cohomologia/ideal-membership/README.md): 46 identidades explícitas y un evaluador independiente demuestran K⊆J; junto con la reducción publicada J⊆K, establecen J=K. La identificación con la cohomología global conserva sus hipótesis de realización de clases y detección.

Cada lote incluye sus archivos y manifiesto. El [manifiesto de la entrega](SHA256SUMS.txt) permite comprobar los bytes de esta edición. Las secciones pendientes se distinguen de las entregas enlazadas y cada área declara su cobertura.

El catálogo de futuras entregas deberá registrar:

| Campo | Contenido requerido |
| --- | --- |
| Identificador y título | Clave estable y nombre comprensible. |
| Versión y fecha | Corte exacto del resultado, no la fecha de una carpeta cambiante. |
| Estado científico | Resultado demostrado bajo hipótesis, cálculo, conjetura, interpretación, refutado o sustituido. |
| Evidencia y revisión | Prueba disponible; cálculo reportado o reproducido; revisión interna, independiente o externa efectivamente realizada. |
| Alcance | Dominio, parámetros, grados, precisión y excepciones. |
| Archivos | Enlaces públicos verificados a informe, fuentes, código, entradas, salidas y manifiesto. |
| Dependencias | Resultados y versiones necesarios para entender o reproducir la entrada. |
| Límites y correcciones | Alcance preciso, faltantes y enlace al resultado posterior si corresponde. |
