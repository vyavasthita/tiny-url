from cassandra.cluster import Cluster, Session, DCAwareRoundRobinPolicy


def db_initialize(session: Session):
    session.execute(
        "CREATE KEYSPACE IF NOT EXISTS urlshortner WITH replication = {'class':'SimpleStrategy','replication_factor':'1'};"
    )

    session.execute(
        """
            CREATE TABLE IF NOT EXISTS urlshortner.user(
                first_name text,
                last_name text,
                email text PRIMARY KEY,
                password text
            )
        """
    )


def get_db():
    try:
        cluster = Cluster(
            contact_points=[
                "cassandra-db-development",
            ]
        )

        session = cluster.connect()
        db_initialize(session)
        yield session
    finally:
        session.shutdown()
