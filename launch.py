from src.settings import MIGRATION_PATH
from psycopg2 import OperationalError
from src.config.database import get_conn


def get_migration_names(connection):
    try:
        cursor = connection.cursor()

        # Проверяем существование таблицы
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'migrations'
            );
        """)
        if not cursor.fetchone()[0]:
            print("Таблица migration не существует")
            return []

        # Получаем все значения из колонки name
        cursor.execute("SELECT name FROM migrations")
        return [row[0] for row in cursor.fetchall()]

    except OperationalError as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return []
    finally:
        if 'conn' in locals():
            connection.close()


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
    connection = next(get_conn())
    migration_names = get_migration_names(connection)
    for migration in sorted(MIGRATION_PATH.iterdir()):
        if migration.name not in migration_names:
            execute_sql_file(connection, migration)




