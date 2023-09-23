from datetime import timedelta, datetime
from cassandra.cluster import Session
from ..db import dao
from ..errors.auth_error import AuthException
from ..schema.user_schema import DBUser as User
from ..utils.security import create_access_token, decode_access_token
from ..dependencies.config_dependency import Config
from ..utils.password_helper import PasswordHash


class AuthService:
    @classmethod
    def create_access_token(cls, email: str, expires_delta: timedelta | None = None):
        expiry_time = None

        if expires_delta:
            expiry_time = datetime.utcnow() + timedelta(minutes=expires_delta)
        else:
            expiry_time = datetime.utcnow() + timedelta(minutes=15)

        return create_access_token(
            dict(sub=email, exp=expiry_time),
            Config().SECRET_KEY,
            algorithm=Config().JWT_ALGORITHM,
        )

    @classmethod
    def decode_access_token(cls, token: str):
        return decode_access_token(token, Config().SECRET_KEY, Config().JWT_ALGORITHM)

    @classmethod
    def get_current_user(cls, token: str, session: Session) -> User:
        payload = cls.decode_access_token(token)

        return cls.validate_token(payload, session)

    @classmethod
    def validate_token(cls, data: dict, session: Session) -> User:
        email = data.get("sub")

        if not email:
            raise AuthException("Invalid Token")

        return cls.verify_user(email=email, session=session)

    @classmethod
    def verify_user(cls, email: str, session: Session) -> User:
        rows = dao.get_user_by_email(email=email, session=session)

        if len(rows.current_rows) == 0:
            raise AuthException("User not found")

        return rows[0]

    @classmethod
    def check_user(cls, email: str, session: Session) -> User:
        return dao.get_user_by_email(email=email, session=session)[0]

    @classmethod
    def verify_password(cls, user: User, password: str) -> bool:
        return PasswordHash.verify_password(password, user.password)
