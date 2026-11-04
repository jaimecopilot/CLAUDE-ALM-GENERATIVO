# Presupuesto de Claude Pro y Claude API — 16 horas, 12 alumnos

**Fecha de referencia:** 4 de noviembre de 2026. **Moneda:** USD, antes de impuestos. **Estado:** presupuesto de planificación, **no** medición empírica de una ejecución completa.

## Premisa técnica

- **L01–L09, modo guiado:** cada alumno utiliza su suscripción Claude Pro y ejecuta Claude Code en su propio ordenador. La suscripción no incluye el coste de API del GitLab Runner.
- **L10, modo automático:** Claude genera el YAML inicial, pero **GitLab Runner** ejecuta los seis jobs generativos y llama a Claude mediante **Anthropic API** con una clave autorizada. La facturación es independiente de Pro.
- **GitLab Free:** 400 minutos de cómputo al mes por namespace personal (si usa runners sujetos a esa cuota). La duración real de seis fases puede consumir una parte relevante de esos minutos y no se garantiza su suficiencia.

## Precios de referencia y modelo

Modelo elegido para presupuestar: **Claude Sonnet 5.5**. Tarifa API estándar publicada por Anthropic:
- Entrada: **2 USD por millón de tokens**.
- Salida: **10 USD por millón de tokens**.
- Prompt caching, relecturas, escritura de caché y otras funciones se facturan según sus condiciones; no se omite su impacto al presupuestar.

Fuentes oficiales:
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/es/models/sonnet-5-5/overview
- https://docs.gitlab.com/ci/pipelines/compute_minutes/
- https://support.claude.com/es/articles/8977456-como-pago-mi-uso-de-la-api-de-claude

## Estimación de una ejecución completa del pipeline de seis fases

\[
\text{Coste base}=\frac{\text{tokens de entrada}}{10^6}\cdot2+
\frac{\text{tokens de salida}}{10^6}\cdot10
\]

| Escenario supuesto | Entrada total | Salida total | Coste base de IA |
|---|---:|---:|---:|
| Contenido breve, pocas correcciones | 500.000 | 100.000 | **2 USD** |
| Referencia docente con generación completa | 1.500.000 | 300.000 | **6 USD** |
| Agentes con relecturas y reparaciones | 3.000.000 | 800.000 | **14 USD** |

**Estos volúmenes son hipótesis de planificación**, no consumos de un piloto observado. Claude Code puede realizar varias solicitudes por fase; el uso real, las herramientas y la caché varían. Por tanto, los importes de la tabla no son precios cerrados ni garantía de ejecución.

## Presupuesto recomendado

**Reservar 20 USD de créditos API por alumno** para un intento completo y una pequeña contingencia, con Sonnet 5.5. No significa que cada intento consuma 20 USD ni garantiza que una ejecución muy larga no agote el saldo.

| Partida | Unidades | Unidad | Presupuesto |
|---|---:|---:|---:|
| Suscripción Claude Pro alumnos | 12 | 20 USD | **240 USD** |
| Créditos API alumnos para L10 | 12 | 20 USD | **240 USD** |
| **Subtotal alumnos** | | | **480 USD** |
| Suscripción Pro formador, si se necesita | 1 | 20 USD | 20 USD |
| Crédito API formador para demostración, si se necesita | 1 | 20 USD | 20 USD |
| **Total incluyendo ambas reservas del formador** | | | **520 USD** |

No incluye impuestos, honorarios, equipos, red, ni ampliaciones de cuota o minutos de runner. Si el formador ya tiene suscripción, si el saldo API no se consume, o si se financia centralmente, distinguir **cantidad reservada** de **gasto efectivo**.

## Control práctico de gasto

1. Cada alumno usa una organización Claude Console propia para comprar créditos o recibe acceso a una configuración **autorizada y aislada por administrador**. Nunca distribuir una única clave del formador entre repositorios administrados por alumnos.
2. Preferir **créditos prepagados**. La documentación de Anthropic indica que la mayoría de organizaciones usan prepago y que, cuando el saldo se agota, las llamadas se detienen.
3. **Desactivar recarga automática**, para no comprar nuevos créditos inadvertidamente.
4. Configurar **límite mensual de gasto por workspace** y alertas cuando corresponda (es una protección adicional, no sustituye al saldo prepago).
5. En GitLab guardar la clave como variable CI/CD enmascarada, idealmente oculta y restringida. **Enmascarar no protege contra código de pipeline malicioso**: revisar el YAML antes de ejecutarlo y no exponer credenciales en trabajos no confiables.
6. Limitar el pipeline a **un disparo manual**, turnos/modelo fijado, timeouts de jobs, una ejecución activa por proyecto y reintentos explícitamente autorizados.
7. Si se agota el saldo o falla un gate, registrar **BLOQUEADO** y no afirmar que las seis fases se completaron.

## Conclusión económica

Para el programa de **12 alumnos y 16 horas**, la reserva docente recomendada asciende a **480 USD sin impuestos**, o **520 USD** si añadimos una suscripción Pro y créditos API específicos para el formador. Este presupuesto cubre la previsión de licencias y créditos, no asegura que la API o los runners completen todos los trabajos; el consumo se debe medir en una ejecución real.

**No confundir el límite mensual de workspace con un límite exacto por job.** Un trabajo ya iniciado puede consumir más de lo previsto antes de reflejarse en los informes. El saldo prepago sin recarga automática es la principal protección de gasto en una cuenta independiente.

## Compatibilidad con la metodología

El alumno mantiene sus dos experiencias: en L03–L09 ejecuta ALM guiado desde Claude Code con Pro; en L10 **GitLab lanza los metaprompts y consume los artefactos anteriores dentro de una ejecución automatizada separada**, con API y presupuesto autorizados. En ningún caso se entrega una especificación nueva inconexa para desarrollo, ni se reutiliza código de la rama manual como si se hubiera generado automáticamente.
