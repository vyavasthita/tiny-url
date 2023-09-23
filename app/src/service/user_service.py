from typing import Annotated
from cassandra.cluster import Session
from ..schema.user_schema import (
    DBUser as User,
    UserCreate,
    UserRead,
    UserProfileUpdate,
    UserProfileUpdateRead,
)
from ..db import dao
from ..errors.db_error import DBException
from ..utils.password_helper import PasswordGenerator, PasswordHash
from ..dependencies.config_dependency import Config
from ..logging.api_logger import ApiLogger


class UserService:
    @classmethod
    def create_user(cls, user: UserCreate, db: Session) -> UserRead:
        user.password = PasswordHash.gen_hash_password(user.password)
        results = dao.create_user(user, db)

        if not results[0].applied:
            raise DBException(
                f"Failed to create user with email {user.email}. User already exists."
            )

        return UserRead(
            first_name=user.first_name, last_name=user.last_name, email=user.email
        )

    @classmethod
    def delete_user(cls, user: User, db: Session) -> None:
        dao.delete_user_by_id(user, db)
        cls.send_delete_account_email(user)

    @classmethod
    def update_profile(
        cls,
        current_user: User,
        user_info: UserProfileUpdate,
        db: Session,
    ) -> UserProfileUpdateRead:
        user = dao.update_user_profile(current_user, user_info, db)

        if not user:
            raise DBException(f"Failed to update user profile for {current_user.email}")

        return user

    @classmethod
    def update_password(
        cls,
        current_user: User,
        password: str,
        db: Session,
    ) -> None:
        hashed_password = PasswordHash.gen_hash_password(password)
        dao.update_user_password(current_user, hashed_password, db)

    @classmethod
    def reset_password(
        cls,
        user: User,
        db: Session,
    ) -> None:
        response = PasswordGenerator().generate_password(Config().PASSWORD_LENGTH)

        hashed_password = PasswordHash.gen_hash_password(response.result)

        dao.update_user_password(user, hashed_password, db)
