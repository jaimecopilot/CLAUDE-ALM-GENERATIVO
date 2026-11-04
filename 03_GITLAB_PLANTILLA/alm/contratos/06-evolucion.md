# Contrato 06 — EVOLUCION

**Actividad formativa origen:** L08. **Tipo:** contrato de una fase; NO contiene el artefacto final prehecho.

## Entradas que deben existir
- docs/requisitos/especificacion.md
- app/
- tests/
- .gitlab-ci.yml
- docs/calidad/informe.md

## Salidas que Claude debe producir tras autorización
- docs/requisitos/especificacion.md actualizado
- app/ actualizado
- tests/ ampliados
- docs/entrega/cambio-CAM-01.md

## Criterios de validación obligatorios
- [ ] Límite de 4 h reconocido por requisitos
- [ ] 3h59 y 4h aceptadas, 4h01 rechazada
- [ ] Regresión sin romper RF originales
- [ ] MR y CI de cambio verificables
- [ ] Impacto y decisión humana documentados

## Protocolo
1. El metaprompt 06 genera primero `alm/prompts-generados/06-evolucion.md` sin producir las salidas.
2. El alumno inspecciona y aprueba el prompt operativo (gate A).
3. Claude ejecuta el prompt sobre archivos reales, mostrando diff y pruebas ejecutadas.
4. Se validan criterios mediante revisión/ejecución real; anotar fallos y correcciones.
5. Registrar evidencias y esperar aprobación humana final (gate B).

## Política de evidencias
No inventar URL de GitLab, número de issue, ejecución o cobertura. Marcar NO EJECUTADO cuando corresponda. Solo avanzar a fase siguiente cuando se cumplan los criterios o exista aceptación explícita y registrada de una limitación no bloqueante.
