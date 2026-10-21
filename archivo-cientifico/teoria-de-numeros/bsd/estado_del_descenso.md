# Descenso 3-Selmer y verificación de evidencia

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

## Alcance

Esta línea estudia un procedimiento de descenso y validación para la curva elíptica de coeficientes de Weierstrass [0, 1, 1, −7109, −233093], identificada como 55297189.a1. No presenta una demostración de la conjetura de Birch y Swinnerton-Dyer.

## Resultados documentados

La auditoría aritmética estática registra comprobaciones exactas de primalidad de N=55297189, discriminante, pertenencia a la curva de los puntos declarados, singularidad nodal y constantes de un carácter local. Estas comprobaciones no calculan un grupo de Selmer, una cubierta ni un emparejamiento Cassels–Tate.

Se documentan un parser con cinco pruebas aprobadas y un contrato estricto de evidencia con catorce pruebas aprobadas. El contrato rechaza campos adicionales, residuos no normalizados, bases dependientes, hashes discordantes y escalares sin una ejecución validada previa. Son resultados de validación de software reportados por las fuentes, no una prueba matemática de corrección universal del programa. No se reejecutaron en esta revisión documental.

## Predicciones, no resultados algebraicos

La fuente de calibración citada en el expediente es el registro LMFDB de la curva: https://www.lmfdb.org/EllipticCurve/Q/55297189/a/1 . El expediente del 27 de septiembre de 2026 recoge rango 2 y un orden analítico de Sha igual a 9. Esa cantidad analítica no constituye una determinación algebraica de Sha.

Las predicciones congeladas son dimensión 4 y orden 81 del 3-Selmer, dimensión 2 del cociente por la imagen de Mordell–Weil y un escalar Cassels–Tate no nulo en F_3. La última predicción utiliza además la no degeneración bajo la hipótesis de finitud pertinente. Ninguna debe presentarse como un resultado computado.

## Frontera abierta

No se ha localizado stdout completo validado, handoff autenticado ni escalar Cassels–Tate calculado. Un registro de envío del 13 de octubre de 2026 no contiene salida observada y no acredita terminación, éxito ni timeout. La siguiente puerta científica sigue siendo una ejecución válida, conservación de salida y hashes, validación del handoff y posterior evaluación Fisher–Newton. Incluso un escalar terminal aislado no resolvería BSD.

Este resumen se basa en lectura documental del 21 de octubre de 2026; no ejecuta Magma, no renueva cálculos científicos y no certifica exhaustividad de archivos inaccesibles.
