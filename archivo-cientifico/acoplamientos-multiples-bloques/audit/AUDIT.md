# Auditoría independiente: reinicios de subconjuntos y compatibilidad triple

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Auditoría histórica del 16 de octubre de 2026, edición pública del 21 de octubre de 2026. Revisión separada dentro del proyecto. El certificado regenerado identifica los derivados ejecutados; la revisión de la prueba conserva su fecha histórica y el arbitraje externo constituye una etapa posterior.

## Afirmación normalizada y veredicto

**Veredicto principal: proved as written (demostrado tal como está escrito).**

Para un número fijo finito k≥1 de bloques marcados F₂^(n_i), con n_i≥1 sin cota superior, las familias de generadores reales de convolución invariantes por GL separado y exactamente consistentes bajo todos los cocientes lineales sobreyectivos separados, con reloj común, son exactamente las sumas únicas Σ_(S≠∅) λ_S(A_S−I), λ_S≥0 independientes de las dimensiones. Para k=3, los datos marginales c_i, θ_ij admiten tal familia exactamente cuando el intervalo (5) no es vacío. El testigo P/Q tiene todos los procesos marginales de pares iguales y gap 1, pero tasas de relajación triple 3/2 y 2.

Se auditan REPORT.md §§1–7 y verify_multiblock.py. El certificado independiente identifica mediante SHA-256 la revisión concreta examinada. Los datos de preflight y sincronización externa no forman parte del veredicto matemático; no se han vuelto a consultar servicios externos. Los datos administrativos de custodia se mantienen fuera de esta edición científica.

## 1. Derivación y dependencias

1. **Contrato → descomposición espectral.** Sobre el grupo binario finito los caracteres reales forman una base: la suma de un carácter no trivial es cero emparejando x con x+y donde χ(y)=−1. Esto establece la ortogonalidad y exhaustividad. La convolución es diagonal en esa base. GL separado identifica exactamente los soportes de bloques de los caracteres; no identifica soportes diferentes.
2. **Cocientes → independencia dimensional.** Cada carácter no trivial de un bloque es el pullback del carácter no trivial de F₂ bajo su propia funcional sobreyectiva. En un bloque trivial puede escogerse cualquier funcional sobreyectiva y el carácter trivial destino. Así, cada autovalor desciende al vector dimensional (1,…,1), sin introducir bloques de dimensión cero. Es esencial usar el mismo reloj.
3. **Espectro → representación real única.** El operador A_S tiene autovalor 0 precisamente si S corta el soporte del carácter. Por tanto r(J)=Σ_(S∩J≠∅)λ_S. Si Λ=r([k]), entonces Λ−r([k]\T)=Σ_(∅≠S⊆T)λ_S. Restar sucesivamente las contribuciones de subconjuntos estrictos obtiene cada λ_T, mostrando existencia y unicidad; es la inversión booleana del informe. En el verificador independiente esta inversión se reconstruye por eliminación gaussiana, no copiando la rutina de inversión del autor.
4. **Positividad universal → λ_T≥0.** Para un salto de soporte exacto T, la probabilidad de ese desplazamiento en un reinicio S es 1/Π_(i∈S)M_i si S⊇T, y cero en otro caso. Al multiplicar su tasa por Π_(i∈T)M_i, queda λ_T más términos λ_S/Π_(i∈S\T)M_i. Hay un número finito de términos y los coeficientes ya son independientes de las dimensiones. Hacer crecer todos los bloques fuera de T anula cada término adicional. El límite de cantidades no negativas es λ_T. Para T=[k] no hay límite que tomar. Esto cubre también k=1.
5. **Recíproco.** Cada λ_S≥0 define un reloj de reinicio válido. El pushforward del uniforme por una sobreyección lineal es uniforme; sus fibras tienen igual tamaño. El entrelazamiento exacto de generadores sigue por linealidad y produce la consistencia de semigrupos en dimensión finita. No se requiere un proceso sobre una unión infinita ni coherencia entre valores diferentes de k.
6. **Marginales → compatibilidad.** Al restringir a bloques B, A_S se convierte en A_(S∩B). Para tres bloques, θ_ij=λ_ij+t y c_i=λ_i+λ_ij+λ_ik+t, con t=λ_123. Las siete desigualdades de no negatividad son exactamente las cuatro cotas inferiores y las tres superiores de (5). No se usa independencia adicional entre los procesos de pares.
7. **Espectro → gap e irreducibilidad.** r(J)≥c_i para todo i∈J y existen caracteres de soporte unitario. Si cada c_i>0, el mínimo no trivial es min_i c_i. Además, algún reinicio que contiene i tiene tasa positiva y puede alterar solo ese bloque, manteniendo los otros valores; tales saltos conectan todos los estados. Si c_i=0, todas las intensidades que contienen i son cero y el bloque queda inmóvil. No se confunde este caso reducible con un gap ergódico positivo.

Las hojas anteriores son argumentos internos elementales. No hay dependencia externa no verificada ni ciclo lógico entre el certificado finito y el teorema universal.

## 2. Matriz de obligaciones

| Obligación | Estado | Evidencia |
|---|---|---|
| Tipos, dominio, bloques marcados y k fijo | passed | Contrato explícito; no cambio de factorización |
| Fourier, dualidad GL, signo −r | passed | Reconstrucción anterior y acción exacta sobre caracteres |
| Independencia de dimensiones | passed | Pullback hacia dimensión uno por bloque |
| Inversión y unicidad | passed | Inversión de subconjuntos; eliminación racional independiente |
| No negatividad de cada λ | passed | Límite exterior finito; no inferencia desde tamaño único |
| Cocientes simultáneos | passed | Prueba por uniformes y 54 productos de mapas comprobados |
| Fórmula de marginalización | passed | Entrelazamiento de matrices en cada fibra |
| Compatibilidad triple | passed | Siete intensidades y 3.645 casos racionales independientes |
| Bordes c_i=0, k=1, intervalo puntual | passed | Prueba anterior, controles de generador nulo y bloques congelados |
| Gap e irreducibilidad | passed | Argumento espectral y conectividad explícita |
| Igualdad de procesos marginales completos | passed | Generador lumpable igual; requiere igual ley inicial marginal |
| Igualdad de leyes conjuntas de múltiples registros | out of scope | No se afirma; el informe la excluye explícitamente |
| Identificación física/experimental sin calibración | out of scope | No se afirma |
| Novedad externa o exhaustividad bibliográfica | not addressed | Evaluación de prioridad pendiente |
| Custodia GitHub/Drive actual | not addressed | Auditoría local, sin relectura de los servicios |

## 3. Control adversarial decisivo: universal no significa finito

Los datos c=(1,1,1), θ=(1,1,0) son incompatibles universalmente porque exigen t≥1 y t≤0. Sin embargo, **sí admiten pegado a tamaño (M₁,M₂,M₃)=(2,2,2)**.

Tomar λ₁=−1, λ₁₂=λ₁₃=1 y las demás intensidades cero. Aunque una intensidad es negativa, el generador finito tiene tasas por vector q₁=0, q₂=q₃=q₁₂=q₁₃=1/4 y q₂₃=q₁₂₃=0. Es Markov e irreducible. Sus pares 12 y 13 son reinicios conjuntos de tasa 1; el par 23 tiene reinicios individuales de tasa 1. Al ampliar los dos últimos bloques a tamaño 4, el salto puro del primer bloque adquiere tasa −1/2+1/8+1/8=−1/4.

Este ejemplo **no refuta** el informe: refuerza la importancia de su hipótesis universal y su advertencia expresa sobre modelos fuera del contrato. El verificador independiente construye las matrices completas de ambos tamaños y comprueba directamente estos hechos. No debe resumirse la obstrucción como imposibilidad absoluta de acoplar tres procesos.

## 4. Testigo P/Q y observaciones

La construcción matricial directa reproduce las tasas binarias publicadas. En ambos modelos los tres generadores de pares tienen reinicios individuales y común de tasa 1/2. Esto implica igualdad de cada ley de trayectoria marginal, para igual ley inicial del par: la proyección es Markov porque las sumas por fibra no dependen del estado oculto. No implica igualdad de los tres registros considerados conjuntamente, ni igualdad condicionada a la trayectoria del tercer bloque.

El triple carácter tiene tasas 3/2 y 2. La estacionaria uniforme producto se verifica por simetría de matrices y es única por conectividad. Todos los bloques tienen marginal c_i=1, luego el gap es 1. El observador de saltos visibles triples tiene tasa tΠ_i(1−1/M_i), que en el caso binario vale 0 y 1/16. Eventos simultáneos de relojes distintos no aportan término lineal en dt.

La frase operacional «no reiniciar tres bloques simultáneamente» es un supuesto adicional de la representación de relojes; no se deduce de la simetría ni del gap. El informe lo presenta correctamente así.

## 5. Código, comandos y cobertura

Comandos ejecutados sin instalaciones ni red:

- python verify_multiblock.py → PASS, 95.790 aserciones.
- python audit/verify_independent.py → PASS, 9.617 aserciones.

La implementación independiente usa solo biblioteca estándar y Fraction. No importa el código del autor. Enumera resultados concretos de cada reinicio, incluyendo resultados sin cambio, y forma matrices completas con su diagonal. Comprueba sumas de fila cero, tasas fuera de diagonal no negativas, simetría, conectividad y acción espectral en todas las filas. Invierte por eliminación gaussiana racional para k=1,…,4; examina P/Q en los ocho vectores de tamaños 2/4; verifica los tres cocientes marginales y los 27 productos de funcionales no nulas F₂²→F₂ para cada modelo, además de 3.645 datos de compatibilidad y los controles degenerados y finitos anteriores.

El código original fue leído y reproducido. Sus 23.625 casos de rejilla y conteos de mapas sobreyectivos 3, 7 y 42 son correctos para los rangos declarados. La formulación inicial de §7 decía «matrices», mientras el original calculaba núcleos de convolución; el autor ya ajustó el texto y el comentario. No era un fallo del resultado matemático. Las matrices completas sí están cubiertas en este segundo verificador.

Los conteos de aserciones son diagnósticos, no un grado de confianza ni una prueba universal. La prueba del teorema está en el argumento matemático, especialmente en el límite de dimensiones, que ninguna rejilla finita sustituye.

## 6. Brecha restante y afirmación segura

**No hay una implicación matemática pendiente en T1/T2 bajo el contrato declarado.** Permanece abierta y fuera de este corte la justificación física de la factorización marcada, los cocientes permitidos, el reloj común y los lectores calibrados. Tampoco se establece prioridad bibliográfica.

La conclusión segura es exactamente la clasificación universal, la condición de compatibilidad triple y la no identificabilidad por marginales de pares más gap. El siguiente control barato es ejecutar ambos verificadores desde el paquete final y cotejar los hashes de entrada de esta auditoría; cualquier cambio posterior del teorema o código exige nueva revisión del cambio, no reutilizar ciegamente este PASS.
