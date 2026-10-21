# Códigos, retículas y vecinos primos

Concordante Lab · Xorch

© 2026. Todos los derechos reservados.

Este paquete presenta demostraciones elementales sobre Construction A, el corte binario por suma módulo cuatro y una obstrucción para eliminar vectores cortos mediante un solo vecino primo. Incluye pruebas completas, código de biblioteca estándar y resultados exactos reproducidos.

## Resultados

- Para un código aditivo no nulo de módulo q, el mínimo cuadrado de Construction A es min(q,d_E/q).
- Para un código binario autodual doblemente par, el corte M(C) tiene índice 2, covolumen 2, determinante de Gram 4 y mínimo min(4,d/2).
- El cascarón √2 D_n queda contenido en M(C); toda sobre-retícula en la misma métrica conserva vectores de norma cuadrada 4.
- Si una retícula integral unimodular contiene M(C), un solo vecino de primo impar p<2n−1 conserva alguno de esos vectores. El informe prueba también una cota inferior para cuántos sobreviven.

## Lectura

1. [Demostraciones y alcance](reticulas_codigos_y_vecinos.md).
2. [Verificación y reproducción](VERIFICACION.md).
3. [Bibliografía](BIBLIOGRAFIA.md).

## Reproducción

Con Python 3 y biblioteca estándar:

```sh
python verificar_vecinos_primos.py > resultado_local.json
python comparar_certificados.py resultado_local.json
sha256sum -c SHA256SUMS.txt
```

Las pruebas finitas recorren 27, 625 y 16807 asignaciones de residuos para p=3,5,7. El script verifica fórmulas de censos y cotas; las demostraciones generales están en el documento. Los controles de enumeradores Golay/Reed–Muller se usan aquí como entradas históricas. El paquete comprende este núcleo de límites y vecinos; los restantes expedientes de empaquetamientos, Barnes–Wall y levantamientos modulares conservan su lugar en las entregas pendientes.
