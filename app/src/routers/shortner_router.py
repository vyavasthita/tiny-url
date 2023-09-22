from typing import Annotated
from fastapi import APIRouter, Depends
from cassandra.cluster import Session
from ..schema.shortner_schema import CreateUrl, ReadUrl
from ..dependencies.db_dependency import get_db
from src.logging.api_logger import ApiLogger

shortner_router = APIRouter(prefix="/api/url")


@shortner_router.post("/create")
def user_info(create_url: CreateUrl, session: Annotated[Session, Depends(get_db)]):
    ApiLogger.get_instance().log_info("Creating Short Url.")
    release_version = session.execute("SELECT release_version FROM system.local").one()

    return {"Release Version": release_version}
