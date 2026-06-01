from fastapi import APIRouter, HTTPException, Query, Response
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter(tags=["Users"])

# Base de datos temporal en memoria
users = [
    {
        "id": 1,
        "name": "Juan Perez",
        "email": "juan@test.com",
        "role": "admin",
        "is_active": True
    },
    {
        "id": 2,
        "name": "Maria Gomez",
        "email": "maria@test.com",
        "role": "user",
        "is_active": False
    }
]


def add_headers(response: Response):
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"


@router.get(
    "/users",
    response_model=list[UserResponse]
)
def get_users(
    response: Response,
    role: str | None = Query(default=None),
    is_active: bool | None = Query(default=None)
):
    add_headers(response)

    result = users

    if role is not None:
        result = [user for user in result if user["role"] == role]

    if is_active is not None:
        result = [
            user for user in result
            if user["is_active"] == is_active
        ]

    return result


@router.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def get_user(user_id: int, response: Response):
    add_headers(response)

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@router.post(
    "/users",
    response_model=UserResponse,
    status_code=201
)
def create_user(user: UserCreate, response: Response):
    add_headers(response)

    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    new_user = user.model_dump()

    users.append(new_user)

    return new_user