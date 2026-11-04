# L04 · METAPROMPT OPERATIVO: diseño desde requisitos aprobados

~~~text
Rol: arquitecto de software que crea instrucciones operativas a partir de requisitos reales.
MODO: GENERAR PROMPT, NO DISEÑAR TODAVÍA.

Lee el contrato alm/contratos/02-diseno.md, los RF y criterios aceptados en docs/requisitos/especificacion.md y el backlog aprobado.

Redacta alm/prompts-generados/02-diseno.md para que, SOLO después de la aprobación humana:
- proponga una arquitectura monolítica sencilla FastAPI + SQLite;
- identifique módulos, entidades y reglas con su relación a cada RF;
- represente actores y componentes en Mermaid en docs/arquitectura/diagramas.md;
- defina modelo de datos y responsabilidades en docs/arquitectura/diseno.md;
- escriba docs/arquitectura/ADR-001.md con contexto, alternativas, decisión y consecuencias;
- señale dónde debe imponerse la regla de intervalo semiabierto y la ausencia de solapamientos;
- prohíba autenticación externa, microservicios, facturación y servicios cloud;
- incluya una revisión de trazabilidad que enlace decisiones con los RF/CA;
- solicite aprobación antes de pasar a implementación.

No generes ahora código Python ni llenes archivos finales de arquitectura. Si faltan los requisitos aprobados, detente y enumera las entradas ausentes.
~~~

## Gate de salida
El prompt operativo solo se aprueba si parte de los requisitos reales, define archivos exactos y especifica cómo revisar su coherencia.