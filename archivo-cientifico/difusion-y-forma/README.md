# Mismos conteos, distinta difusión

Concordante Lab · Xorch. © 2026. Todos los derechos reservados.

## Una pregunta concreta

¿Basta conocer el tamaño, el grado y una curvatura local de un grafo para saber cómo se difunde sobre él?

Este lote presenta dos ejemplos con **4096 vértices, 12288 aristas, grado 6 y curvatura de Ollivier cero, sin permanencia (idleness 0)**: un toro triangular de dos coordenadas y un grafo cúbico periódico de tres coordenadas. A tiempo de difusión 6, sus dimensiones espectrales son aproximadamente **2.0293 y 3.0632**. La difusión distingue lo que esos observables compartidos dejan empatado. También los distingue un observable local más sencillo: **8192 triángulos frente a cero**.

## Explorar en español

Descarga [explorador.html](explorador.html) y ábrelo en un navegador. GitHub muestra el código del archivo; el botón de descarga permite abrirlo como página local. El archivo funciona solo, sin conexión, cuentas, rastreadores ni servicios externos.

1. Compara las curvas del toro triangular y el grafo cúbico.
2. Mueve el control de tiempo para observar la región intermedia y la saturación finita.
3. Activa el grafo cúbico agrupado 8³: su tiempo se divide entre cuatro para comparar la misma escala física convencional.
4. Los toros triangulados de grado 14 añaden un ejemplo genuinamente tridimensional de complejo de cliques. Se muestran como comparadores distintos del par de grado 6.

Las cinco curvas proceden de **200 tiempos históricos cada una**. El control selecciona datos tabulados; las uniones entre puntos son una guía visual.

## Documentos y evidencia

- [Comparación de geometrías](seleccion/informe.md): convenciones, prueba exacta de curvatura nula, fórmulas de Fourier, obstrucción para el selector especificado y controles de minimización.
- [Escala de difusión y toro triangulado](difusion/informe.md): errores finitos al emparejar tiempos, triángulos como discriminador, biblioteca aleatoria de 80 muestras y construcción tridimensional.
- [Verificación](VERIFICACION.md): comprobaciones ejecutadas en esta edición, evidencia histórica y procedimiento de reproducción.
- [Bibliografía](BIBLIOGRAFIA.md): precedentes clásicos y atribuciones.
- En cada subcarpeta: programa científico completo, certificado histórico saneado y tabla CSV.

Los informes técnicos completos conservan su idioma inglés; esta guía y el explorador están en español.

## Qué establece cada resultado

**Argumento exacto.** Cualquier función que dependa exclusivamente del número de vértices y aristas, los grados y las curvaturas declaradas da el mismo valor a los dos grafos emparejados. La afirmación se refiere a esa lista concreta de observables.

**Cálculo finito.** Las fórmulas de Fourier proporcionan perfiles espectrales distintos. El agrupamiento de bloques conserva cada familia de grafos; las dispersiones fina y agrupada introducen errores finitos aun usando t_agrupado = t_fino/4.

**Muestra histórica.** Se comparan dos grafos periódicos con 80 grafos regulares aleatorios de 64 vértices y semillas declaradas. La ponderación de Boltzmann corresponde a esa biblioteca finita, con un peso previo 80:2 por multiplicidad de muestras. Una biblioteca finita tiene función de partición analítica.

**Construcción topológica.** El toro triangulado periódico de lado 5 tiene vector de caras (125,875,1500,750), números de Betti sobre F₂ (1,3,3,1) y grado 14. Su identificación con el toro tridimensional utiliza la subdivisión explícita de cubos y los enlaces de vértices, además de la homología.

## Preguntas siguientes

Fijar una clase admisible de grafos, una medida previa y una acción con escala declarada; estudiar familias de tamaño creciente; distinguir dimensión espectral, topología, curvatura y motivos locales; comparar observables independientes de los utilizados para ajustar la acción. Una interpretación física requiere añadir y justificar esas hipótesis.

Este es un lote acotado del archivo científico. Los estudios históricos anteriores de dimensión, observadores y entropía permanecen pendientes de incorporación completa.
