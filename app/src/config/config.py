from typing import List, Union
import os
from pydantic import validator
from pydantic_settings import BaseSettings


base_dir: str = os.path.abspath(os.path.dirname(__name__))


class DevSettings(BaseSettings):
    API_HOST: str | None = "0.0.0.0"
    API_PORT: int | None = 5001
    RELOAD: bool | None = True

    class Config:
        env_file = os.path.join(base_dir, ".env.app")


class AutTestSettings(BaseSettings):
    pass
