# Protocolo del pipeline ALM generativo (no CI/CD)

**Secuencia:** 01 requisitos → 02 diseño → 03 desarrollo → 04 testing → 05 CI/entrega → 06 evolución → documentación/defensa.

**Por cada fase:**
1. Determinar fase y contrato en alm/contratos/.
2. Verificar existencia de entradas y detenerse si faltan.
3. Ejecutar metaprompt de alm/metaprompts/ en modo **generar un prompt operativo**.
4. Guardar prompt en alm/prompts-generados/NN-fase.md y presentar resumen de objetivos, archivos y riesgos.
5. Pedir **gate A: aprobación del plan**.
6. Ejecutar prompt aprobado, registrar exactamente qué archivos cambiaron y qué pruebas se ejecutaron.
7. Realizar verificaciones del contrato y registrar en alm/evidencias/registro.md.
8. Pedir **gate B: aprobación del resultado**, antes de avanzar.

Para cada laboratorio guiado, abre el metaprompt publicado del laboratorio en Claude (pega el bloque completo o indica su ruta y revisión). Conserva la respuesta que contiene el prompt, la aprobación explícita, el artefacto y su prueba. Registra el commit de entrada, los archivos leídos y el commit de la entrega aprobada. Comienza el laboratorio siguiente después de revisar esa entrega. En L10 registra por separado la preparación offline y cualquier ejecución real autorizada en GitLab.

**Criterio de bloqueo:** salidas inexistentes, inconsistencias funcionales, pruebas críticas fallidas, acceso remoto no comprobado o decisión de negocio no aprobada. Nunca generar «pasa» donde hay bloqueo. Las fases que requieran GitLab y carezcan de accesos se anotan como no ejecutadas.

**Gestión de cuota:** una arquitectura, una ejecución por fase y correcciones concretas. Guardar prompts y resultados; no enviar toda la biblioteca GitHub a Claude en cada paso.

**GitLab CI/CD** será un artefacto generado en la fase 05, no el motor que ejecuta este protocolo. En L10 sí hay llamadas API de Claude desde jobs GitLab, facturadas separadamente y sujetas a autorización de presupuesto.

## Modo automático L10 (independiente del modo guiado)

En modo automático **GitLab CI**, el alumno estudia el YAML sobre una rama aislada que parte de la plantilla inicial. **El formador aprueba y ejecuta una sola vez** el pipeline central con presupuesto y API propios. Los jobs GitLab ejecutan secuencialmente los pasos de cada contrato (metaprompt → prompt operativo → ejecución), comprueban las salidas y ejecutan las pruebas definidas. Si falla una verificación, la ejecución se detiene; nunca se autoriza automáticamente un merge. Esta regla solo se aplica a L10: GitLab Runner invoca Claude mediante API autorizada, no mediante sesión Pro. En L03–L09 permanecen las dos aprobaciones por fase.
