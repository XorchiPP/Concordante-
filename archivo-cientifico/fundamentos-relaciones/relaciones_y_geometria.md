# Relaciones de compatibilidad y geometría de grafos

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Informe del 21 de octubre de 2026. Edición pública con la construcción, los ejemplos y las pruebas del documento fuente; referencias de archivo y marca adaptadas.

## 0. Motivación y frontera de anterioridad

La motivación del programa es estudiar el espacio como geometría de relaciones. La métrica de grafos, los complejos de cliques, la homología simplicial, los laplacianos y la clasificación de conexiones planas son construcciones clásicas. Esta entrega integra pruebas, ejemplos finitos y obstrucciones de selección para delimitar exactamente qué puede y qué no puede deducirse de compatibilidad binaria.

## 1. Axioma mínimo y semántica

Sea `X` un conjunto finito no vacío y `C: X×X -> {0,1}` una relación simétrica y reflexiva. Sea `G_C=(X,E)` el grafo simple `E={{x,y}:x!=y, C(x,y)=1}`. Para la afirmación métrica se exige que `G_C` sea conexo. No se supone ninguna coordenada, espacio envolvente, forma bilineal, campo de fases, reloj ni Hamiltoniano.

**Puerta semántica explícita:** si `C(x,y)` expresa mera coexistencia o consistencia simultánea, la lectura de una arista como **transición elemental** es un **postulado operacional adicional**. Como construcción matemática, el grafo y su distancia no requieren esa lectura física. Tampoco se deduce la relación concreta `C` desde un principio más elemental: `C` es un dato inicial con contenido estructural.

## 2. Proposición (objetos canónicos sobre compatibilidad)

De `(X,C)` se construyen sin elecciones de coordenadas:

1. **Distancia de trayectorias:** `d_C(x,y)=min{k: x=x0 ~ x1 ~ ... ~ xk=y}`. Para el grafo conexo del contrato es una métrica finita. En un grafo desconexo se obtiene una métrica finita en cada componente y una distancia extendida, con valor infinito, entre componentes. `C(x,y)=1` para `x!=y` si y sólo si `d_C(x,y)=1`.
2. **Simetrías exactas:** `Aut(X,C)=Isom(X,d_C)` como grupos de permutaciones, porque ambas preservan exactamente los pares a distancia uno.
3. **Topología de cliques:** `K_C={sigma ⊆ X: cada par de elementos distintos en sigma es compatible}`. Los grupos `H_k(K_C;F_2)` son invariantes combinatorios; no implican por sí solos dimensión física.
4. **Operador de borde y laplaciano:** con incidencia arbitrariamente orientada `B`, `L=BB^T=D-A`. La orientación auxiliar se cancela; `f^T L f = sum_{edges {x,y}}(f_x-f_y)^2 >=0`; `ker L` son constantes en cada componente.
5. **Dos familias naturales, no obligatorias como física:** `P_t=exp(-tL)` es un semigrupo estocástico simétrico (`t>=0`), de difusión reversible con distribución estacionaria uniforme, y `U_t=exp(-itL)` es unitario (`t ∈ R`). Se requiere la elección de interpretación probabilística/cuántica y escala temporal para llamar a uno de estos operadores «ley física».

**Demostración:** concatenar caminos prueba la desigualdad triangular; preservar los pares `d=1` equivale a preservar `E`; el complejo de cliques depende sólo de `E`; `BB^T` no cambia al invertir columnas de `B`; las identidades de la energía prueban positividad y el núcleo; `-L` tiene sumas de fila cero y tasas positivas en las aristas, por lo que genera un semigrupo de Markov, y `L=L^*` implica `U_t^*U_t=I`. Son resultados estándar de matemáticas discretas.

## 3. Experimento computacional replicable

Dos instancias de la **misma especificación** (una relación binaria simétrica), construidas de modos diferentes. Las mediciones reciben solamente conjuntos de adyacencia; las coordenadas modulares se utilizan para **crear el dato de entrada** en el segundo caso, no para calcular los invariantes.

**A: ciclo `C_11`.** Once estados con `i~i±1 (mod 11)`. `|V|=11`, `|E|=11`, cero triángulos, sin tetraedros; bolas centradas en cero para `r=0,1,2,3,4`: `(1,3,5,7,9)`; Betti sobre `F2`: `(b0,b1,b2)=(1,1,0)`.

**B: toro triangulado `T_11`.** Estados `(a,b)∈(Z/11)^2`, aristas para diferencias no orientadas generadas por `(1,0),(0,1),(1,1)`. El algoritmo emplea después la adyacencia. `|V|=121`, `|E|=363`, `|triángulos|=242`, ninguna clique de cuatro vértices; `(rank ∂1, rank ∂2)=(120,241)` sobre `F2`; Betti `(1,2,1)`; bolas `r=0..4`: `(1,7,19,37,61)`. La cuadrícula periódica 11×11 lleva la diagonal (1,1) en cada celda. Sus cliques triangulares son las dos mitades de cada cuadrado: [(a,b),(a+1,b),(a+1,b+1)] y [(a,b),(a,b+1),(a+1,b+1)], con índices módulo 11; el recuento de 242 triángulos y la ausencia de K4 coinciden con esa triangulación. La realización es el cociente R²/(11Z)², de modo que su H₁ integral es Z².

Fórmulas exactas antes del régimen de enrollamiento periódico: `V_ciclo(r)=2r+1`, `V_toro(r)=1+3r(r+1)`. Para familia de tamaño 101 y escalas `r=5,10`, las dimensiones efectivas `log2(V(2r)/V(r))` son respectivamente `(0.932886,0.965235)` para el ciclo y `(1.862893,1.929665)` para el toro.

**Guardia de finitud:** para cualquier grafo finito, `V(r)` se satura y el exponente asintótico `lim_{r→∞} log(V(r))/log r=0`. Aquí se habla sólo de perfiles de escala o de familias cuyo tamaño crece; no de un universo de dimensión «1» o «2» deducido sin condiciones.

**Chequeos numéricos de la ejecución histórica** (ver `certificado_historico.json`; las últimas cifras dependen del entorno de álgebra lineal): autovalor mínimo no negativo dentro de `1e-15`, error máximo de unitariedad `~1.6e-15`, sumas de filas de difusión iguales a uno con error `~4.5e-15`, incidencia triangular consistente, simetría que invierte cada arista testigo y control espectral de `C_11` con `lambda_k=2-2cos(2πk/11)`.

## 4. Puente exacto a holonomía y cohomología: lo permitido frente a lo seleccionado

Dado un grafo conexo, **añadir** una variable de transporte `u_xy ∈ U(1)` en cada arista orientada, con `u_yx=u_xy^{-1}`, permite transformaciones gauge `u_xy -> g_x u_xy g_y^{-1}`. La holonomía de cada lazo cerrado es gauge-invariante, pero **la relación `C` no asigna sus fases**.

Teorema clásico especializado:

- Sin imponer planitud de caras, las conexiones de arista módulo gauge forman `U(1)^{|E|-|V|+1}`.
- Si se exige **como axioma independiente** holonomía trivial alrededor de cada cara triangular del complejo `K_C`, las clases planas módulo gauge corresponden a `H^1(K_C;U(1)) ≅ Hom(H_1(K_C;Z),U(1))`. Si `H_1` es libre de rango `b1`, este espacio es `U(1)^b1`.

Ejemplos:

| Instancia | Parámetros gauge sin planitud | Restricciones de planitud independientes | Clases planas |
|---|---:|---:|---:|
| `C_11` | `11-11+1=1` | `0` | `U(1)` |
| `T_11` | `363-121+1=243` | `241` | `U(1)^2` |

**Control negativo absoluto:** en `C_11`, fijar todas las fases a `1` produce holonomía `1`. Mantener exactamente la misma `C` y cambiar la fase de una arista a `e^{iθ}` produce holonomía `e^{iθ}`. Para `θ` no múltiplo de `2π` son dos configuraciones no gauge-equivalentes. Por tanto **ninguna teoría basada en `C` exclusivamente puede afirmar que determinó el campo de gauge físico concreto** sin un principio adicional de selección.

Esto sí conecta de modo matemático el programa de cohomología con el de holonomía: la topología controla qué clases de conexión *pueden existir*, no cuáles son físicamente realizadas.

## 5. Tres obstrucciones de selección

**NG1: la relación no selecciona una dimensión universal.** Tanto el ciclo como el toro obedecen el mismo tipo de axioma mínimo, pero tienen homología y perfiles dimensionales distintos. Dimensión observable sólo tiene sentido relativo a `C` y al régimen de escala. El axioma no impone `d=3`, `d=4`, ni otra cifra universal.

**NG2: ausencia de orientación de aristas invariante bajo todos los automorfismos, en estos ejemplos.** En `C_11`, la reflexión `i -> 1-i (mod 11)` preserva todas las compatibilidades e intercambia los extremos de la arista `(0,1)`. Si una orientación de las aristas fuera natural e invariante bajo todos los automorfismos, esa reflexión la invertiría y conservaría simultáneamente, contradicción. Un argumento análogo funciona para una arista del toro usando `(a,b)->(1-a,-b)`. El resultado preciso concierne a la orientación de esas aristas y al grupo de automorfismos declarado. Puede elegirse evolución irreversible (p. ej. difusión) o formularse una flecha macroscópica condicionada; vincular esas nociones a una orientación temporal física requiere hipótesis adicionales.

**NG3: relación no selecciona un único Hamiltoniano.** `H=L` y `H=A` son autoadjuntos y determinados de manera natural por el mismo grafo. En el camino de tres vértices con estado inicial extremo y `t=1`, las distribuciones de probabilidades obtenidas son:

- `H=L`: `(0.389633, 0.442221, 0.168147)`;
- `H=A`: `(0.334051, 0.487841, 0.178108)`.

Ambas evoluciones son unitarias; la máxima diferencia probabilística es `0.055581`. La compatibilidad, por sí misma, no dice cuál de estas dos dinámicas es la correcta. Para grafos regulares estas dos elecciones pueden relacionarse mediante reversión de tiempo y fase global; por eso se usa intencionalmente un grafo irregular para el testigo de no unicidad.

## 6. Resultado y siguiente prueba discriminante

**Resultado positivo:** de relaciones compatibles se obtienen algebraicamente distancia, isometrías, complejos topológicos, operadores de difusión y evoluciones unitarias **candidatas**. El ejemplo calculado produce una superficie con clases homológicas `(1,2,1)` y restringe las clases de holonomía plana a `U(1)^2` al introducir un axioma de planitud.

**Límite demostrado:** ni la relación de compatibilidad `C`, ni la dimensión física, ni la elección del Hamiltoniano, ni las fases gauge, ni la flecha temporal son fijadas por el formalismo mínimo. La interpretación física requiere además una regla de selección y contrastación empírica.

**Próxima prueba científica discriminante:** especificar una **regla generadora de compatibilidad que no codifique coordenadas** (p. ej. una regla local de composición y cancelación sobre palabras) y estudiar si selecciona automáticamente, bajo hipótesis explícitas y sin parámetros geométricos puestos a mano, (i) una clase de dimensión estable en un límite de escala, (ii) un operador dinámico físicamente motivado, (iii) restricciones de gauge no triviales; después contrastar predicciones cuantitativas independientes. También sería valioso probar una obstrucción a esa selección bajo hipótesis demasiado débiles.

## 7. Reproducción y referencias

El programa `verificar_geometria_relacional.py` reconstruye las dos entradas y calcula sus invariantes con Python 3 y NumPy. Los conteos combinatorios y los rangos sobre F₂ son exactos; las exponenciales, autovalores y probabilidades se verifican numéricamente con tolerancias explícitas. Las instrucciones y los certificados de las dos ejecuciones están en README.md. Las referencias completas se encuentran en BIBLIOGRAFIA.md.

**Alcance de la clasificación U(1):** para estos ejemplos, la identificación geométrica del ciclo con S¹ y de la malla periódica triangulada con el toro proporciona H₁ integral libre de rangos 1 y 2. El código calcula rangos sobre F₂ y cuenta los parámetros bajo esa hipótesis topológica; no implementa una reducción integral de Smith ni decide torsión para un complejo arbitrario. La comparación entre homología integral, planitud y cocientes gauge utiliza el argumento clásico de la sección 4.
