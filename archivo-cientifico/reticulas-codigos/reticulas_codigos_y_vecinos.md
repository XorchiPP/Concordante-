# Retículas desde códigos: límites de norma y vecinos primos

Concordante Lab · Xorch

© 2026. Todos los derechos reservados.

Edición del 21 de octubre de 2026 de demostraciones archivadas el 19 de octubre. En todo el documento μ denota la mínima **norma cuadrada** y det Gram el cuadrado del covolumen. La dimensión n es positiva; para el código binario autodual doblemente par se exige n≥8.

## 1. Índice y mínimo exacto del corte binario

Para `C` binario autodual y doblemente par de longitud `n` (por ello `n` múltiplo de 8), definimos:

    A(C) = (1/sqrt(2)){x in Z^n : x mod 2 in C}
    M(C) = (1/sqrt(2)){x in Z^n : x mod 2 in C, sum(x_i)=0 mod 4}.

Como el código es autodual y doblemente par, A(C) es una retícula par unimodular, con covolumen uno. El homomorfismo `A(C) -> Z/2` dado por `sum x_i/2 mod 2` está bien definido porque C es par. Su imagen es todo Z/2, pues `(2,0,...,0)/sqrt(2)` tiene suma 2. Por lo tanto

    [A(C):M(C)] = 2,
    covol(M(C)) = 2,
    det Gram(M(C)) = 4.

**Teorema de mínimo exacto:** para `n>=8`, con `d(C)` mínimo Hamming,

    mu(M(C)) = min{4, d(C)/2}.

**Prueba:** si x mod2 es no nulo, como mínimo d(C) coordenadas de x son impares; por tanto `sum x_i^2 / 2 >= d(C)/2`. La cota se alcanza escogiendo +1 en el soporte de una palabra de peso d(C) y 0 fuera; la suma es `d(C)=0 mod4`. Si x mod2 es cero, cada coordenada es par, y la congruencia suma 0 mod4 excluye un único ±2 no nulo; al menos dos coordenadas ±2 dan mínimo `8/2=4`. Tal vector pertenece a M(C), por ejemplo `(2,2,0,...,0)/sqrt2`. QED.

Así, la ecuación `mu=d/2` no es universal: solo vale para esta M si `d<=8`. Y M nunca es unimodular. Necesitamos un **pegado adicional**, escogiendo una clase isotrópica apropiada del grupo discriminante de M, para recuperar covolumen uno sin reintroducir vectores cortos.

## 2. Cascarón D_n obligatorio y cota de norma

Sea C≤F₂ⁿ un código doblemente par y autodual, A(C)=(1/√2){z∈Zⁿ:z mod2∈C} y

M(C)=(1/√2){z∈Zⁿ:z mod2∈C, sum z_i≡0 (mod 4)}.

Como todo z=2w con w∈D_n={w∈Zⁿ:sum w_i par} tiene z mod2=0 y sum z_i≡0 (mod4), obtenemos el resultado exacto:

  sqrt(2)·D_n ⊂ M(C).

En particular, para cada i<j están los cuatro vectores √2(±e_i±e_j) de norma cuadrada 4. Cualquier retícula L que CONTENGA M(C) sin modificar la métrica contiene esos vectores y cumple μ(L)≤4. Añadir una coset jamás borra vectores del subgrupo incluido. Esto prohíbe obtener retículas con μ>4 como sobre-retículas integrales de M(C) en la misma escala, para cualquier código que satisfaga las hipótesis. No prohíbe usar esos códigos en otra construcción que modifique antes el subgrupo.

Si d(C)≥8, el censo de vectores de norma cuadrada 4 en M(C) es EXACTAMENTE

  N₄(M(C)) = 4·binom(n,2) + 128·A₈(C),

donde A₈(C) cuenta las palabras de peso ocho. Prueba: si ||z/√2||²=4, entonces Σz_i²=8. Los únicos patrones compatibles con una palabra del código de peso 0 o ≥8 son: (a) dos coordenadas ±2 y las demás 0; (b) ocho coordenadas ±1 en un soporte de palabra de peso 8, con número par de signos negativos. El caso (a) da 4·binom(n,2); cada palabra del caso (b) da 2⁷=128 signos. No hay otros casos.

Censos:
- Golay 24, A₈=759: 1,104 + 97,152 = 98,256 en M(C).
- Reed–Muller [32,16,8], A₈=620: 1,984 + 79,360 = 81,344 en M(C).
- QR binario [48,24,12]: A₈=0; ya hay 4·binom(48,2)=4,512 vectores obligatorios de norma 4.
- Código Type II de longitud 72 y distancia ≥16, bajo esa hipótesis: A₈=0; ya habría 4·binom(72,2)=10,224 vectores obligatorios de norma 4.

Este censo refuerza el no-go: no se trata de eliminar un único vector corto, sino un cascarón completo de tipo D_n.

## 3. Teorema del filtro primo: obstrucción a UN SOLO vecino p de Kneser

Supongamos que n≥3 y L es integral unimodular y contiene M(C). Sea p un primo impar. Un vecino p de Kneser L′ comparte con L una subretícula H de índice p de la forma

  H = { v∈L : ⟨x,v⟩≡0 (mod p) }

para cierto x∈L primitivo módulo p. Las retículas L y L′ contienen H. Para conseguir μ(L′)>4 habría que excluir de H todos los vectores √2(±e_i±e_j).

Como x es integralmente apareable con √2D_n, escribiendo a_i=√2 x_i se obtiene a_i±a_j∈Z. Por ello b_i=2a_i∈Z y los b_i tienen una misma paridad. Para p impar, la condición de que cada ± raíz tenga producto escalar no nulo módulo p equivale a exigir

  b_i ≠ b_j y b_i ≠ −b_j (mod p)  para todo i<j.

Pero F_p tiene solo (p+1)/2 clases bajo b∼−b. Si n>(p+1)/2, necesariamente hay i<j con b_i=±b_j, y uno de los vectores ±√2(e_i±e_j) está en H⊂L′. Así,

  p < 2n−1 ⇒ μ(L′)≤4.

Esto es un no-go para UN paso desde el marco que contiene M(C); no excluye sucesiones de vecinos después de un cambio estructural del soporte ni construcciones de otros módulos.

Cota reforzada por conteo: poniendo c=(p+1)/2, n=cq+r con 0≤r<c, toda asignación de n residuos en c clases de signo tiene por lo menos (c−r)·binom(q,2)+r·binom(q+1,2) parejas colisionadas; cada pareja conserva por lo menos dos vectores antipodales de norma 4 en H. Cota inferior comprobable:

  N₄(H) ≥ 2[(c−r)·binom(q,2)+r·binom(q+1,2)].

Para n=48, p=3,5,7 obligan respectivamente ≥1,104; ≥720; ≥528 vectores de norma 4. Para n=72 obligan ≥2,520; ≥1,656; ≥1,224. El primer primo que no es excluido POR ESTE ARGUMENTO es 97 (n=48), o 149 (n=72). Esto no afirma que funcionen: es filtro necesario, no suficiente. La prueba no cubre p=2; exige tratamiento separado.

## 4. Motor concreto de vecinos primos: sustitución, no sobre-retícula

Sea L par unimodular y p un primo. Elige x∈L primitivo módulo p con ⟨x,x⟩ divisible por 2p². Define

  H_x = {v∈L:⟨v,x⟩≡0 (mod p)},
  L′ = H_x + Z·(x/p).

Entonces [L:H_x]=p, [L′:H_x]=p, de donde det Gram(L′)=det Gram(L)=1. Las condiciones de producto escalar garantizan integridad y paridad de L′. Por tanto L′ es una retícula par unimodular, potencialmente no isométrica con L.

Para exigir μ(L′)≥t la verificación debe comprobar DOS puertas, no solo la primera: (G1) ningún vector no nulo de H_x tiene norma <t; (G2) ninguna coset a·x/p+H_x (a=1,…,p−1) tiene un representante con norma <t. Los productos escalares con los vectores cortos de L son un filtro barato para G1, pero G2 requiere reducción y certificado de mínimos de cosets. Si t>4 y p es impar, para L que contenga M(C) el teorema del filtro primo bloquea G1 en un único paso con p<2n−1.

No se puede simplemente agregar un pegamento propio a E8³ sin pasar antes por una subretícula: E8³ ya es unimodular; si L⊂L′ con ambas retículas enteras, entonces L′⊂L*=L y resulta L=L′. Los vecinos de Kneser sustituyen cosets a través de H_x, no amplían sin quitar.

## 5. Fórmula general para el techo en Construction A de módulo q

Para un código aditivo D⊂(Z/qZ)^n, q≥2 y n≥1, la Construction A_q en la escala convencional,

  A_q(D) = (1/√q){z∈Z^n : z mod q∈D},

contiene necesariamente √q·e_i (tomando z=q·e_i, cuyo residuo es cero). Luego μ(A_q(D))≤q. Esto no implica que toda retícula μ≤q exista mediante un código q-ario; solo establece una barrera universal. En particular, el techo universal de módulo 8 es 8; alcanzar un valor concreto depende también de la distancia euclidiana del código. La literatura de Chapman–Solé describe construcciones de módulo 8 distintas del corte binario; véase la bibliografía.


## 6. Mínimo exacto de Construction A de módulo general

Para un código aditivo no nulo D⊂(Z/qZ)^n, q≥2 y n≥1, sea d_E(D) el mínimo peso euclidiano de una palabra no nula: se escoge en cada coordenada un representante entero de menor valor absoluto. Entonces

    μ(A_q(D)) = min(q, d_E(D)/q).

En la clase cero, todo vector entero no nulo tiene una coordenada de valor absoluto al menos q; q e_i alcanza norma cuadrada q tras dividir por √q. En una clase no cero, minimizar separadamente cada coordenada da el peso euclidiano de la palabra dividido por q; minimizar entre las palabras prueba la fórmula. Para D={0}, A_q(D)=√q Z^n y el mínimo es q. La normalización es fija.

Para un código binario Type II, la Construction A ordinaria tiene mínimo 2. El corte M(C) tiene mínimo min(4,d(C)/2), covolumen 2 y determinante de Gram 4. Estas son tres magnitudes distintas.

## 7. Alcance y continuación

Las demostraciones son generales bajo las hipótesis indicadas. El certificado comprueba aritmética de los censos y el principio de colisión para los primos pequeños 3,5,7; los conteos A₈=759 y A₈=620 son entradas históricas de Golay y Reed–Muller, no enumeraciones de códigos en este paquete. Los ejemplos condicionales de longitudes 48 y 72 se deducen sin suponer la existencia de un código de distancia específica.

Para superar el cascarón por un solo paso de primo impar es necesario p≥2n−1; p=97 y p=149 únicamente evitan esa obstrucción numérica en dimensiones 48 y 72. La certificación de un vecino concreto exige revisar todas las clases a x/p+H y sus vectores cortos. El caso p=2 requiere otro argumento.

La geometría de códigos y vecinos es clásica. Este documento ofrece una presentación de las pruebas elementales y sus controles finitos; la prioridad bibliográfica del filtro particular queda sin establecer. 
### Pendiente de incorporar

- Tablas y pruebas de normalización Barnes–Wall.
- Masa total de códigos Type II.
- Levantamientos octonarios y sus correcciones históricas.
- Certificados específicos de ejemplos 48/72D y sus comparaciones de isometría.

La clasificación y la optimalidad global requieren argumentos adicionales a los límites de norma y controles finitos aquí incluidos. Estos materiales permanecen en el alcance del archivo científico completo.
