# Igualdad exacta de los ideales de relaciones

Concordante Lab · Xorch · 21 de octubre de 2026.

Las 46 identidades explícitas del certificado expresan cada generador del ideal exportado K como combinación de las nueve relaciones que generan J. El evaluador independiente verifica todas las identidades y rechaza 15 controles negativos. Así se demuestra K⊆J; junto con la reducción J⊆K ya publicada, se obtiene J=K y la serie de Hilbert del cociente por las nueve relaciones.

- [Explicación matemática y prueba](RESULTADO.md).
- [Auditoría independiente](audit_report.md).
- `membership_witness.json`: 46 identidades, 4563 sumandos.
- `inputs/`: las dos entradas completas, idénticas a las publicadas con el manuscrito.
- `find_witness.py`: buscador reproducible, separado del evaluador.
- `verify_membership_independent.py`: expansión exacta sobre F₂, sin importar el buscador.
- `search_output.txt` y `audit_output.txt`: salidas de la reproducción.

Desde esta carpeta, con Python 3 y biblioteca estándar:

```sh
sha256sum -c SHA256SUMS.txt
python3 verify_membership_independent.py
```

Para reproducir la búsqueda, ejecutar `python3 find_witness.py` en una copia de la carpeta: el programa vuelve a escribir el certificado y sus tiempos pueden variar. Las identidades matemáticas están separadas en la clave `witnesses`.

La identificación del cociente con la cohomología global conserva las hipótesis de realización de las ocho clases y autenticación de los argumentos de detección. Esta entrega resuelve la igualdad algebraica de ideales para las entradas fijadas.

© 2026 Xorch · Concordante Lab. Derechos conforme a la política vigente del archivo.
