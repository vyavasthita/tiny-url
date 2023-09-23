from fastapi import FastAPI
from src.errors.db_error import DBException, db_exception_handler
from src.errors.auth_error import AuthException, auth_exception_handler
from src.errors.user_error import (
    UserValidationException,
    user_validation_exception_handler,
)

from src.routers.auth_router import auth_router
from src.routers.shortner_router import shortner_router
from src.routers.user_router import user_router
from src.utils.initialize import initialize

app = FastAPI()


app.add_exception_handler(DBException, db_exception_handler)
app.add_exception_handler(AuthException, auth_exception_handler)
app.add_exception_handler(UserValidationException, user_validation_exception_handler)

app.include_router(auth_router)
app.include_router(shortner_router)
app.include_router(user_router)

initialize()
