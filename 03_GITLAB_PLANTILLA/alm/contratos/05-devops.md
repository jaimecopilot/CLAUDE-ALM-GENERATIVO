# Contrato 05 — DEVOPS

**Actividad formativa origen:** L07. **Tipo:** contrato de una fase; NO contiene el artefacto final prehecho.

## Entradas que deben existir
- app/
- tests/
- requirements.txt
- docs/calidad/informe.md

## Salidas que Claude debe producir tras autorización
- .gitlab-ci.yml
- docs/entrega/informe.md

## Criterios de validación obligatorios
- [ ] YAML específico GitLab
- [ ] Jobs verifican tests
- [ ] No usa secretos de Claude en GitLab CI
- [ ] Artefacto reproducible o informe
- [ ] Estado CI real documentado, o bloqueo explícito

## Protocolo
1. El metaprompt 05 genera primero `alm/prompts-generados/05-devops.md` sin producir las salidas.
2. El alumno inspecciona y aprueba el prompt operativo (gate A).
3. Claude ejecuta el prompt sobre archivos reales, mostrando diff y pruebas ejecutadas.
4. Se validan criterios mediante revisión/ejecución real; anotar fallos y correcciones.
5. Registrar evidencias y esperar aprobación humana final (gate B).

## Política de evidencias
No inventar URL de GitLab, número de issue, ejecución o cobertura. Marcar NO EJECUTADO cuando corresponda. Solo avanzar a fase siguiente cuando se cumplan los criterios o exista aceptación explícita y registrada de una limitación no bloqueante.
