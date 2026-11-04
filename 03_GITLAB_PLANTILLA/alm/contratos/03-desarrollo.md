# Contrato 03 — DESARROLLO

**Actividad formativa origen:** L05. **Tipo:** contrato de una fase; NO contiene el artefacto final prehecho.

## Entradas que deben existir
- docs/requisitos/especificacion.md
- docs/arquitectura/diseno.md
- docs/arquitectura/ADR-001.md

## Salidas que Claude debe producir tras autorización
- app/ (módulos Python)
- requirements.txt actualizado
- README.md de ejecución

## Criterios de validación obligatorios
- [ ] Endpoints de salas, reservas y cancelación
- [ ] Solapamiento en una sola sala
- [ ] Persistencia y validaciones
- [ ] Errores observables 200/201/204/404/409/422 según contrato
- [ ] Ejecución local y revisión de diff

## Protocolo
1. El metaprompt 03 genera primero `alm/prompts-generados/03-desarrollo.md` sin producir las salidas.
2. El alumno inspecciona y aprueba el prompt operativo (gate A).
3. Claude ejecuta el prompt sobre archivos reales, mostrando diff y pruebas ejecutadas.
4. Se validan criterios mediante revisión/ejecución real; anotar fallos y correcciones.
5. Registrar evidencias y esperar aprobación humana final (gate B).

## Política de evidencias
No inventar URL de GitLab, número de issue, ejecución o cobertura. Marcar NO EJECUTADO cuando corresponda. Solo avanzar a fase siguiente cuando se cumplan los criterios o exista aceptación explícita y registrada de una limitación no bloqueante.
