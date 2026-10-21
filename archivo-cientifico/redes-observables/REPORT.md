# Marcas interiores: clasificación exacta y umbral universal

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Informe original: 16 de octubre de 2026. Edición pública: 21 de octubre de 2026.

## Resultado y alcance

El corte previo distinguía un par concreto al abrir un nodo interior. Aquí se clasifica toda la ambigüedad de una realización observable: las preparaciones físicas conocidas P dejan exactamente las isometrías de capacidad que fijan tanto el vector constante como P, siempre que el Laplaciano transformado siga siendo admisible. Para n interiores, n−1 preparaciones nodales bastan universalmente. Menos no bastan como garantía sobre todas las redes completas positivas: se construye una familia de contraejemplos observables. En particular, un nuevo par K5 sigue indistinguible incluso al abrir como frontera un tercer nodo; un cuarto lo distingue.

No se supone que una preparación o una frontera extra estén físicamente disponibles. El coste contado es el número de nodos marcados individualmente y sus respuestas temporales completas, no el número de muestras, la precisión ni el coste experimental. No se afirma que cada red necesite n−1 marcas; muchos pares requieren menos.

## Contrato

Dos redes conexas sobre el mismo conjunto etiquetado B ⊔ I, B no vacío, |I|=n≥1, misma capacidad diagonal conocida M>0. L es un Laplaciano simétrico de conductancias no negativas; la familia de ejemplos tiene todas las conductancias estrictamente positivas. Sean D=L_II, C=L_BI, A=M_I^{-1}D. Se conoce

Λ(s)=L_BB−C(D+sM_I)^{-1}Cᵀ, s>0,

con el mismo reloj y unidades. El modelo interior es observable: la matriz vertical [C;CA;…;CA^{n−1}] tiene rango n. Las marcas adicionales son columnas p de una matriz conocida P: se fija f_B(t)=0, se prepara f_I(0)=p y se registra la corriente de frontera C exp(−tA)p para todo t≥0. Denotamos esta respuesta F_P(t). Son valores de funciones/temperaturas iniciales; no se confunden con inyecciones unitarias de masa.

## Teorema 1: clasificación de todas las realizaciones marcadas

Si ambas redes satisfacen el contrato y tienen iguales Λ y F_P, existe una única matriz S tal que

SᵀM_I S=M_I, S1=1, SP=P,

L̃=diag(I_B,S)ᵀ L diag(I_B,S).

Recíprocamente, cualquier S con esas identidades que produzca otro Laplaciano admisible da los mismos datos. Así, el grupo algebraico residual es O(n−d), con d=dim span{1, columnas de P}, conjugado por la raíz de M_I. La clase física es únicamente el subconjunto cuyos signos y soporte son admisibles, no todo ese grupo. Para un modelo observable, dos S diferentes producen realizaciones diferentes.

### Prueba autocontenida

Escribamos H=M_I^{−1/2}D M_I^{−1/2}, G=C M_I^{−1/2}, v=M_I^{1/2}1 y Z=M_I^{1/2}P. H es simétrica positiva definida. El rango observable equivale a que los vectores H^k Gᵀ a, k≥0, a∈R^{|B|}, generen R^n. La igualdad de Λ da L̃_BB=L_BB al tomar s→∞, y todos los momentos GH^kGᵀ=G̃H̃^kG̃ᵀ por la expansión convergente del resolvente para s suficientemente grande.

Definimos U sobre los generadores por U(H̃^kG̃ᵀa)=H^kGᵀa. Los productos internos de dos generadores son aᵀGH^{k+l}Gᵀb y coinciden en ambos modelos. Por ello la definición es independiente de cualquier relación lineal, conserva la norma y, por observabilidad, da una isometría ortogonal de R^n sobre R^n. Sobre los generadores se obtiene HU=UH̃ y UG̃ᵀ=Gᵀ; por tanto H̃=UᵀHU y G̃=GU. Es única porque los generadores abarcan todo el espacio.

Las sumas de fila del Laplaciano dan Hv=−Gᵀ1_B y H̃v=−G̃ᵀ1_B. Luego H(Uv)=UH̃v=−UG̃ᵀ1_B=Hv; al ser H invertible, Uv=v.

La respuesta preparada es G exp(−tH)Z. En el modelo transformado es G exp(−tH)UZ. Su igualdad para todos t implica GH^k(UZ−Z)=0 para todo k por derivación en t=0. Observabilidad implica UZ=Z. Poniendo S=M_I^{−1/2}UM_I^{1/2} resultan las tres condiciones y la congruencia afirmadas.

A la inversa, las identidades de S dan Ã=S^{-1}AS, C̃=CS y S1=1. La cancelación de S en el complemento de Schur prueba Λ̃=Λ; F̃_P=C exp(−tA)SP=F_P. La observabilidad muestra asimismo que un S que no cambie L debe ser la identidad. Finalmente, un ortogonal que fija punto por punto un subespacio de dimensión d actúa arbitrariamente como O(n−d) en su complemento ortogonal. Esto prueba la clasificación. □

## Corolario 2: n−1 marcas nodales bastan

Si P contiene n−1 vectores coordenados distintos de R^n, entonces {1,P} genera todo R^n. El teorema fuerza S=I y L̃=L. Para n=1 no se requiere ninguna marca. El caso n=0 queda fuera de esta fórmula de marcas. Si se abre cada nodo marcado como frontera completa, los datos son al menos tan discriminantes: toda equivalencia observable con frontera ampliada tiene un gauge que fija esos nodos. También puede aplicarse directamente el caso de un único nodo oculto. La suficiencia se refiere a las redes del contrato, no a un modelo con número interior desconocido.

### Reconstrucción explícita bajo datos exactos

La suficiencia también tiene un procedimiento algebraico. Sea R(s)=C(D+sM_I)^{-1}M_I la transformada de Laplace de la matriz de respuestas a todas las preparaciones nodales. De L1=0 se obtiene

R(s)1=−Λ(s)1_B/s.

Por tanto, las n−1 columnas medidas de R y esta suma reconstruyen la columna faltante. La expansión para s grande es R(s)=Σ_{r≥0}(−1)^r C A^r / s^{r+1}. Extraer sus primeros n+1 coeficientes da K_r=CA^r para r=0,…,n. Formar O=[K_0;…;K_{n−1}] y O_+=[K_1;…;K_n]. La ecuación OA=O_+ tiene una única solución por rango n de O; C=K_0, D=M_I A, L_BB=lim_{s→∞}Λ(s) recuperan todo L. Esto es identificabilidad exacta, no una garantía de estabilidad frente al ruido ni un método de diferencias numéricas recomendado.

## Teorema 3: la cota es óptima en peor caso

Para cada n≥2 y cualquier subconjunto J de k≤n−2 interiores marcados, existen redes completas positivas diferentes, de interior observable y capacidades conocidas distintas entre nodos e iguales en las dos redes, con iguales datos Λ,F_{E_J}. Incluso su transferencia completa sobre B∪J coincide.

### Construcción y prueba

Tomar B={0,1}, capacidades positivas distintas m_i y α=Σm_i. El Laplaciano base L0=αM−mmᵀ es de grafo completo con conductancias m_i m_j. Elegir dos interiores a,b no marcados y un vector w, nulo fuera de ellos, con w_a=m_b, w_b=−m_a. La reflexión S=I−2w(wᵀM_I)/(wᵀM_Iw) fija 1 y todos los e_j marcados. T=diag(I_B,S) conserva M y fija 1, por lo que TᵀL0T=L0.

Elegir números positivos distintos t_i para todos los interiores y

E=Σ_{i∈I} m_i t_i (e_0−e_i)(e_0−e_i)ᵀ,
Lε=L0+εE, L̃ε=L0+εTᵀET.

Para ε>0 suficientemente pequeño ambas matrices tienen todos los elementos fuera de diagonal estrictamente negativos: basta 0<ε<c/(1+K), con c=min_{i<j} m_i m_j y K=max_{i<j}|(TᵀET)_{ij}|. Son Laplacianos conexos por conservación de sumas y simetría. La congruencia prueba igualdad de los datos, incluso al incluir J en frontera.

En coordenadas normalizadas Hε=αI−vvᵀ+ε diag(t_i). La fila de G correspondiente a la frontera 1 es −m_1 vᵀ. Si un autovector x de Hε fuese ortogonal a v, entonces (αI+ε diag(t_i))x=λx. Como los t_i son distintos, x estaría soportado en una sola coordenada; pero v_i>0 hace imposible vᵀx=0. Si la observabilidad fallara, el subespacio invisible, invariante bajo la matriz simétrica Hε, contendría un autovector ortogonal a las filas de G y por tanto a v. Contradicción. Esto prueba observabilidad, incluidos posibles autovalores repetidos.

La reflexión normalizada U=M_I^{1/2}SM_I^{−1/2} no es diagonal (mezcla a y b). Una matriz que conmuta con diag(t_i), de entradas distintas, debe ser diagonal. Luego Uᵀdiag(t_i)U≠diag(t_i), de donde L̃ε≠Lε. Al ser todas las capacidades distintas, tampoco hay isomorfismo no trivial que preserve capacidades. Esto demuestra la cota inferior sobre toda la clase. No se necesita inferirla de una búsqueda finita. □

## Testigo racional K5: una marca aún falla

Orden (0,1,2,3,4), B={0,1}, I={2,3,4}, M=diag(1,2,3,4,5), P=e_2 físico (primera coordenada interior). Tomar L0=15M−mmᵀ y añadir a las aristas 02,03,04 los pesos 1,2,3. La reflexión es

S=[[1,0,0],[0,−1/9,10/9],[0,8/9,1/9]].

L=[[20,−2,−4,−6,−8],
   [−2,26,−6,−8,−10],
   [−4,−6,37,−12,−15],
   [−6,−8,−12,46,−20],
   [−8,−10,−15,−20,53]].

L̃=[[20,−2,−4,−58/9,−68/9],
    [−2,26,−6,−8,−10],
    [−4,−6,37,−12,−15],
    [−58/9,−8,−12,3758/81,−1616/81],
    [−68/9,−10,−15,−1616/81,4253/81]].

La conductancia mínima es 2 en ambas. El menor de las primeras tres filas de [C;CA;CA²] es 8/15 (y −8/15 transformado). Los multiconjuntos de diagonales son distintos, así que este par tampoco es isomorfo como red ponderada aun ignorando capacidades. S fija el nodo 2 y la frontera ampliada {0,1,2} sigue teniendo idéntica transferencia para toda s. La preparación interior e_2 produce exactamente la misma historia temporal de corriente. En cambio, preparar e_3 da ya en t=0 corriente en nodo 0 de −6 frente a −58/9: diferencia 4/9. Abrir también el nodo 3 distingue por el límite de alta frecuencia L_BB. Dos marcas bastan universalmente para n=3; una puede fallar.

No se afirma igualdad de actividad estacionaria: las trazas del nuevo par no coinciden. Este testigo responde a la intervención mínima bajo el contrato señalado, sin importar al nuevo contrato invariantes auxiliares del testigo anterior.

## Procedencia y fuentes

La prueba es autocontenida en álgebra lineal real finita. No usa como premisa externa un teorema de realización mínima ni reivindica prioridad bibliográfica. El antecedente del proyecto resolvía la distinción de un par concreto al abrir un nodo; se conserva íntegro junto con las fuentes y versiones en el registro privado. Este informe desarrolla una clasificación general bajo hipótesis explícitas y una cota óptima en peor caso, sin extrapolar los controles finitos. No se redistribuye material ajeno ni se afirma una búsqueda exhaustiva de literatura. La interpretación gravitatoria queda fuera de alcance.

## Evidencia, reproducción y límites

Ejecutar python3 verify_marks.py. Sólo biblioteca estándar, aritmética racional exacta, tolerancia cero. certificate.json contiene matrices y controles. Las comprobaciones en frecuencias y momentos son controles finitos de implementación; la identidad funcional y la cota para todo n se prueban arriba. El manifiesto conserva entradas, software, comando, salida y hashes. La auditoría independiente, su alcance y sus controles adicionales constan en audit/AUDIT.md. El verificador principal y el independiente son implementaciones separadas; la concordancia computacional no sustituye la prueba.
