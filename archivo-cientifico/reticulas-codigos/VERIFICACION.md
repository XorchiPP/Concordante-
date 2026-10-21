# Verificación del paquete

## Evidencia incluida

El informe aporta las demostraciones generales. El programa verifica exactamente el censo por fórmulas, las cotas de supervivientes, los primeros primos que evitan la obstrucción numérica y 17459 asignaciones pequeñas de residuos. Los primos grandes del ejemplo son 97 y 149; evitar el filtro constituye una condición necesaria, no una certificación de mínimo de un vecino concreto.

El certificado histórico es una **proyección editorial de cuatro campos del certificado original**, conservados exactamente. Las secciones de Barnes–Wall y masa de códigos del original quedan fuera de este paquete y siguen conservadas en el archivo histórico. El certificado reproducido coincide exactamente con esa proyección.

## Revisión del código y reproducción

El código usa únicamente itertools, math y json de Python. Las cinco funciones universal_shell, mandatory_survivors, is_prime, first_unobstructed_prime y exhaustive_pigeonhole_small mantienen el mismo árbol sintáctico que el original. El programa principal está restringido al alcance de este paquete. Solo escribe el resultado en la salida estándar; la redirección del comando crea el archivo elegido por el lector. El comparador lee dos JSON y exige igualdad exacta.

Se inspeccionó el código antes de ejecutarlo: sin red, instalación, procesos secundarios ni dependencias externas. La reproducción local del 21 de octubre de 2026 terminó con código de salida cero. Los certificados histórico y reproducido coinciden byte por byte. El control aritmético utiliza enteros, sin tolerancias numéricas.

## Delimitación de la evidencia

- La prueba de la obstrucción por palomar vale para todo primo impar bajo el contrato del informe. Las enumeraciones pequeñas son controles de implementación, no una sustitución de esa prueba.
- La función mandatory_survivors presupone p primo impar; su aserción interna comprueba imparidad y tamaño, pero no primalidad. Los usos publicados son exclusivamente p=3,5,7. La función is_prime sirve para la búsqueda acotada de 97 y 149; utiliza una raíz de punto flotante en el límite del bucle y no se ofrece como prueba de primalidad de enteros arbitrariamente grandes.
- Los censos ilustrativos con datos Golay/Reed–Muller son sustituciones exactas de valores históricos, sin nueva enumeración de esos códigos.
- Los resultados generales de índices y mínimos son demostraciones escritas. La construcción de matrices Gram y certificación completa de mínimos en dimensiones 48, 72 o mayores corresponden a expedientes específicos pendientes de incorporar.
- La revisión por lectura y la reproducción son controles internos diferenciados de la evaluación externa de una revista o una búsqueda exhaustiva de antecedentes.

## Revisión separada por lectura

Una segunda revisión interna contrastó informe, funciones, proyección histórica y fuente bibliográfica. El dictamen fue favorable tras precisar en la aplicación del filtro que bloquear G1 exige **t>4 y p impar**. La revisión confirmó las cinco funciones sin cambios de algoritmo y la coincidencia de los cuatro campos del certificado; no repitió la ejecución del programa.
