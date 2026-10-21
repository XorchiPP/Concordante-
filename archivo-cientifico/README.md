# Concordante Lab · Archivo científico

> **EDICIÓN PÚBLICA PARCIAL.** Cuatro entregas, 21 de octubre de 2026: geometría, expedientes reproducibles y áreas documentales con alcance definido. Los originales de trabajo permanecen privados.

Concordante Lab reúne investigación matemática, computacional y exploraciones de interpretación física. Este archivo está pensado para mostrar el trabajo completo: resultados, hipótesis, programas, pruebas, límites, correcciones y rutas que no funcionaron. Cada afirmación conserva su estado científico y el tipo de revisión recibido.

## Estado de esta edición

- **Alcance:** geometría y álgebras en cuatro dimensiones, tres expedientes reproducibles y primeras entregas acotadas de teoría de números, modelos e interpretación física y preguntas abiertas, con índice y política editorial. El resto del programa se incorporará por etapas.
- **Material científico acumulado:** atlas de raíces, acoplamientos por dos bloques, reconstrucción de redes, documentos y cálculos autónomos de teoría de números, modelos e interpretación física, y preguntas abiertas.
- **Fecha de la entrega:** 21 de octubre de 2026.
- **Publicación:** cuatro entregas parciales; el catálogo distingue lo incorporado y lo pendiente.
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

## Orden de lectura

La lectura puede comenzar por geometría y simetría, seguir por fundamentos, teoría de números, cohomología, dinámica y redes, retículas y empaquetamientos, y llegar a modelos e interpretación física. Las preguntas abiertas acompañan todas las etapas. El catálogo indica las secciones disponibles y permite incorporar resultados revisados en cualquier etapa.

## Mapa de áreas

El mapa combina áreas previstas y entregas parciales. Solo los enlaces del catálogo inferior corresponden a materiales incorporados. Cada línea distingue sus resultados cerrados y preguntas abiertas.

| Sección prevista | Contenido que agrupará |
| --- | --- |
| Geometría y simetría | Sistemas de raíces, simetrías de la 600-celda, construcciones geométricas, acciones de grupos y representaciones. |
| Fundamentos y relaciones | Definiciones del modelo, estados, observadores, invariantes, hipótesis de selección y límites estructurales. |
| Teoría de números | Programas Beal/BSD, reducciones condicionadas, datos de entrada y cálculos terminados o pendientes. |
| Cohomología y obstrucciones | Cohomología con distintos coeficientes, presentaciones, operaciones, restricciones, extensiones y problemas pendientes. |
| Dinámica e irreversibilidad | Contactos, ramas, fronteras, resultados locales y globales, reconstrucción y modelos dinámicos. |
| Retículas y empaquetamientos | Códigos, construcciones de retículas, normas mínimas, testigos y certificados de exclusión. |
| Modelos e interpretación física | Puentes geométricos, gravedad, Yang–Mills, límites de continuo y contraste empírico. Analogías y predicciones se identifican por separado. |
| Métodos y reproducibilidad | Código, formatos de certificados, verificadores, entornos, instrucciones y criterios de revisión. |
| Preguntas abiertas y rutas fallidas | Conjeturas, contraejemplos, resultados negativos, obstáculos y tentativas abandonadas. |
| Historial científico | Versiones anteriores saneadas, fe de erratas, dependencias y relaciones de sustitución entre resultados. |

Un mismo resultado tendrá una entrada principal y referencias cruzadas, no copias contradictorias en varias secciones. Los títulos y rutas públicos usarán lenguaje matemático o natural comprensible, no apodos, códigos de expediente ni nomenclatura interna. La tabla de equivalencias con los originales se conservará únicamente en el registro privado. Los identificadores públicos nuevos serán estables y neutrales.

## Catálogo de entregas

### Lotes publicados

- [Atlas exacto de sistemas de raíces finitos](atlas-raices/README.md): 34 modelos finitos y comprobación exacta de cierre por reflexión; límites y revisión en el expediente.
- [Acoplamientos proyectivos por dos bloques](acoplamientos-dos-bloques/README.md): pruebas algebraicas bajo hipótesis explícitas, cálculo exacto acotado y auditoría adjunta.
- [Reconstrucción de redes mediante marcas nodales](redes-observables/README.md): identificación exacta bajo observabilidad, capacidades positivas conocidas e iguales y datos completos; n−1 marcas para n≥1, óptimo en peor caso. La estabilidad ante ruido queda pendiente.

### Áreas incorporadas en la tercera entrega

- [Teoría de números](teoria-de-numeros/README.md): argumentos condicionados, fe de erratas, dos cálculos autónomos reproducidos y resultados históricos no reejecutados. Beal y Birch–Swinnerton-Dyer permanecen abiertos; faltan las entradas masivas y el cálculo Cassels–Tate indicado.
- [Modelos e interpretación física](modelos-fisicos/README.md): documentos de modelos, hipótesis, cálculos y criterios de contraste físico.
- [Preguntas abiertas](preguntas-abiertas/README.md): problemas transversales y obligaciones de prueba o contraste pendientes.

La primera entrega contiene atlas y acoplamientos de dos bloques; la segunda, redes; la tercera abre las tres áreas anteriores; la cuarta añade [Simetrías y álgebras en cuatro dimensiones](simetrias-cuatro-dimensiones/README.md), con cálculo exacto y prueba de completación mínima. Los cuatro cortes son del 21 de octubre de 2026. El resto del archivo sigue pendiente de preparación y revisión.

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


