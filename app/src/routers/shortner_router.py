from typing import Annotated, Any
from fastapi import APIRouter, Depends
from cassandra.cluster import Session
from ..schema.shortner_schema import LongUrl
from ..dependencies.db_dependency import get_db
from ..dependencies.auth_dependency import get_auth_schema_optional
from ..dependencies.config_dependency import Config
from src.logging.api_logger import ApiLogger
from ..service.auth_service import AuthService
from ..service.shortner_service import ShortnerService

shortner_router = APIRouter(prefix="/api/url", tags=["Url"])


@shortner_router.post("/")
def user_info(
    long_url: LongUrl,
    session: Annotated[Session, Depends(get_db)],
    token: Annotated[str | None, Depends(get_auth_schema_optional())] = None,
) -> Any:
    ApiLogger.get_instance().log_info(
        f"Creating Short Url for '{long_url.target_url}'."
    )

    email = None

    if token is not None:
        user = AuthService.get_current_user(token, session)
        email = user.email
    else:
        if long_url.expires_in > Config().MAX_EXPIRES_IN_FOR_NON_LOGGED_IN_USERS:
            long_url.expires_in = Config().MAX_EXPIRES_IN_FOR_NON_LOGGED_IN_USERS

    return ShortnerService.shorten_url(long_url=long_url, email=email, session=session)
