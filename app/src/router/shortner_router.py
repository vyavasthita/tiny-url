from fastapi import APIRouter
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from ..schema.shortner_schema import CreateUrl, ReadUrl


shortner_router = APIRouter(prefix="/api/url")


@shortner_router.post("/create")
def user_info(create_url: CreateUrl):
    cluster = Cluster(["cassandra-db-development"])
    session = cluster.connect()

    return "Connected to Cassandra"
