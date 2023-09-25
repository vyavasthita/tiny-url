from datetime import date
from cassandra.cluster import Session, ResultSet
from ..schema.shortner_schema import (
    UrlInfo,
)
from ..dependencies.config_dependency import Config


def check_long_url_exists(long_url: str, session: Session) -> ResultSet:
    return session.execute(
        f"select * from {Config().CASSANDRA_KEYSPACE}.url where long_url='{long_url}';"
    )


def check_short_url_exists(short_url: str, session: Session) -> ResultSet:
    return session.execute(
        f"select * from {Config().CASSANDRA_KEYSPACE}.url where short_url='{short_url}';"
    )


def get_long_url(short_url: str, session: Session) -> ResultSet:
    return session.execute(
        f"select * from {Config().CASSANDRA_KEYSPACE}.url where short_url='{short_url}';"
    )


def get_long_url_by_email(short_url: str, email: str, session: Session) -> ResultSet:
    return session.execute(
        f"select * from {Config().CASSANDRA_KEYSPACE}.url where short_url='{short_url}' AND email='{email}';"
    )


def deactivate_url(short_url: str, email: str, session: Session) -> ResultSet:
    return session.execute(
        f"UPDATE {Config().CASSANDRA_KEYSPACE}.url SET is_active = {False} where short_url='{short_url}' IF email='{email}';"
    )


def create_url(
    long_url: str, short_url: str, expiry_date: date, email: str, session: Session
) -> UrlInfo:
    stmt = session.prepare(
        f"""
        INSERT INTO {Config().CASSANDRA_KEYSPACE}.url (long_url, short_url, email, expiry_date, is_active)
        VALUES (?, ?, ?, ?, ?)
        IF NOT EXISTS
        """
    )
    return session.execute(stmt, [long_url, short_url, email, expiry_date, True])
