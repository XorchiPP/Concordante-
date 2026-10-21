# Relaciones de compatibilidad y geometría de grafos

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

A partir de una relación binaria simétrica se construyen distancia de caminos, simetrías, complejos de cliques y operadores de difusión y evolución unitaria. Este lote reúne las definiciones, pruebas y ejemplos finitos, junto con las hipótesis necesarias para añadir transporte y seleccionar una dinámica.

## Recorrido de lectura

1. [Informe completo](relaciones_y_geometria.md): axioma mínimo, construcción, ejemplos, holonomía y tres obstrucciones de selección.
2. `verificar_geometria_relacional.py`: reconstrucción de entradas, homología F₂, perfiles de bolas, verificaciones numéricas de operadores y ejemplo de Hamiltonianos.
3. `certificado_historico.json` y `certificado_reproducido.json`: edición pública del resultado histórico y resultado de esta reproducción del 21 de octubre de 2026. El saneamiento del histórico adapta solo las etiquetas de alcance; sus cifras se conservan y el original permanece intacto en la trazabilidad.
4. [Revisión de cálculos y alcance](VERIFICACION.md) y [bibliografía](BIBLIOGRAFIA.md).

## Ejemplos reproducidos

| Ejemplo | Vértices | Aristas | Triángulos | Betti sobre F₂ | Clases planas U(1), usando su H₁ integral |
|---|---:|---:|---:|---|---|
| Ciclo de longitud 11 | 11 | 11 | 0 | (1,1,0) | U(1) |
| Toro triangulado periódico | 121 | 363 | 242 | (1,2,1) | U(1)² |

En el toro, los rangos de los bordes sobre F₂ son 120 y 241. Las bolas de radios 0 a 4 contienen 1, 7, 19, 37 y 61 vértices. En el ciclo contienen 1, 3, 5, 7 y 9. El programa también contrasta perfiles a escalas 5 y 10 en las familias de tamaño 101.

La clasificación del transporte plano combina la construcción topológica del ciclo/toro con el teorema clásico de holonomía. El código computa F₂; la ausencia de torsión integral procede de la identificación de esos espacios como S¹ y T². Para otros complejos, el paso a U(1) requiere estudiar H₁ integral y sus posibles factores de torsión.

## Tres niveles de evidencia

- **Pruebas matemáticas:** bajo grafo finito conexo, distancia e isometrías, energía del laplaciano, difusión y unitariedad; selección condicionada de fases, orientación y Hamiltoniano.
- **Cálculos exactos finitos:** conteos de cliques, rangos por eliminación sobre F₂, perfiles de bolas y permutaciones de simetría.
- **Cálculos numéricos:** espectro, exponenciales y probabilidades con NumPy. Las tolerancias del programa son 3×10⁻¹¹ para difusión/unitariedad y 10⁻¹¹ para el control espectral del ciclo. Las últimas cifras dependen del entorno.

Las coordenadas modulares generan la entrada del toro; los invariantes se miden después desde la adyacencia. La relación concreta C sigue siendo un dato del modelo. La selección de C, escala temporal, Hamiltoniano y transporte físico son los siguientes problemas explícitos del informe. Los perfiles dimensionales se refieren a escalas o familias crecientes; en un grafo finito fijo, el crecimiento termina saturándose.

## Reproducción computacional

Entorno utilizado: Python 3.12.14, NumPy 2.3.5, previamente instalados. El programa genera sus entradas y escribe JSON en stdout; funciona sin descargar datos ni llamar a servicios externos.

```sh
sha256sum -c SHA256SUMS.txt
python3 verificar_geometria_relacional.py > nueva_salida.json
python3 comparar_resultados.py nueva_salida.json
```

Ejecutar Python con comprobaciones `assert` activas, sin la opción `-O`. El comparador exige igualdad de los campos discretos y tolerancia absoluta 3×10⁻¹¹ en los flotantes. Esta tolerancia de comparación editorial complementa las comprobaciones científicas contenidas en el propio verificador.

## Estado de edición

Se conserva el informe matemático completo con nomenclatura pública, referencias y precisión sobre el cambio de coeficientes. El cálculo procede de una implementación interna y se revisa mediante lectura separada de código y demostraciones. La bibliografía sitúa las construcciones en matemáticas clásicas. El resto del archivo de fundamentos queda para entregas posteriores.

Marca de presentación: Concordante Lab · Xorch. Derechos conservados, sin nueva licencia ni reasignación de titularidad. Los autores de las referencias externas mantienen sus atribuciones; se enlazan sus publicaciones.
