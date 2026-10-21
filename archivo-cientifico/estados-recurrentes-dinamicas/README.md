# Mismos estados recurrentes, distintas dinámicas

Concordante Lab · Xorch

© 2026. Todos los derechos reservados.

Cuatro redes dirigidas de nueve vértices tienen exactamente las mismas 167.040 configuraciones recurrentes, pero sus grupos críticos y acciones de adición pueden ser distintos. Las pruebas y certificados distinguen dos contratos de aristas:

- Estricto: 24 arcos internos y 12 al sumidero. Las dos adiciones marcadas en las esquinas dejan dos órbitas conjuntas en la variante saliente.
- Relajado: 20 arcos internos y 16 al sumidero. Esas mismas dos adiciones generan una sola órbita en la variante saliente. Cada adición por separado tiene doce ciclos.

El núcleo común de siete vértices tiene grupo Z3⊕Z3480. Los grupos de las redes estrictas son Z2⊕Z12⊕Z6960; los de las relajadas son Z12⊕Z13920. La igualdad del conjunto recurrente se combina así con operaciones de grupo diferentes.

[Pruebas completas y matrices](dinamica_dos_puertos.md) · [Reproducción](VERIFICACION.md) · [Fuentes](BIBLIOGRAFIA.md)

## Reproducir

Requiere Python 3.11+, SymPy 1.12–1.x y compilador C++17 ya disponibles. Desde una copia del directorio:

```sh
python verificar_dos_puertos.py > salida_simbolica.txt
g++ -std=c++17 -O2 censo_fifo.cpp -o /tmp/censo_fifo
/tmp/censo_fifo casos.txt recurrencia_fifo.bin > salida_fifo.txt
g++ -std=c++17 -O2 censo_por_lotes.cpp -o /tmp/censo_lotes
/tmp/censo_lotes recurrencia_lotes.bin > salida_lotes.txt
g++ -std=c++17 -O2 orbitas_marcadas.cpp -o /tmp/orbitas_marcadas
/tmp/orbitas_marcadas recurrencia_fifo.bin > salida_orbitas.txt
python comparar_resultados.py > salida_comparacion.txt
sha256sum -c SHA256SUMS.txt
```

Los programas generan matrices, certificado y bitsets en esta copia. Los archivos históricos de comparación están separados. Los binarios `.bin` son datos de membresía recurrente, no ejecutables. El formato se explica en VERIFICACION. El paquete contiene todos los datos y fuentes necesarios para estos ejemplos finitos.
