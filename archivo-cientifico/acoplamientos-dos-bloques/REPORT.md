# Acoplamientos proyectivos por dos bloques

Concordante Lab · © 2026. Todos los derechos reservados.

Informe original del 16 de octubre de 2026; edición pública del 21 de octubre de 2026.

## Resultado y diferencia respecto del último corte

Un antecedente del proyecto demuestra que la naturalidad bajo todo GL y todos los cocientes lineales, con un reloj exacto común, selecciona `c(A−I)`, y que esta familia no satisface independencia monoidal estricta no nula. Este informe no vuelve a presentar esos resultados como nuevos.

La aportación posterior es una clasificación exacta al **marcar una factorización en dos bloques** y conservar sólo `GL(n,2)×GL(m,2)`: las marginales fijadas admiten una familia de acoplamientos con parámetro `θ`. En dimensiones finitas el intervalo admisible es mayor que el intervalo de familias extensibles coherentemente a todas las dimensiones. La extensión universal elimina precisamente los valores que requieren tasas negativas de reinicio independiente. Se da un contraejemplo irreducible mínimo y un lector espectral de `θ`.

**Estado:** pruebas algebraicas completas bajo el contrato declarado; comprobación exacta acotada adjunta; revisión independiente concluida y adjunta. La prioridad matemática externa, la fundamentación física y la selección de la factorización quedan pendientes de investigaciones específicas.

## 1. Contrato y fuentes fijadas

Sean `n,m≥1`, `U=F₂^n`, `W=F₂^m`, `M=2^n`, `N=2^m`. Se fija la suma y la descomposición `V=U⊕W`. Sea `A` el promedio uniforme en U y `B` el promedio uniforme en W. `I` denota la identidad del espacio apropiado. Se buscan generadores reales de convolución

`L f(x,y)=Σ_(u,v)≠(0,0) q(u,v)[f(x+u,y+v)−f(x,y)]`, `q(u,v)≥0`,

con estas hipótesis:

1. **Naturalidad por bloques:** invariancia de q bajo `GL(n,2)×GL(m,2)`. No se permite mezclar los bloques en este requisito.
2. **Marginales exactas:** sobre funciones de x solamente, `L=c(A−I)`; sobre funciones de y solamente, `L=d(B−I)`, con `c,d≥0` fijados. Son intensidades de reinicio, no tasas de cambios visibles.
3. Para el teorema universal se exige una familia `L_(n,m)` para **todos** `n,m≥1`, con los mismos c,d y **consistencia exacta bajo cocientes separados**: para cualquier par de aplicaciones lineales sobreyectivas `π:U_n→U_r`, `ρ:W_m→W_s`, con `r,s≥1`,

   `L_(n,m)(f∘(π,ρ)) = (L_(r,s)f)∘(π,ρ)`.

   Incluye una sobreyección junto a la identidad del otro bloque. Se conserva un único reloj, sin reescalamiento dependiente de dimensión o cociente. Las marginales hacia un solo bloque están impuestas explícitamente en 2; no se ocultan como cocientes a dimensión cero.

Los bordes c=0 o d=0 están admitidos para la clasificación. La irreducibilidad se trata aparte. La dimensión cero queda excluida: allí los operadores degeneran y θ deja de ser identificable.

La prueba que sigue es autocontenida. Los antecedentes históricos del proyecto se conservan en el registro privado; no son dependencias ejecutables ni premisas ocultas de los teoremas. La revisión de prioridad y de literatura queda pendiente.

## 2. T1: cono de acoplamientos a tamaño finito

**Teorema.** Bajo 1–2, para cada M,N existe un único parámetro θ tal que

`L=(c−θ)(A⊗I−I)+(d−θ)(I⊗B−I)+θ(A⊗B−I)`.

Este operador es un generador Markov si y sólo si

`0≤θ≤min(cN/(N−1), dM/(M−1))`.

En particular, la positividad del generador **no** exige a tamaño finito que los tres coeficientes de esta descomposición sean no negativos.

**Prueba.** La acción por bloques tiene exactamente tres órbitas sobre los desplazamientos no nulos: `(u≠0,0)`, `(0,v≠0)`, `(u≠0,v≠0)`. Sus tasas constantes se denotan α,β,γ, respectivamente. La proyección al primer bloque suma sobre los N posibles v, y la proyección al segundo sobre los M posibles u. Las marginales exigen

`α+(N−1)γ=c/M`, `β+(M−1)γ=d/N`.

Sea `θ=MNγ`. Entonces

`γ=θ/(MN)`, `α=c/M−(N−1)θ/(MN)`, `β=d/N−(M−1)θ/(MN)`.

La no negatividad de estas tres tasas es exactamente el intervalo declarado. La parte fuera de la diagonal del operador enunciado da esas mismas tasas; la diagonal es la negativa de su suma, por lo que los operadores son iguales. Como M,N≥2, existen desplazamientos mixtos y θ es único. Recíprocamente estas tasas construyen el generador y satisfacen ambas marginales. QED.

**Bordes.** Si c=0 o d=0, el intervalo fuerza θ=0; el bloque con intensidad cero queda inmóvil. Si c,d>0, el generador es irreducible excepto el caso `M=N=2`, `c=d`, `θ=2c`.

**Prueba de la excepción.** Si γ=0, α,β>0 y los desplazamientos de cada bloque generan todo V. Si γ>0 y α>0 o β>0, los desplazamientos mixtos y los de ese bloque generan ambos bloques. Si α=β=0, sólo quedan todos los desplazamientos mixtos. Cuando M>2, sumas de dos mixtos con el mismo v generan todos `(u,0)` (cada u no nulo es suma de dos no nulos distintos); de ahí y los mixtos se obtiene W. Simétricamente para N>2. Cuando M=N=2, sólo queda `(1,1)` y hay dos clases cerradas; las ecuaciones marginales dan precisamente c=d y θ=2c. QED.

Esta salvedad impide confundir marginales irreducibles con un proceso conjunto irreducible.

## 3. T2: la extensión proyectiva a todas las dimensiones recorta el cono

**Teorema.** Bajo 1–3, existe un único número `θ∈[0,min(c,d)]`, independiente de n,m, y todas las familias son exactamente

`L_(n,m)=(c−θ)(A_n⊗I−I)+(d−θ)(I⊗A_m−I)+θ(A_n⊗A_m−I)`.

Por tanto, estas familias admiten una construcción con tres relojes de Poisson independientes:

- a tasa c−θ se reinicia uniformemente sólo U;
- a tasa d−θ se reinicia uniformemente sólo W;
- a tasa θ se reinician juntos ambos bloques a una pareja uniforme.

El último evento usa un instante compartido; sus dos nuevos valores son independientes y uniformes. Reiniciar puede dejar un bloque o ambos sin cambio visible.

**Necesidad.** A tamaño n,m, T1 da `θ_(n,m)=MNγ_(n,m)`. Proyectar ambos bloques sobre F₂ lleva cualquier desplazamiento mixto no cero del destino a `(M/2)(N/2)` preimágenes mixtas. La consistencia exacta implica `γ_(1,1)=MNγ_(n,m)/4`, por tanto `θ_(n,m)=4γ_(1,1)=θ`. Alternativamente se pueden componer dos cocientes separados con el otro bloque fijo. No basta que cada dimensión tenga un parámetro independiente.

Por T1, para todos n,m se cumple `θ≤c/(1−2^(-m))` y `θ≤d/(1−2^(-n))`. Haciendo crecer m y n se obtiene `θ≤c` y `θ≤d`. También θ≥0.

**Suficiencia.** Si `0≤θ≤min(c,d)`, los tres coeficientes son no negativos. Cada término es un generador de reinicio uniforme; sus marginales suman c y d. Toda aplicación lineal sobreyectiva manda la medida uniforme a la medida uniforme porque todas sus fibras tienen igual tamaño. Los tres términos respetan por separado cada cociente, con las mismas intensidades. Su suma es por tanto una familia admisible. La unicidad viene de T1. QED.

**Nota de alcance.** El límite anterior es una prueba algebraica universal bajo hipótesis explícitas. El experimento finito adjunto sólo verifica casos acotados y no reemplaza esa prueba. No se ha demostrado que un principio físico subyacente imponga disponer de todos esos tamaños ni de esos cocientes.

## 4. T3: contraejemplo mínimo y frontera truncada

Tómese `M=N=2`, `c=d=1`, `θ=3/2`. Las tasas de los tres desplazamientos son

`q(1,0)=q(0,1)=1/8`, `q(1,1)=3/8`.

Todas son estrictamente positivas. Cada marginal binaria salta a tasa `1/2`, es decir, tiene generador `A_1−I`, y el proceso conjunto es irreducible. Pero el único candidato compatible a `M=N=4` debe conservar θ; T1 fuerza

`α=β=1/4−3(3/2)/16=−1/32`, `γ=3/32`.

No existe tal extensión Markov. Esta obstrucción no procede de desconexión, de una marginal degenerada ni de un cambio de reloj. También aparece ya en una extensión 4×2 o 2×4, porque una de las tasas puras es negativa.

**Corolario truncado exacto.** Si sólo se exige una familia para `1≤n≤a`, `1≤m≤b`, con todos los cocientes separados dentro de ese rectángulo dimensional, el intervalo es

`0≤θ≤min(c/(1−2^(-b)), d/(1−2^(-a)))`.

La necesidad se ve en el nivel máximo y la suficiencia en que esas cotas disminuyen al aumentar cada dimensión. Para c=d=1 y a=b=D, la región finita excede el intervalo universal θ≤1 por

`1/(2^D−1)`.

Así, pasar cualquier número finito de niveles no basta por sí solo para concluir extendibilidad universal. El verificador incluye, para D=1,2,3,4, un θ racional que pasa todos los niveles hasta D y falla en D+1.

## 5. T4: composición, naturalidad total y lectura de interacción

**Composición independiente.** θ=0 da exactamente la suma de Kronecker `c(A−I)⊗I+I⊗d(B−I)`.

**Naturalidad bajo GL(n+m,2) completo.** Dentro de esta clase, equivale a `c=d=θ` (incluida la familia nula). En efecto, GL total es transitivo sobre los desplazamientos no cero y exige `α=β=γ`. Las ecuaciones de T1 dan primero c=θ y d=θ. La recíproca da `L=c(A⊗B−I)`, con todas las tasas no nulas iguales a `c/(MN)`.

**Identidad exacta de composición para Haar**, con c>0 y `L_U=c(A−I)`, `L_W=c(B−I)`:

`L_(U⊕W)=L_U⊗I+I⊗L_W+(1/c)L_U⊗L_W`.

El término bilineal no es por sí solo un generador Markov: tiene signos fuera de la diagonal. No se debe presentarlo como una interacción positiva aislada. La suma completa sí lo es. Esta identidad organiza el defecto de independencia del antecedente de simetría total sin negar su incompatibilidad con independencia estricta.

**Lector espectral calibrado.** El espacio de funciones se divide en cuatro sectores: constantes, media cero en U solamente, media cero en W solamente, y media cero en ambos. Las tasas de relajación son respectivamente

`0`, `c`, `d`, `r_UW=c+d−θ`,

con multiplicidades `1`, `M−1`, `N−1`, `(M−1)(N−1)`. La prueba es aplicar A y B, que valen 1 sobre constantes y 0 sobre media cero, a la fórmula de T1. Así

`θ=c+d−r_UW`.

Con marginales y factorización calibradas, el modo conjunto discrimina independencia (θ=0), reinicio Haar completo (c=d=θ) y acoplamiento finito no extensible (θ>min(c,d)). Las marginales aisladas no contienen θ. El testigo de §4 tiene `r_UW=1/2`, frente a 1 para Haar total y 2 para independencia con c=d=1.

**Consecuencia para el selector de brecha.** En toda familia universal con c,d>0,

`max(c,d)≤r_UW≤c+d`, y por tanto `gap(L)=min(c,d)` para **todos** los θ admisibles.

La prueba sustituye `0≤θ≤min(c,d)` en `r_UW=c+d−θ` y toma el mínimo de las tres tasas no nulas. Así, con las marginales fijadas, maximizar la brecha no distingue ningún acoplamiento de esta familia, aunque el sector conjunto sí los distinga. Esta degeneración del objetivo es distinta del problema de optimizar las tasas marginales estudiado en un antecedente del proyecto. La desigualdad `r_UW<max(c,d)` refuta la extendibilidad universal bajo este contrato, sin refutar el modelo finito.

**Lector de trayectorias.** La tasa instantánea de saltos visibles simultáneos de los dos bloques es

`R_both=(M−1)(N−1)γ=θ(1−1/M)(1−1/N)`.

Para θ=0, la probabilidad de ver cambiar ambos en una ventana infinitesimal es O(dt²); para θ>0 tiene término lineal `R_both dt`. Este dato requiere resolver eventos y calibrar los bloques, no se obtiene de una sola muestra estacionaria. De hecho, la distribución uniforme producto es estacionaria para toda la familia, por simetría de cada desplazamiento en característica dos. Una foto estacionaria no identifica θ.

Los lectores anteriores son afirmaciones del modelo limpio. Canales de ruido desconocidos o agregación temporal no calibrada pueden destruir la identificabilidad. No se atribuye validez experimental a una tasa inferida sin ese contrato.

## 6. Controles, reproducibilidad y límites

`python3 verify_coupling.py` usa sólo enteros y `fractions.Fraction`:

- verifica todas las tasas y todos los caracteres Fourier para `1≤n,m≤4` y siete ternas de intensidades explícitas, incluidos casos degenerados;
- construye por separado el operador desde los tres reinicios y comprueba la identidad con las tasas por órbitas;
- enumera exhaustivamente las 3, 7 y 42 sobreyecciones lineales `F₂²→F₂`, `F₂³→F₂`, `F₂³→F₂²`, y verifica cada cociente por separado con el otro bloque de dimensión 1, 2 o 3;
- comprueba el intervalo de positividad sobre una rejilla racional que cruza cada extremo, el contraejemplo irreducible y la excepción desconectada;
- verifica los testigos que fallan en el primer nivel posterior y el selector de GL(2,2).

El certificado da el número de aserciones realmente ejecutadas. Un `PASS` sólo cubre ese contrato computacional. El script es autocontenido y no importa código de antecedentes. No se usa red, GitHub Actions, paquetes de pago ni instalaciones. Una revisión independiente de la prueba y controles se documenta aparte, sin atribuirle independencia a una mera segunda ejecución.

**Limitaciones:** no se ha elegido una factorización desde el grupo desnudo, no se ha eliminado la libertad θ bajo naturalidad sólo por bloques, no se ha derivado la categoría de cocientes desde un principio físico subyacente y no se ha justificado un reloj físico. El contenido no prueba gravedad, espacio-tiempo, firma Lorentz ni teoría global de Concordante Lab. La base más rica y el principio físico siguen abiertos.

**Siguiente paso discriminante:** estudiar qué subfamilia de cocientes admite realmente el modelo enriquecido. Si sólo hay tamaños finitos, conservar la cota truncada; si hay una familia coherente no acotada, el teorema T2 elimina los acoplamientos finitos excesivos. Una vez fijados bloque y lectores, contrastar el modo conjunto con las marginales es más informativo que volver a optimizar la brecha sola. No aumentar la rejilla sin una nueva pregunta.

