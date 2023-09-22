from fastapi import FastAPI
from src.routers.shortner_router import shortner_router
from src.dependencies.config_dependency import Config


app = FastAPI()


app.include_router(shortner_router)
