from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    ConfigDict
)
from typing import Literal


class UserRegister(BaseModel):

    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        examples=["Ivan Florez"]
    )

    email: EmailStr = Field(
        ...,
        examples=["ivan@example.com"]
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        examples=["Password123"]
    )

    role: Literal["admin", "support", "user"] = "user"

    is_active: bool = True

    @field_validator("password")
    @classmethod
    def validate_password(
        cls,
        password: str
    ):
        if " " in password:
            raise ValueError(
                "Password must not contain spaces"
            )

        if not any(
            character.isupper()
            for character in password
        ):
            raise ValueError(
                "Password must contain at least one uppercase letter"
            )

        if not any(
            character.islower()
            for character in password
        ):
            raise ValueError(
                "Password must contain at least one lowercase letter"
            )

        if not any(
            character.isdigit()
            for character in password
        ):
            raise ValueError(
                "Password must contain at least one number"
            )

        return password


class UserLogin(BaseModel):

    email: EmailStr = Field(
        ...,
        examples=["ivan@example.com"]
    )

    password: str = Field(
        ...,
        min_length=8,
        examples=["Password123"]
    )


class Token(BaseModel):

    access_token: str
    token_type: str


class TokenData(BaseModel):

    email: EmailStr | None = None


class AuthUserResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool

    model_config = ConfigDict(
        from_attributes=True
    )