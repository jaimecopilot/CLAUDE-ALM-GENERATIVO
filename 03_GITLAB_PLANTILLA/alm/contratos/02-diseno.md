# Contrato 02 — DISENO

**Actividad formativa origen:** L04. **Tipo:** contrato de una fase; NO contiene el artefacto final prehecho.

## Entradas que deben existir
- docs/requisitos/especificacion.md
- docs/requisitos/backlog.md

## Salidas que Claude debe producir tras autorización
- docs/arquitectura/diseno.md
- docs/arquitectura/diagramas.md
- docs/arquitectura/ADR-001.md

## Criterios de validación obligatorios
- [ ] Componentes mínimos FastAPI y SQLite
- [ ] Responsabilidades de reglas de disponibilidad
- [ ] Diagramas Mermaid representativos
- [ ] ADR con alternativas y consecuencias
- [ ] Correspondencia con RF/CA

## Protocolo
1. El metaprompt 02 genera primero `alm/prompts-generados/02-diseno.md` sin producir las salidas.
2. El alumno inspecciona y aprueba el prompt operativo (gate A).
3. Claude ejecuta el prompt sobre archivos reales, mostrando diff y pruebas ejecutadas.
4. Se validan criterios mediante revisión/ejecución real; anotar fallos y correcciones.
5. Registrar evidencias y esperar aprobación humana final (gate B).

## Política de evidencias
No inventar URL de GitLab, número de issue, ejecución o cobertura. Marcar NO EJECUTADO cuando corresponda. Solo avanzar a fase siguiente cuando se cumplan los criterios o exista aceptación explícita y registrada de una limitación no bloqueante.
