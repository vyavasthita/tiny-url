from typing import Annotated
from pydantic import BaseModel
from datetime import datetime


class CreateUrl(BaseModel):
    orignal_url: str
    expiration_date: datetime | None = None


class ReadUrl(BaseModel):
    short_url: str
