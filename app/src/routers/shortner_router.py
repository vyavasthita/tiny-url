from typing import Annotated
from fastapi import APIRouter, Depends
from cassandra.cluster import Session
from ..schema.shortner_schema import CreateUrl, ReadUrl
from ..dependencies.db_dependency import get_db


shortner_router = APIRouter(prefix="/api/url")


@shortner_router.post("/create")
def user_info(create_url: CreateUrl, session: Annotated[Session, Depends(get_db)]):
    release_version = session.execute("SELECT release_version FROM system.local").one()

    return {"Release Version": release_version}
