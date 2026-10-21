# Auditoría de acoplamientos por dos bloques

Concordante Lab · © 2026. Todos los derechos reservados.

Auditoría histórica del 16 de octubre de 2026, edición pública del 21 de octubre de 2026.

## 1. Enunciado normalizado y veredicto

**Veredicto primario: demostrado tal como está escrito en el contrato normalizado que sigue.** La clasificación finita, su recíproca y la restricción por extensión proyectiva a todas las dimensiones son correctas. La irreducibilidad requiere la precisión de frontera indicada en §5; el informe final auditado ya la incluye. No se deriva una ley física ni una elección de acoplamiento.

La revisión matemática original del 16 de octubre de 2026 cubrió las afirmaciones de las secciones 2–5 del informe. Esta edición conserva sus argumentos y elimina identificadores privados; la correspondencia y los hashes originales se mantienen privadamente. No se contabiliza repetir un programa como otra demostración independiente. Los hashes adjuntos corresponden a los derivados actuales.

Para enteros **n,m≥1**, sean U=F₂ⁿ, W=F₂ᵐ, M=2ⁿ, N=2ᵐ. Se fija la descomposición ordenada U⊕W. Sobre funciones reales del producto, se considera un generador Markov conservativo de tiempo continuo y convolución:

L f(x,y)=Σ_(u,v)≠(0,0) q(u,v)[f(x+u,y+v)−f(x,y)], con q(u,v)≥0.

La invariancia significa igualdad individual bajo GL(U)×GL(W), no mera identificación de órbitas por gauge. A y B son los promedios uniformes **incluido cero** sobre U y W. Se prescriben las marginales c(A−I) y d(B−I), con c,d≥0, mediante la acción sobre funciones de cada bloque por separado.

Entonces existe un único θ y

L=(c−θ)(A⊗I−I)+(d−θ)(I⊗B−I)+θ(A⊗B−I),

si y solo si

0≤θ≤min{cN/(N−1), dM/(M−1)}.

Para una familia L_(n,m) definida para **todos** n,m≥1, el contrato de cocientes separados exactos es, para cada par de sobreyecciones lineales π:U→U′ y ρ:W→W′ con ambos destinos no triviales,

L_(n,m)(f∘(π⊕ρ))=(L_(n′,m′) f)∘(π⊕ρ).

La igualdad usa un reloj común, sin reescalamiento. Bajo este contrato, θ es una misma constante en todas las dimensiones y la familia es Markov si y solo si 0≤θ≤min(c,d). La misma compatibilidad también fuerza c,d comunes si inicialmente se permiten índices dimensionales.

**Hipótesis que no deben omitirse:** convolución, invariancia del representante, bloques ya suministrados, promedios normalizados, dimensiones positivas y una familia realmente compatible. Pedir que cada dimensión tenga alguna dinámica, sin compatibilidad entre ellas, no fuerza θ común. Cocientes que mezclan bloques constituyen otro contrato.

## 2. Grafo de dependencias

1. Definición de generador convolucional + invariancia del representante → tasas constantes en tres órbitas no nulas. **Prueba interna.**
2. Tres órbitas + marginales exactas → dos ecuaciones lineales y un parámetro único. **Prueba interna.**
3. No negatividad de las tres tasas → intervalo finito necesario y suficiente. **Prueba interna.**
4. Fibra uniforme de una sobreyección lineal + unicidad paramétrica → conservación de c,d,θ en cada cociente separado. **Prueba interna.**
5. Proyección de cada par de dimensiones a (1,1) → un único triple global. **Prueba interna.**
6. Positividad en dimensiones sin cota → θ≤c y θ≤d; fórmula de reinicios con coeficientes no negativos → suficiencia global. **Prueba interna.**
7. Base de caracteres de F₂ⁿ⊕F₂ᵐ → espectro; identidad de energía del grafo → irreducibilidad. **Pruebas internas explicitadas abajo.**

No hay dependencia de un teorema externo, de un supuesto físico, de un resultado computacional ni de la conclusión que se está auditando. El cálculo finito es corroboración, no un paso de la demostración universal.

## 3. Prueba independiente de la clasificación finita

Los desplazamientos no cero se dividen exactamente en

- (u≠0,0), de tamaño M−1;
- (0,v≠0), de tamaño N−1;
- (u≠0,v≠0), de tamaño (M−1)(N−1).

GL(U) es transitivo sobre U\{0}, también cuando n=1; lo mismo vale para W. El producto de los dos grupos actúa transitivamente en cada clase. Denotemos las tres tasas **por desplazamiento** por α,β,γ≥0.

Para un desplazamiento marginal u≠0, todos los v contribuyen a la tasa del primer bloque. Para uno v≠0, contribuyen todos los u. Por tanto,

α+(N−1)γ=c/M,  β+(M−1)γ=d/N.

Definiendo θ=MNγ, se obtiene necesariamente

α=[cN−θ(N−1)]/(MN),
β=[dM−θ(M−1)]/(MN),
γ=θ/(MN).

Esto prueba unicidad. Comparar las entradas fuera de diagonal de la fórmula propuesta reproduce exactamente estas tres tasas; las diagonales coinciden porque ambos operadores anulan constantes. Finalmente, α,β,γ≥0 equivale exactamente al intervalo declarado. También prueba suficiencia: esas tasas definen el generador requerido.

**Precisión importante:** en dimensión finita puede ocurrir c−θ<0 o d−θ<0. Eso no invalida al operador total cuando sus tasas α,β,γ son no negativas. Solo invalida interpretar en ese caso los tres sumandos escritos como tres mecanismos Markov separados con intensidades no negativas.

## 4. Coherencia de θ y límite de extensión

Sea π:U→U′ sobreyectiva. Todas sus fibras tienen tamaño M/M′. Así, el promedio sobre U de una función que proviene de U′ coincide con el promedio uniforme sobre U′. Análogamente para W. Por ello la proyección de la fórmula de L conserva exactamente c,d,θ.

En el destino con M′,N′≥2, el parámetro θ vuelve a ser único por la tasa de desplazamiento mixto. La igualdad con L_(n′,m′) obliga, por tanto, a que los parámetros coincidan. Todas las dimensiones tienen cocientes separados a (1,1), por lo que hay un solo θ global.

Para cada N=2ᵐ, la positividad obliga θ≤cN/(N−1). Al hacer m→∞, el extremo derecho decrece a c. Al variar n de la misma forma resulta θ≤d. No hace falta un paso probabilístico al límite: si θ>c, alguna dimensión finita ya viola la desigualdad.

Recíprocamente, con 0≤θ≤min(c,d), los coeficientes c−θ,d−θ,θ son no negativos. Cada sumando es un generador de reinicio uniforme y su suma es Markov en todas las dimensiones. El argumento de fibras prueba la compatibilidad para **toda** sobreyección separada.

Un rectángulo truncado 1≤n≤n₀, 1≤m≤m₀ admite exactamente el intervalo correspondiente a M₀=2ⁿ⁰,N₀=2ᵐ⁰. Todos sus cocientes descendentes son compatibles. Ningún conjunto finito de niveles sustituye la hipótesis de extensibilidad sin cota dimensional.

## 5. Espectro e irreducibilidad, incluidos los bordes

A⊗I e I⊗B son proyectores que conmutan. Sus cuatro espacios simultáneos son: constantes; funciones de media cero del primer bloque y constantes en el segundo; el caso simétrico; y el producto de los dos espacios de media cero. Sobre ellos, L tiene respectivamente:

- 0, multiplicidad 1;
- −c, multiplicidad M−1;
- −d, multiplicidad N−1;
- −(c+d−θ), multiplicidad (M−1)(N−1).

También se obtiene directamente evaluando L en todos los caracteres χ_(p,r)(x,y)=(−1)^(p·x+r·y). Estas MN funciones constituyen una base ortogonal: el producto de dos caracteres distintos suma cero, ya que trasladar por un punto donde difieren invierte el signo de la suma.

En característica dos cada desplazamiento es su propio inverso. El grafo ponderado es simétrico y

−⟨f,Lf⟩=(1/2)Σ_z Σ_h q(h)[f(z+h)−f(z)]²,

con producto escalar de conteo. El núcleo consta de las funciones constantes en cada componente conexa. En consecuencia, irreducibilidad equivale a que el cero tenga multiplicidad uno, es decir,

**c>0, d>0 y θ<c+d.**

Dentro del intervalo finito admisible y con c,d>0, θ≤2c y θ≤2d, luego θ≤c+d. Si θ=c+d, las dos desigualdades obligan c=d y θ=2c. A su vez, θ≤cN/(N−1) y θ≤dM/(M−1) obligan M=N=2. La única excepción positiva es, por tanto,

**n=m=1, c=d>0, θ=2c.**

Solo permanece el desplazamiento (1,1), con tasa c/2; hay dos clases cerradas, {(0,0),(1,1)} y {(0,1),(1,0)}. Un estado estacionario uniforme existe, pero no es único.

Si c=0 o d=0, el intervalo fuerza θ=0 y el bloque correspondiente queda congelado; la cadena producto es reducible. Si ambos son cero, L=0.

En una familia globalmente coherente, θ≤min(c,d)<c+d cuando c,d>0, por lo que todos los niveles son irreducibles. Su brecha espectral es min(c,d), independiente de θ. La variación de θ se observa en el sector mixto; la brecha por sí sola no selecciona el acoplamiento.

Que α=β=0 no implica siempre desconexión: para M=N=4,c=d=1,θ=4/3, solo hay desplazamientos mixtos con tasa 1/12 y el grafo sigue conectado. La excepción binaria anterior no debe generalizarse.

## 6. Contraejemplo finito de exceso

En n=m=1, c=d=1, tomar θ=3/2. Entonces

q(1,0)=1/8, q(0,1)=1/8, q(1,1)=3/8.

Todas las tasas son positivas. Las dos marginales tienen tasa de salto 1/2, exactamente la de A−I y B−I. El espectro es 0,−1,−1,−1/2, por lo que la cadena es irreducible. Sin embargo θ>min(c,d)=1.

No es extendible con los mismos parámetros ni siquiera al siguiente tamaño en un solo bloque: en (n,m)=(1,2), la tasa de (u≠0,0) tendría que ser

[4−(3/2)·3]/8=−1/16.

Extender ambos bloques a (2,2) da las tasas de eje −1/32. Ambas contradicciones son válidas; la primera requiere menos aumento de dimensión. Este contraejemplo refuta la cota global aplicada indebidamente a un solo producto finito, sin recurrir a un ejemplo desconectado.

## 7. Matriz de obligaciones

| Obligación | Estado | Evidencia |
|---|---|---|
| Tipado de operador, reloj, bloques y promedios | PASSED con las hipótesis de §1 | Convenciones explícitas |
| Necesidad y suficiencia finita | PASSED | Tres órbitas y dos ecuaciones |
| Unicidad y coherencia dimensional de θ | PASSED | Fibras uniformes y proyección a (1,1) |
| Intervalo global necesario y suficiente | PASSED | Ínfimo de cotas y reinicios positivos |
| Bordes c=0, d=0, θ=0, θ máximo | PASSED | Espectro y soporte |
| Irreducibilidad con marginales positivas | PASSED tras incluir la excepción finita | §5 |
| Contraejemplo irreducible de exceso finito | PASSED | θ=3/2 y tasa negativa en extensión |
| Bloques de dimensión cero | Fuera del enunciado | Con A=I o B=I, θ no es identificable localmente y la fórmula del intervalo divide por cero |
| Cocientes que mezclan bloques | Fuera del contrato | No se deducen de compatibilidad separada |
| Selección de un θ físico desde un principio físico subyacente | No abordada; sigue abierta | Ninguna hipótesis aquí la aporta |
| Coherencia asociativa para tres o más bloques | No abordada | No forma parte de esta clasificación de dos bloques |

Como control adicional, exigir invariancia bajo todo GL(n+m,2), que mezcla bloques, iguala α=β=γ y fuerza **c=d=θ**. Exigir composición independiente fuerza **θ=0**. Con marginales no nulas, ambas condiciones no pueden coexistir. Son axiomas adicionales distintos.

También se comprobaron las afirmaciones adicionales del informe: la identidad bilineal de composición resulta al expandir `c(A−I)⊗I+cI⊗(B−I)+c(A−I)⊗(B−I)=c(A⊗B−I)`; el término bilineal aislado tiene tasas negativas en desplazamientos de eje, tal como se advierte. La inversión espectral `θ=c+d−r_UW`, la tasa visible `R_both=θ(1−1/M)(1−1/N)`, la distinción entre orden dt y orden dt² y la distribución estacionaria uniforme compartida son correctas dentro del modelo y con los lectores calibrados declarados. No suministran identificabilidad bajo un canal de ruido desconocido.

## 8. Cálculo independiente, alcance y reproducción

El archivo `audit_block_couplings.py` se escribió y ejecutó antes de revisar el verificador principal. No importa sus funciones ni usa paquetes externos. Genera primero las tasas α,β,γ, reconstruye c,d,θ, evalúa todos los caracteres y obtiene conectividad mediante exploración directa del soporte.

Resultado exacto: **PASS, 7.146.584 aserciones**.

- 576 ternas de tasas: α,β,γ∈{0,1,2,3}, para cada n,m∈{1,2,3}.
- 227 sobreyecciones lineales de un bloque, incluyendo todos los automorfismos, con 1≤dimensión destino≤dimensión fuente≤3.
- Sus 51.529 parejas, verificadas con (c,d,θ)=(2,3,0),(2,3,1),(2,3,2): 154.587 casos de cociente.
- 7.127.505 comparaciones exactas de tasas proyectadas, más las pruebas espectrales, marginales y de frontera.
- Aritmética entera y `fractions.Fraction`; ninguna tolerancia ni reconstrucción numérica.

Reproducción desde la carpeta del expediente:

```
python3 independent_audit/audit_block_couplings.py
```

El certificado `audit_certificate.json` contiene el rango, el número de aserciones, el testigo y SHA-256 del programa. La rejilla no prueba la clasificación universal; esa función corresponde a §§3–5.

## 9. Brecha restante y afirmación segura

**No queda una brecha matemática en la clasificación normalizada de dos bloques.** La versión de `REPORT.md` fijada arriba conserva todas las hipótesis y la excepción de irreducibilidad. Los bloques n=0 o m=0 pueden añadirse mediante una convención degenerada, pero no conservan la parametrización única local ni la fórmula de cotas tal como está escrita.

La afirmación segura más fuerte es que simetría por bloques, marginales de Haar y cocientes separados exactos clasifican una familia continua de acoplamientos, θ∈[0,min(c,d)]. Si c,d>0, estas condiciones **no seleccionan un θ único**, incluso imponiendo irreducibilidad en todas las dimensiones. No establecen la procedencia del factor, del reloj o de la dinámica Markov, ni una fundamentación física de la dinámica.

Los controles de cotejo y repetición sobre la revisión fijada ya están completados. Si cambia el contenido matemático, habrá que revisar de nuevo las afirmaciones afectadas. Esta auditoría es local y no realizó escrituras remotas, ejecuciones de Actions ni publicación.
