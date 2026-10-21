# Operaciones de Steenrod: tabla documental

Concordante Lab · Xorch · 21 octubre 2026

## Aporte y condición

La tabla especifica las 28 operaciones sobre los ocho generadores de la presentación del manuscrito. Sq^0 es identidad; la inestabilidad fija Sq^i(z)=0 para i>|z| y Cartan extiende las fórmulas a productos. El resultado está condicionado a las clases auténticas y los certificados de restricciones e ideales de la investigación fuente.

Esta edición transcribe las fórmulas para revisión. La fuente documenta 168 identidades de restricciones, 28 pruebas de estabilidad del ideal y 128 identidades de Adem. Su reproducción completa requiere incorporar las seis restricciones originales y la base de Gröbner de 46 polinomios. Las pruebas ejecutadas en esta entrega constan en verification_output.txt, buchberger_output.txt y hilbert_output.txt; la tabla de operaciones conserva su estado documental.

## Tabla completa


All coefficients are in \(\mathbb F_2\); `+` denotes binary XOR. Expressions are representatives modulo the nine relations, chosen for explicit verification.

| Generator | Degree | Steenrod square | Polynomial image |
|---|---:|---|---|
| `x` | 1 | `Sq^1` | `x^2` |
| `y` | 1 | `Sq^1` | `y^2` |
| `alpha` | 2 | `Sq^1` | `gamma` |
| `alpha` | 2 | `Sq^2` | `alpha^2` |
| `gamma` | 3 | `Sq^1` | `0` |
| `gamma` | 3 | `Sq^2` | `w5 + alpha*gamma + x*w4 + x^2*gamma + x^2*y^3 + x*y^4` |
| `gamma` | 3 | `Sq^3` | `gamma^2` |
| `w4` | 4 | `Sq^1` | `w5 + x*w4` |
| `w4` | 4 | `Sq^2` | `w6 + alpha*w4 + x*y*w4` |
| `w4` | 4 | `Sq^3` | `alpha*w5 + gamma*w4 + x*Theta + y*Theta + y*w6 + x*y*w5 + alpha^2*gamma + y^2*w5 + x^2*y*w4 + y^3*w4 + x^3*y^4 + y^7` |
| `w4` | 4 | `Sq^4` | `w4^2` |
| `w5` | 5 | `Sq^1` | `x*w5` |
| `w5` | 5 | `Sq^2` | `alpha*w5 + x*w6 + x*y*w5` |
| `w5` | 5 | `Sq^3` | `gamma*w5 + x*y*Theta + x*y*w6 + x^2*Theta + x^2*w6 + x*alpha^2*gamma + x*y^2*w5 + x^2*y*w5 + y^3*w5` |
| `w5` | 5 | `Sq^4` | `gamma*w6 + w4*w5 + x*alpha*Theta + alpha^2*w5 + gamma^3 + x^2*y*w6 + alpha^3*gamma + x^2*y^2*w5 + y^4*w5` |
| `w5` | 5 | `Sq^5` | `w5^2` |
| `w6` | 6 | `Sq^1` | `x*Theta + y*Theta + y*w6 + x*alpha*w4 + alpha^2*gamma + y^2*w5 + x*y^2*w4 + x^2*y*w4 + y^3*w4 + x^3*y^4 + y^7` |
| `w6` | 6 | `Sq^2` | `alpha*w6 + x*y*w6` |
| `w6` | 6 | `Sq^3` | `gamma*w6 + x*alpha*Theta + x*alpha^2*w4 + x^2*y*w6 + alpha^3*gamma + x^2*y^2*w5 + y^4*w5` |
| `w6` | 6 | `Sq^4` | `w4*w6 + alpha*gamma*w5 + x*alpha*gamma*w4 + alpha^2*gamma^2 + alpha^3*w4 + x*gamma^3 + alpha^5` |
| `w6` | 6 | `Sq^5` | `w5*w6 + x*w4*Theta + x*w4*w6 + y*w4*Theta + y*w4*w6 + gamma^2*w5 + x*alpha*gamma*w5 + x*alpha*w4^2 + x*alpha^2*Theta + y^2*w4*w5 + alpha^3*w5 + x*y^2*w4^2 + x^2*y*w4^2 + y^3*w4^2 + alpha^4*gamma + x^3*y^4*w4 + y^7*w4` |
| `w6` | 6 | `Sq^6` | `w6^2` |
| `Theta` | 6 | `Sq^1` | `x*Theta + alpha^2*gamma + x*alpha^3` |
| `Theta` | 6 | `Sq^2` | `alpha*Theta + gamma*w5 + x*alpha*w5 + alpha*gamma^2 + alpha^2*w4 + x^2*Theta + x*alpha^2*gamma + x^2*gamma^2 + alpha^4` |
| `Theta` | 6 | `Sq^3` | `gamma*Theta + x*alpha*w6 + alpha^2*w5 + gamma^3 + x*alpha*gamma^2 + x*y^2*Theta + alpha^3*gamma` |
| `Theta` | 6 | `Sq^4` | `w4*Theta + x*gamma*Theta + x*gamma*w6 + alpha^2*Theta + x*alpha*gamma*w4 + alpha^2*gamma^2 + x*alpha^3*gamma + alpha^5` |
| `Theta` | 6 | `Sq^5` | `w5*Theta + x*alpha*gamma*w5 + alpha^2*gamma*w4 + x*alpha^2*w6 + x^2*gamma*w6 + x*alpha^2*gamma^2` |
| `Theta` | 6 | `Sq^6` | `Theta^2` |


## Verificación pendiente

Autenticar la construcción de clases; evaluar cada fórmula en seis subgrupos elementales; contrastar la inyectividad en los grados de salida; verificar estabilidad del ideal mediante Cartan y reducción; reproducir las 128 identidades de Adem. La homología de Margolis documentada hasta grado 24 es un cálculo finito distinto de la determinación integral.

Referencia clásica: Steenrod y Epstein, Cohomology Operations (1962).

© 2026 Xorch — Concordante Lab.
