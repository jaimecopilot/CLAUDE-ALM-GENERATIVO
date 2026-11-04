# Contrato 04 — TESTING

**Actividad formativa origen:** L06. **Tipo:** contrato de una fase; NO contiene el artefacto final prehecho.

## Entradas que deben existir
- docs/requisitos/especificacion.md
- app/ (código generado)
- tests/ existentes si los hay

## Salidas que Claude debe producir tras autorización
- tests/ (pytest)
- docs/calidad/matriz-pruebas.md
- docs/calidad/informe.md

## Criterios de validación obligatorios
- [ ] CA → prueba
- [ ] pytest ejecutado con salida real
- [ ] Casos límite y fallos cubiertos
- [ ] Revisión de seguridad básica
- [ ] Errores no ocultos alterando tests

## Protocolo
1. El metaprompt 04 genera primero `alm/prompts-generados/04-testing.md` sin producir las salidas.
2. El alumno inspecciona y aprueba el prompt operativo (gate A).
3. Claude ejecuta el prompt sobre archivos reales, mostrando diff y pruebas ejecutadas.
4. Se validan criterios mediante revisión/ejecución real; anotar fallos y correcciones.
5. Registrar evidencias y esperar aprobación humana final (gate B).

## Política de evidencias
No inventar URL de GitLab, número de issue, ejecución o cobertura. Marcar NO EJECUTADO cuando corresponda. Solo avanzar a fase siguiente cuando se cumplan los criterios o exista aceptación explícita y registrada de una limitación no bloqueante.
