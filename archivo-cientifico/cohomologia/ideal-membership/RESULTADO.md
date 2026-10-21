# Igualdad exacta de los dos ideales de relaciones

Concordante Lab · Xorch · 21 de octubre de 2026. Edición pública con auditoría algebraica independiente.

## Afirmación algebraica

Sea R=F₂[x,y,alpha,gamma,w4,w5,w6,Theta], con pesos (1,1,2,3,4,5,6,6). Sea J el ideal de las nueve relaciones de `inputs/relations.json`, enumeradas por orden de inserción de sus grados y después por orden de lista. Sea K el ideal de los 46 polinomios de `inputs/groebner_supports.hex`, enumerados por orden de segmentos separados por `;` (índices desde cero).

`membership_witness.json` proporciona, para cada gᵢ, una lista de pares (j,m) que significa la identidad exacta gᵢ=Σ x^m fⱼ sobre F₂. Contiene 46 identidades y 4563 sumandos monomio×relación, de pesos entre 3 y 41. La identidad implica gᵢ∈J para cada generador y por tanto K⊆J. La contención J⊆K fue verificada previamente mediante reducción de las nueve relaciones por los 46 polinomios. J=K resulta de ambas contenciones.

El certificado es finito, pero su consecuencia es una igualdad completa de ideales, no solamente la coincidencia de componentes hasta peso41: por definición todo elemento de K es una combinación polinomial de sus 46 generadores, y sustituir las identidades lo expresa en J.

## Por qué basta el evaluador

Para verificar una identidad, el evaluador multiplica cada monomio de fⱼ por x^m sumando exponentes componente a componente; cuenta las apariciones de cada vector de exponentes módulo2; y compara la lista resultante con los términos de gᵢ. Esta es exactamente la definición de suma y producto del anillo polinomial sobre F₂. Una comparación exhaustiva de soportes valida la identidad sin presuponer una base de Gröbner, orden monomial, CAS, factorización, aritmética aproximada ni la corrección del buscador.

## Búsqueda reproducible

`python3 find_witness.py` usa únicamente biblioteca estándar. Se fija orden grevlex por grado ordinario y orden de variables arriba; los pesos se emplean para comprobar homogeneidad, no para elegir el orden monomial. Se sigue una representación explícita en las nueve relaciones a través de pasos de Buchberger y divisiones. Se detiene en cuanto los 46 objetivos tienen representación. Los 104 polinomios auxiliares generados no se presentan como base final: quedaron 1574 pares sin procesar, irrelevantes para las 46 identidades ya construidas.

La búsqueda observada consumió 2.871 s, máximo 15632 KiB de RSS, procesó 3006 pares, con límites CPU 120 s y memoria virtual 512 MiB; el proceso externo además tenía timeout 125 s. Python 3.12.14, arquitectura x86_64. No se instaló ni utilizó CAS externo. La salida se conserva en `search_output.txt`. El JSON incluye tiempos observados que pueden variar entre reproducciones; las combinaciones matemáticas están separadas en la clave `witnesses`.

## Integridad y procedencia

Los dos inputs fueron copiados byte a byte del paquete público de cohomología congelado localmente. SHA-256:

- relations.json: 130743859b2e3b2d18642811c8615bea74212187a3da722cb8bdeb5e86703103
- groebner_supports.hex: 550dfeb94726e42de31395b90b51da3018955025d2a75881ca5270383fe1de6d

Las entradas coinciden byte a byte con las versiones distribuidas en este archivo científico. Sus hashes permiten cotejar directamente esta entrega con el manuscrito y los verificadores de Gröbner e Hilbert publicados.

## Alcance científico

Este aporte reemplaza la dependencia CAS de la contención inversa por testigos verificables. Junto con el criterio de Buchberger previo y el cómputo Hilbert previo, permite trasladar esos resultados del ideal K al ideal de las nueve relaciones J. La identificación con el anillo cohomológico global conserva sus demás hipótesis: realización de las ocho clases y autenticación de los detectores/argumentos pertinentes. La conclusión global conserva esas hipótesis separadas.

## Auditoría independiente completada

`python3 verify_membership_independent.py` pasó las 46 identidades mediante un segundo parser y expansión con Counter/paridad, sin importar ni ejecutar el buscador. Se contaron 12233 monomios expandidos antes de cancelar. Quince controles negativos fueron rechazados: corrupción de hashes, población, índices y exponentes, e incluso mutaciones homogéneas de relaciones, objetivos y testigos que alcanzan la comparación algebraica. Los archivos originales permanecieron idénticos. Véanse `audit_output.txt` y `audit_report.md`.

SHA-256 del certificado JSON observado: 8daa3bee78ecc0ce51aaa36c7654cff8272c2faee0f5ab0f6717327b1f6aaff5.
SHA-256 de solo la lista matemática `witnesses`, serializada JSON con sort_keys=True y separadores (',',':'): b32275348a0f4c47b716cf69cfc7a0e0434dd9abf56ddb0186b0430274848da1.
