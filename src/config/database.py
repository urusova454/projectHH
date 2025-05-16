from src.settings import POSTGRES_PORT, POSTGRES_PASSWORD, POSTGRES_DBNAME, POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD
from psycopg2 import pool


connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    dbname=POSTGRES_DBNAME,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)

def get_conn():
    conn = connection_pool.getconn()
    try:
        yield conn
    finally:
        connection_pool.putconn(conn)
connection = next(get_conn())