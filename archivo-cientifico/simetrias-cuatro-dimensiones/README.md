# Simetrías y álgebras en cuatro dimensiones

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Edición acotada del 21 de octubre de 2026. Contiene un argumento matemático sustantivo, el código exacto completo que lo acompaña y su certificado reproducido. Forma una entrega parcial de geometría y fundamentos.

## Resultado

En una acción clásica de H₄ sobre 360 puntos, dos adyacencias simétricas concretas generan un álgebra A de dimensión 16 dentro del álgebra orbital B de dimensión 32. El programa construye ambas desde coordenadas exactas, sin leer bases de datos ni matrices precalculadas.

Aísla un ideal central D≅M₂(R) sobre el cual ambos generadores actúan como −2I. Adicionar una sola matriz T no puede completar B: su imagen en D queda contenida en R[T_D], conmutativa y de dimensión a lo sumo dos. Dos matrices orbitales dirigidas y transpuestas sí completan B. El resultado establece la generación mínima de estas álgebras de relaciones.

La cuenta «dos» utiliza generación asociativa real sin trasposición automática. Si la clausura incluye automáticamente el adjunto, basta una relación dirigida junto con su traspuesta, contada como una familia. La cuenta corresponde a generadores algebraicos; su realización mediante mediciones físicas requiere un modelo adicional.

## Contenido y alcance

- [Geometría y demostración de completación](geometria_y_completacion.md): edición de las secciones pertinentes del manuscrito de trabajo v1.4, con límites explícitos donde el verificador adjunto no acredita las formas reales restantes.
- [Informe computacional](informe_computacional.md): sección H₄ del informe del 9 de octubre, reproducida aquí.
- `verificar_algebra_h4.py`: código científico idéntico al original del 9 de octubre; solo cambia su nombre de archivo público. Reconstruye raíces, cartas, acción, orbitales, constantes integrales de productos, cierres y el ideal escindido.
- `certificado_historico.json`: certificado original del 9 de octubre.
- `certificado_reproducido.json`: envoltura que distingue fecha de reproducción y fecha de fuente. El certificado interior coincide íntegramente con el histórico.
- `salida_verificacion.txt`: salida completa de la reproducción del 21 de octubre, con tiempos incidentales.
- `comparar_certificado.py`: comprobador documental de igualdad entre una nueva salida y el certificado histórico; no sustituye el cálculo.
- [Bibliografía](BIBLIOGRAFIA.md) y [revisión de alcance](VERIFICACION.md).

## Reproducir

Entorno comprobado: Python 3.12.14 y SymPy 1.14.0, ya instalados. El programa no usa red, ejecutables externos, servicios de pago ni instaladores. Su único resultado externo es stdout. Usa racionales exactos y Q(√5); no clasifica mediante aproximaciones flotantes. Los tiempos impresos no son datos matemáticos.

```sh
sha256sum -c SHA256SUMS.txt
python3 -u verificar_algebra_h4.py > nueva_salida.txt
python3 comparar_certificado.py nueva_salida.txt
```

No usar `python -O`: las comprobaciones emplean `assert`. La nueva salida puede diferir en los tiempos; el JSON científico debe coincidir exactamente. El programa reconstruye los datos intermedios, por lo que no necesita descargar ninguna tabla ausente.

## Fronteras científicas y editoriales

1. Las 120 raíces, 60 líneas proyectivas, geometría del 600-cell y conjunto de 360 puntos son clásicos. La identificación con una clase de subgrupos y con parejas antipodales de aristas es una deducción geométrica expuesta en el informe, no una novedad del portador.
2. El lema de una sola matriz es Cayley–Hamilton elemental. La posible contribución estrecha reside en los dos generadores concretos, el ideal que no distinguen y la completación óptima. La prioridad bibliográfica requiere revisión especializada.
3. El programa certifica dimensiones 16/32, centros 7/12, conmutador e ideal escindido M₂(R). **Los tipos reales de los restantes bloques de Wedderburn quedan pendientes de su suplemento específico.** Las dimensiones certificadas son la evidencia disponible en este corte.
4. El subespacio común de autovalor −2 tiene dimensión 13 y no es todo él un ideal bilateral. El programa aísla después el ideal central de dimensión 4: no deben confundirse ambos espacios.
5. Las etiquetas de pares (24,26) y (25,29) dependen de la enumeración del programa. No son invariantes intrínsecos. Tampoco la identificación del portador con aristas demuestra que ambas cartas sean el mismo grafo de aristas.
6. «Independiente» en los informes históricos significa un camino computacional separado dentro de la investigación, no arbitraje externo. Esta edición reproduce ese mismo código y conserva la identidad de su implementación.
7. Quedan pendientes el manuscrito íntegro con todas sus formas reales, la revisión especializada de prioridad y la edición separada de fundamentos sobre observador/relaciones/selección. Ese material conserva su lugar en el archivo pendiente de preparación.

No se concede nueva licencia ni se reasigna titularidad. La marca de presentación es Concordante Lab · Xorch. Se mantienen atribuciones bibliográficas legítimas. No se copian obras completas de terceros. No se conoce aquí un conflicto editorial específico; tampoco se garantiza compatibilidad con toda revista futura.
