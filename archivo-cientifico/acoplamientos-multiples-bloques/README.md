# Acoplamientos de múltiples bloques

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Edición pública del 21 de octubre de 2026 de un informe y auditoría del 16 de octubre de 2026. El resultado histórico se conserva bajo su contrato y con su fecha de origen.

## Alcance

Para un número fijo finito k≥1 de bloques binarios etiquetados, dimensiones positivas sin cota superior, convolución, invariancia por GL separado, todos los cocientes lineales separados y reloj común, la clasificación universal es una suma única de reinicios uniformes de subconjuntos con intensidades λ_S≥0. No se exige coherencia cuando cambia k.

La no negatividad de las intensidades de reinicio se deduce del contrato universal: a un tamaño finito basta que las tasas de salto resultantes sean no negativas, incluso si algunos λ_S son negativos. En ese caso no se interpretan esos coeficientes como relojes de Poisson independientes positivos.

Para tres bloques, el informe da el intervalo exacto de compatibilidad de tres procesos marginales de pares. Tres pares admisibles individualmente pueden ser incompatibles universalmente aunque sí se acoplen al tamaño binario. Dos familias universales pueden compartir cada proceso marginal de pares completo, su estacionaria y brecha espectral, y diferir en el modo triple. Igualdad de cada marginal requiere iguales leyes iniciales de ese par: no implica igualdad de todos los registros de pares considerados conjuntamente o condicionados al tercer bloque.

Con intensidades universales no negativas y todas las intensidades marginales c_i>0, el sistema es irreducible y la brecha es min_i c_i. Si algún c_i=0, el bloque queda inmóvil; no se describe un menor autovalor positivo como brecha ergódica. La clasificación determina los coeficientes de cada generador. La selección física de valores, bloques, reloj, acceso a cocientes y lectores calibrados permanece como problema adicional.

## Pruebas y reproducción

REPORT.md contiene las pruebas autocontenidas de Fourier finito e inversión booleana y los contraejemplos. audit/AUDIT.md conserva la revisión algebraica histórica y los límites. La revisión disponible es interna al proyecto; la evaluación de prioridad, la revisión bibliográfica exhaustiva y el arbitraje de revista son pasos editoriales posteriores.

Python 3.12.14 y biblioteca estándar. Sin instalaciones, red ni cuentas. Desde esta carpeta:

    sha256sum -c SHA256SUMS.txt
    python verify_multiblock.py
    python audit/verify_independent.py

Los programas escriben sus certificados en las respectivas carpetas. Se incluyen salidas stdout/stderr de la reproducción de esta edición. El principal usa núcleos de convolución y prueba 95.790 aserciones. El independiente construye matrices completas de reinicio, invierte por eliminación racional y prueba 9.617 aserciones, incluidos 54 cocientes simultáneos y 3.645 casos de compatibilidad. La rejilla principal contiene 23.625 casos. Los certificados detallan rangos finitos; ningún conteo sustituye el argumento universal de dimensiones sin cota.

Ambos códigos se conservan idénticos a los originales. La edición documental cambia los hashes que el certificado independiente registra. Repetir código no se cuenta como una demostración independiente adicional.

## Fuentes y derechos

Fuentes originales, antecedentes propios del proyecto, revisión histórica y correspondencias permanecen íntegros en custodia privada y pendientes de preparación separada. Aquí se incluyen completos los argumentos y programas necesarios para reproducir este resultado. El paquete se limita a los argumentos y materiales propios identificados en el manifiesto.

RIGHTS.md mantiene la reserva de derechos, sin licencia nueva ni transferencia de titularidad. La presentación por marca y alias no cambia la identificación original preservada privadamente. Una revista elegida no es requisito universal para preparar este recurso; se revisarán conflictos concretos de embargo, anonimato o publicación previa, sin garantizar compatibilidad universal.
