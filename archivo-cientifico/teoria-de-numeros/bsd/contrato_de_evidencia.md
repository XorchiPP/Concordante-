# Contrato documental de evidencia para descenso elíptico

Concordante Lab · Xorch · © 2026. Todos los derechos reservados.

Especificación histórica del 27 de septiembre de 2026, editada el 21 de octubre. Se publica el contrato, no el paquete de implementación ni un resultado de ejecución.

## Resultado materializado

El validador histórico separa y valida dos capas:

1. el JSON aritmético producido por el lector de descenso;
2. el sobre mínimo de evidencia que enlaza ese handoff con un eventual escalar Cassels–Tate.

El sobre terminal tiene exactamente cinco campos de nivel superior:

- `schema`;
- `target`;
- `magma_execution`;
- `cassels_tate`;
- `claim_scope`.

No acepta propiedades adicionales. El fixture positivo persistente es deliberadamente `not_executed/not_computed`; por tanto no contiene un valor matemático fingido.

## Invariantes fail-closed

### Handoff Magma

- claves exactas del lector de descenso;
- versión `V2.29[-patch]`;
- errores de validación vacíos;
- ramas admitidas solamente `sha3_quotient_zero` y `terminal_handoff_complete`;
- rama cero: dimensión 2, orden 9, cociente 0 y ningún dato terminal espurio;
- rama terminal: dimensión 4, orden 81, cociente 2 y discriminante `55297189`;
- vectores normalizados en `{0,1,2}` (no meramente congruentes módulo 3);
- complemento MW + representantes de cociente de rango 4;
- base MW + par terminal de rango 4;
- coordenadas terminales independientes;
- segundo argumento local exactamente cero en 3 y N;
- bloques de cúbica reducida y mapa no vacíos.

### Escalar Cassels–Tate

- `computed` requiere primero `validated_handoff`;
- ejecución validada requiere código de salida cero, versión V2.29 y SHA-256 de stdout/handoff;
- método fijado a `Fisher-Newton`;
- el hash del handoff consumido debe coincidir con el hash producido por Magma;
- el transcript CT debe tener SHA-256;
- `epsilon_f3` pertenece exactamente a `{0,1,2}`;
- las banderas humanas deben coincidir con los estados de ejecución;
- `bsd_solution_claimed=true` está prohibido: un escalar terminal aislado no cierra BSD.

El archivo JSON Schema documenta la forma estructural; las igualdades entre hashes y estados se comprueban en Python.


## Pruebas reportadas y límite

La fuente reporta 14 pruebas del contrato y 5 del lector. Incluyen rechazo de escalar sin ejecución, propiedad extra, hash discordante, afirmación BSD indebida, booleano como entero, residuos no normalizados, bases dependientes y mutación posterior del handoff. No se reejecutaron aquí. Un conjunto finito de pruebas no demuestra corrección universal de software. No hay un grupo Selmer real ni emparejamiento Cassels–Tate validado en esta entrega.
