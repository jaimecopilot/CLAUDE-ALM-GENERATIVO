# L08 · METAPROMPT: evolución controlada por impacto

~~~text
Rol: generador de prompts operativos para mantenimiento y evolución del ALM.
MODO: escribir el prompt de cambio, NO aplicar el cambio todavía.

Nueva petición aprobada:
«No permitir reservas superiores a cuatro horas; exactamente cuatro horas sí».

Lee el contrato alm/contratos/06-evolucion.md, requisitos aprobados, arquitectura real, código y pruebas, informe de calidad y estado de la última MR.

Genera alm/prompts-generados/06-evolucion.md con:
1. Diagnóstico de impacto: RF, criterios, módulos, tests, diagramas y docs afectados.
2. Lista concreta de archivos que se modificarían y de archivos que deben permanecer intactos.
3. Solicitud de actualización de requisito y criterios Gherkin antes de editar implementación.
4. Plan mínimo de cambio funcional sin reescribir el proyecto.
5. Pruebas frontera: 3h59 aceptada, 4h aceptada, 4h01 rechazada; sin olvidar solapamiento/cancelación.
6. Ejecución de regresión con evidencia de pytest y CI real.
7. Registro de issue CAM-01, rama, commit y MR cuando existan.
8. Bloqueo frente a nuevas funcionalidades no pedidas.
9. Prohibición de falsear resultados, rebajar tests o hacer merge sin revisión.
10. Gate humano antes de ejecutar y al cerrar la fase.

No cambies código todavía; presenta análisis y prompt para revisión.
~~~

## Revisión obligatoria
El alumno comprueba que el prompt propaga el cambio por todas las fases afectadas pero NO reinicia el ALM desde cero.