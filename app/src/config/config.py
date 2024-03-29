import os
from typing import List
from pydantic import AnyHttpUrl
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
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]
    MAX_EXPIRES_IN_FOR_LOGGED_IN_USERS: int
    MAX_EXPIRES_IN_FOR_NON_LOGGED_IN_USERS: int
    CASSANDRA_HOST: str
    CASSANDRA_KEYSPACE: str

    model_config = SettingsConfigDict(env_file=os.path.join(base_dir, ".env.app"))


class AutTestSettings(BaseSettings):
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
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]
    MAX_EXPIRES_IN_FOR_LOGGED_IN_USERS: int
    MAX_EXPIRES_IN_FOR_NON_LOGGED_IN_USERS: int
    CASSANDRA_HOST: str
    CASSANDRA_KEYSPACE: str

    model_config = SettingsConfigDict(env_file=os.path.join(base_dir, ".env.test"))
