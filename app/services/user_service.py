from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User


def get_all_users(
    db: Session,
    role: str = None,
    is_active: bool = None,
    sort: str = None
):
    query = db.query(User)

    if role:
        query = query.filter(User.role == role)

    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    if sort == "name":
        query = query.order_by(User.name)

    elif sort == "created_at":
        query = query.order_by(User.created_at)

    return query.all()


def get_user_by_id(
    db: Session,
    user_id: int
):
    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(
    db: Session,
    user_data
):
    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user = User(
        name=user_data.name,
        email=user_data.email,
        role=user_data.role,
        is_active=user_data.is_active
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(
    db: Session,
    user_id: int,
    user_data
):
    user = get_user_by_id(
        db,
        user_id
    )

    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if (
        existing_user
        and existing_user.id != user_id
    ):
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user.name = user_data.name
    user.email = user_data.email
    user.role = user_data.role
    user.is_active = user_data.is_active

    db.commit()
    db.refresh(user)

    return user


def patch_user(
    db: Session,
    user_id: int,
    update_data: dict
):
    user = get_user_by_id(
        db,
        user_id
    )

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No data provided for update"
        )

    if "email" in update_data:

        existing_user = get_user_by_email(
            db,
            update_data["email"]
        )

        if (
            existing_user
            and existing_user.id != user_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id: int
):
    user = get_user_by_id(
        db,
        user_id
    )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }