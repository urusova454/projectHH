import psycopg2
from src.settings import PORT, PASSWORD, DBNAME, HOST, USER

def get_conn():
    try:
        conn = psycopg2.connect(
            port=PORT,
            password=PASSWORD,
            dbname=DBNAME,
            host=HOST,
            user=USER
        )
        yield conn
        conn.commit()
    except BaseException:
        conn.rollback()
    finally:
        conn.close()

conn = get_conn()
