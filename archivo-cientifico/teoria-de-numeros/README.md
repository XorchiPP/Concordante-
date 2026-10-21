# Teoría de números: estructuras exactas y fronteras abiertas

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Edición documental y computacional acotada del 21 de octubre de 2026. **No contiene una demostración de Beal ni de Birch y Swinnerton-Dyer.** No representa todavía la totalidad del archivo de teoría de números.

## Qué se puede leer

- [Comparación aritmética](beal/comparacion_aritmetica.md): contrato de igualdad de dos construcciones, controles históricos y entradas aún ausentes.
- [Estructura ciclotómica](beal/estructura_ciclotomica.md): relaciones entre diferencias de raíces, forma simbólica, retículo de índice 11, norma y ejemplo cuadrático.
- [Fe de erratas](beal/fe_de_erratas.md): distingue el bit de signo ν del generador algebraico s. **Prevalece sobre las fórmulas con (-1)^s del informe anterior**, conservadas como historia documental, no como notación recomendada.
- [Estado del descenso elíptico](bsd/estado_del_descenso.md) y [contrato de evidencia](bsd/contrato_de_evidencia.md): predicciones, validación y datos que faltan para un resultado Cassels–Tate.
- [Bibliografía](BIBLIOGRAFIA.md).

## Clasificación de las afirmaciones

1. **Argumentos algebraicos bajo las hipótesis declaradas:** identidad de raíces opuestas; retículo núcleo de la aplicación de fases; cálculo de norma bajo la estructura y los grados de campo indicados. Esta edición no vuelve a demostrar los grados 165 y 330 de la construcción original.
2. **Cálculos reproducidos aquí:** ejemplo de cobordes en Q(√2) y matriz integral explícita de determinante +11. Son pruebas finitas de aritmética exacta, no avances que resuelvan las conjeturas.
3. **Cálculos históricos documentados:** 5103 códigos, 4719 valores reducidos, 424 parejas y 2²¹ estados del sector fijado; diez anclajes. Los JSON `historico_*.json` son ediciones de salidas anteriores, con envoltura explícita de no reejecución. Sus hashes internos identifican originales, no estos archivos editados.
4. **Predicciones y cuestiones abiertas:** segunda construcción auténtica desde la cónica de grado 165; igualdad por estado; descenso 3-Selmer real y escalar Cassels–Tate. Las predicciones BSD no son resultados computados.
5. **Interpretación física:** ninguna conclusión física, psicológica o sobre IA se deduce de este paquete.

Los dos modos de cálculo del ejemplo cuadrático comparten U: **no son fuentes matemáticamente independientes**. El testigo integral autónomo tampoco verifica que sus filas aparezcan en los datos históricos ni la inyectividad de las claves en esos datos. La inyectividad histórica se limita a los 5103 símbolos, no a M× entero.

## Reproducir la parte autónoma

Requisitos: Python 3 y biblioteca estándar. No red, Magma, instalación ni servicios pagados.

Desde este directorio:

```sh
python3 beal/verificar_conica_cuadratica.py
python3 beal/verificar_indice_reticular.py
sha256sum -c SHA256SUMS.txt
```

El primer programa escribe `beal/resultado_conica.json` y comprueba 16 parejas, 64 identidades de 2-cociclo, 64 valores de 3-coborde y 256 identidades de 3-cociclo, además de una mutación detectada. El segundo escribe `beal/resultado_indice_reticular.json`: determinante +11, cinco filas en el núcleo de fases y control negativo. Las salidas de consola conservadas están junto a los programas. No ejecutar con `python -O`: los controles emplean `assert`.

El segundo programa es una extracción acotada del cálculo de determinante y su control negativo del verificador histórico, con la matriz declarada explícitamente. No añade una afirmación matemática nueva.

## Dependencias pendientes, sin ocultarlas

No se incluye la tabla masiva histórica cuyo ZIP tiene SHA256 `4d9326c8f457b7a046772268e9af9ca501243525956be69fdf5bf56b906946eb`, ni los comparadores/verificadores que dependen de ella. Por ello este lote **no permite reproducir los 2²¹ estados, las 5103 claves ni los diez anclajes archivados**. Se conservan como resultados reportados, no resultados nuevos. No basta sustituir el ZIP por datos sintéticos o contrastar una fila por cada clase de la primera construcción.

Tampoco se incluyen aquí el runtime Magma, los paquetes completos de validación elíptica ni su salida auténtica. El contrato elíptico es documental; sus 14 y 5 pruebas son reportadas, no reejecutadas. Un envío sin salida observada no acredita ejecución terminada. El material científico histórico restante permanece pendiente de edición, no descartado.

Las condiciones de coherencia de las soluciones de cónicas en la hipótesis 4.4.3 de Shukla deben verificarse antes de aplicar su construcción. Los pequeños ejemplos de este lote no verifican esas hipótesis en la instancia grande.

## Derechos y edición

Marca de presentación: Concordante Lab · Xorch. No se concede una nueva licencia ni se reasigna titularidad. Las referencias de terceros conservan su atribución; no se redistribuyen sus PDF ni sus programas. La presentación pública no garantiza compatibilidad con toda revista: cualquier conflicto editorial concreto debe revisarse para el manuscrito afectado.
