# Caso único de negocio: Coworking Norte

## Solicitud inicial del cliente
El coworking dispone de salas de reuniones. El personal necesita consultar salas, crear reservas para un intervalo, evitar que una misma sala tenga dos reservas activas solapadas y cancelar una reserva para dejar libre su intervalo.

## Restricciones de producto aceptadas para el taller
- El MVP no tiene gestión de identidades, membresías, facturación ni eventos.
- Se usa una sola aplicación FastAPI con base SQLite; el objetivo es uso didáctico local.
- El intervalo temporal utiliza la convención **[inicio,fin)**; dos reservas contiguas son compatibles.
- Dos reservas activas colisionan si corresponden a la misma sala y los intervalos se intersectan.
- Las reservas canceladas dejan de bloquear disponibilidad.
- Los datos de entrada deben tener fechas con zona horaria o normalización explícita; no se aceptan ventanas vacías o invertidas.
- Los códigos HTTP deben documentarse coherentemente y verificarse en tests.

## Cambio posterior (NO introducir antes de L08)
**CAM-01:** una reserva no puede superar cuatro horas consecutivas; exactamente cuatro horas se permiten. Este requisito se libera por el formador solo durante L08.

## Material que Claude debe generar
No se adjunta aquí especificación funcional completa ni código. El alumno utilizará los metaprompts para generar especificación, arquitectura, aplicación, pruebas y entrega a partir de estas reglas y de las aclaraciones del formador.
