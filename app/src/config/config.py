import os
from pydantic_settings import BaseSettings, SettingsConfigDict


base_dir: str = os.path.abspath(os.path.dirname(__name__))


class DevSettings(BaseSettings):
    API_HOST: str | None = "0.0.0.0"
    API_PORT: int | None = 5001
    RELOAD: bool | None = True
    # Configuration file for logging
    LOG_CONFIG_FILE: str
    # Directory where logs will be generated.
    LOGS_DIR: str
    # Log File name
    LOG_FILE_NAME: str
    JWT_ALGORITHM: str | None
    TOKEN_EXPIRY_TIME: int | None
    SECRET_KEY: str | None
    PASSWORD_LENGTH: int | None = 10

    model_config = SettingsConfigDict(env_file=os.path.join(base_dir, ".env.app"))


class AutTestSettings(BaseSettings):
    pass
