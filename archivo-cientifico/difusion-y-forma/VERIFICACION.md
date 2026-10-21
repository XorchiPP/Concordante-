# Evidencia y reproducción

Concordante Lab · Xorch. © 2026. Todos los derechos reservados.

## Fuentes y edición

Los dos informes, programas, certificados y tablas proceden del corte científico del 21 de octubre de 2026. Se conserva íntegro el contenido matemático de los informes; los preámbulos operativos y la identificación personal quedan en custodia privada. Las figuras estáticas se sustituyen en la lectura por el explorador de las mismas familias. Las referencias bibliográficas de terceros conservan su atribución.

Los certificados entregados son **ediciones públicas de resultados históricos**, con metadatos y nombres de referencias saneados. Los originales exactos, sus hashes y el mapa de equivalencias se conservan por separado. Los campos matemáticos mantienen sus valores históricos. Las tablas CSV conservan sus bytes originales.

## Comprobación actual acotada

Se inspeccionaron ambos programas, el generador original y el HTML antes de ejecutar. NumPy está disponible; NetworkX no lo está, por lo que los experimentos completos y la biblioteca aleatoria quedan documentados como ejecución histórica.

Se ejecutó `comprobar_edicion.py` con NumPy y un único hilo BLAS:

- Tres matrices laplacianas construidas por adyacencia, de 36, 125 y 125 vértices, frente a sus espectros de Fourier: errores máximos inferiores a 3.2×10⁻¹⁴.
- Las cinco series incrustadas, 1000 valores en total, frente a las fórmulas originales y sus mismos tiempos geométricos. Diferencia máxima de redondeo inferior a 5×10⁻⁸.
- Cuatro filas de emparejamiento temporal fino/agrupado.
- Coherencia de campos seleccionados del certificado y de los datos incrustados en el HTML.
- Inspección estática de peticiones de red, recursos externos, cookies y almacenamiento. El URI de espacio de nombres SVG identifica el formato, sin solicitar un recurso.

El resultado está en [comprobacion_edicion.json](comprobacion_edicion.json). La comprobación actual no recalcula la homología, los transportes lineales ni la biblioteca de 80 grafos; esos resultados están acompañados por sus programas históricos completos.

## Reproducir la edición ligera

Desde esta carpeta, con Python 3 y NumPy disponibles:

```sh
sha256sum -c SHA256SUMS.txt
python construir_explorador.py
OPENBLAS_NUM_THREADS=1 python comprobar_edicion.py
```

El constructor usa exclusivamente la plantilla y el JSON incluidos; la comprobación extrae tres funciones puras inspeccionadas del verificador de difusión sin importar ni ejecutar sus experimentos completos. Los cambios de versión numérica pueden modificar los últimos dígitos de la salida de comprobación y, por tanto, su hash; las tolerancias científicas están expresas en el programa.

## Reproducir los experimentos históricos completos

En copias de trabajo separadas de `seleccion/` y `difusion/`, ejecutar `python verificar.py` con NumPy, SciPy y NetworkX ya disponibles. El segundo programa también usa Matplotlib para crear figuras. Las copias separadas evitan sobrescribir los certificados históricos entregados. Sus salidas numéricas pueden variar en los últimos dígitos por versiones de bibliotecas o solucionadores.

El primer programa comprueba espectros, contracciones de bloques, transporte óptimo y controles pequeños de curvatura. El segundo genera la biblioteca de 80 grafos, enumera cliques, reduce fronteras sobre F₂, comprueba enlaces y resuelve siete transportes óptimos. Los espectros de las familias grandes se obtienen por fórmulas de Fourier; no se necesita diagonalizar matrices densas de 4096 vértices.

## Convenciones que acompañan la evidencia

Laplaciano combinatorio D−A, aristas sin pesos, Ollivier con ociosidad cero y medidas uniformes sobre vecinos. El tiempo físico emparejado es una convención de escala con longitud efectiva doble al agrupar. La topología tridimensional corresponde al comparador de grado 14. La obstrucción al selector usa exactamente los observables nominales del par de grado 6.

## Comprobación de interfaz

La inspección estática cubre los controles, datos incrustados y ausencia de servicios externos. Una prueba funcional adicional de JavaScript con DOM mínimo simulado comprobó cinco selectores, cuatro curvas iniciales, activación de la quinta, actualización de lecturas y ambos extremos del control sin valores inválidos. Esta prueba comprueba la lógica de interfaz, no el renderizado visual. El intento de abrir Chromium local quedó bloqueado por la política de sockets del entorno; la captura visual en navegador permanece pendiente. No se modificaron permisos ni instalaciones.

Las semillas de la biblioteca aleatoria se interpretan junto con la versión de NetworkX. Una reproducción con otra versión debe comparar los resultados y registrar la diferencia, en vez de exigir identidad binaria universal.
