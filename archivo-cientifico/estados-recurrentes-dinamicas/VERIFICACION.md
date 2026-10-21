# Verificación del ejemplo de dos puertos

## Evidencia exacta reproducida

El 21 de octubre de 2026 se ejecutaron las fuentes revisadas con Python 3.12.14, SymPy 1.14.0 y g++ disponible, compilación C++17 con -O2. Los procesos tuvieron límite de 60 segundos cada uno y finalizaron correctamente sin instalaciones, red ni servicios externos.

- 104 comprobaciones simbólicas: matrices, forma de Smith, índices rectangulares de subgrupos, períodos, 16 variantes de paridad y testigo de disipación.
- Censo FIFO: 1.048.576 membresías de cuatro espacios estables de 4^9 estados, más 16.384 estados del núcleo. En cada variante 167.040 recurrentes y cero discrepancias frente al producto SCC.
- Censo por lotes: reconstrucción separada de grafos, scripts duplicados y orden inverso de disparo;1.048.576 membresías.
- Censo de órbitas: recorre todos los ciclos de cada adición marcada y todas las órbitas conjuntas de las cuatro variantes.

Los dos bitsets tienen 131.072 bytes y son idénticos entre sí y al SHA256 histórico:

d9f36fb21df7aa427e04bfeba4cf67097093d1a9767f3a8007f211ccf9e4b4ce

El certificado simbólico coincide exactamente como objeto JSON con la copia histórica normalizada editorialmente incluida aquí; las matrices coinciden byte por byte. Respecto del JSON original, se cambió el identificador id y se sustituyó la descripción nonclaim por scope, sin modificar datos matemáticos. También se adaptaron nombres de archivos. Los algoritmos y datos matemáticos permanecen idénticos. Los originales permanecen intactos en custodia.

## Formato de membresía

Cada archivo contiene cuatro bloques de 32.768 bytes, en orden SP,SQ,RP,RQ: estricto saliente, estricto entrante, relajado saliente, relajado entrante. El estado se codifica en base 4 por alturas h_i: code=Σh_i·4^i. Su pertenencia está en el bit (code mod8) del byte floor(code/8) del bloque. Todos los bloques coinciden, lo que certifica igualdad bajo etiquetas fijas, no solo igualdad de cardinalidades. El comparador también comprueba la recurrencia del testigo code 855.

## Contratos y alcance

El teorema de producto recurrente usa componentes fuertemente conexas con sumidero accesible y presupuesto de arcos no negativo. Los puertos no tienen arcos entre sí. Las fórmulas de períodos y órbitas usan las adiciones específicas en vértices 0 y 8 y sus clases enteras de acoplamiento al núcleo.

La transitividad de dos adiciones corresponde a RP, el contrato relajado saliente. Las 16 variantes del argumento de paridad pertenecen a la subfamilia estricta expresamente definida. La clasificación de redes con otros presupuestos y otras interfaces permanece abierta como continuación.

Los censos son dos implementaciones distintas y una exploración dinámica adicional dentro del mismo trabajo interno. Comparten el problema matemático y sus reglas declaradas. La revisión bibliográfica y la segunda lectura se distinguen de la ejecución computacional y de una evaluación editorial externa.

## Revisión separada por lectura

El dictamen de una segunda revisión interna fue favorable. Cotejó las 14 funciones auxiliares Python por árbol sintáctico y los tres programas C++ por normalización de cambios editoriales; verificó los hashes de bitsets y la igualdad JSON declarada, sin reejecutar ciencia. Se explicitó el paso de la acción libre y transitiva del grupo crítico al conteo de órbitas, y se aclaró la normalización editorial del certificado histórico.
