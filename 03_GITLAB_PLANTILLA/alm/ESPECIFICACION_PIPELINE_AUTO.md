# Contrato docente del pipeline ALM automático — L10

## Objetivo
En L10 cada alumno debe **crear un pipeline declarativo** \`alm/pipeline_auto.json\` con Claude a partir de los seis contratos y metaprompts manuales. El ejecutor \`scripts/alm_auto.py\`, preparado para evitar permisos peligrosos, interpreta ese archivo y desencadena **las seis fases ALM** de forma secuencial.

No se proporciona \`pipeline_auto.json\` resuelto: Claude debe generarlo, el alumno debe revisarlo y el script valida el contrato antes de ejecutarlo.

## Esquema JSON exacto
~~~json
{
  "version": 1,
  "mode": "automatico-local",
  "stages": [
    {
      "id": "01",
      "name": "requisitos",
      "contract": "alm/contratos/01-requisitos.md",
      "metaprompt": "alm/metaprompts/01-requisitos.md",
      "prompt_out": "alm/prompts-generados/01-requisitos.md",
      "outputs": ["docs/requisitos/especificacion.md", "docs/requisitos/backlog.md"]
    }
  ]
}
~~~

El ejemplo enseña una sola fase. La configuración final debe tener **seis fases en orden exacto** (01 requisitos, 02 diseno, 03 desarrollo, 04 testing, 05 devops, 06 evolucion). Para cada una:
- \`contract\`: \`alm/contratos/NN-nombre.md\`.
- \`metaprompt\`: \`alm/metaprompts/NN-nombre.md\`.
- \`prompt_out\`: \`alm/prompts-generados/NN-nombre.md\`.
- \`outputs\`: rutas exactas exigidas por \`scripts/alm_auto.py\`. Se pueden leer en \`PHASES\` de ese archivo y en los contratos.
- No se permiten campos adicionales ni comandos arbitrarios en JSON.

## Contratos de entrada y flujo de los artefactos
1. **01 → 02:** los requisitos y backlog aprobados alimentan el diseño.
2. **01+02 → 03:** especificación + arquitectura + ADR alimentan el código.
3. **01+03 → 04:** requisitos + código alimentan tests y matriz.
4. **03+04 → 05:** código + tests + informe alimentan GitLab CI/CD.
5. **01+03+04+05 → 06:** requisito de cambio CAM-01 sobre la implementación y pruebas ya generadas.

La ejecución **automática no puede sustituir con ejemplos inventados** los resultados de las fases anteriores. Tampoco «pasa CI remoto» por generar un YAML. Solo al hacer push y comprobar un pipeline real de GitLab se dispone de esa evidencia.

## Paradas y autorizaciones
- En el modo manual L03–L09 hay **dos gates humanos por fase**.
- En el modo automático L10 hay **una aprobación global al inicio**; el ejecutor comprueba rutas, RF y pytest y se detiene si una fase falla.
- Un gate técnico automático NO equivale a la validación de negocio humana: al terminar se compara el resultado, y jamás se hace merge automático.
- Los outputs se guardan en la rama automática, separada de la manual.
- Si un límite de cuota interrumpe el proceso, se conserva \`.alm-run/estado.json\` y se reanuda con \`--resume\`. La ejecución no se declara completa mientras haya un bloqueo.

## Autenticación y costes
El script usa la CLI **sin modificaciones** instalada por el propio alumno; inicia sesión mediante \`claude auth login\`. No almacena credenciales ni recopila tokens. Impide \`ANTHROPIC_API_KEY\` para no desencadenar facturación API inesperada. **No utilizar \`--bare\`** en esta modalidad, porque esa opción exige credenciales API. La cuenta Claude Pro tiene límites de uso; no se garantiza que todos terminen una segunda generación completa bajo una sola cuota.

## Alternativa no incluida en presupuesto
Un pipeline que llame a Claude **dentro de los runners remotos de GitLab** requiere la integración oficial con claves API facturadas (o proveedores cloud), no la suscripción personal Pro. Puede explicarse conceptualmente, pero este laboratorio ejecuta la automatización local, y GitLab CI/CD se ocupa de pruebas/entrega.
