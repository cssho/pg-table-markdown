import psycopg2
from urlparse import urlparse


class UnableToConnectToDatabase(Exception):

    pass


def database_connection(database_url):
    parsed = urlparse(database_url)
    user = parsed.username
    password = parsed.password
    host = parsed.hostname
    port = parsed.port
    database = parsed.path.strip('/')

    try:
        connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
    except psycopg2.OperationalError:
        raise UnableToConnectToDatabase
    connection.set_session(autocommit=True)

    return connection
