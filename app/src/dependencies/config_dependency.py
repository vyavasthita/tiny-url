import os
from functools import lru_cache
from src.config.config import DevSettings, AutTestSettings


environment = os.getenv("BUILD_ENV") or "development"


config_by_name = dict(development=DevSettings(), aut_testing=AutTestSettings())


@lru_cache
def Config():
    return config_by_name[environment]
