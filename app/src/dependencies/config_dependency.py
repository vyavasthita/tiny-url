import os
from functools import lru_cache
from src.config.config import DevSettings, AutTestSettings


build_environment = os.getenv("BUILD_ENV") or "development"
run_environment = os.getenv("RUN_ENV") or "app"  # running application or unit tests

print(f"Build environment -> {build_environment}.")
print(f"Run environment -> {run_environment}.")

config_by_name = dict(app=DevSettings(), test=AutTestSettings())


@lru_cache
def Config():
    return config_by_name[run_environment]
