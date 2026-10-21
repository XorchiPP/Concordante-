# Estructura ciclotómica: Dominio de 2²¹ estados, codominio M× y las 384 coincidencias ciclotómicas

> Edición documental del 21 de octubre de 2026. El cuerpo matemático corresponde al informe del 20 de octubre; sus resultados de datos masivos son históricos, no reejecutados en esta edición. Véase ../README.md para la reproducción autónoma disponible y las dependencias ausentes. La fe de erratas prevalece sobre la notación de signo del informe de estructura.


**Concordante Lab · Xorch · informe de investigación · 20 de octubre de 2026**  
**Presentación pública:** Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

**Estado del informe histórico:** comprobaciones parciales reportadas; comparación auténtica abierta; Cassels–Tate desconocido; sin demostración de Beal.

## 1. El universo de 2.097.152 estados

El contrato congelado de la tabla histórica, su precompromiso y su protocolo de comparación tiene dos máscaras binarias independientes `S,T` de diez bits, y el signo `chi'_1(tau)∈{+1,-1}`, **con `chi'_1(rho)=-1` fijado**:

\[
X=(\mathbb F_2^{10})_S\times(\mathbb F_2^{10})_T\times C_2,
\quad |X|=2^{10}\cdot2^{10}\cdot2=2^{21}=2,097,152.
\]

La enumeración es completa para **este dominio**; no está tomando una muestra. No demuestra que la dimensión de un grupo Selmer sea 21 ni cubre sin cambio de contrato todos los parámetros de Beal. La rama `chi'_1(rho)=+1` está fuera de la tabla y se declara trivial en la tabla histórica de la primera construcción.

Índice exacto de fila: `2*(1024*S+T)+tau_slot`, con `tau_slot=0` para +1 y 1 para −1. El informe histórico leyó exactamente 23.068.672 bytes de Ruta A, reprodujo las frecuencias por cada uno de los 5103 códigos y verificó 1.572.864 filas de signo positivo y 524.288 de signo negativo.

Una advertencia importante para cualquier prueba de normalización: los **2048** estados con `S=0` valen 1. Para `T=0, tau=+1`, los **1024** estados valen 1, pero para `T=0, tau=-1` solo `S=0` vale 1 y **1023** estados son no triviales. No debe imponerse la falsa identidad universal `eta(S,0,tau)=1` sin considerar el tercer argumento de carácter.

## 2. Codominio: M× y base racional de dimensión 330

Los valores de `eta_A` son números algebraicos no nulos en el grupo **multiplicativo** `M^×`, donde

\[
M=\mathbb Q(\rho,s,\zeta_{11}),\quad
\rho^3+\rho^2-4\rho+1=0,\quad
s^{11}=2\rho,\quad [M:\mathbb Q]=330.
\]

La base `rho^a s^b zeta_11^c` (`a=0..2,b=0..10,c=0..9`) es de un **espacio vectorial sobre Q usado para serializar el campo**, no `Q/Z`, no `\mu_n`, ni una afirmación sobre el rango de un grupo de unidades. La composición y los inversos se hacen en `M`; las 330 coordenadas son solo una representación fiel de cada elemento.

La Ruta B pretende construir la cochain `epsilon_1` en el campo **identificado explícitamente con este mismo M** y producir `eta_B=partial(epsilon_1)`. Igualar únicamente los grados de campos no bastaría: se requieren el mapa de torre/base y las convenciones Galois congeladas. El protocolo de comparación mantiene `SOURCE_DEPENDENCY_EXPLICIT=true` y `FULL_SOURCE_INDEPENDENCE=false`, a la vez que distingue implementaciones computacionales separadas.

El modo `literal_canonical` exige igualdad aritmética exacta por fila; el modo `explicit_coboundary_witness` admite equivalencia por coborde **solo si** una `lambda` fue derivada por cambios de representantes, congelada antes de leer ambas tablas, y después verificada. `comparador_historico` mantiene el segundo modo bloqueado hasta existir aritmética de multiplicación y acción exacta para el testigo.

## 3. ¿Qué significan 5103 → 4719 y el 384?

Al agrupar los 5103 códigos simbólicos por su vector exacto reducido, la distribución de tamaños de fibra es:

| Tamaño de fibra | Valores de M× | Códigos simbólicos |
|---|---:|---:|
| 1 | 4375 | 4375 |
| 2 | 304 | 608 |
| 3 | 40 | 120 |
| **Total** | **4719** | **5103** |

Por tanto, las redundancias son `304 + 2*40 = 384`, repartidas entre **344 fibras** no unitarias. El conjunto de estados cuya etiqueta tiene representaciones múltiples contiene **150.392 filas**, una propiedad distinta del 384. Las 344 fibras reúnen 728 códigos simbólicos.

### Lema ciclotómico de las raíces opuestas

Con `theta_j=zeta_11^j theta_0`, `f_j=theta_0-theta_j`, se tiene, para `j=1,...,5`,

\[
\frac{f_j}{f_{11-j}}=-\zeta_{11}^{j}.
\tag{*}
\]

Sean dos monomios firmados de la tabla y `delta_0` la diferencia de sus bits de signo, `delta_j` la diferencia de sus exponentes de `f_j`. Si `delta_{11-j}=-delta_j` para los cinco pares y `a_j=delta_j`, su cociente firmado vale

\[
(-1)^{\delta_0+\sum_j a_j}\,\zeta_{11}^{\sum_j j a_j}.
\]

Por tanto **dentro de este tipo de diferencias**, ambos monomios coinciden exactamente si

\[
\sum_{j=1}^5 j a_j\equiv0\pmod{11},\qquad
\delta_0+\sum_{j=1}^5a_j\equiv0\pmod2.
\]

Se comprobaron las **424 parejas** de códigos correspondientes a fibras repetidas (304 pares y `3*40` pares de triples), y **todas** cumplen estas identidades, con 17 diferencias de exponentes distintas hasta cambio de signo. Las 424 identidades no se infieren de coincidencia de hashes: el chequeo inspecciona ambas representaciones simbólicas y demuestra su igualdad mediante (*).

### Forma normal ciclotómica: 5103 símbolos en 4719 claves sin operar en el campo de grado 330

La identidad (*) permite reducir **todo** monomio simbólico firmado `(-1)^s prod_j f_j^{e_j}` a una forma de cinco exponentes, una fase y un signo:

\[
\boxed{(-1)^s\prod_{j=1}^{10} f_j^{e_j}
=(-1)^\epsilon\zeta_{11}^{t}\prod_{j=1}^{5}f_j^{b_j},}
\]

con

\[
b_j=e_j+e_{11-j},\quad
 t\equiv-\sum_{j=1}^5j e_{11-j}\pmod{11},\quad
 \epsilon\equiv s+\sum_{j=1}^5e_{11-j}\pmod2.
\]

Este algoritmo usa solo enteros, cinco sumas y dos congruencias. En el conjunto **congelado** de 5103 símbolos se obtienen exactamente **4719 claves** `(b_1,...,b_5,t,epsilon)`. El cotejo bidireccional con los vectores racionales originales demuestra que **cada clave corresponde a un solo valor de M× y viceversa** en este conjunto. De ahí provienen todas las 384 identificaciones. No se afirma que los cinco `f_j` y la fase den una forma normal completa para cualquier elemento arbitrario de M.

Importante para la comparación aritmética: esta compresión simbólica facilita validar Ruta A, pero **no sustituye las 2.097.152 comprobaciones** contra Ruta B, salvo que primero se pruebe que los valores de B respetan las fibras de A.

### La ley subyacente es de índice 11, no un grupo de orden 384

Los 17 vectores proyectados `(a_1,...,a_5)` generan el retículo

\[
\mathcal K=\{a\in\mathbb Z^5:\sum_{j=1}^5 j a_j\equiv0\pmod{11}\}.
\]

Cada vector observado está en `K`. La matriz de cinco vectores observados

```text
-1 -1  1  0  0
-1  0 -1  1  0
-1  0  0 -1  1
-1  1 -1 -1 -1
 0 -1 -1  0  1
```

tiene determinante **+11**. Como `K` tiene índice exactamente 11 en `Z^5`, esos cinco vectores ya generan `K`. El bit de signo se determina por `sum(a_j) mod 2`.

Dos ejemplos independientes de cálculo numérico:

\[
\prod_{j\in\{1,2,3,5\}}\frac{f_j}{f_{11-j}}=(-1)^4\zeta_{11}^{11}=1,
\]

\[
\prod_{j\in\{2,4,5\}}\frac{f_j}{f_{11-j}}=(-1)^3\zeta_{11}^{11}=-1.
\]

**Alcance:** hemos explicado todas las identidades observadas en los 5103 códigos congelados, no clasificado universalmente todas las relaciones multiplicativas posibles del campo M. Tampoco aparece una sola órbita de 384 códigos con el mismo valor.

## 4. Diez valores campo con norma independiente

Los diez símbolos `f_j=theta_0-theta_j` están en Ruta A en los estados `S=T=2^(j−1),tau=+1`. Para `j≤9`, sus coordenadas congeladas son:

- coeficiente −6 en índice 270 y +6 en índice `270+j`;
- coeficiente +2 en índice 290 y −2 en índice `290+j`.

Para `j=10`, la relación `1+zeta+...+zeta^10=0` produce 20 términos, igualmente reconstruidos desde cero. **Los diez** coinciden con los vectores racionales archivados.

La norma se calcula algebraicamente. Sea `K=Q(rho)`. Como la reducción de `p(x)=x³+x²−4x+1` por `x²=3` es `4−x`, se deduce

\[
N_{K/\mathbb Q}(\rho^2-3)=p(\sqrt3)p(-\sqrt3)=16-3=13,
\quad N_{K/\mathbb Q}(2\rho)=-8.
\]

Para `theta_0=2(rho²−3)s^9` y `s^11=2rho`,

\[
\left|N_{K(s)/\mathbb Q}(\theta_0)\right|
=104^{11}8^9=2^{60}13^{11}.
\]

Por lineal disjunción de las extensiones de grados 33 y 10, y `N_{Q(zeta11)/Q}(1-zeta11^j)=11`,

\[
\boxed{
N_{M/\mathbb Q}(f_j)=2^{600}\,11^{33}\,13^{110}
\quad (1\le j\le10).
}
\]

Son enteros algebraicos de norma mayor que 1, no raíces de unidad. Esta es una comprobación directa de **diez valores y su codificación**, no una validación externa de toda la fórmula aritmética de Shukla.

## 5. Un minicaso con punto racional explícito, claramente separado de Beal

El script `verificar_conica_cuadratica.py` emplea

\[
X^2-2Y^2=-W^2,\quad(X:Y:W)=(1:1:1),\quad
M'=\mathbb Q(\sqrt2),\quad U=1+\sqrt2,\ V=1-\sqrt2.
\]

Verifica `N(U)=UV=-1`. Para el grupo `C2×C2`, cuya primera involución conjuga `sqrt2`, construye `e`, el 2-coborde `E=partial e`, una 2-cochain `epsilon` y su 3-coborde `eta=partial epsilon`. Comprueba por aritmética racional exacta 16 parejas de 2-coborde, 64 identidades de 2-cociclo, 64 entradas del 3-coborde y 256 identidades de 3-cociclo. Una mutación deliberada de un valor del 3-coborde se detecta.

**Esta cónica NO es un subcaso del problema específico de Beal, la Ruta B de Shukla NO se ha implementado aquí, y la definición toy de `eta_direct` usa deliberadamente el mismo U.** Su utilidad se limita a verificar el mecanismo de representación, conjugación y cobordes sobre un campo real pequeño. No se obtiene independencia matemática entre dos rutas ni una comprobación de la comparación aritmética.

## 6. Una advertencia lógica acerca de 4719 frente a 2²¹

No basta comparar `eta_B` contra `eta_A` en **una** fila por cada uno de los 4719 valores de Ruta A: dos estados que comparten `eta_A` pueden producir valores `eta_B` distintos. Solo puede usarse esa compresión después de demostrar que `eta_B` es constante sobre **todas** las fibras de `eta_A`; de otro modo deben verificarse las 2.097.152 correspondencias, como exige el protocolo de comparación.

La equivalencia de campo y la equivalencia de cochains son contratos diferentes. La comparación aritmética se mantiene abierta hasta tener la auténtica `eta_B=partial epsilon_1` desde el punto racional de la cónica sobre F de grado 165 y una identificación válida con M de grado 330.

## 7. Evidencias y fronteras de esta edición

Los certificados históricos de fibras y anclajes se incluyen para lectura y contraste, no como resultados recién reproducidos. El programa autónomo verificar_conica_cuadratica.py y el testigo verificar_indice_reticular.py sí son ejecutables con Python estándar. El archivo masivo y sus verificadores dependientes quedan pendientes de una entrega con datos completos. No existe segunda construcción auténtica ni certificado de Cassels–Tate.
