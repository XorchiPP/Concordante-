# Sistemas, memoria e información
*Jorge Rosales Pérez · Concordante*

Un sistema puede estudiarse mediante sus **estados**, las **reglas de transición** y la **información** que conserva o pierde cuando cambia.

## Estados y transiciones

Una descripción mínima puede usar un conjunto de estados \(S\), un conjunto de entradas \(U\) y una transición

\[
T:S\times U\rightarrow S.
\]

Este esquema es deliberadamente general: aparece en autómatas, control, modelos discretos y computación.

Con memoria, una evolución puede depender tanto del estado actual como de un resumen del historial. Eso genera preguntas sobre qué debe recordarse, qué puede olvidarse y cómo distinguir estados que parecen iguales pero responden distinto ante futuras entradas.

## Información relevante

Dos historias pueden considerarse equivalentes respecto a una tarea si cualquier continuación permitida produce la misma respuesta observable para ambas. La idea conecta con minimización de autómatas y nociones clásicas de equivalencia comportamental.

La pregunta principal deja de ser «¿cuántos datos tengo?» y se transforma en «¿qué datos son indispensables para distinguir futuros relevantes?».

## Auditoría y reproducibilidad

Un experimento computacional riguroso deja claros los parámetros, las semillas, el software empleado, los criterios previos de éxito y los controles negativos. Si cambia una definición durante la evaluación, debe registrarse la nueva versión.

Las pruebas en simulación son resultados sobre el modelo especificado; toda extrapolación a sistemas reales requiere evidencia adicional.

*Página educativa y de programa. No es una especificación del software privado de Concordante.*

[← Inicio](README.md) · [Método](METODO.md)

© 2026 Jorge Rosales Pérez — Concordante. Todos los derechos reservados.
