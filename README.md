#### Todos los videos:
- https://youtu.be/mDLfxfS1LoA  Ev07
- https://youtu.be/lHaWwOxL5ro  Ev08
- https://youtu.be/epdIPZ_sSco  Ev09
- https://youtu.be/Fl4qdM1U2kk  Ev10
- https://youtu.be/SJQyjImKjCc  Ev11

# Device Systems - API REST de Gestión de Usuarios

## Descripción

**device_systems** es una API REST desarrollada con FastAPI para la gestión de usuarios. La aplicación permite consultar, filtrar y registrar usuarios mediante endpoints HTTP, aplicando validaciones con Pydantic, parámetros de ruta (Path Parameters), parámetros de consulta (Query Parameters), modelos de respuesta (Response Models) y cabeceras HTTP personalizadas.

## Tecnologías Utilizadas

* Python 3
* FastAPI
* Uvicorn
* Pydantic v2


Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución del Proyecto

Iniciar el servidor:

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000
```

Documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

## Estructura del Proyecto

```text
device_systems/
│
├── app/
│   ├── main.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   └── routes/
│       └── user_routes.py
│
├── requirements.txt
└── README.md
```

## Endpoints Disponibles

| Método | Endpoint              | Descripción                |
| ------ | --------------------- | -------------------------- |
| GET    | /users                | Obtiene todos los usuarios |
| GET    | /users/{user_id}      | Obtiene un usuario por ID  |
| GET    | /users?role=admin     | Filtra usuarios por rol    |
| GET    | /users?is_active=true | Filtra usuarios por estado |
| POST   | /users                | Registra un nuevo usuario  |

---

# Evidencias de Funcionamiento

## Captura de Swagger UI


![Swagger UI](images/swagger.png)

---

## Evidencia GET /users

Solicitud:

```http
GET /users
```

Resultado esperado:

```json
[
  {
    "id": 1,
    "name": "Juan Perez",
    "email": "juan@test.com",
    "role": "admin",
    "is_active": true
  }
]
```

Captura:

![GET Users](images/rol1.png)
![GET Users](images/rol2.png)

---

## Evidencia GET /users/{user_id}

Solicitud:

```http
GET /users/1
```

Resultado esperado:

```json
{
  "id": 1,
  "name": "Juan Perez",
  "email": "juan@test.com",
  "role": "admin",
  "is_active": true
}
```

Captura:

![GET User By Id](images/id.png)

---

## Evidencia POST /users

Solicitud:

```json
{
  "id": 3,
  "name": "Carlos Ruiz",
  "email": "carlos@test.com",
  "role": "support",
  "is_active": true
}
```

Respuesta:

```json
{
  "id": 3,
  "name": "Carlos Ruiz",
  "email": "carlos@test.com",
  "role": "support",
  "is_active": true
}
```

Captura:

![POST User](images/post1.png)

---

# Evidencia de Validaciones y Errores

## Error por correo duplicado

Solicitud:

```json
{
  "id": 4,
  "name": "Pedro Lopez",
  "email": "juan@test.com",
  "role": "user",
  "is_active": true
}
```

Respuesta:

```json
{
  "detail": "Email already exists"
}
```

Captura:

![Duplicate Email](images/error_correo.png)

---

## Error por nombre inválido

Solicitud:

```json
{
  "id": 5,
  "name": "AB",
  "email": "ab@test.com",
  "role": "user",
  "is_active": true
}
```

Respuesta:

```json
{
  "detail": [
    {
      "type": "string_too_short"
    }
  ]
}
```

Captura:

![Name Validation](images/validacion_nombre.png)

---

## Error por correo inválido

Solicitud:

```json
{
  "id": 6,
  "name": "Pedro Perez",
  "email": "correo_invalido",
  "role": "user",
  "is_active": true
}
```

Respuesta:

```json
{
  "detail": [
    {
      "type": "value_error"
    }
  ]
}
```

Captura:

![Email Validation](images/validacion_correo.png)

---

## Error por rol inválido

Solicitud:

```json
{
  "id": 7,
  "name": "Pedro Perez",
  "email": "pedro@test.com",
  "role": "manager",
  "is_active": true
}
```

Respuesta:

```json
{
  "detail": [
    {
      "type": "literal_error"
    }
  ]
}
```

Captura:

![Role Validation](images/validacion_rol.png)

---

# Cabeceras HTTP Personalizadas

La API incluye las siguientes cabeceras en las respuestas:

```http
X-App-Name: device_systems
X-API-Version: 1.0
```

Estas cabeceras permiten identificar la aplicación y la versión de la API.

---

# Reflexión sobre el Uso de FastAPI para Construir APIs REST

Durante el desarrollo de esta actividad aprendí que FastAPI es un framework moderno que facilita la creación de APIs REST de forma rápida y organizada. Una de sus principales ventajas es la integración con Pydantic, que permite validar automáticamente los datos recibidos y reducir errores en la aplicación.

También comprendí la importancia de utilizar métodos HTTP adecuados, parámetros de ruta y parámetros de consulta para construir servicios más flexibles. La documentación automática generada mediante Swagger UI facilita las pruebas y la comprensión de los endpoints sin necesidad de herramientas adicionales.

Finalmente, esta práctica me permitió fortalecer conceptos relacionados con el desarrollo backend, validación de información, manejo de respuestas HTTP y diseño de servicios REST, competencias fundamentales para el desarrollo de aplicaciones modernas.

# Link Video

https://youtu.be/mDLfxfS1LoA


# EVO 8
## Descripción

device_systems es una API REST desarrollada con FastAPI para la gestión de usuarios.

La aplicación permite:

- Crear usuarios.
- Listar usuarios.
- Consultar usuarios por ID.
- Filtrar usuarios por rol y estado.
- Actualizar usuarios completamente mediante PUT.
- Actualizar usuarios parcialmente mediante PATCH.
- Eliminar usuarios mediante DELETE.

Además, implementa validaciones con Pydantic, manejo de errores con HTTPException, códigos de estado HTTP adecuados, Dependency Injection mediante Depends() y documentación automática con Swagger/OpenAPI.


---

## Explicación de la Estructura

### routes
Contiene los endpoints de la API.

### schemas
Contiene los modelos Pydantic utilizados para validar la información de entrada y salida.

### services
Contiene la lógica de negocio del recurso users.

### dependencies
Contiene funciones reutilizables implementadas mediante Dependency Injection utilizando Depends().

### data
Simula una base de datos en memoria mediante una lista de usuarios.

## Endpoints Disponibles

| Método | Endpoint | Descripción |
|----------|----------|----------|
| GET | /users | Obtener todos los usuarios |
| GET | /users/{user_id} | Obtener usuario por ID |
| GET | /users?role=admin | Filtrar por rol |
| GET | /users?is_active=true | Filtrar por estado |
| POST | /users | Crear usuario |
| PUT | /users/{user_id} | Actualizar usuario completamente |
| PATCH | /users/{user_id} | Actualizar parcialmente un usuario |
| DELETE | /users/{user_id} | Eliminar usuario |

## Uso de Dependency Injection

Se implementó Dependency Injection mediante Depends() para reutilizar lógica común dentro de la aplicación.

La función get_user_or_404() se utiliza para buscar un usuario por su identificador. Si el usuario existe, se devuelve el objeto correspondiente; de lo contrario, se genera una excepción HTTP 404.

Gracias a Depends(), esta lógica puede reutilizarse en diferentes endpoints sin duplicar código.

## Manejo de Errores

La API implementa manejo de errores mediante HTTPException.

Errores controlados:

- Usuario no encontrado.
- Correo electrónico duplicado.
- Actualización parcial sin datos.
- Eliminación de usuario inexistente.
- Validaciones automáticas mediante Pydantic.

Ejemplo:


{
  "detail": "User not found"
}


---

## 11. Agregar evidencias nuevas

La guía pide capturas adicionales.


# Evidencias de Funcionamiento

## Swagger UI

![imagen](images/AO8_6.png)

## ReDoc

![imagen](images/AO8_1.png)


## PUT /users/{user_id}

![imagen](images/AO8_4.png)

## PATCH /users/{user_id}

![imagen](images/AO8_3.png)

## DELETE /users/{user_id}

![imagen](images/AO8_2.png)

## Consola

![imagen](images/AO8_5.png)

# Reflexión Final

Durante esta actividad comprendí cómo una API REST puede evolucionar desde operaciones básicas de consulta y creación hacia una solución más completa y profesional.

Aprendí a implementar operaciones de actualización y eliminación mediante los métodos PUT, PATCH y DELETE, así como a utilizar códigos de estado HTTP adecuados para cada situación. También entendí la importancia del manejo de errores mediante HTTPException para proporcionar respuestas claras a los clientes de la API.

Otro aspecto importante fue el uso de Dependency Injection mediante Depends(), que permite reutilizar lógica y mejorar la organización del código. Finalmente, la documentación automática generada por Swagger UI y ReDoc facilitó la prueba y comprensión de todos los endpoints implementados.

Esta actividad fortaleció mis conocimientos sobre FastAPI, diseño de APIs REST y buenas prácticas de desarrollo backend.

# Link Video 2

https://youtu.be/lHaWwOxL5ro

# EVO9


## Descripción

device_systems es una API REST desarrollada con FastAPI para la gestión de usuarios.

En esta versión se incorporó persistencia de datos mediante SQLAlchemy y SQLite, permitiendo almacenar, consultar, actualizar y eliminar usuarios directamente desde una base de datos relacional.

La API implementa operaciones CRUD completas, validaciones con Pydantic, manejo de errores mediante HTTPException y documentación automática con Swagger/OpenAPI.

---

## Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic v2
- SQLite
- Swagger UI
- ReDoc

---

## Estructura del proyecto

```text
device_systems/
│
├── app/
│   ├── database/
│   │   └── connection.py
│   │
│   ├── dependencies/
│   │   └── database_dependency.py
│   │
│   ├── models/
│   │   └── user_model.py
│   │
│   ├── routes/
│   │   └── user_routes.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   └── main.py
│
├── device_systems.db
├── requirements.txt
└── README.md
```

### Evidencia de la estructura del proyecto

![imagen](images/EVO9.png)



Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Iniciar servidor:

```bash
uvicorn app.main:app --reload
```

Servidor:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Base de datos

La aplicación utiliza SQLite para almacenar los usuarios.

Archivo generado:

```text
device_systems.db
```

### Evidencia de la base de datos

![imagen](images/EVO9_2.png)


---

# Endpoints

| Método | Endpoint | Descripción |
|----------|----------|----------|
| GET | /users | Listar usuarios |
| GET | /users/{id} | Obtener usuario por ID |
| POST | /users | Crear usuario |
| PUT | /users/{id} | Actualizar usuario completo |
| PATCH | /users/{id} | Actualizar usuario parcialmente |
| DELETE | /users/{id} | Eliminar usuario |

---

# Ejemplos de uso

## Crear usuario

### Request

POST /users

```json
{
  "name": "Ivan Florez",
  "email": "ivan@test.com",
  "role": "admin",
  "is_active": true
}
```

### Response

```json
{
  "id": 1,
  "name": "Ivan Florez",
  "email": "ivan@test.com",
  "role": "admin",
  "is_active": true,
  "created_at": "2026-06-16T00:00:00"
}
```

### Evidencia

![imagen](images/EVO9_4.png)


---

## Listar usuarios

GET /users

### Evidencia

![imagen](images/EVO9_5.png)

---

## Consultar usuario por ID

GET /users/2

### Evidencia

![imagen](images/EVO9_6.png)

---

## Actualizar usuario completo

PUT /users/3

### Evidencia

![imagen](images/EVO9_7.png)


---

## Actualizar usuario parcialmente

PATCH /users/2

### Evidencia

![imagen](images/EVO9_8.png)


---

## Eliminar usuario

DELETE /users/1

### Evidencia

![imagen](images/EVO9_3.png)

---

# Validaciones y errores controlados

## Email duplicado

Código:

```text
400 Bad Request
```

Respuesta:

```json
{
  "detail": "Email already exists"
}
```

### Evidencia

![imagen](images/EVO9_9.png)


---

## Usuario no encontrado

Código:

```text
404 Not Found
```

Respuesta:

```json
{
  "detail": "User not found"
}
```

### Evidencia

![imagen](images/EVO9_10.png)


---

## Error de validación

Código:

```text
422 Unprocessable Entity
```

Ejemplo:

```json
{
  "name": "Juan",
  "email": "correo-invalido",
  "role": "admin",
  "is_active": true
}
```

### Evidencia

![imagen](images/EVO9_11.png)


---

# Diferencia entre modelo SQLAlchemy y schema Pydantic

## Modelo SQLAlchemy

El modelo SQLAlchemy representa la estructura de la tabla en la base de datos y permite realizar operaciones CRUD mediante el ORM.

Ejemplo:

```python
class User(Base):
```

Funciones principales:

- Crear tablas.
- Definir columnas.
- Aplicar restricciones.
- Realizar consultas.

## Schema Pydantic

Los schemas Pydantic validan la información que recibe y devuelve la API.

Ejemplo:

```python
class UserCreate(BaseModel):
```

Funciones principales:

- Validar datos.
- Validar correos electrónicos.
- Controlar formatos.
- Definir respuestas de la API.

---

# Swagger y ReDoc

FastAPI genera automáticamente la documentación de la API.

### Swagger UI

![imagen](images/EVO9_12.png)


### ReDoc

![imagen](images/EVO9_13.png)


---

# Reflexión final

Durante el desarrollo de esta actividad se evolucionó la API device_systems desde una implementación basada en estructuras de datos en memoria hacia una solución con persistencia real utilizando SQLAlchemy y SQLite.

La integración de SQLAlchemy permitió comprender el uso de ORM para trabajar con bases de datos relacionales desde Python, facilitando la creación de modelos, consultas y operaciones CRUD. Asimismo, el uso de schemas Pydantic ayudó a validar la información de entrada y salida de la API, mejorando la calidad y seguridad de los datos.

Finalmente, esta actividad permitió entender la importancia de la persistencia de datos en aplicaciones backend, así como la utilidad de FastAPI para construir APIs REST modernas, escalables y bien documentadas.



# Link video 3

https://youtu.be/epdIPZ_sSco



## EV10

# device_systems - EV10 FastAPI Avanzado


## Descripción del proyecto

Este proyecto corresponde a la evolución de la API `device_systems`, en la cual se implementan migraciones con Alembic, relaciones entre modelos (User, Device y Loan) y consultas avanzadas con joins y filtros. El sistema permite gestionar usuarios, dispositivos tecnológicos y préstamos de forma estructurada y escalable.

---

## Tecnologías utilizadas

- FastAPI
- SQLAlchemy
- Alembic
- MySQL
- Pydantic
- Swagger 

---

## Migraciones con Alembic

### Inicialización de Alembic
![imagen](images/EV10.png)
- alembic init alembic

### Creación de migración automática
![imagen](images/EV10_2.png)
- alembic revision --autogenerate -m "create devices and loans tables"

### Aplicación de migraciones
![imagen](images/EV10_3.png)
- alembic upgrade head

### Historial de migraciones
- alembic history
![imagen](images/EV10_4.png)
---

## Estructura de base de datos

![imagen](images/EV10_5.png)

- users
- devices
- loans

---

## Documentación API (Swagger)

![imagen](images/EV10_6.png)

- Users
- Devices
- Loans

---


Reflexión

La implementación de Alembic permitió gestionar cambios en la base de datos de forma controlada, asegurando la integridad de la información.

El uso de relaciones entre modelos facilitó la representación de escenarios reales como préstamos de dispositivos a usuarios.

Las consultas con joins y filtros avanzados mejoraron la capacidad de análisis de la información, permitiendo obtener datos combinados de múltiples tablas de forma eficiente.

Este proyecto demuestra la importancia de construir APIs escalables, mantenibles y basadas en buenas prácticas de desarrollo backend.

# Video 4
https://youtu.be/Fl4qdM1U2kk


## EV11 – Seguridad, autenticación y protección de endpoints

En esta evolución del proyecto device_systems se implementó una capa de seguridad para proteger la API REST. Se conservaron los recursos existentes de usuarios, dispositivos y préstamos, y se agregaron autenticación, autorización por roles, middleware, CORS y rate limiting.

# Funcionalidades implementadas

- Registro de usuarios con contraseña segura.
- Almacenamiento de contraseñas mediante hash con passlib y bcrypt.
- Inicio de sesión mediante OAuth2 y JWT.
- Generación de token de acceso tipo Bearer.
- Consulta de información del usuario autenticado.
- Protección de rutas mediante token JWT.
- Control de acceso por roles: admin, support y user.
- Validaciones avanzadas con Pydantic v2.
- Middleware personalizado para trazabilidad de peticiones.
- Configuración CORS para permitir clientes autorizados.
- Rate limiting para limitar solicitudes repetidas.
- Migración Alembic para agregar el campo hashed_password a la tabla  users.

# Estructura agregada para seguridad

- app/
- │── auth/
- │   ├── auth_routes.py
- │   ├── auth_service.py
- │   └── security.py
- │
- │── dependencies/
- │   └── auth_dependency.py
- │
- │── middlewares/
- │   └── request_middleware.py
- │
- │── schemas/
- │   └── auth_schema.py
- │
- │── .env
- │── .env.example
`
# Dependencias de seguridad
 
Las siguientes dependencias fueron agregadas al proyecto:

- python-jose[cryptography]
- passlib[bcrypt]
- slowapi
- python-multipart
- python-dotenv
- Variables de entorno
----
El proyecto utiliza un archivo .env para almacenar configuraciones sensibles, como la clave secreta usada para firmar los tokens JWT.

Ejemplo del archivo .env.example:
``
SECRET_KEY=coloca_una_clave_secreta_segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
``

El archivo .env no debe subirse al repositorio, ya que contiene información sensible.

# Migración de autenticación

Se creó una migración con Alembic para agregar el campo hashed_password a la tabla users.

- Comandos utilizados:

alembic revision --autogenerate -m "add authentication fields to users"
alembic upgrade head

La contraseña no se guarda en texto plano. Antes de registrar un usuario, se convierte en un hash seguro utilizando passlib.

# Registro de usuario

- Endpoint:

``
POST /auth/register
``

Ejemplo de solicitud:

``{
  "name": "Ivan Florez",
  "email": "ivan@example.com",
  "password": "ClaveSegura123",
  "role": "admin",
  "is_active": true
}``

### La contraseña debe cumplir las siguientes reglas:

- Tener mínimo 8 caracteres.
- Tener al menos una letra mayúscula.
- Tener al menos una letra minúscula.
- Tener al menos un número.
- No contener espacios.
- Inicio de sesión

### Endpoint:
``
POST /auth/login
``

- Ejemplo de solicitud:

{
  "email": "ivan@example.com",
  "password": "ClaveSegura123"
}

- Ejemplo de respuesta:

{
  "access_token": "token_jwt_generado",
  "token_type": "bearer"
}

El token generado debe enviarse en las solicitudes protegidas mediante el encabezado:

Authorization: Bearer TOKEN_JWT
Usuario autenticado

- Endpoint:

GET /auth/me

Este endpoint retorna la información del usuario autenticado a partir del token JWT enviado.

La respuesta no expone el campo hashed_password.

Roles y autorización

## La API maneja los siguientes roles:

Rol	Permisos principales
admin	Administración completa de usuarios, dispositivos y préstamos.
support	Gestión de dispositivos y préstamos según los permisos configurados.
user	Consulta de información permitida y creación de préstamos autenticados.

Las rutas protegidas implementan validación de token y validación de rol.

## Ruta	Protección aplicada
- GET /users	Usuario autenticado
- GET /users/{user_id}	Usuario autenticado
- POST /devices	Rol admin o support
- PUT /devices/{device_id}	Rol admin o support
- DELETE /devices/{device_id}	Rol admin
- POST /loans	Usuario autenticado
- PATCH /loans/{loan_id}/return	Rol admin o support
- GET /loans/details	Rol admin o support

Cuando no se envía un token o el token no es válido, la API responde con:

#### 401 Unauthorized

Cuando el usuario está autenticado, pero no tiene el rol necesario, la API responde con:

#### 403 Forbidden
Configuración CORS

Se configuró CORSMiddleware para permitir solicitudes desde clientes locales durante el desarrollo.

Orígenes permitidos:

- http://localhost:5173
- http://localhost:3000
---
La configuración permite credenciales, métodos y cabeceras necesarias para que un frontend autorizado pueda consumir la API.

En producción no se recomienda usar allow_origins=["*"] cuando allow_credentials=True, porque permitiría solicitudes desde cualquier origen y aumentaría el riesgo de accesos no autorizados. En un entorno real se deben definir únicamente los dominios confiables.

### Middleware personalizado

Se implementó un middleware global para mejorar la trazabilidad de las solicitudes.

El middleware realiza las siguientes acciones:

- Mide el tiempo de procesamiento de cada petición.
- Agrega la cabecera X-Process-Time.
- Agrega la cabecera X-App-Name: device_systems.
- Genera o conserva la cabecera X-Request-ID.
- Registra el método HTTP, la ruta y el código de estado de cada petición.

Ejemplo de cabeceras generadas:

- X-App-Name: device_systems
- X-Process-Time: 0.0042
- X-Request-ID: 8f42e9c1
----
### Rate limiting

Se implementó rate limiting con slowapi para limitar la cantidad de solicitudes realizadas por un cliente.

Límites configurados:

- Endpoint	Límite
- POST /auth/login	5 solicitudes por minuto
- POST /auth/register	3 solicitudes por minuto
- GET /users	30 solicitudes por minuto
- POST /loans	10 solicitudes por minuto

Cuando se supera el límite, la API responde con:

429 Too Many Requests
Pruebas funcionales realizadas

### Durante las pruebas se validaron los siguientes escenarios:

- Registro de usuario con contraseña segura.
- Registro rechazado con contraseña débil.
- Registro rechazado con correo duplicado.
- Inicio de sesión correcto y generación de token JWT.
- Inicio de sesión rechazado con contraseña incorrecta.
- Consulta de GET /auth/me.
- Acceso a ruta protegida sin token.
- Acceso a ruta protegida con token inválido.
- Acceso denegado para un usuario sin el rol requerido.
- Creación de dispositivo con rol permitido.
- Intento de eliminación de dispositivo con rol no permitido.
- Validación de configuración CORS.
- Validación de cabeceras generadas por middleware.
- Prueba de rate limiting.
- Verificación de Swagger/OpenAPI con OAuth2.

## Evidencias


Luego agregar las imágenes al README:

# Estructura
![Estructura del proyecto](images/EV11/estructura_proyecto.png)

# Migracion
![Migración Alembic aplicada](images/EV11/migracion_alembic.png)

# Registro de usuario
![Registro de usuario](images/EV11/resgistro_usuario.png)

# Login y Token Jwt
![Login y token JWT](images/EV11/login_token.png)

# Consulta de Usuario autenticado
![Consulta de usuario autenticado](images/EV11/auth_me.png)

# Acceso con rol no permitido
![Acceso con rol no permitido](images/EV11/acceso_rol_no_permitido.png)

# OAuth2
![Swagger con OAuth2](images/EV11/swagger_oauth2.png)

## Reflexión final

La implementación de seguridad en una API REST es necesaria para proteger los recursos y controlar quién puede acceder a cada funcionalidad.

El uso de hash de contraseñas evita almacenar credenciales en texto plano. JWT permite autenticar usuarios sin mantener sesiones en el servidor, mientras que la autorización por roles permite restringir operaciones según las responsabilidades de cada usuario.

Además, CORS controla qué clientes pueden consumir la API, el middleware mejora la trazabilidad de las solicitudes y el rate limiting ayuda a prevenir abuso o ataques de fuerza bruta en endpoints sensibles como el inicio de sesión.

## Video 5
https://youtu.be/SJQyjImKjCc