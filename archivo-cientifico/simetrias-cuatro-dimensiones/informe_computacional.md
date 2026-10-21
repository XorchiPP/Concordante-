# Informe computacional H₄

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Sección H₄ del informe científico del 9 de octubre de 2026. Las secciones de aritmética y Hodge del documento fuente no pertenecen a este paquete. Reproducida el 21 de octubre: el certificado resultante coincide exactamente con el histórico.

## 1. Completación de la acción de 360 banderas de H₄


Se construyeron desde cero las 120 raíces del sistema no cristalográfico H₄ en \(\mathbb Q(\sqrt5)^4\), proyectadas en 60 líneas. Las dos relaciones doradas tienen 360 pares cada una y determinan dos cartas biyectivas del mismo conjunto de 360 banderas. Las matrices naturales \(L_+,L_-\) representan grafos de grado 22 con vecindarios no diagonales disjuntos.


Las cuatro reflexiones de un sistema simple con diagrama 5–3–3 generan una acción transitiva sobre 360 banderas, con estabilizador proyectivo de orden 20 y grupo de orden 7.200. Las 32 subórbitas tienen multiplicidades de tamaños \(1^1,2^2,5^3,10^{18},20^8\). De ellas se reconstruyen **32 matrices orbitales**, su tabla integral de multiplicación y el álgebra completa \(B\).


Los cálculos racionales exactos dan


\[
\dim A=16,\quad \dim B=32,\quad \dim Z(A)=7,\quad \dim Z(B)=12,
\qquad A=\operatorname{alg}_{\mathbb R}(I,L_+,L_-).
\]


Para \(C=[L_+,L_-]\) se certifica


\[
C(C^2+1620I)(C^2+2560I)=0,\qquad \operatorname{rank}C=68.
\]


Las multiplicidades de los autovalores no nulos de \(C^2\) son 32 para \(-1620\) y 36 para \(-2560\).


Un proyector central explícitamente computable separa un ideal bilateral \(D\) de dimensión cuatro y centro unidimensional. Ambos \(L_+\) y \(L_-\) actúan sobre él por \(-2I\). Un elemento de traza reducida nula verifica \(x^2=21e_D\), lo que prueba que el álgebra real simple de dimensión cuatro es **\(M_2(\mathbb R)\)**, no el álgebra de cuaterniones. Cualquier nueva matriz \(T\) produce en este cociente \(\mathbb R[T_D]\), conmutativa, por lo que **una sola matriz no completa** \(B\).


Dos pares concretos de orbitales dirigidas y traspuestas sí generan \(B\) por cierre exacto. Sus etiquetas son (24,26) y (25,29), relativas exclusivamente a la enumeración determinista del programa. Por tanto, el número mínimo de matrices adicionales es **dos** bajo las operaciones de álgebra asociativa real.


**Alcance histórico:** esta pasada verifica mediante otro camino computacional interno la geometría, el rango orbital, los centros, el conmutador, el ideal invisible y ambas direcciones del teorema de completación mínima. La clasificación del resto de bloques de Wedderburn fue reportada en auditorías previas, pero no queda certificada por el programa de esta entrega. Sigue abierta la búsqueda especializada de prioridad.


