from cassandra.cluster import Session
from ..schema.user_schema import (
    DBUser as User,
    UserCreate,
)


def create_user(user: UserCreate, session: Session) -> User:
    stmt = session.prepare(
        """
        INSERT INTO urlshortner.user (first_name, last_name, email, password)
        VALUES (?, ?, ?, ?)
        IF NOT EXISTS
        """
    )
    return session.execute(
        stmt, [user.first_name, user.last_name, user.email, user.password]
    )


def delete_user_by_email(user: User, session: Session) -> User:
    return session.execute(
        f"DELETE FROM urlshortner.user WHERE email='{user.email}';"
    )


def get_user_by_email(email: str, session: Session) -> User:
    return session.execute(
        f"select first_name, last_name, email, password from urlshortner.user where email='{email}';"
    )

