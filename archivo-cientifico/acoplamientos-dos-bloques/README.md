# Acoplamientos proyectivos por dos bloques

Concordante Lab · © 2026. Todos los derechos reservados.

Edición pública del 21 de octubre de 2026 de un resultado y auditoría fechados el 16 de octubre. El objeto es el acoplamiento proyectivo de dos bloques.

## Resultado y límites

Bajo convolución, simetría GL(n,2)×GL(m,2), bloques previamente fijados, dimensiones n,m≥1 y marginales de reinicio uniforme con intensidades c,d≥0, los generadores se parametrizan por θ. El intervalo finito es 0≤θ≤min(cN/(N−1),dM/(M−1)), con M=2ⁿ y N=2ᵐ. Para familias coherentes bajo todos los cocientes lineales separados y con reloj común, en dimensiones positivas sin cota, queda 0≤θ≤min(c,d).

REPORT.md contiene las pruebas condicionadas, la excepción de irreducibilidad y un contraejemplo finito no extensible. independent_audit/AUDIT.md contiene una revisión algebraica independiente histórica. Las ejecuciones exactas corroboran los casos enumerados y la prueba algebraica establece el resultado universal bajo su contrato. La selección física de θ, de la factorización y del reloj permanece abierta; la prioridad bibliográfica requiere revisión especializada.

## Reproducir

Python 3.12.14 y biblioteca estándar. Sin paquetes externos ni red. Desde esta carpeta:

    python verify_coupling.py
    python independent_audit/audit_block_couplings.py

Cada programa escribe su certificado JSON en su propia carpeta y lo imprime. El primero verifica 10.919 aserciones; el segundo 7.146.584. Véanse los certificados para rejillas y rangos exactos. Los archivos stdout y stderr adjuntos son las salidas de la nueva ejecución. Antes de reproducir: sha256sum -c SHA256SUMS.txt. Si cambia un archivo, regenerar el manifiesto del nuevo corte, no fingir que conserva los hashes anteriores.

El verificador principal usa tasas racionales parametrizadas por c,d,θ. El segundo construye directamente tasas α,β,γ y calcula conectividad y espectro sin importar el principal. La reproducción comprueba la ejecución de ambas implementaciones.

## Fuentes, edición y derechos

Las demostraciones son autocontenidas y no necesitan asumir resultados de los antecedentes privados. El expediente contiene argumentos propios; la revisión exhaustiva de literatura queda pendiente. Los antecedentes, la identificación original de autoría, las versiones y sus hashes permanecen en custodia privada; quedan pendientes de preparación separada, no eliminados del archivo científico.

Esta edición retira etiquetas internas, referencias privadas y datos personales, conserva los argumentos matemáticos y generaliza el identificador del certificado. Las fórmulas del código se conservan. La auditoría incluida es una revisión algebraica histórica dentro del proyecto.

RIGHTS.md conserva la reserva de derechos sin conceder licencia nueva ni transferir titularidad. La divulgación de resultados y código puede ser compatible con artículos posteriores: se reserva material cuando exista conflicto editorial concreto o ambigüedad relevante, sin exigir revista elegida para preparar este recurso y sin garantizar compatibilidad universal.

## Condiciones del resultado

θ se identifica de forma única para cada generador, pero las hipótesis no seleccionan un único θ entre los admisibles. A tamaño finito, c−θ o d−θ pueden ser negativos mientras el generador total sigue siendo Markov: en ese caso los sumandos no son tres relojes de Poisson con intensidades no negativas. Con c,d>0, la única excepción de irreducibilidad dentro del intervalo finito es n=m=1, c=d, θ=2c. La brecha min(c,d) se afirma para la familia universal, no para cualquier exceso finito. La distribución estacionaria uniforme no identifica θ. Quedan fuera dimensiones cero, cocientes que mezclen bloques, más de dos bloques y cualquier deducción física.
