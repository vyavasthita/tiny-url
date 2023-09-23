from typing import Annotated
from fastapi import Depends, Body
from cassandra.cluster import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from ..dependencies.db_dependency import get_db
from ..service.auth_service import AuthService
from ..errors.auth_error import AuthException
from ..logging.api_logger import ApiLogger
from ..schema.user_schema import UserCreate


def get_auth_schema():
    return OAuth2PasswordBearer(tokenUrl="/api/auth/token")


class ValidateDuplicateUser:
    def __call__(
        self,
        user: Annotated[UserCreate, Body()],
        session: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info(f"Verifying user with email '{user.email}'.")
        rows = AuthService.check_user(email=user.email, session=session)

        if len(rows.current_rows) != 0:
            raise AuthException(
                f"Duplicate Email. User already exists with email '{user.email}'."
            )

        return user


class UserAuthenticator:
    def __call__(
        self,
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info(f"Verifying user with email '{form_data.username}'.")
        user = AuthService.verify_user(email=form_data.username, session=session)

        ApiLogger.log_info(f"Verifying user has provided correct password.")
        if not AuthService.verify_password(user, form_data.password):
            raise AuthException("Invalid Password")

        return {"email": form_data.username, "password": form_data.password}


class ValidateToken:
    def __call__(
        self,
        token: Annotated[str, Depends(get_auth_schema())],
        session: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info("Verifying token.")
        return AuthService.get_current_user(token=token, session=session)


class ValidateDeleteAccount:
    def __call__(
        self,
        token: Annotated[str, Depends(get_auth_schema())],
        session: Annotated[Session, Depends(get_db)],
    ):
        ApiLogger.log_info("Verifying token.")
        return AuthService.get_current_user(token=token, session=session)
