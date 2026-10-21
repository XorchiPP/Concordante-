# Comparación aritmética y reproducción de la primera construcción

> Edición documental del 21 de octubre de 2026. El cuerpo matemático corresponde al informe del 20 de octubre; sus resultados de datos masivos son históricos, no reejecutados en esta edición. Véase ../README.md para la reproducción autónoma disponible y las dependencias ausentes. La fe de erratas prevalece sobre la notación de signo del informe de estructura.


**Concordante Lab · Xorch, informe de investigación, 20 de octubre de 2026.**  
**Presentación pública:** Concordante Lab · Xorch · © 2026. Todos los derechos reservados.  
**Estado del informe histórico:** comprobaciones parciales reportadas; comparación auténtica abierta; Cassels–Tate desconocido; sin demostración de Beal.

## 1. Resultado y alcance

Se recuperaron, **sin crear un ZIP nuevo**, los paquetes preexistentes `tabla_historica.zip`, `precompromiso_historico.zip` y `protocolo_historico.zip` desde las carpetas auténticas de Drive. Se revisaron los contratos de precompromiso y comparación en GitHub y las limitaciones del diagnóstico de ejecución en Drive. La comparación aritmética **no se ha cerrado**, porque no existe entre las entradas disponibles una salida aritmética de Ruta B procedente del punto de la cónica.

Se obtuvo un avance independiente del bloqueo: un lector exacto que recorre la tabla auténtica de Ruta A y un comparador de igualdad *entre valores reducidos del campo* preparado para la futura Ruta B.

| Afirmación | Estado |
|---|---|
| ZIP original de la tabla histórica íntegro, contra recibo de procedencia | `PASS` |
| 2.097.152 filas de 11 bytes, SHA256 crudo y comprimido | `PASS` |
| 5.103 códigos simbólicos, recuentos de cada uno | `PASS` |
| 4.719 valores exactos distintos de dimensión 330 | `PASS` |
| 344 grupos de colisión simbólica después de reducción | `PASS` |
| 524.288 filas de signo negativo y 1.572.864 positivo | `PASS` |
| Reejecución completa de 2.097.152 estados de la fórmula de pairing de A | `PASS` |
| Segunda fórmula `eta_closed_block`, 32 secciones / 65.536 filas | `PASS`, mismo paquete fuente |
| Comparación con eco SINTÉTICO independiente de orden de diccionario, 2.097.152 estados | `TEST_PASS`, no Ruta B |
| Mutación artificial de una única fila | Detecta una sola discrepancia y testigo lexicográfico |
| Fila truncada, Magma no probado, convención alterada, \(\lambda\) post hoc | Rechazos `PASS` |
| Tabla real de Ruta B, derivada de \(\partial\epsilon_1\) | `NOT_PROVIDED` |
| Comparación aritmética real | **`OPEN`** |
| Signo \(\epsilon_{CT}\) y conjetura de Beal | **`UNKNOWN` / `NOT_PROVED`** |

## 2. Entradas bloqueadas por SHA256

**Paquete de la tabla histórica de la primera construcción:** `4d9326c8f457b7a046772268e9af9ca501243525956be69fdf5bf56b906946eb` (recibo original de Drive).  
**Tabla simbólica sin comprimir:** `e9dcccfdd621239d14c13f6aeadabba8167e6a61b70a33dde1d1eabb1d964801`.  
**Tabla comprimida:** `29c231595360410edc949dd471ec4348cc7bae9893e658b4f06d4b06719199b4`.  
**Diccionario de valores reducidos:** `e565ad6d8bab1cd2e5a434dc5a7eea8314ac50e2997d7a427986a6c321bb1eca`.  
**Fuente de compilación A:** `a927a5962ff17f5240c2d09f4b806c621ab148c06a93594425fc409b351b134d`.

La tabla A está codificada por estado en once bytes: un bit de signo y diez exponentes con signo. El orden es

\[
i=2(1024 S+T)+\mathrm{slot}_{\tau},\quad S,T\in\{0,\ldots,1023\},\quad \mathrm{slot}_{\tau}=0\,(+1),\ 1\,(-1),\]

con \(\rho\) fijo en \(-1\). La rama \(\rho=+1\) se conserva fuera de esta tabla.

La canonización descomprime cada monomio a un vector esparso con índices entre 0 y 329, y racionales `numerador/denominador` **reducidos**, siguiendo

\[
\rho^a s^b\zeta^c,\quad ((b\cdot3+a)\cdot10+c),\quad 0\le a<3,\quad0\le b<11,\quad0\le c<10.
\]

Dos monomios diferentes que se reducen al mismo vector canónico se tratan correctamente como el mismo valor. Un identificador de campo **nunca** sustituye el cotejo de los propios racionales canonizados: se construye desde la clave exacta del vector. Un hash sirve para custodia, no se usa como axioma de igualdad aritmética.

## 3. Contrato del comparador histórico (no incluido en esta entrega)

**Modo sin Ruta B:** revisa todos los hashes, todos los códigos, todo el diccionario, todas las frecuencias de las 2.097.152 filas y los signos; emite el estado de comparación abierta.

**Modo de regresión:** construye un eco **sintético** de Ruta A cuyo diccionario de campo está invertido, para impedir falsos positivos por coincidencia de etiquetas de código. Compara exactamente las 2.097.152 filas. En una copia temporal cambia la fila `1234567` a otro valor; devuelve una sola diferencia con

`S=602, T=835, tau=-1, rho=-1`.

La regresión además rechaza longitud no válida, declaraciones faltantes de punto Magma, cambios de política de uniformizadores y una \(\lambda\) post hoc. Las copias sintéticas se borran y **no se archivan como prueba Ruta B**.

**Modo aritmético real (preparado, aún no ejercitado):** recibe un manifiesto precomprometido por ruta; un diccionario B `formato de valores racionales exactos` con vectores exactos en la base de 330; y una tabla B binaria ordenada de 2.097.152 índices `uint32` little-endian hacia ese diccionario. Antes de leer las filas compara los manifiestos, el convenio de Galois por la izquierda, los cinco hashes compartidos, los representantes divisorales, el pairing, los uniformizadores y las etiquetas de raíces cuadradas. Comprueba los SHA256 de los archivos B y sus 660 racionales de procedencia y verifica que la fórmula final es `partial(epsilon1)` y no `partial(e1)`.

**Limitación del modo real:** un manifiesto con hashes autodeclarados no constituye por sí mismo certificación de que Magma haya resuelto la cónica. La salida real y los cálculos de \(p_j\), \(e_1\) y \(\epsilon_1\) deberán auditarse separadamente antes de promover un posible cotejo a teorema aritmético. El lector no inventa esos datos.

### Dos modalidades y su frontera

`literal_canonical`: solo con manifiestos iguales en todas las convenciones declaradas. Exige igualdad exacta de vectores campo en las **2.097.152** filas. No compara cadenas de productos de raíces ni números decimales.

`explicit_coboundary_witness`: sigue **cerrada por defecto**. Requiere derivación anterior a las tablas, precompromiso de \(\lambda\), verificación exacta de la multiplicación y acción sobre el campo, y prueba de \(\eta_B=\eta_A\partial\lambda\). Ese motor de multiplicación de un coborde general sobre el campo de grado 330 **no está implementado en este corte**: ninguna tabla puede cerrar por esta modalidad todavía.

La selección se hace con manifiestos, **nunca** tras observar los valores finales. El informe no declara que las rutas sean matemáticamente independientes: el protocolo de comparación establece `SOURCE_DEPENDENCY_EXPLICIT=true`, `FULL_SOURCE_INDEPENDENCE=false`, `DUAL_IMPLEMENTATION_SEPARATION=true`.

## 4. Ruta que queda para la comparación aritmética

1. Materializar un punto racional \((X:Y:W)\) sobre \(F\), \([F:\mathbb Q]=165\), en `X²−nY²=αW²`; conservar ejecución y stdout de Magma (o certificado aritmético legítimo equivalente). **No hay todavía coordenadas verificadas.**
2. Levantar al campo \(M\) de grado 330 y obtener **660 coordenadas racionales**, 330 para cada una de \(U,V\), con orden de torre congelado. El diagnóstico de ejecución ya conserva el controlador, no hace falta escribir otro.
3. Construir los diez \(p_j\), certificar las 90 acciones cruzadas, sellar \(E_1\) como entrada fuente; ejecutar lema 4.4.1 y contrastar \(\partial e_1=E_1\) sobre 1.048.576 pares.
4. Construir \(\epsilon_1\) mediante proposición 4.4.4; evaluar \(\eta_B:=\partial\epsilon_1\) en la misma base. Sellar antes la modalidad de comparación y, si procede, la derivación de \(\lambda\).
5. Entregar los manifiestos y las tablas B al comparador; solo una ejecución sobre **los dos conjuntos auténticos** podrá emitir un cierre de la comparación aritmética. El resultado no resolvería por sí solo el objetivo global de Beal ni \(\epsilon_{CT}\).

**Misma convención la convención de consistencia:** verificar \(\partial e_1=E_1\) es `LEMMA_4_4_1_IMPLEMENTATION_CONSISTENCY`; no es una segunda prueba independiente del origen de \(E_1\).

## 5. Reproducción y procedencia de esta edición

Los comparadores históricos y la tabla masiva no se incluyen en este lote. Sus resultados anteriores se conservan como resultados reportados, no como nuevas ejecuciones. La comparación auténtica permanece abierta. Véanse ../README.md y ../BIBLIOGRAFIA.md.
