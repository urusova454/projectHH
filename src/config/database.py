from src.settings import PORT, PASSWORD, DBNAME, HOST, USER
from psycopg2 import pool


connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=HOST,
    port=PORT,
    dbname=DBNAME,
    user=USER,
    password=PASSWORD
)

def get_conn():
    conn = connection_pool.getconn()
    try:
        yield conn
    finally:
        connection_pool.putconn(conn)
connection = next(get_conn())