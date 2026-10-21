# Reinicios de subconjuntos: acoplamiento triple invisible a cada proceso marginal de pares

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Informe original: 16 de octubre de 2026. Edición pública: 21 de octubre de 2026.

## Resultado y alcance histórico

Se clasifica la extensión del contrato anterior a un número finito k de bloques marcados: las familias universales son exactamente sumas de reinicios uniformes de subconjuntos, con 2^k−1 intensidades no negativas. Para tres bloques se obtiene la condición exacta para pegar tres acoplamientos de pares y el intervalo de libertad triple. Dos familias universales irreducibles pueden tener todos los procesos marginales de pares idénticos y el mismo gap, pero distinta relajación del modo triple. También se exhiben tres pares universalmente admisibles por separado que no admiten pegado conjunto.

Esto no vuelve a reclamar como nuevo el parámetro de dos bloques, el antecedente de naturalidad total ni la degeneración del gap del corte anterior. No se afirma prioridad matemática externa. El resultado es una deducción bajo un contrato enriquecido, no una ley física ni una selección desde un principio físico subyacente.

## Procedencia

Edición de un resultado fechado el 16 de octubre de 2026, no afirmación de ser el último avance del programa. El antecedente de dos bloques y las fuentes originales se conservan íntegros en el registro privado; esta clasificación incluye su propio argumento de Fourier finito e inversión booleana y no depende de importar código del antecedente. No se declara prioridad externa ni revisión exhaustiva de literatura.

## 1. Contrato

Fijar k≥1 finito y bloques etiquetados V_i=F₂^(n_i), n_i≥1, M_i=2^(n_i). Se fija la descomposición directa y la suma. En cada vector dimensional se tiene un generador real de convolución

L f(x)=Σ_(z≠0) q_n(z)[f(x+z)−f(x)], q_n(z)≥0.

Se exige invariancia por el producto de GL(n_i,2) y consistencia exacta bajo todas las sobreyecciones lineales separadas entre dimensiones positivas, con reloj común y para todos los vectores dimensionales sin cota superior. A_i promedia uniformemente el bloque i; A_S=producto de A_i para i∈S, identidad en los restantes. A_∅=I. Los bloques están marcados, no son una factorización extraída del grupo desnudo. No se exige coherencia al variar k; k queda fijo. Las marginales sobre subconjuntos de bloques se obtienen restringiendo a funciones de esos bloques, no mediante dimensiones cero.

Hipótesis añadidas explícitamente: factorización marcada, convolución, reloj común, disponibilidad de todos los tamaños y cocientes separados. La aplicación a un sistema físico requiere justificar por separado esas hipótesis.

## 2. Teorema universal de k bloques

**T1.** Bajo este contrato existen únicos números λ_S≥0, uno por cada ∅≠S⊆[k], independientes de n, tales que

L_n = Σ_(S≠∅) λ_S (A_S−I).

Recíprocamente toda elección no negativa produce una familia admisible. Para un desplazamiento de soporte exacto T≠∅, su tasa individual es

q_n(T)=Σ_(S⊇T) λ_S / Π_(i∈S) M_i.                                      (1)

Aquí q_n(T) es la tasa de cada vector de ese soporte; no la suma sobre la órbita.

**Prueba completa.** La invariancia hace q constante en cada soporte T. La transformada Fourier de un operador de convolución es diagonal en los caracteres χ_a(x)=(-1)^(Σ a_i·x_i). El producto GL es transitivo en los caracteres con un mismo soporte J de bloques no triviales, así que el autovalor depende solo de J. Escribamos −r_n(J), con r_n(∅)=0. Para cada carácter a, se puede elegir una sobreyección V_i→F₂ cuya funcional sea a_i si a_i≠0; para a_i=0 se elige cualquier sobreyección y se usa el carácter trivial del destino. Consistencia implica r_n(J)=r_(1,...,1)(J)=r(J).

A_S actúa como 0 si S∩J≠∅ y como 1 en caso contrario. Por tanto basta resolver

r(J)=Σ_(S:S∩J≠∅) λ_S.                                                   (2)

Esta transformación es invertible sobre los reales. En efecto, poner Λ=r([k]) y F(T)=Λ−r([k]\T) da F(T)=Σ_(∅≠S⊆T) λ_S, incluyendo F(∅)=0. La inversión booleana da

λ_S=Σ_(T⊆S) (-1)^(|S|−|T|) F(T).                                       (3)

La identidad de inversión se verifica intercambiando sumas: para R⊆S, la suma de signos sobre R⊆T⊆S vale 0 salvo R=S, donde vale 1. Así λ es único e independiente de n. Los caracteres forman una base: la suma de χ_aχ_b sobre el grupo es su tamaño si a=b y cero si a≠b, por emparejamiento con una traslación que cambia el signo. La igualdad en todos los caracteres implica la igualdad de operadores. El núcleo de A_S es uniforme en los desplazamientos de S y nulo fuera, dando (1).

Falta lo decisivo: λ_S no negativo. Multiplicar (1), para T fijo, por Π_(i∈T) M_i produce λ_T+Σ_(S⊋T) λ_S/Π_(i∈S\T)M_i≥0. Manteniendo dimensiones de T y haciendo crecer simultáneamente las restantes, la suma finita extra tiende a cero. Luego λ_T≥0. Para T=[k] ya no hay términos extra. Esto utiliza la familia universal, no se puede deducir de un único tamaño. Recíprocamente, con λ≥0 cada término es un generador de reinicio, y una sobreyección lineal envía uniforme a uniforme por igualdad de tamaños de fibras. Las sumas conservan positividad, invariancia y consistencia exacta. QED.

Interpretación: reloj de Poisson independiente por subconjunto S, tasa λ_S; en su evento se reemplazan los valores de S por uniformes independientes entre sí. Comparten instante de reinicio, no nuevo valor. Se permiten eventos sin cambio visible.

**Lema finito.** A dimensiones fijas la misma representación real única existe, pero ser Markov exige solamente las 2^k−1 desigualdades (1)≥0; no exige λ≥0. Es importante no importar el cono universal al caso finito.

## 3. Marginalización y gap

Para un conjunto conservado B, A_S se restringe a A_(S∩B). Los S disjuntos de B contribuyen cero. Por ello la intensidad marginal de un subconjunto no vacío R⊆B es

λ_R^(B)=Σ_(S:S∩B=R) λ_S.                                                (4)

La marginal unaria i es c_i(A_i−I), donde c_i=Σ_(S∋i)λ_S. Todo carácter de soporte J no vacío relaja a tasa r(J) de (2). Con λ≥0 y i∈J, r(J)≥c_i. Los soportes unitarios aparecen porque n_i≥1. Si todos c_i>0, todas las tasas no constantes son positivas, el generador es irreducible y

gap(L)=min_i c_i.

Irreducibilidad también se ve porque una tasa λ_S>0 produce desplazamientos puros en cualquier coordenada i∈S; si c_i>0, se generan todos los bloques. Si algún c_i=0, ese bloque no se mueve y no hay irreducibilidad; no se usa en ese caso la convención de menor autovalor estrictamente positivo como si fuera un gap ergódico.

## 4. Tres pares y su pegado exacto

Para k=3 se fijan c_i≥0 y los tres parámetros de pares θ_ij, entendidos como intensidad de reinicio común en el proceso marginal sobre i,j del corte de dos bloques. Por (4), θ_ij=λ_ij+λ_123. Escribiendo t=λ_123 se obtiene necesariamente

λ_123=t;
λ_ij=θ_ij−t;
λ_i=c_i−θ_ij−θ_ik+t, {i,j,k}={1,2,3}.

**T2.** Hay una familia conjunta universal exactamente cuando

max(0, θ_12+θ_13−c_1, θ_12+θ_23−c_2, θ_13+θ_23−c_3)
≤ t ≤ min(θ_12,θ_13,θ_23)                                                (5)

tiene solución. Cada t del intervalo da una familia distinta. La prueba sustituye las siete intensidades en T1; las siete condiciones de no negatividad son precisamente (5). No hace falta añadir por separado las condiciones de admisibilidad de cada par: quedan implicadas por las intensidades no negativas y (4).

**Obstrucción de pegado.** c_1=c_2=c_3=1; θ_12=θ_13=1, θ_23=0. Cada par está dentro de [0,min(c_i,c_j)], pero (5) exige t≥1 y t≤0. Por ello los tres procesos de pares, individualmente universales e irreducibles, no admiten una familia conjunta del contrato. La obstrucción corresponde exactamente a las familias del contrato indicado.

**Control que separa tamaño finito y universal.** Estos mismos tres pares sí se pegan en F₂×F₂×F₂: tomar λ_1=−1, λ_12=λ_13=1 y las demás intensidades cero. Por (1), q(100)=0, q(010)=q(001)=q(110)=q(101)=1/4 y q(011)=q(111)=0; son tasas Markov e incluso generan todo el grupo. Las marginales tienen exactamente c_i=1 y los θ indicados. Sin embargo, conservar esos coeficientes al ampliar a tamaños (2,4,4) da q(100)=−1/2+1/8+1/8=−1/4. Otro t no rescata la extensión universal, por (5). Por tanto el no-go de pegado aquí es estrictamente universal, no una incompatibilidad de los tres pares en el tamaño binario.

## 5. Testigo invisible a los pares

Tomar c_i=1 y θ_ij=1/2 para todos i,j. El intervalo exacto es 0≤t≤1/2.

- Modelo P: t=0, λ_12=λ_13=λ_23=1/2 y λ_i=λ_123=0.
- Modelo Q: t=1/2, λ_1=λ_2=λ_3=λ_123=1/2 y λ_ij=0.

Ambos son universales, invariantes por permutación de los tres bloques y por GL separado, irreducibles en todas las dimensiones positivas, con la misma distribución estacionaria uniforme producto. Sus tres generadores marginales de pares son idénticos: cada uno tiene coeficientes 1/2 para reiniciar el primer bloque, el segundo y ambos. La igualdad se refiere a cada proceso marginal entero para iguales leyes iniciales de ese par, no solo a su distribución estacionaria; no implica igualdad de la ley conjunta de varios registros de pares observados simultáneamente, que pueden revelar los tres bloques.

En el tamaño mínimo F₂×F₂×F₂, las tasas individuales por soporte son:

P: q_single=1/4; q_pair=1/8; q_triple=0.
Q: q_single=5/16; q_pair=1/16; q_triple=1/16.

Las tres tasas espectrales unitarias son 1; las tres tasas de pares son 3/2; la tasa triple vale 3/2 para P y 2 para Q. El gap es 1 en ambos. Así la fotografía estacionaria, todas las dinámicas marginales de pares y el selector de brecha dejan una ambigüedad genuinamente triple. Tres es el mínimo número de bloques para esta pregunta, pues con dos bloques el único par ya es todo el sistema.

**Lector triple calibrado.** En general

r(123)=c_1+c_2+c_3−θ_12−θ_13−θ_23+t.

Por tanto la tasa del sector media cero en cada uno de los tres bloques identifica t una vez calibrados los parámetros de pares. Alternativamente, la tasa de cambios visibles simultáneos de los tres bloques es

R_123=t Π_i(1−1/M_i).

Solo el reloj triple produce ese término de orden dt; coincidencias de relojes distintos tienen probabilidad O(dt²). Para P es 0, para Q en tamaño binario es 1/16. Se requieren resolución temporal y lectores calibrados; ruido desconocido o agregación pueden ocultarlo. La identificabilidad experimental requiere satisfacer y verificar esas condiciones.

## 6. Alcance operacional y siguiente frontera

El principio adicional «no hay eventos que reinicien tres bloques a la vez» fija t=0 cuando es factible, pero es un supuesto operacional agregado. La simetría entre los tres bloques tampoco selecciona t: toda la familia simétrica anterior la satisface. La brecha sola tampoco. La no negatividad y consistencia imponen un politopo, no un valor físico único.

La aportación acotada queda cerrada con T1/T2 y los dos contraejemplos. Queda pendiente determinar qué factorización, cocientes, reloj o lectores admite una fundamentación física del modelo. Resolver esa frontera requiere una condición operacional justificada y contrastable, además de las comprobaciones finitas aquí incluidas.

## 7. Verificación

verify_multiblock.py es stdlib, enteros/Fraction, sin red ni paquetes nuevos. Comprueba inversión y positividad sobre bases y familias de k=1..4; núcleos de convolución de los modelos P,Q a tamaños 2/4 por bloque; todos sus caracteres; igualdad de los tres generadores marginales; todos los mapas lineales sobreyectivos F₂²→F₂, F₂³→F₂ y F₂³→F₂² por separado en cada posición, con los otros dos bloques binarios; y rejilla racional para (5). Incluye control negativo finito λ_single=−1/8, λ_pair=0, λ_triple=1 en tres bloques binarios, Markov allí pero con una tasa pura negativa al ampliar los otros bloques a dimensión 3. La demostración universal corresponde a §2; estos controles verifican los casos finitos declarados.

Estado de revisión: prueba y código sometidos a autoauditoría y a revisión independiente en audit/AUDIT.md; veredicto «proved as written» bajo este contrato. El verificador independiente audit/verify_independent.py ejecutó 9,617 aserciones exactas con matrices completas, eliminación gaussiana y 54 cocientes simultáneos. La auditoría independiente complementa la prueba dentro del mismo contrato matemático. Dependencias matemáticas externas: ninguna; Fourier finito e inversión booleana se justifican aquí. Fuentes del proyecto sirven para fijar antecedente y alcance. Esta edición pública conserva las fechas y el alcance de la revisión histórica.
