from fastapi import (
    APIRouter,
    Depends,
    Query,
    Response,
    status
)

from sqlalchemy.orm import Session

from app.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserPatch,
    UserResponse
)

from app.dependencies.database_dependency import get_db

from app.services.user_service import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    patch_user,
    delete_user
)

router = APIRouter(
    prefix="",
    tags=["Users"]
)


def add_headers(response: Response):
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "3.0"


@router.get(
    "/users",
    response_model=list[UserResponse],
    summary="List users",
    description="Returns all users with optional filters",
    response_description="List of users"
)
def get_users(
    response: Response,
    role: str | None = Query(default=None),
    is_active: bool | None = Query(default=None),
    sort: str | None = Query(default=None),
    db: Session = Depends(get_db)
):

    add_headers(response)

    return get_all_users(
        db,
        role,
        is_active,
        sort
    )


@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
    summary="Get user by ID",
    description="Returns a user by its ID",
    response_description="User found"
)
def get_user(
    user_id: int,
    response: Response,
    db: Session = Depends(get_db)
):

    add_headers(response)

    return get_user_by_id(
        db,
        user_id
    )


@router.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create user",
    description="Creates a new user",
    response_description="User created successfully"
)
def create_new_user(
    user: UserCreate,
    response: Response,
    db: Session = Depends(get_db)
):

    add_headers(response)

    return create_user(
        db,
        user
    )


@router.put(
    "/users/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Update user completely",
    description="Replaces all user information",
    response_description="User updated successfully"
)
def replace_user(
    user_id: int,
    user: UserUpdate,
    response: Response,
    db: Session = Depends(get_db)
):

    add_headers(response)

    return update_user(
        db,
        user_id,
        user
    )


@router.patch(
    "/users/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Update user partially",
    description="Updates one or more user fields",
    response_description="User updated successfully"
)
def modify_user(
    user_id: int,
    user: UserPatch,
    response: Response,
    db: Session = Depends(get_db)
):

    add_headers(response)

    update_data = user.model_dump(
        exclude_unset=True
    )

    return patch_user(
        db,
        user_id,
        update_data
    )


@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete user",
    description="Deletes a user from the database",
    response_description="User deleted successfully"
)
def remove_user(
    user_id: int,
    response: Response,
    db: Session = Depends(get_db)
):

    add_headers(response)

    return delete_user(
        db,
        user_id
    )