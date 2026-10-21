# Preguntas abiertas de los modelos

Concordante Lab · Xorch · Corte: 21 de octubre de 2026.

Esta lista se limita a modelos de redes, discretización gauge, selección del acoplamiento y alcance gravitatorio. Cada pregunta tiene un obstáculo concreto y un criterio de cierre. Es una selección temática del archivo de preguntas abiertas.

## 1. ¿Qué datos identifican la red, no solo su respuesta?

**Resultado negativo cerrado:** las dos realizaciones de [redes de frontera](../modelos-fisicos/redes-frontera/REPORT.md) tienen respuesta dinámica idéntica, sin modos interiores oscuros, pero no son isomorfas. Más frecuencias del mismo lector no distinguen este par.

**Resultado positivo condicionado ya cerrado:** [las preparaciones nodales identifican la red](../redes-observables/REPORT.md): para n≥1 nodos interiores conocidos y etiquetados, n−1 preparaciones nodales bastan; la cota es óptima en el peor caso. El contrato exige capacidades positivas conocidas y comunes, observabilidad interior completa, respuesta Λ(s) completa, corrientes temporales completas tras las preparaciones y el mismo reloj y unidades. Esa suficiencia constituye un resultado establecido bajo el contrato indicado.

**Preguntas abiertas fuera de ese resultado:** estabilidad frente a ruido o muestreo finito, disponibilidad física de las preparaciones e identificación bajo contratos con información o acceso restringidos.

**Cierre exigido:** cotas de estabilidad y algoritmos bajo el nuevo contrato, con hipótesis de precisión y acceso explícitas, o contraejemplos que delimiten su alcance. Añadir el nodo 2 distingue el par del paquete de frontera; esa observación aislada no sustituye al teorema general de preparaciones nodales ni demuestra estabilidad experimental.

## 2. ¿Qué explica cuantitativamente el residual no abeliano?

**Cálculo documentado:** el [predictor aditivo](../modelos-fisicos/predictor-curvatura-residual.md) tiene coseno dual superior a 0.996, pero su magnitud es aproximadamente 11.7% de la del residual. Tras restarlo permanece aproximadamente 88.3% de la norma. La explicación de amplitud y causalidad permanece pendiente.

**Pregunta abierta:** obtener un predictor gauge-covariante a amplitud finita que incluya holonomías, BCH y transportes compatibles, sin ajuste escalar retrospectivo.

**Cierre exigido:** comparación componente a componente, en idéntica base y norma dual, con código, arrays, control de gauge y cotas de error. La disección cúbica en un campo y malla concretos no demuestra un factor universal de tres.

## 3. ¿Convergen las variaciones y las soluciones, además de la acción?

**Obstáculo:** S_h(a)=S(a)+h² sin²(a/h²) tiene error de acción O(h²), mientras que su derivada añade sin(2a/h²), de orden O(1). Este ejemplo analítico basta para mostrar que convergencia de valores no implica convergencia de derivadas.

**Pregunta abierta:** demostrar consistencia variacional uniforme, estabilidad y convergencia de una familia lorentziana 3+1; controlar también condiciones de frontera, restricciones y soluciones acopladas Einstein–Yang–Mills.

**Cierre exigido:** hipótesis de regularidad y forma de malla explícitas, norma adecuada, cotas uniformes y controles independientes. Una raíz de un sistema finito no certifica el límite continuo; el ensayo documental publicado no es una raíz acoplada.

## 4. ¿Puede seleccionarse el acoplamiento electromagnético sin ajuste?

**Resultado condicionado:** con β libre y la asintótica declarada, [α_h≈1/(4πβ)](../modelos-fisicos/acoplamiento-electromagnetico.md) no selecciona una constante positiva única.

**Pregunta abierta:** regla ultravioleta autónoma, materia dinámica, observable renormalizado y extrapolación controlada.

**Cierre exigido:** predicción independiente sin introducir el valor experimental en la selección de parámetros. La no selección en este esquema no excluye otros mecanismos.

## 5. ¿Qué conecta estos objetos con la física observada?

**Estado:** la conexión entre redes y gravedad es una línea abierta. Los resultados actuales aportan modelos formales y reproducciones de soluciones clásicas; una ley nueva requiere una predicción discriminante y contraste independiente.

**Pregunta abierta:** construir el mapa entre los objetos matemáticos, una dinámica seleccionada y observables calibrados, recuperar el régimen conocido y obtener una predicción discriminante.

**Cierre exigido:** especificar unidades, condiciones iniciales y medición; recuperar resultados conocidos con error controlado; fijar antes del contraste una predicción nueva y evaluarla con datos independientes. La eventual validación o falsación pertenece a ese contrato experimental, no al PASS de una matriz finita.

## Estado de la evidencia

Los testigos de redes incluyen pruebas, código y salidas reproducidos en este corte. La nota de residual conserva derivaciones y cifras de un informe previo; no incluye aún su expediente computacional completo. La nota de acoplamiento presenta una inferencia condicionada. Las preguntas conservan los estados y criterios de cierre aquí descritos.

© 2026 Xorch — Concordante Lab. Derechos reservados.
