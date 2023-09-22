from cassandra.cluster import Cluster


def get_db():
    try:
        cluster = Cluster(["cassandra-db-development"])
        session = cluster.connect()
        yield session
    finally:
        session.shutdown()
