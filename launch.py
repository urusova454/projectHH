import psycopg2
from src.settings import PORT, PASSWORD, DBNAME, HOST, USER, MIGRATION_PATH



def get_db_connection(port, password, dbname, host, user):
    """Создает соединение с базой данных в зависимости от типа"""
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port,
        options = "-c client_encoding=utf8"
    )

connection = get_db_connection(PORT, PASSWORD, DBNAME, HOST, USER)

def execute_sql_file(connection, filepath):
    """Выполняет SQL-скрипт из файла"""
    with open(filepath, 'r', encoding='utf-8') as sql_file:
        sql_script = sql_file.read()

    cursor = connection.cursor()
    try:
        cursor.execute(sql_script)
        connection.commit()
        print(f"Successfully executed: {filepath}")
    except Exception as e:
        connection.rollback()
        print(f"Error executing {filepath}: {e}")
        raise



if __name__ == "__main__":

    for child in MIGRATION_PATH.iterdir():
        execute_sql_file(connection, child)



