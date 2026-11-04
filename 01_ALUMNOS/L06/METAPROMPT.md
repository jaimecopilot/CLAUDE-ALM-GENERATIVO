# L06 · METAPROMPT DE PRUEBAS Y VERIFICACIÓN

~~~text
Rol: diseñador de un prompt operativo de calidad y testing para una aplicación generada con IA.
MODO: redactar instrucciones, NO modificar código ni tests todavía.

Entradas reales obligatorias:
- contrato alm/contratos/04-testing.md
- docs/requisitos/especificacion.md con RF y CA identificados
- código actual de app/ y tests/ (no asumir una estructura que no has leído)
- diseño y ADR aprobados

Produce alm/prompts-generados/04-testing.md, que deberá indicar:
1. Mapa CA → tipo de prueba → archivo propuesto.
2. Casos unitarios del algoritmo de solapamiento y tests de integración de API.
3. Procedimiento para instalar dependencias y ejecutar pytest con resultados textuales.
4. Escenarios normales, negativos, de límite, cancelación y sala inexistente.
5. Protocolo de fallo: clasificar → diagnosticar → corregir código → volver a ejecutar.
6. Prohibición de cambiar una aserción correcta para conseguir un test verde.
7. Cobertura medida solo si hay herramienta y ejecución real; sin porcentajes inventados.
8. Revisión básica de secretos, validación de entrada y tratamiento de errores.
9. Registro de informe docs/calidad/informe.md y matriz de pruebas.
10. Gate humano y no avance cuando un criterio obligatorio falla.

No declares seguridad de producción. No escribas tests todavía: espera autorización explícita tras generar el prompt operativo.
~~~

## Revisión
El prompt incluye criterios provenientes de requisitos, comandos comprobables y un mecanismo de corrección que no altere las reglas de negocio.