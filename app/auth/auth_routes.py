from fastapi import (
    APIRouter,
    Depends,
    Request,
    status
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies.database_dependency import get_db
from app.schemas.auth_schema import (
    UserRegister,
    Token,
    AuthUserResponse
)
from app.auth.auth_service import (
    register_user,
    login_user
)
from app.dependencies.auth_dependency import (
    get_current_active_user,
    limiter
)


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
    "/register",
    response_model=AuthUserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description=(
        "Creates a user with a securely hashed password. "
        "The password is never returned in the response."
    )
)
@limiter.limit("3/minute")
def register(
    request: Request,
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(
        db,
        user
    )


@router.post(
    "/login",
    response_model=Token,
    summary="Login and generate JWT token",
    description=(
        "Authenticates the user and returns a Bearer JWT token."
    )
)
@limiter.limit("5/minute")
def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(
        db,
        form_data.username,
        form_data.password
    )


@router.get(
    "/me",
    response_model=AuthUserResponse,
    summary="Get authenticated user",
    description=(
        "Returns the profile of the user identified by the JWT token."
    )
)
def get_me(
    current_user=Depends(get_current_active_user)
):
    return current_user
