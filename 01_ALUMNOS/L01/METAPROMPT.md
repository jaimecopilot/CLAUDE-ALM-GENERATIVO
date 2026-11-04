# L01 · METAPROMPT: generar un prompt de exploración acotado

## Uso
Este metaprompt es un ejercicio preparatorio. En L02 se establece el protocolo definitivo metaprompt → prompt operativo → artefacto → validación.

~~~text
Actúa como diseñador de experimentos para desarrolladores junior. Debes GENERAR UN PROMPT OPERATIVO, sin escribir código todavía. Objetivo: explorar con Claude un prototipo de reserva de salas y detectar supuestos no especificados.

Entrada: idea de negocio «gestor simple de reservas de salas de un coworking».
Salidas del prompt que vas a redactar:
1. Lista de supuestos que la IA tendría que inventar.
2. Propuesta de prototipo mínimo sin autenticación ni facturación.
3. Tres escenarios de error susceptibles de comprobarse.
4. Tabla que distinga observado, supuesto y pendiente de prueba.

Restricciones: no afirmar que se han ejecutado tests; no inventar capturas ni URL; no añadir funcionalidades. Formula un solo prompt operativo de menos de 500 palabras.
Guarda ese prompt operativo en el espacio de trabajo y solicita autorización antes de ejecutarlo.
~~~

## Verificación
El prompt generado debe indicar qué petición recibe, qué salida espera, qué no debe inventar y cómo se anotará el resultado. Si Claude devuelve directamente el código, corrígelo: «Te pedí el prompt operativo, no la solución».