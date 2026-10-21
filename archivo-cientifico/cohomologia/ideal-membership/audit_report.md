# Auditoría independiente de contención de ideales

Fecha: 2026-10-21 (UTC). Resultado: **PASS**.

## Método e independencia

Se escribió desde cero `verify_membership_independent.py`, usando únicamente la biblioteca estándar de Python. No se leyó, importó ni ejecutó `find_witness.py`. El parser de relaciones usa una gramática restringida de sumas de productos de potencias; el parser del soporte hexadecimal consume ocho dígitos por monomio, en el orden de variables declarado. La comprobación expande cada múltiplo de relación como un `Counter` de tuplas de exponentes y reduce sus coeficientes módulo 2. No utiliza reducción de Gröbner, el algoritmo de búsqueda de testigos ni su representación de vectores binarios.

Se comprobó:
- SHA-256 de ambos inputs frente a los valores congelados y el manifiesto del certificado.
- Campo F2, ocho variables, orden de variables, pesos [1,1,2,3,4,5,6,6] y orden de relaciones.
- Nueve relaciones no nulas homogéneas; 46 soportes distintos y 46 índices testigo, sin omisiones ni repeticiones.
- Integridad del formato, índices de relaciones, dimensiones de multiplicadores, exponentes enteros no negativos y homogeneidad de cada término testigo.
- Las 46 igualdades de polinomios completas, no solamente evaluaciones puntuales o comprobaciones de grado.

## Resultados reproducibles

Ejecutar:

```sh
python verify_membership_independent.py
```

O desde cualquier directorio, usar la ruta absoluta del script. `audit_output.txt` contiene la salida completa.

- Igualdades exactas verificadas: **46/46**.
- Relaciones: **9**.
- Términos de los testigos: **4.563**.
- Monomios expandidos antes de cancelación: **12.233**.
- Grados ponderados de los objetivos: mínimo **3**, máximo **41**.
- Pruebas negativas: **15/15** rechazadas.

Las pruebas negativas cubren hashes, población, índices, exponentes, dimensiones, homogeneidad, pérdida de un término no trivial, sustitución de una relación por otra del mismo grado, cambios homogéneos de input que fallan la igualdad exacta, codificación hexadecimal y claves JSON duplicadas. En los tests de contenido se recalcula expresamente un manifiesto de prueba en memoria para alcanzar las comprobaciones algebraicas, no detenerse en el hash. El manifiesto de producción permanece congelado. Se confirmó que los archivos originales no cambiaron.

## Conclusión matemática y límites

Sea R = F2[x,y,alpha,gamma,w4,w5,w6,Theta], J el ideal generado por las nueve relaciones de `relations.json` y K el ideal generado por los 46 polinomios codificados en `groebner_supports.hex`. Cada certificado exhibe una identidad exacta g_i = sum_j m_ij r_j en R. Por cierre de un ideal bajo suma y multiplicación por elementos de R, las 46 identidades prueban **K ⊆ J**. Esta conclusión es global como igualdad formal de polinomios y contención de estos ideales; no está limitada al máximo grado observado.

Combinada con una comprobación válida previa de **J ⊆ K**, para estos mismos generadores, campo y orden de variables, se obtiene **J = K**. La dirección previa no se reaudita aquí. Tampoco se certifica aquí que los 46 polinomios formen una base de Gröbner para algún orden, que las nueve relaciones sean mínimas, o que esta presentación sea la cohomología de un objeto geométrico. La igualdad de estos ideales no prueba una realización global cohomológica ni ninguna interpretación física.

Los hashes fijan los bytes sometidos a auditoría, no autentican por sí solos su procedencia matemática. La auditoría certifica las identidades para esos inputs congelados.
