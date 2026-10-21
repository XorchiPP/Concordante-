# Predictor de curvatura y residual variacional no abeliano

**Concordante Lab · Xorch · Fuente matemática: 20 de octubre de 2026. Edición: 21 de octubre de 2026.**

**Clasificación: informe de cálculos previos y derivación perturbativa, no teorema de convergencia.** Esta edición conserva el contenido matemático del informe de origen, salvo la corrección notacional explícita de la fe de erratas sobre proyección que se incluye más abajo. Los arrays y scripts del ensayo no están incluidos en este corte: sus cifras se transcriben como resultados documentados, no como reproducción independiente aquí. El paquete de redes adyacente sí tiene código y salidas reproducidos. El potencial y la triangulación completos pertenecen al expediente computacional no distribuido: este documento no es por sí solo un benchmark autosuficiente.

## Resumen ejecutivo

Se puso a prueba la hipótesis concreta de que **el error de interpolación de la curvatura por Whitney de grado dos explica por sí solo el residual variacional no abeliano** observado en el ensayo previo de residual dual. Se fijaron exactamente el mismo potencial afín SU(2) de referencia, el mismo complejo simplicial de referencia lorentziano plano, la acción logarítmica de Christiansen–Halvorsen (ecuación 37) con masa Whitney no diagonal y transportes locales, las mismas cochains libres Dirichlet, y el mismo Gram positivo auxiliar de la norma dual H(curl)'.

**Hallazgo central:** el predictor aditivo de primer orden en el error de curvatura apunta casi exactamente en la dirección del residual (
cos 0.9965, 0.9981, 0.9987 para N=2,3,4), **pero solo alcanza el 11.7 % de su magnitud**. El 88.3 % del error de covector permanece al restarlo sin parámetros libres. El mismo resultado se mantiene dentro del **complemento ortogonal de las 60 direcciones afines**, que capturaba 84.16 % del error cuadrático en N=4. Un ajuste escalar libre puede llevar los cosenos casi a la unidad, pero no prueba atribución física y cambia con la amplitud del campo.

Una derivación independiente de los **coeficientes cúbicos de la acción logarítmica de Christiansen–Halvorsen (ecuación 37)** (Baker–Campbell–Hausdorff para la holonomía de caras y el primer término del transporte entre caras) y sus **derivadas respecto de cada enlace** identificó contribuciones que el predictor aditivo omite. En el límite de acoplamiento débil, el factor de mejor ajuste del predictor pasa a aproximadamente 3.00445, 3.00303 y 3.00228 en N=2,3,4. No existe aquí una demostración de factor universal exactamente 3: se cuantificó el resultado para **este campo y esta triangulación**.

**Alcance importante:** el error de aproximación FEEC/Whitney es real y está comprobado en el control previo de interpolación; también existe inconsistencia de la acción logarítmica de Christiansen–Halvorsen (ecuación 37) no abeliana evaluada sobre un potencial que pertenece exactamente al espacio Whitney. Ambos mecanismos deben permanecer separados. Ni el nuevo test ni el expediente resuelven una raíz Einstein–Yang–Mills acoplada ni certifican la convergencia variacional general en norma dual.

## 1. Objeto geométrico y comparación definida antes de medir

Se reutilizan los archivos congelados del ensayo previo de residual dual: para N=2,3,4 los vectores de enlace libres `continuum_coeff`, `discrete_coeff`, `error_coeff=discrete−continuum` y la matriz `gram` densa o su representación CSR dispersa. El número de variables SU(2) libres es 240, 1827 y 6960. La norma de prueba es **siempre**

\[
\|e\|_{G^{-1}}^2=\sum_{a=1}^3(e^a)^T G^{-1}e^a,
\quad
G=M_{1,+}+D^{T}M_{2,+}D \succ0.
\]

La acción física que motiva la comparación está construida con la **métrica lorentziana** `g=diag(−0.49,1,1,1)`; solo la norma de ensayo usa la métrica auxiliar positiva `g_+=diag(0.49,1,1,1)`.

La curvatura continua en el gauge global fijo del campo afín de referencia es `F=dA+A∧A`, con corchete `[X,Y]=2X×Y`. Para un triángulo orientado `f`, definimos su flujo aditivo `ϕ_f=∫_f F` y la interpolación Whitney2 `I_h^2F=Σ_fϕ_f W_f^{(2)}`. Las integrales polinómicas de los flujos son exactas hasta redondeo. Para cualquier arista libre e y componente de color a, definimos dos predictores **de diagnóstico**, que no son sustitutos gauge-invariantes de la acción logarítmica de Christiansen–Halvorsen (ecuación 37):

\[
 p^{(1)}_{h,e,a}=\int_\Omega
 \langle I_h^2F-F, D_A(W_e T_a)\rangle_g\,dV,
\]

\[
 p^{(2)}_{h,e,a}=
 \frac{\partial}{\partial c_{e,a}}\left[
 \tfrac12\|I_h^2F(A_h+cW_e T_a)\|_{g}^{2}
 -\tfrac12\|F(A_h+cW_e T_a)\|_{g}^{2}
 \right]_{c=0}.
\]

`p^(2)` incluye tanto la variación de F como el cambio que produce interpolar `D_AW_e`. No es la derivada de la acción logarítmica de Christiansen–Halvorsen (ecuación 37) con logaritmos de holonomía basada en vértices distintos y transportes entre caras. Las comparaciones se hacen **componente por componente**, en la misma base de cochains y en la misma norma dual.

### Controles y distinción entre funcionales

- Las 63 pruebas del control previo de interpolación validaron la exactitud variacional de Maxwell/Cartan sobre su propia reconstrucción Whitney1, **no** la identidad `S_CH37(A_h)=S_YM(A_h)` para todo campo no abeliano.
- De hecho, el potencial afín de referencia pertenece exactamente a Whitney1 y tiene holonomías de arista exactas, pero en N=2 la acción logarítmica de Christiansen–Halvorsen (ecuación 37) difiere del funcional continuo en `2.6652219128e−6`. Esta diferencia es un defecto de consistencia del funcional discretizado a malla fija, distinto del error de representar A.
- El contrajemplo funcional correcto para convergencia de acciones sin convergencia de derivadas puede tomarse como `S_h(a)=S(a)+h sin²(a/h)`, cuyo error es `O(h)` y cuya derivada extra es `sin(2a/h)=O(1)`. Para obtener error de acción `O(h²)` con derivada `O(1)` se puede usar `h² sin²(a/h²)`. La cancelación de términos cruzados no se sigue de la estacionariedad de F: Yang–Mills exige `D_A^*F=0`, no `F=0`.

## 2. Falsador directo: dirección excelente, magnitud insuficiente

| complejo simplicial de referencia | Norma del residual CH−continuo | Norma del predictor p^(1) | Cociente predictor/error | Coseno dual | Error tras restar p^(1) |
|---:|---:|---:|---:|---:|---:|
| N=2 | 3.8959591467e−4 | 4.5664944809e−5 | 0.117211 | 0.996507 | 0.883253 |
| N=3 | 3.1443214983e−4 | 3.6761861797e−5 | 0.116915 | 0.998135 | 0.883332 |
| N=4 | 2.56002719497e−4 | 2.9924184220e−5 | 0.116890 | 0.998746 | 0.883276 |

El predictor `p^(2)`, que varía también la interpolación de F, tiene prácticamente los mismos cocientes y cosenos: el efecto adicional `||p^(2)−p^(1)||_*` vale aproximadamente `7.98e−8`, `4.70e−8` y `2.93e−8` de N=2 a N=4. Ambos son correctos como operaciones sobre una interpolación **aditiva y con gauge fijo**, pero **no bastan** para recuperar la acción logarítmica de Christiansen–Halvorsen (ecuación 37).

Los covectores continuos recreados por el integrador de este expediente coinciden con los certificados del ensayo previo de residual dual con errores relativos `5.40e−15`, `9.30e−15` y `1.11e−14`. Esto controla signos, índice de arista y coordenadas.

El ajuste ex post `α=⟨e,p⟩/⟨p,p⟩` es aproximadamente `8.5018`, `8.5373`, `8.5443`, **no** una normalización validada: el covector sin ajustar mantiene 88.3 % de su norma de diferencia. No reclamar que el `cos² ≈ 99.75 %` constituya atribución causal cuantitativa.

### El 84.16 % del complemento afín

**Fe de erratas editorial: distinguir vectores de Riesz y covectores.** El informe de origen describía `B(BᵀGB)⁻¹Bᵀ` como proyector actuando sobre representaciones de Riesz. Esa descripción confunde dos convenciones y se corrige aquí expresamente.

Sea `G∈R^{n×n}` simétrica definida positiva y `B∈R^{n×60}` de rango columna completo, cuyas columnas son las direcciones afines. Para un covector `e∈R^n`, su representante de Riesz es `r=G⁻¹e`. Entonces:

- El proyector G-ortogonal que actúa sobre vectores de Riesz es `P_G=B(BᵀGB)⁻¹BᵀG`, de modo que `P_G r` es el vector proyectado.
- El mapa de covectores a vectores proyectados es `e↦B(BᵀGB)⁻¹Bᵀe=P_G G⁻¹e`. Esta es la fórmula escrita en la fuente, pero no actúa como proyector vectorial sobre r.
- El proyector correspondiente que actúa sobre covectores es `P_*=G B(BᵀGB)⁻¹Bᵀ`; el covector proyectado es `P_*e=G P_G r`.

La hipótesis de rango completo garantiza la inversa de `BᵀGB`; si hay dependencias entre columnas debe usarse una base independiente o la pseudoinversa y el subespacio efectivamente generado. Todas estas matrices son n×n, pero sus dominios y el uso de la identificación de Riesz importan: la igualdad de dimensiones no vuelve intercambiables las tres operaciones.

**Límite de esta corrección:** al no distribuirse ni revisarse aquí los arrays y scripts del ensayo, no se determina qué convención implementó el cálculo original ni se afirma un error de código. La corrección notacional no valida ni recalcula el porcentaje afín. Se conserva el **84.1589 % del error cuadrático en N=4 como cifra reportada, no verificada independientemente**. Las siguientes cifras del complemento afín también son documentales:

- Coseno dual: `0.99874570`.
- Relación de magnitudes: `0.11688346`.
- Error al restarlo sin ajuste: `0.88328253` de la norma original del complemento.

Según las cifras reportadas, la predicción **reproduce aproximadamente la dirección del defecto en ese complemento**, pero no explica su amplitud; esta lectura queda sujeta a verificar el expediente computacional y la convención de proyección. **`ATRIBUCIÓN CUANTITATIVA FALLIDA`** se conserva.

## 3. Controles independientes de la derivación

**Cartan cuadrático:** para `A0=−(f/2)x² T` y `F01=fxT`, el predictor p^(1) reproduce el covector de error completo de Maxwell en N=1,2,3,4, con discrepancia dual relativa máxima `7.63e−15`. El mismo ensayo satisface las identidades exactas del control previo de interpolación:

\[
\|F-I_h^2F\|_{L^2,+}^2=\frac{5f^2}{63N^2},\qquad
S_h-S=\frac{5f^2}{126N^2}.
\]

**Diferencial del funcional auxiliar:** se comparó la fórmula analítica usada en p^(2) con derivadas finitas directas de `1/2||I_hF(A+c W_e)||²` sobre seis 4-símplices independientes, en resoluciones N=1,2,4. La mayor discrepancia relativa fue menor que `3e−13`. Esto verifica la implementación de p^(2), no su equivalencia con la acción logarítmica de Christiansen–Halvorsen (ecuación 37).

**Control negativo:** sustituir los flujos aditivos por logaritmos de lazos **sin transportar todas las caras a fibras compatibles** generó predictores con cosenos negativos (~−0.45); usar un transporte arbitrario a la raíz de cada símplice dio cosenos de solo ~0.11–0.19. Se conservaron como pruebas negativas, **no** como rechazo del transporte correcto de la acción logarítmica de Christiansen–Halvorsen (ecuación 37): las dos reconstrucciones de prueba son distintas de su regla variacional basada en pares.

## 4. Qué explica la diferencia: desarrollo cúbico de la acción logarítmica de Christiansen–Halvorsen (ecuación 37)

Para un factor de amplitud `s`, fijamos `A_s=s A_0`, donde `A_0` es el campo no abeliano afín de referencia, perteneciente exactamente al espacio Whitney1. Sus enlaces tienen holonomías `U_e(s)=exp(sB_e)` y su curvatura continua se expande:

\[
F(A_s)=s\,dA_0+s^2[A_0\wedge A_0],
\]

con `dA_0` constante y exactamente interpolable. Por tanto,

\[
I_h^2F(A_s)-F(A_s)
=s^2\bigl(I_h^2[A_0\wedge A_0]-[A_0\wedge A_0]\bigr).
\]

Al desarrollar cada lazo triangular `exp(sa) exp(sb) exp(−sc)`:

\[
\log(U_{ij}U_{jk}U_{ik}^{-1})
=s(a+b-c)+s^2\bigl(a\times b-(a+b)\times c\bigr)+O(s^3),
\]

la acción logarítmica de Christiansen–Halvorsen (ecuación 37) tiene un término cúbico `S_3` que incluye **dos fuentes**: (i) la corrección BCH de las caras y (ii) la primera adjunción del transporte `Ad_U`. Su derivada se computó directamente respecto de **cada coeficiente de enlace** diferenciando el polinomio cúbico exacto mediante *complex-step*, no ajustando una serie de errores numéricos.

La relación medida entre el predictor aditivo y el coeficiente `s²` exacto del residual es:

| N | Norma del predictor / norma del coeficiente cúbico real | Coseno | `α` de mejor ajuste, diagnóstico |
|---:|---:|---:|---:|
| 2 | 0.332807 | 0.999904 | 3.004453 |
| 3 | 0.332982 | 0.999955 | 3.003026 |
| 4 | 0.333071 | 0.999974 | 3.002282 |

La diferencia entre la contribución BCH menos continuo y la contribución del transporte tiene cosenos `−0.7602`, `−0.7677`, `−0.7749`. **Son dos efectos grandes que se cancelan parcialmente.** No tiene sentido adjudicar el multiplicador faltante solamente a uno dellos.

En una prueba independiente por barrido de amplitud, para N=2 el factor de mejor ajuste varió de `3.02614` a escala `1/256`, a `3.09118` a escala `1/64`, `5.77216` a escala `1/2` y `8.50182` a escala original `1`. La comparación de diferencias finitas a pasos `5e−5`, `1e−4` y `2e−4` fue estable a precisión numérica. **El factor no es constante en amplitud y no debe adoptarse como coeficiente de renormalización.**

### La acción global oculta derivadas libres mediante cancelaciones de frontera

La expansión del error del **valor de la acción** sobre la línea `A_s` posee un coeficiente cúbico diminuto que decrece como `N^(−2)`:

`S_{3,CH}−S_{3,cont} ≈ −5.444312279e−9 / N²`, verificado en N=1,2,3,4 mediante BCH local, sin ajuste de valores a amplitud finita.

Aun así, el gradiente restringido a enlaces libres es grande a orden `s²`. La diferencia no es contradictoria: variar el parámetro global `s` cambia también los **enlaces de frontera**, que Dirichlet mantiene fijos al evaluar el residual libre. En N=2, s=1/64, se derivaron las 544 variables de enlace:

| Contribución a la derivada del error de acción global | Valor |
|---|---:|
| Enlaces libres, 80 | −4.456390620e−9 |
| Enlaces de frontera, 464 | +4.460534963e−9 |
| Suma | +4.144343314e−12 |

Esta cancelación explica por qué el ensayo del valor de la acción sobre una familia global no certifica su gradiente con Dirichlet. No se debe inferir del valor pequeño de `S_h(A_s)−S(A_s)` que sus derivadas en todas las direcciones sean pequeñas.

## 5. Significado científico y límites

1. **PASS**: el predictor aditivo de curvatura Whitney de primer orden tiene la dirección correcta del residual de la acción logarítmica de Christiansen–Halvorsen (ecuación 37) en este campo, con coseno creciente hasta 0.998746.
2. **FAILED**: su magnitud alcanza solo aproximadamente 11.7 % del residual completo, incluida la parte del complemento afín responsable del 84.16 % en N=4.
3. **PASS**: un Maxwell Cartan cuadrático reproduce exactamente el covector, y seis derivadas de la acción auxiliar interpolada pasan pruebas independientes.
4. **PASS**: los coeficientes cúbicos BCH/transportes explican **por qué** el primer término no abeliano del residual es distinto del predictor puramente aditivo; en acoplamiento débil la relación de magnitudes tiende a alrededor de un tercio.
5. **PASS limitado**: el test de derivada sobre la familia global muestra cancelaciones internas-borde; tampoco puede usarse para extrapolar una conclusión sobre el residual Dirichlet.
6. **OPEN**: convertir esta disección perturbativa y de gauge fijo en un **predictor gauge-covariante** para el residual de la acción logarítmica de Christiansen–Halvorsen (ecuación 37) a amplitud finita y demostrar una cota uniforme en h.
7. **OPEN**: evaluar una formulación alternativa de orden superior o recuperación de curvatura con el **mismo** benchmark y la **misma** norma. Es prematuro afirmar que un cambio de espacio Whitney solucionará el defecto logarítmico del funcional.
8. **OPEN**: evolución de Dirac, restricciones temporales y gravitacionales, raíz Einstein–Yang–Mills no abeliana, estabilidad lorentziana física.

No se reivindica como novedad la interpolación Whitney, FEEC, la expansión BCH ni el transporte de caras. El resultado distintivo y auditable del proyecto es **la prueba cuantitativa y la identificación de qué parte del predictor falla dentro de este complejo simplicial de referencia lorentziano**.

## 6. Referencias y reproducibilidad de esta edición

- Arnold, Falk y Winther, *Finite element exterior calculus, homological techniques, and applications*, Acta Numerica 15 (2006). https://doi.org/10.1017/S0962492906210018
- Christiansen y Halvorsen, *A simplicial gauge theory*, J. Math. Phys. 53 (2012). https://doi.org/10.1063/1.3692167

Las referencias identifican métodos existentes; no se redistribuyen sus textos. Esta edición no reivindica novedad de Whitney, BCH ni transporte. La evidencia numérica aquí es documental: no incluye un certificado de reproducción del cálculo completo. El verificador auxiliar `verify_reported_ratios.py` solo comprueba aritméticamente la consistencia de las cifras redondeadas de la tabla; no genera residual alguno.

© 2026 Xorch — Concordante Lab. Derechos reservados.
