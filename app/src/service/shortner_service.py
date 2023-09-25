from cassandra.cluster import Session
from ..schema.shortner_schema import (
    LongUrl,
    UrlInfo,
)
from ..dao import shortner_dao
from ..logging.api_logger import ApiLogger
from ..utils.key_gen import KeyGenerator
from ..utils.datetime_utils import get_expiry_date
from ..errors.shortner_error import ShortnerException


class KeyGenService:
    @classmethod
    def check_short_url_exists(cls, short_url: str, session: Session) -> bool:
        rows = shortner_dao.check_short_url_exists(short_url, session=session)

        return len(rows.current_rows)

    @classmethod
    def generate_key(cls, session: Session):
        hash_str = KeyGenerator.generate_key()

        while cls.check_short_url_exists(hash_str, session):
            hash_str = KeyGenerator.generate_key()

        return hash_str


class ShortnerService:
    @classmethod
    def check_long_url_exists(cls, url_info: UrlInfo, db_info: tuple) -> UrlInfo:
        url_info.short_url = db_info.short_url
        url_info.expiry_date = db_info.expiry_date.date()
        url_info.is_active = db_info.is_active

        return url_info

    @classmethod
    def gen_new_short_url(
        cls, url_info: UrlInfo, long_url: LongUrl, session: Session
    ) -> UrlInfo:
        hash_str = KeyGenService.generate_key(session)
        expiry_date = get_expiry_date(long_url.expires_in)

        shortner_dao.create_url(
            long_url=long_url.target_url,
            short_url=hash_str,
            expiry_date=expiry_date,
            email=url_info.email,
            session=session,
        )

        url_info.short_url = hash_str
        url_info.expiry_date = expiry_date
        url_info.is_active = True

        return url_info

    @classmethod
    def shorten_url(cls, long_url: LongUrl, email: str, session: Session) -> UrlInfo:
        url_info = UrlInfo(target_url=long_url.target_url, email=email)

        # Check if given url already exists
        rows = shortner_dao.check_long_url_exists(long_url.target_url, session=session)
        if (
            len(rows.current_rows) != 0
        ):  # Url already exists, no need to gen new short url
            return cls.check_long_url_exists(url_info=url_info, db_info=rows[0])

        else:
            return cls.gen_new_short_url(
                url_info=url_info, long_url=long_url, session=session
            )

    @classmethod
    def get_long_url(cls, short_url: str, session: Session):
        # Check if given url already exists
        rows = shortner_dao.get_long_url(short_url, session=session)

        if len(rows.current_rows) == 0:
            raise ShortnerException("Invalid URL Key")

        if not rows[0].is_active:
            raise ShortnerException("Expired")

        return rows[0].long_url

    @classmethod
    def deactivate_url(cls, short_url: str, email: str, session: Session):
        # Check if given url already exists
        rows = shortner_dao.get_long_url_by_email(short_url, email, session=session)

        if len(rows.current_rows) == 0:
            raise ShortnerException("Invalid URL Key")

        shortner_dao.deactivate_url(short_url, email, session)
