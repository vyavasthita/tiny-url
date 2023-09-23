from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi_cache.decorator import cache
from cassandra.cluster import Session
from ..dependencies.db_dependency import get_db
from ..dependencies.auth_dependency import (
    get_auth_schema,
    ValidateDuplicateUser,
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
    session: Session = Depends(get_db),
) -> UserRead:
    return UserService.create_user(user, session)


@user_router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    user: Annotated[dict, Depends(ValidateDeleteAccount())],
    session: Session = Depends(get_db),
) -> None:
    return UserService.delete_user(user, session)


@user_router.get("/me", response_model=UserRead)
@cache()
def me(
    token: Annotated[str, Depends(get_auth_schema())], session: Session = Depends(get_db)
) -> UserRead:
    return AuthService.get_current_user(token, session)
