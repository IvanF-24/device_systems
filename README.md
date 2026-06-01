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
