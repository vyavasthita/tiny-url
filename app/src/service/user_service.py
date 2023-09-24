from cassandra.cluster import Session
from ..schema.user_schema import (
    DBUser as User,
    UserCreate,
    UserRead,
)
from ..dao import user_dao
from ..errors.db_error import DBException
from ..utils.password_helper import PasswordHash
from ..logging.api_logger import ApiLogger


class UserService:
    @classmethod
    def create_user(cls, user: UserCreate, db: Session) -> UserRead:
        user.password = PasswordHash.gen_hash_password(user.password)
        results = user_dao.create_user(user, db)

        if not results[0].applied:
            raise DBException(
                f"Failed to create user with email {user.email}. User already exists."
            )

        return UserRead(
            first_name=user.first_name, last_name=user.last_name, email=user.email
        )

    @classmethod
    def delete_user(cls, user: User, db: Session) -> None:
        user_dao.delete_user_by_email(user, db)
