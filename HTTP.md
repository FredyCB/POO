# HTTP
## Métodos HTTP y códigos de estado comunes

### GET
Descripción: Solicita un recurso del servidor.

Identidad: Sí.

Códigos de estado comunes:
- 200 OK: Solicitud exitosa, recurso recuperado correctamente.
- 304 Not Modified: El recurso no ha cambiado desde la última solicitud.

### POST
Descripción: Envía datos al servidor para crear un recurso.

Idempotencia: No.

Códigos de estado comunes:
- 201 Created: Recurso creado exitosamente.
- 400 Bad Request: Error en la solicitud, los datos enviados no son válidos.
- 409 Conflict: Conflicto con el estado actual del recurso (e.g., un elemento ya existe).

### PUT
Descripción: Reemplaza un recurso existente o lo crea si no existe.

Idempotencia: Sí.

Códigos de estado comunes:
- 200 OK: Recurso actualizado correctamente.
- 201 Created: El recurso fue creado porque no existía previamente.
- 400 Bad Request: Datos inválidos o incorrectos en la solicitud.

### PATCH
Descripción: Modifica parcialmente un recurso existente.

Idempotencia: No.

Códigos de estado comunes:
- 200 OK: Recurso actualizado correctamente.
- 400 Bad Request: Datos inválidos en la solicitud.
- 404 Not Found: El recurso solicitado no fue encontrado.

### DELETE
Descripción: Elimina un recurso del servidor.

Idempotencia: Sí.

Códigos de estado comunes:
- 200 OK: Recurso eliminado exitosamente.
- 204 No Content: Eliminación exitosa, sin contenido en la respuesta.
- 404 Not Found: El recurso no fue encontrado.

**Nota:** Un método idempotente es aquel que puede ser ejecutado múltiples veces sin cambiar el estado del servidor.

## Otros códigos de estado
- 401 Unauthorized: El cliente debe autenticarse para obtener la respuesta solicitada.
- 403 Forbidden: El cliente no tiene permiso para acceder al recurso.
- 405 Method Not Allowed: Método no permitido para el recurso solicitado.
- 500 Internal Server Error: Error interno del servidor.
- 503 Service Unavailable: El servidor no puede manejar la solicitud en este momento.
