# Auditoría independiente: no unicidad de generadores desde una frontera observable

Fecha: 2026-10-16. Método: álgebra racional exacta y pruebas locales, sin consultas ni modificaciones externas.

## Dictamen

**El contraejemplo es válido.** Dos redes completas ponderadas, conectadas y reversibles pueden tener capacidades conocidas idénticas, respuesta dinámica de frontera idéntica para todo parámetro de Laplace no negativo, todos los núcleos de transición vistos en esa frontera idénticos y realizaciones interiores completamente observables, sin ser la misma red ni ser isomorfas por ninguna permutación.

El testigo principal de esta auditoría fortalece el original: **las cinco capacidades son distintas y conocidas**, y también coincide la actividad media estacionaria de saltos. El testigo original con capacidades unitarias se conserva como segundo ejemplo.

Dos precisiones son indispensables en el testigo de capacidades distintas:

1. El generador del modelo de difusión/saltos es **Q = −M⁻¹L**. Coinciden los bloques de exp(tQ) y el espectro generalizado de (L,M), no los de exp(−tL) ni necesariamente el espectro ordinario de L.
2. Las razones de tasas son **qᵢⱼ/qⱼᵢ = mⱼ/mᵢ**, idénticas entre las dos redes. Sólo son todas 1 en el ejemplo de capacidades iguales.

La observabilidad completa de un sistema lineal y la identificabilidad de sus parámetros físicos son propiedades distintas. Aquí no hay un modo interior invisible: hay realizaciones físicas distintas de una misma respuesta de frontera.

## 1. Convenciones y alcance experimental

Los vértices están etiquetados 0,1,2,3,4; la frontera inicial es B={0,1}; el interior es I={2,3,4}. Las capacidades forman una matriz diagonal positiva M. La matriz L es el laplaciano de conductancias: Lᵢⱼ=−wᵢⱼ para i≠j y Lᵢᵢ=Σⱼ≠ᵢwᵢⱼ.

La ecuación de difusión es M u̇=−Lu. Q=−M⁻¹L es un generador de Markov por filas; P(t)=exp(tQ) es su matriz de transición. La distribución estacionaria es πᵢ=mᵢ/Σⱼmⱼ.

La respuesta aquí considerada es

Λ(s)=L_BB−L_BI(L_II+sM_I)⁻¹L_IB,   s≥0.

Esto corresponde a eliminar el interior con condición inicial interior nula en Laplace. Si se contabiliza además la acumulación en las propias capacidades de frontera, la respuesta total es sM_B+Λ(s); también coincide porque M_B es la misma.

Los experimentos permitidos actúan y observan en B. No se presupone que se puedan preparar estados localizados en un vértice interior etiquetado, medir su ocupación o distinguir el destino interior de cada salto de salida de B. Esas intervenciones aportan datos adicionales y pueden romper la equivalencia.

## 2. Mecanismo general y demostración

Sea S invertible en el interior y supongamos

S1=1,    SᵀM_I S=M_I.

Definamos T=diag(I_B,S) y L₂=TᵀLT. Si todos los elementos fuera de diagonal de L₂ son negativos, L₂ vuelve a ser un laplaciano de conductancias positivas sobre el grafo completo.

- Simetría: L₂ᵀ=L₂.
- Sumas de fila: L₂1=TᵀLT1=TᵀL1=0.
- Positividad semidefinida y nulidad unidimensional se conservan por congruencia. En los ejemplos, la positividad estricta de todas las conductancias certifica directamente la conectividad.
- Capacidad: TᵀMT=M.

Escribiendo C=L_BI y K=L_II, se obtiene

C₂=CS,    K₂=SᵀKS,
K₂+sM_I=Sᵀ(K+sM_I)S.

La inversión de esta última identidad cancela los factores S en el complemento de Schur, de donde **Λ₂(s)=Λ₁(s)**. La igualdad vale donde el resolvente existe; en particular para todo s≥0, porque K es definida positiva cuando la red es conectada y B no es vacía.

De la isometría de M se obtiene M⁻¹Tᵀ=T⁻¹M⁻¹, y por tanto

Q₂=−M⁻¹L₂=T⁻¹Q₁T,
exp(tQ₂)=T⁻¹ exp(tQ₁)T.

Como T y T⁻¹ son identidad en los vectores de frontera,

[exp(tQ₂)]_BB=[exp(tQ₁)]_BB   para todo t≥0.

Asimismo, el espectro de Q y el de M⁻¹L se conservan. No es necesario inferir esta igualdad a partir de una muestra de tiempos: es una identidad matricial exacta.

Para observabilidad, la matriz dinámica interior correcta es A=M_I⁻¹K. Satisface A₂=S⁻¹A₁S. La matriz apilada

O = [C; CA; CA²]

obedece O₂=O₁S y conserva el rango. En ambos testigos ese rango es 3. La entrada colocada en la frontera tiene matriz M_I⁻¹Cᵀ; también se verifica controlabilidad de rango 3. Por ello las realizaciones interiores son mínimas.

### Actividad media: condición adicional, no consecuencia automática

Definiendo actividad como número medio de saltos por unidad de tiempo bajo la distribución estacionaria,

𝒜=ΣᵢπᵢΣⱼ≠ᵢqᵢⱼ=tr(L)/(Σᵢmᵢ).

Una isometría de M conserva tr(M⁻¹L), pero **no conserva generalmente tr(L)**. La coincidencia de actividad necesita una comprobación adicional cuando las capacidades no son iguales. El testigo principal está construido para satisfacerla.

## 3. Testigo principal: capacidades distintas y actividad coincidente

Sean m=(1,2,3,4,5)ᵀ, M=diag(1,2,3,4,5) y bᵢⱼ=eᵢ−eⱼ. Definimos

L₀=15M−mmᵀ,
L=L₀+11b₀₂b₀₂ᵀ+13b₀₄b₀₄ᵀ+b₂₄b₂₄ᵀ.

Entonces

L =

    [ 38  −2 −14  −4 −18 ]
    [ −2  26  −6  −8 −10 ]
    [−14  −6  48 −12 −16 ]
    [ −4  −8 −12  44 −20 ]
    [−18 −10 −16 −20  64 ]

Tomamos v=(1,−2,1)ᵀ y M_I=diag(3,4,5). La reflexión ponderada es

S=I−2v(vᵀM_I)/(vᵀM_Iv)

    [ 3/4   2/3  −5/12 ]
    [ 1/2  −1/3   5/6  ]
    [−1/4   2/3   7/12 ]

Cumple S²=I, det(S)=−1, S1=1 y SᵀM_I S=M_I. El laplaciano transformado es

L₂ =

    [ 38  −2     −8    −20     −8   ]
    [ −2  26     −6     −8    −10   ]
    [ −8  −6     44    −26/3  −64/3 ]
    [−20  −8    −26/3  164/3  −18   ]
    [ −8 −10    −64/3  −18    172/3 ]

En orden 01,02,03,04,12,13,14,23,24,34, los pesos son

- L: (2,14,4,18,6,8,10,12,16,20)
- L₂: (2,8,20,8,6,8,10,26/3,64/3,18)

Todos son positivos. Ambas redes tienen exactamente la topología K₅. Los multiconjuntos de grados difieren: L tiene todos sus grados enteros, mientras que L₂ tiene 164/3 y 172/3. Por tanto, **ninguna permutación**, ni siquiera una que mueva la frontera, transforma L en L₂. El script además comprueba exhaustivamente las 120 permutaciones.

### Datos coincidentes

- Capacidades conocidas: M=diag(1,2,3,4,5)
- Medida estacionaria: π=(1,2,3,4,5)/15
- Reversibilidad: πᵢqᵢⱼ=πⱼqⱼᵢ=wᵢⱼ/15
- Razones de tasas: qᵢⱼ/qⱼᵢ=mⱼ/mᵢ en las dos redes
- Trazas: tr(L)=tr(L₂)=220
- Actividad media estacionaria: 𝒜₁=𝒜₂=44/3
- Espectro generalizado: el polinomio característico común de M⁻¹L es

  x⁵−(454/5)x⁴+(14181/5)x³−37296x²+177120x

- Observabilidad: rango 3; el menor formado por las dos primeras filas C y la primera fila de CA vale 21376/15 para L y −21376/15 para L₂
- Controlabilidad interior: rango 3 en ambos casos
- Respuesta Λ(s) idéntica para todo s≥0
- Núcleo [exp(tQ)]_BB idéntico para todo t≥0

La igualdad de actividad no es accidentalmente deducida del espectro: bajo esta S, el cambio de traza de b₀₂b₀₂ᵀ es 13/72, el de b₀₄b₀₄ᵀ es −11/72 y el de b₂₄b₂₄ᵀ es 0. La elección 11 y 13 cancela exactamente el cambio.

### Transferencia explícita

Sea d(s)=15s³+597s²+7088s+21952. La transferencia común es

Λ(s) = 1/d(s) ·

    [570s³+20674s²+206144s+354240,  −30s³−2274s²−50976s−354240]
    [−30s³−2274s²−50976s−354240,    390s³+14802s²+159232s+354240]

El determinante de L_II+sM_I es 4d(s), estrictamente positivo para s≥0.

### Lo que no coincide

Q₁≠Q₂: la tasa del salto 0→2 es 14 en la primera red y 8 en la segunda.

No se debe reemplazar Q por −L. Se verifica exactamente

(L²−L₂²)_BB = [[8,8],[8,0]].

Así, los segundos derivados en t=0 de los bloques exp(−tL) difieren. Tampoco coincide el espectro ordinario de L. Estas diferencias no afectan la igualdad de la difusión del modelo M u̇=−Lu.

### Control discriminante al añadir el vértice 2 a la frontera

Tomemos B′={0,1,2}, I′={3,4} y s=0. Las matrices de respuesta estática son

Λ₁,B′(0) = (1/151) ·

    [ 4603 −1155 −3448 ]
    [−1155  3195 −2040 ]
    [−3448 −2040  5488 ]

Λ₂,B′(0) = (1/6323) ·

    [ 167842  −53818 −114024 ]
    [ −53818  137362  −83544 ]
    [−114024  −83544  197568 ]

El control concreto es fijar u₀=u₁=0, u₂=1 y dejar equilibrar los vértices 3 y 4. La corriente suministrada por el terminal 2 es

- Primera red: j₂=5488/151
- Segunda red: j₂=197568/6323
- Diferencia: 4867856/954773 ≠ 0

No requiere resolución temporal: una medición estática adicional basta para distinguir este par. No prueba que cualquier frontera de tres vértices determine cualquier red; es un control explícito para estos dos testigos.

## 4. Testigo secundario: capacidades unitarias

M=I₅ y pesos originales (5,6,5,4,4,7,5,5,6,4), en el mismo orden de aristas. En este caso

L =

    [20 −5 −6 −5 −4]
    [−5 21 −4 −7 −5]
    [−6 −4 21 −5 −6]
    [−5 −7 −5 21 −4]
    [−4 −5 −6 −4 19]

S=(1/7)·[[6,−2,3],[−2,3,6],[3,6,−2]].

S es ortogonal, fija 1 y tiene determinante −1. La transformación produce pesos

(5,38/7,27/7,40/7,25/7,43/7,44/7,314/49,208/49,213/49).

Los grados son (20,21,963/49,1017/49,1009/49), diferentes de los grados originales (20,21,21,21,19), por lo que no hay isomorfismo por permutación. Los menores de observabilidad correspondientes valen 617 y −617.

Aquí Q=−L, así que la igualdad de los bloques de exp(−tL) sí es correcta. Coincide también el espectro ordinario de L, con polinomio

x⁵−102x⁴+3891x³−65792x²+416065x.

La estacionaria es uniforme, las razones de tasas son 1 y la actividad media es 102/5. La transferencia común es

Λ(s) = 1/(s³+61s²+1162s+6572) ·

    [20s³+1143s²+19380s+83213,  −5s³−384s²−9808s−83213]
    [−5s³−384s²−9808s−83213,    21s³+1191s²+19952s+83213]

Al añadir frontera 2 y fijar (u₀,u₁,u₂)=(0,0,1), la corriente en 2 es 6572/383 frente a 80507/5004. Su diferencia es 2052107/1916532. Por tanto el control adicional también distingue el testigo original.

## 5. Hipótesis y límites que deben constar en un enunciado

1. **Definir el experimento.** La igualdad es para frontera fija B y capacidades M comunes; no incluye instrumentación o preparación arbitraria de estados interiores etiquetados.
2. **Definir la dinámica.** Con masas distintas hay que usar Q=−M⁻¹L, el lápiz L+sM y observabilidad de (M_I⁻¹L_II,L_BI). Usar simplemente L_II cambia el sistema.
3. **Separar igualdad de capacidad y ortogonalidad.** S debe ser M_I-ortogonal, no necesariamente ortogonal en la métrica euclídea. Las masas distintas no eliminan estas transformaciones.
4. **Comprobar los signos y la topología.** Una congruencia arbitraria no preserva los signos de un laplaciano. Aquí se verifican todas las conductancias. En grafos dispersos podría crear aristas prohibidas.
5. **Precisar el espectro.** El espectro dinámico es el de Q o, con signo contrario, el de M⁻¹L. Coincide con el espectro de L sólo si M=I u otra normalización pertinente.
6. **Precisar la actividad.** La actividad de saltos estacionaria es tr(L)/Σm. No es tr(M⁻¹L)/5 salvo casos especiales. Si se usa una convención de actividad con otro factor, debe explicitarse.
7. **Precisar las razones de tasas.** Para M distinto, qᵢⱼ/qⱼᵢ=mⱼ/mᵢ. Reversibilidad no significa que las tasas brutas sean simétricas.
8. **No confundir observabilidad con identificación.** El rango 3 permite reconstruir el estado de cada realización conocida; no selecciona una realización física única entre realizaciones equivalentes por transformación interior.
9. **No confundir transformación algebraica con relabelado físico.** S contiene coeficientes negativos y no es una matriz de permutación ni un canal estocástico. Se exhiben dos redes matemáticamente admisibles distintas que producen los mismos datos de frontera, no equivalencia de todas las intervenciones físicas posibles.
10. **No universalizar la no unicidad.** El contraejemplo refuta una afirmación universal de identificabilidad bajo estos datos. Información espacial, conductancias fijadas, familias paramétricas rígidas, más terminales, tasas locales conocidas o entradas interiores podrían identificar una red.
11. **No inferir gravedad.** Estos cálculos son sobre redes de difusión/Markov. No se especifican una geometría física, una métrica espacio-temporal, un principio de acoplamiento gravitatorio ni ecuaciones de campo. La equivalencia de frontera no identifica un generador Q único y por sí misma no permite extraer una afirmación positiva o negativa sobre gravedad física.

## 6. Reproducción

Archivos entregados en esta carpeta:

- `verify_boundary_gauge.py`: cálculo local reproducible con SymPy, sin red
- `audit_results.json`: matrices, transferencias, invariantes y controles como racionales exactos
- `AUDITORIA_MATEMATICA.md`: este dictamen y demostración

Ejecución:

    python verify_boundary_gauge.py

Se verifican, para cada testigo: capacidades, conservación de 1, simetría, signos positivos, 120 permutaciones, igualdad racional de la transferencia, similitud de Q, estacionaria, reversibilidad, razones de tasas, bloques de potencias Qᵏ para k=0,…,12 como control adicional, polinomio característico, observabilidad y controlabilidad de rango completo, actividad estacionaria y discriminación mediante frontera extra.

Las comprobaciones de potencias son controles del script; la demostración de igualdad de todos los núcleos temporales se apoya en la similitud exacta, no en extrapolar esas trece potencias. Todas las comprobaciones finalizaron correctamente.

### Nota breve de revisión

La primera propuesta con capacidades distintas preservaba transferencia y generador espectral, pero no la actividad media estacionaria. Esa afirmación fue corregida antes del dictamen final. El testigo principal presentado arriba preserva explícitamente también la traza de L y elimina ese defecto.
