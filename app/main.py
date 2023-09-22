import os
from fastapi import FastAPI
from src.routers.shortner_router import shortner_router
from src.dependencies.config_dependency import Config


app = FastAPI()


app.include_router(shortner_router)


def create_log_directory():
    base_dir = os.path.abspath(os.path.dirname(__name__))

    if not os.path.exists(os.path.join(base_dir, Config().LOGS_DIR)):
        os.mkdir(os.path.join(base_dir, Config().LOGS_DIR))


create_log_directory()
