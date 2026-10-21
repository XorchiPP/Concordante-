# Cohomología módulo dos del cociente central de W(F4)

**Concordante Lab · Xorch · 21 octubre 2026**

## Aporte

Manuscrito completo con ocho generadores, nueve relaciones y serie de Hilbert en todos los grados para G=W(F4)/{±I}. El argumento combina transferencia de índice impar, colapso aditivo de Nakaoka, invariantes de fibra, Shapiro y generación filtrada. La igualdad exacta de ideales está demostrada mediante identidades explícitas verificadas. El teorema del anillo conserva las hipótesis de realización de las clases globales y autenticación de los argumentos de detección.

- [Manuscrito legible](manuscript.md) y [fuente LaTeX](manuscript.tex).
- [Datos de fibra](f4_algebra_data.json) y [nueve relaciones](relations.json).
- [Tabla documental de Steenrod](steenrod_operations.md).
- [Teorema condicionado de reducción](reducedness.md).
- [Estado integral separado](integral_status_2026-10-21.md).

## Reproducir las comprobaciones incluidas

Desde esta carpeta, con Python 3 y su biblioteca estándar:

```sh
python verify_public_inputs.py
python verify_buchberger.py
python verify_hilbert.py
sha256sum -c SHA256SUMS.txt
```

Las salidas originales de esta edición están en verification_output.txt, buchberger_output.txt y hilbert_output.txt. Los dos últimos scripts regeneran los certificados JSON. La salida de Buchberger incluye tiempo de ejecución, que puede variar entre máquinas.

## Resultados reejecutados

- Nueve relaciones homogéneas en los grados anunciados.
- Dos identidades de fibra en F2[t0,t1,t2,t3], determinante entero −8 y cuártica irreducible.
- Rangos de fibra en grados 0–12 y 41 totales orbitales en grados 0–40.
- Los 46 polinomios exportados forman una base de Gröbner de su ideal: 809 S-pares reducidos y 226 cubiertos por criterio del producto; las nueve relaciones reducen a cero.
- Los 852 estados de la retícula de mínimos comunes múltiplos producen una identidad racional exacta con la serie declarada, por multiplicación cruzada en Z[t]. Esta identidad corresponde directamente al ideal exportado. Si J es el ideal de las nueve relaciones y K el ideal exportado, la reducción publicada verifica J⊆K y las 46 identidades explícitas del [certificado de pertenencia](ideal-membership/README.md) prueban K⊆J. Por tanto J=K y la identidad de Hilbert se aplica al cociente por las nueve relaciones en todos los grados.

## Disponibilidad de restricciones y dependencias pendientes

1. [Suplemento de restricciones](restrictions/README.md): datos de seis detectores localizados, saneados y reconstruidos; 144 columnas comparadas y convención de fibra idéntica al manuscrito. La justificación antecedente de realización global de las ocho clases y la autenticación completa de detección permanecen como hipótesis separadas.
2. [Igualdad exacta de ideales](ideal-membership/README.md): 46 identidades, 4563 sumandos monomio×relación y evaluador independiente con 15 controles negativos. La contención inversa queda demostrada para las entradas publicadas; el buscador y su salida están incluidos. La prueba de pertenencia se verifica directamente, sin depender del replay CAS antecedente.
3. Para la tabla Steenrod, los datos originales de restricciones y verificadores de las 168 identidades, 28 reducciones de estabilidad y 128 identidades de Adem.
4. Para la nota integral, el paquete de resoluciones, Bockstein y registros cíclicos correspondiente a los resultados aditivos transcritos.

La inclusión de estos materiales permitirá convertir la reproducción parcial aquí disponible en una auditoría completa del teorema condicionado. Los argumentos escritos y las referencias clásicas forman parte del manuscrito.

## Secuencia lógica

```text
Sylow regular → Nakaoka y transferencia → colapso aditivo → serie exacta
Fibra y Shapiro → generación filtrada → sobreyectividad global
Relaciones auténticas + igualdad de ideales → cociente correcto
Cociente correcto + igualdad de Hilbert → isomorfismo del anillo
```

La edición conserva la atribución a los autores de los teoremas clásicos. La evaluación de prioridad histórica y la revisión por pares constituyen pasos editoriales posteriores.

© 2026 Xorch — Concordante Lab.
