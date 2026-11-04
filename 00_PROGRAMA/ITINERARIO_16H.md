# Programa oficial — taller junior de ALM generativo (16 horas)

## Resultado exigible
Cada equipo utiliza Claude Code y un proyecto GitLab para producir y explicar la cadena **idea → requisitos → diseño → implementación → pruebas → CI/CD → evolución → trazabilidad**. Cada fase posee metaprompt de creación de instrucciones, prompt operativo específico, contrato de salida y evidencia comprobable.

**MVP obligatorio:** listar salas, realizar reserva, impedir solapamientos, cancelar reserva. **Cambio de mantenimiento:** impedir intervalos de más de 4 h. No añadir usuarios, facturación, membresías ni despliegue cloud.

## Cronograma de dos jornadas (horas lectivas; pausas fuera)

| Día | Laboratorio | Tiempo | Producto verificable |
|---|---|---:|---|
| 1 | L01 Vibe Coding y límites | 1 h | Prototipo inicial y errores detectados |
| 1 | L02 Metaprompts, Claude Code y GitLab | 1 h | Proyecto, rama y primer prompt operativo |
| 1 | L03 Requisitos generativos | 1,5 h | Especificación, Gherkin, backlog e issues |
| 1 | L04 Diseño generativo | 1 h | Modelo, diagrama, ADR |
| 1 | L05 Desarrollo generativo | 3,5 h | API de reservas ejecutable |
| 2 | L06 Testing y revisión de seguridad | 2 h | Tests, cobertura y correcciones |
| 2 | L07 GitLab CI/CD | 2 h | Pipeline remoto y artefactos |
| 2 | L08 Mantenimiento y cambio | 2 h | Nuevo requisito, código y tests |
| 2 | L09 Trazabilidad y documentación | 1 h | Matriz requisitos–código–tests–MR |
| 2 | L10 Evaluación final | 1 h | Demostración funcional y explicación |
| | **TOTAL** | **16 h** | |

## Qué enseñamos y qué no

**Enseñamos:** terminología ALM, calidad de un metaprompt, generación de prompts operativos con entradas y salidas formales, aprobación humana, relación con GitLab Issues y Merge Requests, pruebas y cierre de ciclo.

**No enseñamos:** IA teórica avanzada, administración de GitLab, Kubernetes, servicios en nube, desarrollo de un motor propio de orquestación, sistemas multiagente complejos.

## Método pedagógico de cada laboratorio

1. **Teoría (contexto):** concepto y significado dentro del ALM; lectura antes de practicar.
2. **Demostración:** el formador muestra una ejecución y un problema típico.
3. **Metaprompt:** Claude propone el prompt operativo; los alumnos revisan objetivo, entradas, restricciones, salidas y validaciones.
4. **Práctica:** Claude ejecuta el prompt sobre el clon GitLab; se comprueba el resultado real.
5. **Gate humano:** no se avanza si faltan evidencias, y se registra la razón de fallos.

## Preparación y coste asumidos

Cada alumno tiene acceso personal autorizado a Claude Code (plan compatible), VS Code, Python, Git y GitLab. El uso de Claude Free web no reemplaza a Claude Code. No habrá llamadas API desde jobs GitLab. Las cuotas de Pro no son ilimitadas: los checkpoints son planes de continuidad, no una garantía de ejecución por alumno.

## Evaluación

- Requisitos y especificaciones: 20%.
- Aplicación funcional: 25%.
- Pruebas y CI/CD: 25%.
- GitLab e historial de revisión: 15%.
- Argumentación y uso crítico de IA: 15%.

**Criterio irrenunciable:** ninguna prueba se declara «pasada» sin una evidencia de ejecución. Ninguna fase se «aprueba» solo por haber generado un documento.

## Aplicación al taller senior

El caso, el vocabulario y la base de requisitos son iguales; el senior modifica contratos, arquitectura, controles, límites de agentes y política de aprobación, pero no hay que rehacer los materiales junior.
