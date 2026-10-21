# Fe de erratas: Aclaración de signo, testigo integral de índice 11 y alcance del minicaso

> Edición documental del 21 de octubre de 2026. El cuerpo matemático corresponde al informe del 20 de octubre; sus resultados de datos masivos son históricos, no reejecutados en esta edición. Véase ../README.md para la reproducción autónoma disponible y las dependencias ausentes. La fe de erratas prevalece sobre la notación de signo del informe de estructura.


**Concordante Lab · Xorch · 20 de octubre de 2026 · fe de erratas.**  
**Concordante Lab · Xorch · © 2026. Todos los derechos reservados.**  
**Estado del informe histórico:** comprobaciones parciales reportadas; comparación auténtica abierta; Cassels–Tate desconocido; sin demostración de Beal.

## Resultado que debe abrir cualquier resumen de la comparación aritmética

**La comparación aritmética solo se cierra comparando las dos construcciones aritméticas auténticas en cada uno de los `2^21=2.097.152` estados del sector `chi'_1(rho)=-1`, con igualdad literal o con coborde previamente derivado y congelado según el protocolo de comparación.** Las `4719` clases canónicas de Ruta A **no sustituyen** la comprobación por estado: dos estados con igual resultado en A podrían diferir en B. La Ruta B verdadera aún no fue materializada, y Cassels–Tate continúa `UNKNOWN`.

## I. Corregir la notación: signo `nu`, no generador de campo `s`

El informe de estructura ciclotómica escribió `(-1)^s` y `epsilon = s+...` por una colisión desafortunada de letras. En `verificador_historico_de_fibras`, `c[0]` es el **bit de signo** del producto de diferencias de raíces. **No** es el exponente del elemento algebraico `s` que satisface `s^11=2rho` en `M=Q(rho,s,zeta_11)`.

Definimos explícitamente `nu ∈ {0,1}` como `c[0]`, reservamos `b_s` para el exponente de `s` en la base racional del campo `rho^a s^b_s zeta_11^c`, y utilizamos `b_j` para los exponentes de las cinco diferencias restantes. Así:

\[
(-1)^\nu\prod_{j=1}^{10}f_j^{e_j}
=(-1)^\epsilon\zeta_{11}^{t}\prod_{j=1}^{5}f_j^{b_j},
\]
\[
 b_j=e_j+e_{11-j},\qquad
 t\equiv-\sum_{j=1}^{5}j e_{11-j}\pmod{11},\qquad
 \boxed{\epsilon\equiv\nu+\sum_{j=1}^{5}e_{11-j}\pmod 2}. 
\]

Prueba elemental: `f_(11-j)=-zeta_11^(-j) f_j`, deducida de `theta_j=zeta_11^j theta0`. **No sustituir `nu` por `b_s`**: hacerlo altera la expresión y el dato congelado. Para todo monomio firmado la reescritura da esta representación; **la inyectividad** de las claves frente a valores del campo se ha verificado únicamente en el conjunto de 5103 símbolos de la tabla histórica de la primera construcción, no para cualquier elemento de `M^×`.

## II. Los cinco patrones de índice 11, íntegros

La edición del certificado histórico `historico_fibras.json` conserva el testigo siguiente; `verificador_historico_de_notacion` recalcula su determinante por la fórmula exacta de Leibniz, sin pedir confianza en el JSON:

\[
 A=\begin{pmatrix}
 -1&-1& 1& 0& 0\\
 -1& 0&-1& 1& 0\\
 -1& 0& 0&-1& 1\\
 -1& 1&-1&-1&-1\\
  0&-1&-1& 0& 1
 \end{pmatrix},\qquad \boxed{\det(A)=+11}.
\]

Cada fila `a=(a_1,...,a_5)` cumple `sum(j*a_j) ≡ 0 mod 11`. La aplicación `Z^5 -> Z/11`, `a |-> sum(j*a_j)`, es sobreyectiva porque su primer coeficiente vale 1. Su núcleo `K` tiene entonces **índice 11 y rango 5** (no rango 4). Las filas de `A` generan un retículo de índice `|det A|=11` contenido en `K`; como ambos tienen el mismo índice, son idénticos. Los 17 patrones históricos incluyen estas cinco filas y por ello generan `K`.

Esto clasifica el **retículo de relaciones de fases observadas**. No pretende clasificar todas las dependencias multiplicativas posibles entre elementos arbitrarios de `M`.

## III. Los diez testigos y su órbita de Galois

En `K(s)` fijamos `theta0=2(rho²-3)s^9`. Como los grados 33 y 10 de `K(s)` y `Q(zeta11)` son coprimos, las extensiones son linealmente disjuntas. Cada automorfismo `zeta11 -> zeta11^a` (`a=1,...,10`) se extiende a `M` fijando `theta0` y permuta transitivamente los diez valores `f_j=theta0(1-zeta11^j)`. Por lo tanto todos tienen la **misma norma absoluta**: `2^600 11^33 13^110` según el cálculo exacto del informe de estructura ciclotómica. Los diez vectores de 330 coordenadas fueron comprobados frente a la tabla archivada; esa comprobación de puntos de anclaje **no sustituye** una demostración independiente de la fórmula completa de Ruta A.

## IV. Tipado del caso de prueba de cónica

El minicaso `X²-2Y²=-W²`, punto `(1:1:1)`, usa `F'=Q`, `M'=Q(sqrt(2))` y `U=1+sqrt(2)`, `V=1-sqrt(2)`. La involución Galois conjuga `U` y `V`, `UV=-1`; el programa verifica explícitamente los cobordes y las identidades de 2- y 3-cociclo en `C2×C2`.

**Eso prueba únicamente la mecánica aritmética/cohomológica del verificador en una extensión cuadrática.** No es un subcaso de Beal, no prueba el lema 4.4.1 ni la proposición 4.4.4 de Shukla y no construye un punto en la cónica original sobre `F` de grado 165, ni la correspondiente Ruta B sobre el campo `M` de grado 330. La `eta_direct` de juguete usa el mismo `U` que la cochain y carece de independencia.

## V. Reproducción de esta edición

La corrección de notación y el argumento de índice y rango se conservan completos. El programa verificar_indice_reticular.py extrae únicamente el cálculo del determinante y el control negativo; no revalida las 5103 claves ni su presencia en la tabla histórica. La revisión histórica de esas claves se conserva en historico_notacion.json, sin reclamar reejecución actual.
