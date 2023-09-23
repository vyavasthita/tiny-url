from datetime import date
from cassandra.cluster import Session, ResultSet
from ..schema.shortner_schema import (
    UrlInfo,
)


def check_long_url_exists(long_url: str, session: Session) -> ResultSet:
    return session.execute(
        f"select * from urlshortner.url where long_url='{long_url}';"
    )


def check_short_url_exists(short_url: str, session: Session) -> ResultSet:
    return session.execute(
        f"select * from urlshortner.url where short_url='{short_url}';"
    )


def create_url(
    long_url: str, short_url: str, expiry_date: date, email: str, session: Session
) -> UrlInfo:
    stmt = session.prepare(
        """
        INSERT INTO urlshortner.url (long_url, short_url, email, expiry_date, is_active)
        VALUES (?, ?, ?, ?, ?)
        IF NOT EXISTS
        """
    )
    return session.execute(stmt, [long_url, short_url, email, expiry_date, True])
