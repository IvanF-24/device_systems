from fastapi import (
    APIRouter,
    Depends,
    Query,
    Response,
    status
)

from app.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserPatch,
    UserResponse
)

from app.dependencies.user_dependencies import (
    get_user_or_404
)

from app.services.user_service import (
    get_all_users,
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
    response.headers["X-API-Version"] = "2.0"


@router.get(
    "/users",
    response_model=list[UserResponse],
    summary="List users",
    description="Returns all users",
    response_description="List of users"
)
def get_users(
    response: Response,
    role: str | None = Query(default=None),
    is_active: bool | None = Query(default=None)
):

    add_headers(response)

    return get_all_users(role, is_active)


@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
    summary="Get user by id"
)
def get_user(
    response: Response,
    user=Depends(get_user_or_404)
):

    add_headers(response)

    return user


@router.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create user"
)
def create_new_user(
    user: UserCreate,
    response: Response
):

    add_headers(response)

    return create_user(user.model_dump())


@router.put(
    "/users/{user_id}",
    response_model=UserResponse,
    summary="Update user completely"
)
def replace_user(
    user_id: int,
    user: UserUpdate,
    response: Response
):

    add_headers(response)

    return update_user(
        user_id,
        user.model_dump()
    )


@router.patch(
    "/users/{user_id}",
    response_model=UserResponse,
    summary="Update user partially"
)
def modify_user(
    user_id: int,
    user: UserPatch,
    response: Response
):

    add_headers(response)

    update_data = user.model_dump(
        exclude_unset=True
    )

    return patch_user(
        user_id,
        update_data
    )


@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete user"
)
def remove_user(
    user_id: int,
    response: Response
):

    add_headers(response)

    return delete_user(user_id)