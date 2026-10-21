# Auditoría independiente: marcas interiores

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Auditoría original: 16 de octubre de 2026. Edición pública: 21 de octubre de 2026. Objeto: REPORT.md y verify_marks.py del paquete padre. El certificado regenerado identifica por SHA-256 los derivados ejecutados; la revisión algebraica es histórica, y sus originales quedan preservados en el registro privado.

## Afirmación normalizada y veredicto

**Veredicto principal: proved as written (demostrado tal como está escrito).**

En redes finitas conexas sobre el mismo conjunto etiquetado B ⊔ I, frontera no vacía, capacidades diagonales positivas conocidas e iguales, y realización interior observable, la igualdad de la transferencia completa Λ(s), s>0, y de respuestas temporales completas a preparaciones físicas conocidas P equivale a una única congruencia interior por una isometría de capacidad S que fija 1 y P, sujeta a admisibilidad del Laplaciano resultante. n−1 preparaciones nodales identifican L. Para cada n≥2 y cada subconjunto de hasta n−2 marcas existe una pareja completa, positiva y observable que esas marcas no separan, ni siquiera abriéndolas como frontera.

El veredicto cubre los teoremas algebraicos, la reconstrucción exacta y el testigo. La prioridad bibliográfica, la exhaustividad de búsquedas externas, la robustez experimental y la interpretación gravitatoria quedan fuera del alcance de esta revisión algebraica. La revisión se realizó separadamente: primero se derivaron las implicaciones desde el informe; el programa independiente no importa código ni certificados del autor. Esta separación reduce errores de implementación compartidos, pero no constituye por sí sola una prueba de corrección.

## 1. Grafo de dependencias

1. Conexión y B no vacío → D positivo definido. Prueba elemental: extender un vector interior por ceros en B; energía nula obliga a ser constante en toda la red y por tanto cero.
2. Capacidad diagonal positiva → normalización H=M_I^(-1/2) D M_I^(-1/2), G=C M_I^(-1/2), v=M_I^(1/2)1.
3. Igualdad de Λ → igualdad de L_BB y de todos los momentos GH^rGᵀ, por expansión convergente a frecuencia grande.
4. Igualdad de momentos + observabilidad → única isometría U entre generadores de Krylov, con H U=U H̃ y G U=G̃.
5. Conservación + invertibilidad H → Uv=v.
6. Igualdad de respuestas preparadas + observabilidad → U M_I^(1/2)P=M_I^(1/2)P.
7. Desnormalización → clasificación por S; cancelación exacta del resolvente → recíproco.
8. Span{1,P}=R^n → S=I; conservación permite además reconstrucción explícita.
9. Base completa positiva + reflexión fijando marcas + perturbación diagonal simple → parejas admisibles, distintas y observables para todo n≥2.
10. Testigo K5 → especialización racional controlada por dos implementaciones.

Las hojas 1–9 son argumentos internos de álgebra lineal real finita; no dependen de una cita externa de teoría de realización. El punto 10 ofrece evidencia de implementación y un ejemplo concreto, no una inducción sobre n.

## 2. Derivación independiente de la implicación central

La expansión en 1/s permite leer todos los productos internos de vectores H^kGᵀa. Por tanto el envío H̃^kG̃ᵀa ↦ H^kGᵀa preserva el cuadrado de la norma de cualquier combinación lineal finita. Si una combinación representa cero, su imagen también tiene norma cero: ésta es la obligación de buena definición, y está satisfecha. La observabilidad hace que ambos spans sean todo R^n, de modo que U es ortogonal y único. Desplazar k por uno demuestra el entrelazamiento sin elegir eigenvectores ni requerir espectro simple.

De Hv=−Gᵀ1_B y H̃v=−G̃ᵀ1_B se deduce H(Uv−v)=0. D positivo definido elimina el núcleo, luego Uv=v. En la respuesta preparada, la diferencia equivale a G exp(−tH)(UZ−Z). Derivadas en t=0 anulan G H^k(UZ−Z); observabilidad obliga a UZ=Z. Al conjugar por M_I^(1/2), esto da exactamente SᵀM_I S=M_I, S1=1 y SP=P. No se requiere positividad de S: se requiere positividad de conductancias en la realización transformada.

Si dos S produjeran el mismo L̃, ambas tendrían el mismo entrelazador en el espacio de Krylov y coincidirían. El estabilizador algebraico es O(n−d), con d=dim span{1,P}; la clase física es un subconjunto admisible de ese estabilizador, no necesariamente un grupo. En particular O(1) todavía contiene dos elementos: d=n−1 no basta en general.

## 3. Preparar un nodo y abrirlo como frontera

Una preparación es un estado inicial, con B mantenida a cero. Abrir un nodo permite prescribir su trayectoria como entrada y medir corriente: son protocolos distintos, y la prueba no promete acceso físico a ninguno.

Para marcas nodales J, S e_j=e_j y SᵀM_I S=M_I implican e_jᵀ S=e_jᵀ, ya que M_I es diagonal y m_j>0. Por eso S no mezcla J con I\J. Reordenando los índices, la transformación total tiene forma diag(I_(B∪J),S_restante), lo que prueba rigurosamente la igualdad de transferencias sobre la frontera ampliada en la construcción inferior.

Para la suficiencia de abrir n−1 nodos puede evitarse cualquier comparación informal de protocolos: queda un solo nodo oculto. Está conectado por alguna arista a la frontera y su salida no es nula, de modo que el sistema reducido es observable. La clasificación para n=1 fuerza identidad. Esta justificación no infiere que una preparación aislada equivalga experimentalmente a acceso de frontera.

## 4. Reconstrucción y observabilidad

Con D1=−Cᵀ1_B y L_BB1_B=−C1, se obtiene Λ(s)1_B=−s C(D+sM_I)^(-1)M_I1. Así, n−1 columnas de R(s)=C(D+sM_I)^(-1)M_I más esta suma determinan la restante, con el signo del informe correcto. Como (D+sM_I)^(-1)M_I=(A+sI)^(-1), los coeficientes son (−1)^r CA^r. Rango n de O hace única la solución OA=O_+. Recuperar D=M_I A y L_BB por el límite da L completo. La extracción de coeficientes es una operación con datos exactos; no implica estabilidad numérica.

La observabilidad es esencial para preparaciones, no decorativa. Considérese B={0}, I={1,2}, M=I y

L(a)=[[2,−1,−1], [−1,1+a,−a], [−1,−a,1+a]], a>0.

Para todos los a, Λ(s)=2−2/(s+1), y la preparación e_1 produce corriente −exp(−t). Por tanto una marca, que es n−1, no identifica a sin observabilidad. La matriz interior tiene eigenvalores 1 y 1+2a; a=1 y a=2 no están relacionados por isometría interior. Son redes completas positivas. La frontera ampliada {0,1} sí los distingue. Este ejemplo no contradice el contrato: su observabilidad tiene rango 1, no 2. Está comprobado racionalmente por el verificador independiente.

## 5. Universalidad y cota inferior

La familia inferior funciona para cada n≥2 y para cualquier elección de J con |J|≤n−2. Existen siempre dos interiores sin marcar. Su reflexión fija todas las marcas, es isometría y preserva la base L0. La perturbación sólo usa aristas desde frontera 0; la fila de la otra frontera permanece proporcional a vᵀ y da el control de observabilidad.

Si un eigenvector de Hε fuera invisible, sería perpendicular a v. Entonces también sería eigenvector de la diagonal αI+ε diag(t_i), cuyas entradas son distintas para cualquier ε>0. Sólo podría estar soportado en una coordenada, incompatible con v_i>0. En caso de eigenvalores repetidos de Hε, cualquier subespacio propio de dimensión al menos dos tendría un vector perpendicular a v, de modo que el argumento tampoco oculta una hipótesis de simplicidad. La reflexión no diagonal no conmuta con diag(t_i); las redes resultan distintas.

La positividad se garantiza por un ε suficientemente pequeño que depende de n, capacidades, t_i y reflexión. No hay una cota numérica uniforme en n ni un margen uniforme de identificabilidad o de separación ante ruido. Para n, M y t_i fijos, incluso puede elegirse un mismo ε para todos J: hay sólo un número finito de pares a,b; basta tomar el máximo de sus K. El verificador independiente usa esta elección común en cada n ensayado. La prueba general no necesita extrapolarla desde los ensayos.

La cota cuenta nodos individualmente marcados y respuestas completas. No es una cota de muestras temporales, señales arbitrarias, precisión, coste, ni garantía de que cada red exija todas las marcas. Un protocolo adaptativo no obtiene una excepción automática: se puede mantener una misma Lε y escoger su competidora después del subconjunto final de marcas usando la elección común anterior. Ello no es un análisis de coste o estabilidad de protocolos adaptativos.

## 6. Matriz de obligaciones

| Obligación | Estado | Evidencia |
|---|---|---|
| Dominio, signos, capacidades y etiquetas | passed | Contrato y reconstrucción desde energía |
| Buena definición y unicidad de U | passed | Productos internos de todos los generadores |
| Conservación fuerza S1=1 | passed | H invertible y sumas de fila |
| Marcas fuerzan SP=P | passed | Derivadas y observabilidad |
| Grupo algebraico frente a clase física | passed | Restricción explícita a Laplacianos admisibles |
| n=1 y O(1) | passed | Cero marcas cuando n=1; reflexión residual cuando d=n−1 |
| Reconstrucción R, signo y OA=O_+ | passed | Derivación independiente anterior |
| Frontera ampliada | passed | Bloque diagonal forzado por isometría diagonal |
| Cota para todo n y J | passed | Construcción simbólica y eigenvector invisible imposible |
| Testigo K5 y cifras racionales | passed | Dos implementaciones; identidad en Q[s] independiente |
| Retirar observabilidad | failed fuera del contrato | Contrajemplo explícito a=1,2 |
| Robustez, ruido y disponibilidad experimental | out of scope | No afirmados |
| Prioridad externa y exhaustividad de búsqueda | not addressed | No son hojas de la prueba algebraica |

## 7. Comprobación de código y alcance exacto

Comandos desde el paquete:

- python3 verify_marks.py
- python3 audit/verify_independent.py

El verificador del autor usa Fraction, comprueba las identidades de isometría y congruencia, signos, rangos por menores, invariantes y controles finitos de frecuencias y momentos. La revisión del código no encontró que las muestras finitas se presenten como prueba universal. La construcción de L̃ por congruencia hace que ese control sea parcialmente por construcción; por eso el programa independiente reconstruye L desde las aristas y la reflexión desde capacidades, y comprueba además los valores racionales impresos.

El programa independiente da 97 comprobaciones y 42 instancias: todos los subconjuntos J de tamaño hasta n−2 para n=2,3,4,5, con una pareja construida por subconjunto. No enumera todas las redes. Para K5 verifica directamente identidades racionales de transferencia usando determinantes polinómicos exactos en Q[s] y multiplicación cruzada de numeradores/denominadores, tanto con B original como con B∪{2}; comprueba desigualdad al añadir también 3. La respuesta preparada se verifica del mismo modo a través de su transformada de Laplace. Esas identidades sí son funcionales para este testigo, no sólo coincidencia de muestras.

El archivo independent_certificate.json conserva conteos, alcance y hashes de las fuentes revisadas. Cambiar REPORT.md o verify_marks.py obliga a revisar los cambios y renovar los hashes; un hash distinto no invalida automáticamente las matemáticas, pero sí impide tratar esta ejecución como auditoría de la nueva revisión.

## 8. Brecha restante y conclusión segura

No se identificó una implicación faltante en las afirmaciones algebraicas bajo el contrato escrito. La conclusión segura es identificación exacta con n−1 preparaciones nodales, óptima en peor caso sobre esta clase, junto con clasificación completa de la ambigüedad observable y testigo racional de una marca insuficiente. El siguiente control barato es ejecutar ambos verificadores después de cualquier edición y confirmar que el manifiesto final incluye audit/. No se requiere otra fuente externa para cerrar esta prueba autocontenida.
