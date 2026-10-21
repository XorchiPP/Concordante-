# Verificación computacional y alcance matemático

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

## Fuentes y reproducción

El informe, programa y certificado originales coinciden con las tres sumas SHA-256 registradas en su entrega del 21 de octubre de 2026. La edición de código conserva el árbol sintáctico de las operaciones matemáticas: cambios limitados a cabecera, marca y texto de alcance. Los certificados públicos adaptan ese mismo texto de alcance.

Se ejecutó el programa con Python 3.12.14 y NumPy 2.3.5. Terminó correctamente. Todos los campos discretos coinciden con la fuente; la diferencia absoluta máxima entre flotantes fue 1,66×10⁻²¹, dentro de las tolerancias explícitas. El código se leyó antes de ejecutarse: solo construye datos finitos, usa NumPy y escribe stdout.

## Qué comprueba cada parte

- Construcción por adyacencia: aristas, triángulos y ausencia de cliques de cuatro vértices en los ejemplos.
- Eliminación binaria exacta: rangos de ∂₁ y ∂₂ y Betti sobre F₂. La fórmula de b₂ usa expresamente que C₃=0.
- Distancia combinatoria: tamaños de bolas en los radios declarados y comprobación de las fórmulas en escalas 5, 10 y 20 de las familias de tamaño 101.
- Simetría: las permutaciones propuestas preservan la adyacencia e invierten la arista testigo.
- Operadores numéricos: positividad del laplaciano dentro de tolerancia, conservación de sumas, entradas de difusión y unitariedad; contraste del espectro conocido del ciclo.
- Selección dinámica: dos Hamiltonianos autoadjuntos construidos del mismo camino irregular producen probabilidades diferentes.

## Pruebas e hipótesis complementarias

El informe demuestra la construcción métrica, la equivalencia entre automorfismos e isometrías y las identidades del laplaciano. Expone además las obstrucciones de selección y el ejemplo de holonomías diferentes con la misma relación. La clasificación U(1) combina el teorema de holonomía con H₁ integral: la identificación del ciclo/toro justifica los rangos libres 1 y 2. El cálculo F₂ aporta sus propios invariantes y no decide por sí solo la torsión integral de un espacio general.

La implementación, sus tolerancias y sus entradas quedan disponibles para reproducción. La interpretación como modelo físico añade reglas de selección, unidades y contraste empírico, indicados como siguientes problemas del informe.

## Revisión matemática separada

La revisión de lectura aprobó el lote tras precisar la distancia extendida entre componentes, el alcance de la obstrucción de orientación de aristas, la identificación integral del toro y la diferencia entre elección convencional de fases y selección física. Cotejó informe, programa y certificados; los cálculos fueron ejecutados por la preparación y la revisión se realizó separadamente por lectura.
