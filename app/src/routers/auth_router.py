from typing import Annotated
from fastapi import APIRouter, Depends
from ..dependencies.auth_dependency import UserAuthenticator
from ..schema.auth_schema import Token
from ..service.auth_service import AuthService
from ..dependencies.config_dependency import Config


auth_router = APIRouter(prefix="/api/auth", tags=["Auth"])


@auth_router.post("/token", tags=["Auth"], response_model=Token)
def token(user: Annotated[dict, Depends(UserAuthenticator())]) -> Token:
    access_token = AuthService.create_access_token(
        user.get("email"), Config().TOKEN_EXPIRY_TIME
    )

    return {"access_token": access_token, "token_type": "bearer"}
