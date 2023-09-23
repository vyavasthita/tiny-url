from cassandra.cluster import Cluster, Session


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

    session.execute(
        """
            CREATE TABLE IF NOT EXISTS urlshortner.url(
                long_url text,
                short_url text PRIMARY KEY,
                email text,
                expiry_date date,
                is_active boolean
            )
        """
    )

    session.execute(
        """
            CREATE INDEX IF NOT EXISTS long_url_index
            ON urlshortner.url (long_url)
        """
    )

    session.execute(
        """
            CREATE INDEX IF NOT EXISTS email_index
            ON urlshortner.url (email)
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
