# Verificación y alcance reproducible

## Entradas y procedencia

El cálculo original del 10 de octubre usa un atlas de relaciones de 388.493 bytes y un certificado anterior de 4.516 bytes. Esta edición proyecta sus únicos campos consumidos: las 759 máscaras de octadas y, del certificado, el testigo de seis máscaras y el valor 49 de la cota de peso. Los originales permanecen intactos en custodia. Los hashes embebidos en los programas corresponden a esas entradas públicas, y los certificados históricos publicados son ediciones de presentación con nombres y hashes actualizados.

El pequeño control adicional reconstruye la presentación cíclica clásica g=x¹¹+x⁹+x⁷+x⁶+x⁵+x+1, genera 4096 palabras extendidas por paridad y confirma el enumerador 1+759y⁸+2576y¹²+759y¹⁶+y²⁴. Su capa de peso ocho coincide exactamente con las máscaras de entrada. También recalcula 49 como la suma de los 24 menores pesos de firmas de cinco bits.

## Reproducción del 21 de octubre de 2026

Python 3.12.14, biblioteca estándar. Lectura de seguridad previa: los verificadores leen JSON locales y escriben únicamente sus certificados y atlas en el propio directorio. Sin acceso a red, instalación, procesos secundarios ni servicios pagos.

- Ruta principal: 125 controles aprobados. Revisa candidatos de simetría contra las 759 octadas.
- Ruta alternativa: 119 controles aprobados. Genera el código completo y verifica imágenes de una base binaria de 12 palabras.
- Certificados principal y alternativo: igualdad exacta como objetos JSON con sus versiones históricas editadas; difiere solo el orden de serialización de claves renombradas.
- Atlas de separadores: igualdad byte por byte con la edición histórica.

Las dos rutas comparten las máscaras de entrada y los representantes; son controles internos por procedimientos distintos, no fuentes de datos independientes. La tercera rutina coteja las máscaras con la presentación cíclica archivada y compara todos los resultados.

## Qué comprueban las afirmaciones

La enumeración de 82 vecinos es completa respecto a reemplazar una sola octada del testigo fijo. La lista de once triples de invariantes es exhaustiva en ese vecindario. Los triples diferentes prueban inequivalencia; los iguales requieren trabajo adicional para decidir equivalencia. Sumando los dos representantes C6 se certifican al menos trece órbitas globales.

Los valores del orden M24, su transitividad y la estructura de Conway son hechos clásicos citados. Los controles que usan esos valores comprueban consecuencias aritméticas o compatibilidades, no reconstruyen los grupos completos. La obstrucción de selección equivariante es una prueba escrita bajo esas hipótesis.

La mínima cardinalidad seis se demuestra mediante 49>40 y un testigo explícito. El paquete estudia separación de 24 puntos por octadas; los mínimos de la retícula de Leech y la clasificación global de sus marcos pertenecen a desarrollos antecedentes distintos. La conexión física requeriría un modelo adicional.

## Revisión separada por lectura

La segunda revisión interna aprobó el núcleo matemático, contrastó las funciones sin cambios algorítmicos, las proyecciones de entradas y la igualdad de resultados. Se precisaron la identificación clásica Aut(C24)=M24, la introducción de la cruz únicamente al interpretar el transporte reticular y la distinción entre verificar testigos y reproducir la exploración que los encontró. Esta revisión no volvió a ejecutar los programas.
