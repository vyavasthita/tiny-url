from cassandra.cluster import Cluster, Session
from ..dependencies.config_dependency import Config


def db_initialize(session: Session):
    keyspace_name = Config().CASSANDRA_KEYSPACE

    session.execute(
        f"CREATE KEYSPACE IF NOT EXISTS {keyspace_name}"
        + " WITH replication = {'class':'SimpleStrategy','replication_factor':'1'};"
    )

    session.execute(
        f"""
            CREATE TABLE IF NOT EXISTS {keyspace_name}.user(
                first_name text,
                last_name text,
                email text PRIMARY KEY,
                password text
            )
        """
    )

    session.execute(
        f"""
            CREATE TABLE IF NOT EXISTS {keyspace_name}.url(
                long_url text,
                short_url text PRIMARY KEY,
                email text,
                expiry_date date,
                is_active boolean
            )
        """
    )

    session.execute(
        f"""
            CREATE INDEX IF NOT EXISTS long_url_index
            ON {keyspace_name}.url (long_url)
        """
    )

    session.execute(
        f"""
            CREATE INDEX IF NOT EXISTS email_index
            ON {keyspace_name}.url (email)
        """
    )


def get_db():
    try:
        cluster = Cluster(
            contact_points=[
                Config().CASSANDRA_HOST,
            ]
        )

        session = cluster.connect()
        db_initialize(session)
        yield session
    finally:
        session.shutdown()
