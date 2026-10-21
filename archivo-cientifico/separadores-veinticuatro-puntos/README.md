# Distinguir 24 puntos con seis conjuntos de ocho

Concordante Lab · Xorch

© 2026. Todos los derechos reservados.

Seis octadas bastan para distinguir los 24 puntos del código de Golay extendido, y cinco son imposibles por una cota de peso. Este paquete desarrolla esa prueba y estudia la acción de Mathieu sobre sistemas de seis octadas.

## Resultados

- Censo exhaustivo de 82 vecinos por sustitución de una octada de un testigo fijo.
- Once triples distintos de invariantes entre esos vecinos, y dos representantes adicionales con estabilizador C6.
- Trece órbitas distintas certificadas, que aportan una cota inferior de 2.489.034.240 sistemas separadores no ordenados.
- Estabilizador de cada separador embebido en S6; pérdida de separación al borrar cualquier sensor.
- Transporte de marcos decorados y obstrucción a una selección equivariante sobre el marco desnudo, bajo la estructura clásica de Conway citada.

[Demostraciones](separadores_y_orbitas.md) · [Verificación](VERIFICACION.md) · [Bibliografía](BIBLIOGRAFIA.md)

## Reproducción

Solo Python 3 estándar. Ejecutar desde una copia del directorio:

```sh
python verificar_separadores.py
python verificar_por_codigo.py
python comprobar_entrada_y_resultados.py
sha256sum -c SHA256SUMS.txt
```

Los dos primeros programas escriben sus certificados y el atlas en este directorio con resultados deterministas; los certificados históricos de referencia se conservan en archivos separados. Las entradas comprenden las 759 máscaras y el testigo base completo. El control final reconstruye las 4096 palabras de la presentación cíclica de Golay y coteja las entradas y salidas.

El objetivo global pendiente es clasificar todas las órbitas de separadores. Los once triples locales pueden agrupar más de una órbita. El desarrollo histórico completo de retículas y sextetos se conserva para incorporaciones posteriores.
