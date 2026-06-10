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


# AO8
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