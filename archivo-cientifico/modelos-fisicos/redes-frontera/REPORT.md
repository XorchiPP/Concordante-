# Observabilidad completa sin identificación de una red reversible

**Concordante Lab · Xorch · 16 de octubre de 2026. Edición pública: 21 de octubre de 2026.**

Resultado de álgebra finita clásica, con prueba y cálculo exactos; no derivación gravitatoria ni reivindicación de prioridad histórica.

## 1. Resultado y diferencia respecto del corte previo

Existen dos redes reversibles completas de cinco vértices, con las mismas
capacidades conocidas y todas distintas, que cumplen simultáneamente:

1. Sus diez conductancias son estrictamente positivas y las redes ponderadas
   no son isomorfas, ni siquiera permitiendo cualquier permutación de vértices.
2. La frontera etiquetada es la misma, `B={0,1}`. El bloque `L_BB` es idéntico.
3. Tienen idéntica transferencia de frontera para **todo** `s≥0`, y el mismo
   núcleo de transición `exp(tQ)` restringido a `B×B` para **todo** `t≥0`.
4. El sistema interior es completamente observable: rango `3/3`. Por tanto
   la equivalencia no procede de un modo interno oscuro.
5. Comparten medida reversible, razones direccionales de tasas en cada arista,
   holonomías de esas razones, escala temporal del lector y actividad media
   estacionaria. Sin embargo, sus generadores no son iguales.

La igualdad del lector dinámico completo **no identifica la realización física
de los vértices internos**, incluso después de eliminar modos oscuros. Conocer
capacidades distintas tampoco basta en ausencia de restricciones adicionales
sobre las conductancias o acceso interno.

Conocer capacidades distintas no identifica por sí solo conductancias desconocidas. Este resultado no se aplica a un experimento que fije de antemano las conexiones individuales entre frontera e interior.

## 2. Contrato exacto del lector

Sea `L` el Laplaciano simétrico positivo de una red conexa con conductancias
positivas y `M=diag(m_0,...,m_4)>0` la matriz conocida de capacidades. La dinámica
de funciones es `f'=Qf`, con `Q=−M⁻¹L`. Los factores `m_i` son capacidades del
modelo, no masas gravitatorias.

Particionar los vértices en frontera `B` e interior `I`. Con frontera prescrita
y estado interior inicialmente nulo, la relación entrada/salida es

`Λ_B(s)=L_BB−L_BI(L_II+sM_I)⁻¹L_IB`.

Si se incluye la capacidad de frontera en la corriente medida, se añade
`sM_B`, idéntico en ambos modelos. El contrato permite cualquier entrada
temporal lineal aplicada en B y todas las frecuencias, pero no prepara ni mide
por separado vértices internos. La topología completa y M sí son conocidas.
Las conductancias internas y las individuales B–I son desconocidas.

No se afirman equivalentes protocolos que observen estados internos,
transiciones individuales, tiempos de residencia de vértices ocultos o
perturbaciones controladas de conductancias. Esa información es más rica.

## 3. Lema de invariancia por isometría de capacidad

**Hipótesis.** Sea `S` invertible en el interior y tal que

`S1_I=1_I`,  `SᵀM_I S=M_I`.

Poner `T=diag(I_B,S)` y `L̃=TᵀLT`. Exigir además que los elementos fuera de la
diagonal de `L̃` sean no positivos y que su soporte sea conexo. Esta condición
de signos no se deduce de ser S una isometría y debe comprobarse.

**Conclusiones.** `L̃` es otro Laplaciano de red; con la misma M,

`Λ̃_B(s)=Λ_B(s)` para todo `s≥0`,

`Q̃=T⁻¹QT`,

`[exp(tQ̃)]_BB=[exp(tQ)]_BB` para todo `t≥0`.

**Prueba.** La congruencia conserva simetría y semidefinitud positiva. Como
`T1=1`, `L̃1=TᵀL1=0`. Los signos y la conectividad dan la interpretación como
Laplaciano de una red conexa con pesos no negativos. Los bloques satisfacen

`L̃_BB=L_BB`, `L̃_BI=L_BI S`, `L̃_II=SᵀL_II S`.

De la isometría resulta

`L̃_II+sM_I=Sᵀ(L_II+sM_I)S`.

Su inversa es `S⁻¹(L_II+sM_I)⁻¹S⁻ᵀ`; al sustituir en el complemento de Schur
se cancelan S y sus inversas. Para `s≥0`, la inversa existe porque el bloque
interior Dirichlet de una red conexa con frontera no vacía es positivo definido.
La identidad `TᵀMT=M` implica `M⁻¹Tᵀ=T⁻¹M⁻¹`, de donde se obtiene la semejanza
de Q. La identidad exponencial sigue de la serie convergente de la exponencial,
y el bloque B queda fijo por T y su inversa. Esto prueba las afirmaciones para
todas las frecuencias y tiempos, sin inferirlas de un muestreo finito. □

**Observabilidad.** Poner `A=M_I⁻¹L_II`, `C=L_BI`. En el modelo transformado
`Ã=S⁻¹AS`, `C̃=CS`. Por tanto la matriz apilada
`O=[C;CA;CA²;...]` se transforma como `Õ=OS`; su rango no cambia. Un modelo
completamente observable puede pertenecer a una clase de realizaciones distintas.
Con los signos convencionales de la dinámica, usar `−A` sólo cambia signos de
bloques de O y no su rango.

**Advertencia sobre la actividad.** La isometría anterior conserva el espectro
de Q, pero no necesariamente la traza ordinaria de L. La actividad estacionaria
de saltos es `Σ_i π_i(−Q_ii)=tr(L)/Σ_i m_i`. Su igualdad será una condición
adicional comprobada en el testigo, no una conclusión general del lema.

## 4. Testigo principal: capacidades todas distintas

Orden de vértices `(0,1,2,3,4)`, frontera `(0,1)`, interior `(2,3,4)` y

`M=diag(1,2,3,4,5)`.

Las matrices son

```text
L =
 [ 38   -2  -14   -4  -18 ]
 [ -2   26   -6   -8  -10 ]
 [-14   -6   48  -12  -16 ]
 [ -4   -8  -12   44  -20 ]
 [-18  -10  -16  -20   64 ]

L̃ =
 [ 38   -2    -8      -20       -8    ]
 [ -2   26    -6       -8      -10    ]
 [ -8   -6    44      -26/3    -64/3  ]
 [-20   -8   -26/3    164/3    -18    ]
 [ -8  -10   -64/3    -18      172/3  ]

S =
 [ 3/4    2/3   -5/12 ]
 [ 1/2   -1/3    5/6  ]
 [-1/4    2/3    7/12 ]
```

Una construcción exacta evita ajustar transferencias después: sea
`m=(1,2,3,4,5)ᵀ` y `b_ij=e_i−e_j`. Tomar

`L=15M−mmᵀ+11b_02b_02ᵀ+13b_04b_04ᵀ+b_24b_24ᵀ`.

El primer término tiene conductancias `m_i m_j`. Con
`v=(1,−2,1)ᵀ`, `M_I=diag(3,4,5)` y `vᵀM_I1=0`,

`S=I−2v(vᵀM_I)/(vᵀM_Iv)`.

Es una reflexión para la forma M_I, fija el vector constante y genera L̃ por
congruencia. El ajuste `11,13` hace que el cambio de traza de los términos
correspondientes se cancele; la actividad común no se deriva gratuitamente.

### Certificados elementales

- Todos los pesos de ambas redes son positivos; el mínimo es `2`.
- `tr(L)=tr(L̃)=220`, así que la actividad estacionaria es `44/3` en ambas.
- La medida estacionaria es `π=(1,2,3,4,5)/15`.
- Para cada enlace, `q_ij/q_ji=m_j/m_i` en ambos modelos. Todos los productos
  de ciclo de estas razones valen `1`.
- Los menores de observabilidad formados por las primeras tres filas de
  `[C;CA;CA²]` valen `21376/15` y `−21376/15`. Ambos rangos son exactamente 3.
- Los multiconjuntos de grados ponderados son distintos:
  `{26,38,44,48,64}` frente a `{26,38,44,164/3,172/3}`. Ninguna permutación de
  vértices transforma L en L̃. El verificador también comprueba las 120
  permutaciones, aunque la diferencia de grados ya basta como prueba.
- La topología sin pesos es K5 en ambos: la no-isomorfía afirmada es de redes
  **ponderadas**, no de grafos no ponderados.

El espectro relevante es el de `Q=−M⁻¹L`, equivalentemente el problema
generalizado `(L,M)`. Con capacidades distintas no se afirma igualdad del
espectro ordinario de L ni de `exp(−tL)`.

## 5. Intervención concreta que rompe la equivalencia

Si el nodo 2 se vuelve accesible como tercera frontera, fijar
`(u_0,u_1,u_2)=(0,0,1)` y dejar 3,4 en equilibrio. La corriente estática en 2 es

`j_2(L)=5488/151`,  `j_2(L̃)=197568/6323`.

La diferencia es exactamente `4867856/954773`, distinta de cero. Es un
discriminador previsto por ambos modelos, fuera del lector B original.

Otra intervención, más exigente, prepara `f(0)=e_2` y mide la derivada inicial
de `f_0(t)`. Se obtiene `Q_02=14` frente a `Q̃_02=8`. No se presume acceso a esa
preparación; queda claramente especificado qué información adicional resolvería
**este par**, sin prometer resolver todas las redes.

## 6. Segundo testigo con capacidades uniformes

El certificado también incluye `M=I5`, pesos
`(5,6,5,4,4,7,5,5,6,4)` en orden `01,02,03,04,12,13,14,23,24,34` y

`S=(1/7)[[6,−2,3],[−2,3,6],[3,6,−2]]`.

Aquí S es ortogonal euclídea, de modo que también se conservan el espectro
ordinario de L y `exp(−tL)` en B. Los menores observables son `617` y `−617`,
y la actividad común es `102/5`. Este ejemplo más simple permite comprobar la
construcción sin confundir isometría euclídea con isometría de capacidad.

## 7. Consecuencia para el acoplamiento común

Dos sondas o especies a las que se asignen Q y Q̃ producen las mismas respuestas
de este lector, con el mismo reloj y las mismas capacidades. Por eso observar
igualdad en B no demuestra que empleen **literalmente la misma Q** sobre los
vértices físicos internos. Sólo restringe su clase de equivalencia observable.

No se afirma que las especies físicas efectivamente obedezcan estos generadores,
ni que posean tasas o vértices identificables de esta manera. Tampoco se deriva
universalidad de caída, fuerza, aceleración, métrica, signatura o gravedad. La
selección de un mecanismo dinámico y su interpretación física siguen abiertas.

La siguiente pregunta útil debe fijar una restricción que no sea invariante
bajo esta semejanza: acceso interno, pesos B–I medidos, una clase topológica
recuperable o una intervención controlada. Añadir más frecuencias del mismo
lector B no rompe este par, porque la equivalencia ya es funcional exacta.

## 8. Antecedentes y alcance

- Blåsten, Isozaki, Lassas y Lu, *Inverse problems for discrete heat equations
  and random walks for a class of graphs*, [arXiv:2107.00494v2, 4-01-2023](https://arxiv.org/pdf/2107.00494v2),
  [DOI 10.1137/21M1439936](https://doi.org/10.1137/21M1439936). Se consultaron
  Definiciones 1.1–1.2 y Teorema 1.3 (p. 6 del PDF), además de la introducción:
  la ausencia de modos invisibles y la reconstrucción de red son condiciones
  distintas; la reconstrucción se demuestra allí bajo una condición geométrica
  adicional. En nuestro K5 con B={0,1}, el subconjunto {2,3} no tiene punto
  único más cercano desde B: ambas distancias son 1. Falla la Two-Points
  Condition. El testigo no contradice ese teorema.

La semejanza de realizaciones y la invariancia del complemento de Schur son
mecanismos clásicos. La contribución de este corte al programa es el testigo
racional tipado y su control discriminante, no una afirmación de descubrimiento
histórico de la no unicidad de problemas inversos.

S contiene entradas negativas: no es una permutación ni una identificación
estocástica de los estados internos. Se usa para construir dos matrices Q
válidas por separado y demostrar igualdad del lector; no para afirmar que una
preparación física interna arbitraria se pueda trasladar entre las redes.

## 9. Reproducción, prueba y auditoría

Ejecutar `python3 verify_boundary_gauge.py`: Python estándar, aritmética
`fractions.Fraction`, tolerancia cero. Produce `certificate.json` con **74
comprobaciones exactas**, matrices, menores, medidas y controles. Los cinco
valores de s por testigo y once momentos de Q por testigo son controles de
implementación finitos. La igualdad para todos s y t procede de la prueba del
lema, no de esos controles.

La auditoría independiente vive en `audit/`: derivación y programa separados,
sin importar el verificador principal. Su dictamen y alcance constan en
`audit/AUDITORIA_MATEMATICA.md` y su certificado. No convertir un PASS finito en selección
universal del generador. Los archivos de esta edición contienen el informe, dos verificadores independientes y sus salidas.

**Dictamen matemático:** contraejemplo exacto dentro del contrato declarado.
**Identificación general de Q:** abierta y falsada si se exige sólo este lector.
**Gravedad física:** no evaluada ni derivada.

© 2026 Xorch — Concordante Lab. Derechos reservados.
