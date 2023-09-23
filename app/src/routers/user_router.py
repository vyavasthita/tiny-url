from typing import Annotated, Any
from fastapi import APIRouter, Body, Depends, status
from cassandra.cluster import Session
from ..dependencies.db_dependency import get_db
from ..dependencies.auth_dependency import (
    get_auth_schema,
    ValidateToken,
    ValidateDuplicateUser,
    ValidatePassword,
    ValidatePasswordReset,
    ValidateDeleteAccount,
)
from ..schema.user_schema import (
    UserRead,
)
from ..service.user_service import UserService
from ..service.auth_service import AuthService


user_router = APIRouter(prefix="/api/users", tags=["User"])


@user_router.post(
    "/",
    response_model=UserRead,
    response_model_exclude={"id"},
    status_code=status.HTTP_201_CREATED,
)
def create(
    user: Annotated[dict, Depends(ValidateDuplicateUser())],
    db: Session = Depends(get_db),
) -> UserRead:
    return UserService.create_user(user, db)


# @user_router.delete("/users", status_code=status.HTTP_204_NO_CONTENT)
# def delete(
#     user: Annotated[dict, Depends(ValidateDeleteAccount())],
#     db: Session = Depends(get_db),
# ) -> None:
#     return UserService.delete_user(user, db)


# @user_router.put("/users", response_model=UserProfileUpdateRead)
# def update_profile(
#     current_user: Annotated[dict, Depends(ValidateToken())],
#     user_info: Annotated[UserProfileUpdate, Body()],
#     db: Session = Depends(get_db),
# ) -> UserProfileUpdateRead:
#     return UserService.update_profile(current_user, user_info, db)


# @user_router.put("/users/password", status_code=status.HTTP_204_NO_CONTENT)
# def update_password(
#     user_info: Annotated[dict, Depends(ValidatePassword())],
#     db: Session = Depends(get_db),
# ) -> None:
#     return UserService.update_password(
#         user_info.get("user"), user_info.get("password"), db
#     )


# @user_router.put(
#     "/users/reset_password",
#     status_code=status.HTTP_204_NO_CONTENT,
# )
# def reset_password(
#     user: Annotated[dict, Depends(ValidatePasswordReset())],
#     db: Session = Depends(get_db),
# ) -> None:
#     return UserService.reset_password(user, db)


@user_router.get("/me", response_model=UserRead)
def me(
    token: Annotated[str, Depends(get_auth_schema())], db: Session = Depends(get_db)
) -> UserRead:
    return AuthService.get_current_user(token, db)
