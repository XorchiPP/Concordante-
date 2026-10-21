# Reconstrucción de restricciones sobre seis detectores

Concordante Lab · Xorch · 21 octubre 2026

## Aporte reproducido

Este suplemento reconstruye los ocho polinomios de restricción en cada uno de seis subgrupos elementales de rangos (4,3,3,3,3,3), usando las tablas antecedentes de grados 10, 11 y 12. Exporta los soportes en generator_restrictions.json y compara exactamente el primer detector con los datos de fibra del manuscrito.

```sh
python reconstruct_restrictions.py
sha256sum -c SHA256SUMS.txt
```

Python 3.10 o posterior, exclusivamente biblioteca estándar. El replay se ejecutó con límite externo de 60 segundos. Los hashes fijados en el programa se comprueban antes de los cálculos.

## Comprobaciones realizadas

- Rango completo de las tablas antecedentes: 39, 48 y 57 columnas.
- Reconstrucción por raíces de Frobenius, divisiones exactas y búsqueda finita de formas lineales; 144 columnas recuperadas y comparadas término a término.
- Sq¹(alpha)=gamma y alpha*y=0 sobre cada detector.
- Conteos orbitales hasta grado de fibra 13 y cotejo de las columnas LHS suministradas en grados de fibra 0–12; se conservan las diagonales E2 finitas de grados totales 10–13 del programa antecedente.
- Sección del modelo de grupo: órdenes 16 y 36, intersección trivial y 576 productos distintos.
- Restricciones de Stiefel–Whitney de la acción de permutación en 12 puntos: w1=x, w2=alpha+xy, y coincidencia de w4,w5,w6.
- Coincidencia exacta de los ocho soportes del detector normal de rango cuatro con la convención del manuscrito.

## Procedencia del extracto

El programa conserva los algoritmos de los bloques iniciales del verificador antecedente: autenticación, álgebra polinomial, lectura de tablas, reconstrucción, comparación de columnas, conteo orbital y sección del grupo. Además conserva el bloque de restricciones de Stiefel–Whitney hasta la comparación de w1,w2,w4,w5,w6. Se añadió únicamente la comparación explícita con el JSON de fibra ya distribuido y la exportación de los soportes/certificado.

El alcance se limita a esos bloques. Los cálculos posteriores del programa antecedente sobre la base y el rango detector en grado 13, matrices Sq², productos de ciclos, representación aumentada y Massey quedan fuera de este replay.

Los cinco CSV suministrados preservan exactamente los bytes matemáticos archivados. detector_subgroups.json selecciona únicamente los seis subgrupos, sus bases de permutaciones y los campos de rango y restricciones q,x,y del certificado antecedente; sus demás secciones quedan en la custodia original. manuscript_fiber.json es la extracción exacta de soportes del JSON del manuscrito.

## Tres niveles de disponibilidad y prueba

1. Datos de restricciones: disponibles aquí, autenticados por hashes y reejecutados en el alcance indicado.
2. Realización global de clases: la identificación de todos los ocho símbolos como clases globales con estas restricciones permanece como hipótesis antecedente del manuscrito. Reconstruir raíces o cocientes en los anillos polinomiales de detectores acredita compatibilidad de datos; su levantamiento a clases globales requiere la justificación de las construcciones antecedentes. La comparación de Stiefel–Whitney apoya parte de esa correspondencia.
3. Ideal de relaciones: permanece separada la contención inversa K⊆J, donde K es el ideal de los 46 polinomios exportados y J el de las nueve relaciones. El replay CAS antecedente está localizado; autenticar su salida exacta o aportar combinaciones explícitas continúa pendiente.

El teorema global conserva esas hipótesis. Los nuevos archivos resuelven la disponibilidad y reconstrucción de los datos de restricciones, con el estado lógico de realización global y pertenencia inversa explicitado por separado.

© 2026 Xorch — Concordante Lab.
