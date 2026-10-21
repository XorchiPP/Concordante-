# Sistemas separadores de octadas y órbitas de Mathieu

Concordante Lab · Xorch

© 2026. Todos los derechos reservados.

Edición del 21 de octubre de resultados archivados el 10 de octubre de 2026.

## 0. Contrato y mínimo de seis octadas

Fijamos el código binario extendido de Golay en 24 coordenadas y su familia de 759 palabras de peso ocho, llamadas octadas. Un sistema separador es una colección de octadas que asigna firmas de pertenencia distintas a los 24 puntos. En el texto «lector» designa únicamente esa función combinatoria.

**Prueba de la minimalidad.** Con k≤4 hay como máximo 2^k≤16 firmas. Con cinco octadas hay 5·8=40 incidencias. Los 24 vectores distintos de F₂⁵ con menor peso total tienen pesos 0 (uno), 1 (cinco), 2 (diez), 3 (ocho): suman 0+5+20+24=49>40. Cinco octadas tampoco pueden separar los 24 puntos. Las seis máscaras exhibidas abajo sí lo hacen, verificando suficiencia. Esta prueba vale para observables de peso ocho y no presupone búsqueda exhaustiva entre todas las colecciones.

La entrada pública conserva las 759 máscaras y el testigo de seis octadas. La otra ruta de verificación reconstruye las 4096 palabras del código desde esas máscaras. El orden de M24 y los hechos globales sobre Conway se usan como resultados clásicos citados; las comprobaciones propias conciernen a los datos finitos y estabilizadores descritos.

## 1. Portador exacto y equivalencias

Sea `X24={0,...,23}` el conjunto de 24 coordenadas del código y sea `O` el sistema de 759 octads del código de Golay extendido `C24`. Para una colección de seis octads distintos y sin orden `R={O_0,...,O_5}` escribimos

\[
\sigma_R(i)=\big(\mathbf 1_{i\in O_0},\ldots,\mathbf 1_{i\in O_5}\big)\in\mathbb F_2^6.
\]

`R` es un **lector mínimo de seis octads** si sus 24 firmas son distintas (la minimalidad cardinal proviene del no-go para cinco octads del §0). Dos lectores se consideran equivalentes únicamente si alguna permutación de `M24` lleva el conjunto no ordenado de seis octads del primero al del segundo. La reordenación de los seis bits de lectura no cambia el lector. La identificación Aut(C24)=M24 es un hecho clásico citado; el programa reconoce automorfismos del código mediante sus octadas o una base, usando esa identificación.

**Teorema de rigidez del lector.** Si `g ∈ Stab_M24(R)`, entonces induce una permutación `π ∈ S6` de los seis octads. Se cumple `σ_R(g i)=π σ_R(i)` y la inyectividad de `σ_R` muestra que `π` determina `g` completamente. De aquí:

\[
\boxed{\operatorname{Stab}_{M_{24}}(R)\hookrightarrow S_6.}
\]

Ésta es una prueba de grupo, no un cálculo aproximado. En particular, ningún automorfismo no trivial puede fijar **individualmente** los seis octads de un lector resolvente.

Para computar exactamente el estabilizador solo hacen falta las `6!=720` permutaciones de bits de lectura. Se construye la permutación inducida de `X24` (cuando preserva el conjunto de firmas) y se comprueba si conserva los 759 octads. El verificador independiente, en cambio, comprueba si conserva una base de 12 generadores del **código completo** de 4096 palabras. Los dos métodos coinciden.

## 2. Vecindario completo de un lector congelado

El testigo del §0 (hexadecimal; bit `i` significa punto `i`) es

`708191, 868a05, 125858, a00d2a, 28c690, 90a246`.

Se deja fija una quinteta de octads y se reemplaza exactamente uno de los seis. Para construir todas las completaciones, cada clase de puntos indistinguibles por los otros cinco lectores tiene que tener tamaño como máximo dos; si tiene exactamente dos puntos `{i,j}`, el octad final debe contener **exactamente uno** de ellos. Esto da un criterio de completación finito y exhaustivo, sin recorrer \(\binom{759}{6}\).

Los números de completaciones posibles, **incluido el octad original**, son

\[
\boxed{(4,12,24,4,12,32)}.
\]

Por tanto hay `3+11+23+3+11+31=82` vecinos resolventes distintos a distancia de una sustitución. Todos fueron enumerados. Para cada uno se registraron dos invariantes conservados por `M24`:

1. **Histograma de firmas** `h_k=#{i: |σ_R(i)|=k}` para `k=0,...,6`.
2. **Intersecciones de pares**: multiconjunto de las quince cantidades `|O_r ∩ O_t|`.

Al incluir el orden del estabilizador exacto, los 82 vecinos contienen **al menos once órbitas `M24` diferentes**, porque aparecen once triples `(h,intersecciones,|Stab|)` distintos: nueve con estabilizador trivial, una con estabilizador `C2`, y una con estabilizador `C3`. El certificado conserva un representante hex explícito de cada tipo; el censo de 82 vecinos y sus once triples es completo. La igualdad de triple no prueba equivalencia global, por lo que once es una cota inferior de órbitas.

## 3. Dos representantes adicionales con estabilizador cíclico C6

Se exhiben dos lectores válidos de estabilizador `C6` hallados en la exploración histórica. Su validez se verifica directamente: el certificado relee sus seis máscaras y **demuestra directamente** las 24 firmas distintas, sus 720 candidatos de permutación y la pertenencia exacta a `Aut(C24)`.

**Primer lector cíclico:**

`2e04a8, 802b8c, 421962, 90444b, 851231, 1d8806`.

Sus quince intersecciones satisfacen todas

\[
|O_r\cap O_t|=2\ (r\ne t),\qquad
G_{rs}=|O_r\cap O_s|=6I_6+2J_6.
\]

Los 24 puntos presentan pesos de firma `6` de peso uno, `12` de peso dos y `6` de peso tres; ninguna firma se repite. El estabilizador del conjunto de seis octads en `M24` consta de seis permutaciones; su distribución de órdenes es `1^1,2^1,3^2,6^2`, por lo que es **C6**, no S3. Un generador de orden seis actúa sobre las 24 líneas en **cuatro órbitas de longitud seis**:

- `(0,20,19,7,8,12)`;
- `(1,18,3,11,5,23)`;
- `(2,17,9,6,16,10)`;
- `(4,14,15,21,13,22)`.

Esto da una carta exacta `24 = 4×6` obtenida de la simetría del *lector*. La comparación con otras acciones de C6 o con el sexteto `24=6×4` requiere construir un mapa adicional entre esas acciones.

**Segundo lector cíclico:**

`11e103, c38260, 4d3014, 2a1702, 884e06, 221139`.

Su estabilizador también es C6, pero su histograma de puntos y sus intersecciones difieren de las del anterior. Por eso las dos selecciones pertenecen a órbitas `M24` distintas. Ninguna de ellas coincide con los once tipos locales (cuyo estabilizador tiene orden 1, 2 o 3).

## 4. Cota inferior de órbitas y número de lectores

La acción de `M24` sobre sextetos de octads resolventes produce una órbita de cardinal `|M24|/|K|` cuando el estabilizador tiene orden `|K|`. Los **trece representantes inequivalentes certificados** tienen distribución:

| Orden `|K|` | Órbitas distintas certificadas | Lectores por órbita | Cota sumada |
|---:|---:|---:|---:|
| 1 | 9 | 244,823,040 | 2,203,407,360 |
| 2 | 1 | 122,411,520 | 122,411,520 |
| 3 | 1 | 81,607,680 | 81,607,680 |
| 6 | 2 | 40,803,840 | 81,607,680 |
| **Total** | **≥ 13** | | **≥ 2,489,034,240** |

\[
\boxed{\#\{\text{lectores mínimos de seis octads}\}\ge2\,489\,034\,240.}
\]

Ésta es una **cota inferior exacta demostrada por órbitas disjuntas** y no el número total de lectores. El espacio completo de órbitas bajo `M24` continúa abierto.

## 5. Toda lectura mínima es frágil a borrar un sensor

Existe un no-go adicional que deriva del cierre del §0: **cada uno de los seis lectores es necesario individualmente**. Si al eliminar algún lector las 24 firmas siguieran distintas, cinco octads bastarían, lo que contradice la cota de peso `49>40` del §0.

Equivalentemente, para **cada** bit `r` del lector existen al menos dos puntos `i,j` que difieren exclusivamente en ese bit:

\[
\boxed{\forall r\in\{0,\ldots,5\}\ \exists i\ne j:\ \sigma_R(i)\oplus\sigma_R(j)=e_r.}
\]

Por tanto una lectura mínima de seis octads **no tolera el borrado arbitrario de un sensor** y no garantiza detección de un error de un bit. El testigo del §0 tiene números de parejas críticas `(8,6,6,8,6,4)`; el primer testigo C6 tiene `(6,6,6,6,6,6)`. Esta uniformidad es consecuencia de la simetría cíclica de ese lector, no una ley universal.

## 6. Transporte entre cruces: qué es equivariante y qué no

La construcción preserva la separación del §0: `Co0` es el grupo de isometrías globales de Leech; su estabilizador de una cruz no orientada es el grupo clásico `H0=2^12:M24`. Sobre una cruz marcada `F`, el lector es una colección de seis operadores diagonales de signos de octad en el subgrupo `2^12`. Para cualquier `g∈Co0`, transportar el par **decorado** `g·(F,R)=(gF,gRg^{-1})` conserva las 24 firmas por conjugación.

El grupo que conserva el par decorado es `2^12:K`, con `K=Stab_M24(R)` de orden 1, 2, 3 o 6 en los ejemplos. Sobre un marco fijo, su órbita de elecciones tiene `|M24|/|K|` lectores. Los 8 292 375 marcos de Conway son un hecho **externo clásico** (no censado computacionalmente aquí).

**No-go canónico.** No existe una asignación `Co0`-equivariante de **un solo** conjunto de seis lectores a cada marco desnudo: tal sección obligaría al estabilizador completo `H0`, en particular a `M24`, a preservar el conjunto elegido en el marco base. Pero `M24` es transitivo sobre los 759 octads y un conjunto invariante de octads solo puede ser vacío o total; seis no es ninguna de esas posibilidades.

Así, **la selección de un lector mínimo es posible y transportable una vez marcada, pero no puede ser una función canónica del marco desnudo**. El subgrupo de signos `2^12` continúa siendo una ambigüedad de levantamiento incluso cuando los seis lectores fijan todas las 24 líneas.


## 7. Continuación

Quedan por incorporar el desarrollo completo de construcción de Leech y cruces de Conway, y la incidencia de sextetos de los expedientes antecedentes. La clasificación global de sistemas separadores y los sistemas redundantes de siete o más octadas son preguntas distintas del censo local aquí demostrado. Los hechos clásicos y los controles de este caso se distinguen en [la bibliografía](BIBLIOGRAFIA.md) y [la verificación](VERIFICACION.md).
