from cassandra.cluster import Session
from ..schema.shortner_schema import (
    LongUrl,
    UrlInfo,
)
from ..db import shortner_dao
from ..logging.api_logger import ApiLogger
from ..utils.key_gen import KeyGenerator
from ..utils.datetime_utils import get_expiry_date


class ShortnerService:
    @classmethod
    def check_long_url_exists(cls, url_info: UrlInfo, db_info: tuple) -> UrlInfo:
        url_info.short_url = db_info.short_url
        url_info.expiry_date = db_info.expiry_date
        url_info.is_active = db_info.is_active

        return url_info

    @classmethod
    def gen_new_short_url(
        cls, url_info: UrlInfo, long_url: LongUrl, session: Session
    ) -> UrlInfo:
        hash_str = KeyGenerator.generate_key()
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
