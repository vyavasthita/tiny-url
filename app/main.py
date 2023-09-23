from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.errors.db_error import DBException, db_exception_handler
from src.errors.auth_error import AuthException, auth_exception_handler
from src.errors.user_error import (
    UserValidationException,
    user_validation_exception_handler,
)
from src.errors.shortner_error import (
    ShortnerException,
    shortner_validation_exception_handler,
)
from src.routers.auth_router import auth_router
from src.routers.shortner_router import shortner_router
from src.routers.user_router import user_router
from src.utils.initialize import initialize
from src.dependencies.config_dependency import Config


app = FastAPI(
    title="Url Shortner",
    description="Url Shortner",
    openapi_url=f"/",
    docs_url="/docs",
    redoc_url="/redoc",
)


app.add_exception_handler(DBException, db_exception_handler)
app.add_exception_handler(AuthException, auth_exception_handler)
app.add_exception_handler(UserValidationException, user_validation_exception_handler)
app.add_exception_handler(ShortnerException, shortner_validation_exception_handler)


app.include_router(auth_router)
app.include_router(shortner_router)
app.include_router(user_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=Config().BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=Config().ALLOW_METHODS,
    allow_headers=Config().ALLOW_HEADERS,
)


@app.on_event("startup")
def start_up():
    initialize()
