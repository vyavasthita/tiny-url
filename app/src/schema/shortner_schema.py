from pydantic import BaseModel, Field
from datetime import date
from ..dependencies.config_dependency import Config


class UrlBase(BaseModel):
    target_url: str = Field(description="Target Long URL", max_length=2048)


class ExpiresIn(BaseModel):
    expires_in: int | None = Field(default=7, description="Expiry days", gt=0, lt=Config().MAX_EXPIRES_IN_FOR_LOGGED_IN_USERS)


class ExpiryDate(BaseModel):
    expiry_date: date | None = Field(default=None, description="Expiry date")


class LongUrl(UrlBase, ExpiresIn):
    pass


class UrlInfo(UrlBase, ExpiryDate):
    short_url: str | None = Field(
        default=None, description="Short URL", max_length=2048
    )
    email: str | None = Field(default=None, description="Email Id")
    is_active: bool | None = Field(default=True, description="Is URL active.")
