# Contrato 01 — REQUISITOS

**Actividad formativa origen:** L03. **Tipo:** contrato de una fase; NO contiene el artefacto final prehecho.

## Entradas que deben existir
- evidencias/L01.md
- evidencias/L02.md
- README.md
- docs/instrucciones/CASO_NEGOCIO.md
- alm/maestro.md

## Salidas que Claude debe producir tras autorización
- docs/requisitos/especificacion.md
- docs/requisitos/backlog.md

## Criterios de validación obligatorios
- [ ] Cada hallazgo L01 tiene un destino verificable en la especificación
- [ ] RF-01 a RF-04 identificados
- [ ] Historias y CA Gherkin verificables
- [ ] Regla de intervalos [inicio,fin)
- [ ] Hipótesis sin validar marcadas
- [ ] Ninguna funcionalidad ajena al MVP

## Protocolo
1. El metaprompt 01 genera primero `alm/prompts-generados/01-requisitos.md` sin producir las salidas.
2. El alumno inspecciona y aprueba el prompt operativo (gate A).
3. Claude ejecuta el prompt sobre archivos reales, mostrando diff y pruebas ejecutadas.
4. Se validan criterios mediante revisión/ejecución real; anotar fallos y correcciones.
5. Registrar evidencias y esperar aprobación humana final (gate B).

## Política de evidencias
No inventar URL de GitLab, número de issue, ejecución o cobertura. Marcar NO EJECUTADO cuando corresponda. Solo avanzar a fase siguiente cuando se cumplan los criterios o exista aceptación explícita y registrada de una limitación no bloqueante.
