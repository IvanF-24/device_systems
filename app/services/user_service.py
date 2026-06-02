from fastapi import HTTPException
from app.data.users_db import users


def get_all_users(role=None, is_active=None):

    result = users

    if role is not None:
        result = [
            user for user in result
            if user["role"] == role
        ]

    if is_active is not None:
        result = [
            user for user in result
            if user["is_active"] == is_active
        ]

    return result


def create_user(user_data):

    for user in users:
        if user["email"] == user_data["email"]:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    users.append(user_data)

    return user_data


def update_user(user_id, user_data):

    for index, user in enumerate(users):

        if user["id"] == user_id:

            for existing_user in users:
                if (
                    existing_user["email"] == user_data["email"]
                    and existing_user["id"] != user_id
                ):
                    raise HTTPException(
                        status_code=400,
                        detail="Email already exists"
                    )

            users[index] = user_data

            return user_data

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


def patch_user(user_id, update_data):

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No data provided for update"
        )

    for user in users:

        if user["id"] == user_id:

            if "email" in update_data:

                for existing_user in users:
                    if (
                        existing_user["email"] == update_data["email"]
                        and existing_user["id"] != user_id
                    ):
                        raise HTTPException(
                            status_code=400,
                            detail="Email already exists"
                        )

            user.update(update_data)

            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


def delete_user(user_id):

    for index, user in enumerate(users):

        if user["id"] == user_id:

            users.pop(index)

            return {
                "message": "User deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )