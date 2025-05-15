from src.config.database import connection
from uuid import UUID, uuid4


class VacancyRepository:

    def __init__(self, connection):
        self.connection = connection

    def create(self, values):
        cursor = self.connection.cursor()
        query = """ 
        INSERT INTO vacancy(id, name, salary, address, description, url)
        VALUES (%s,%s,%s,%s,%s,%s)
        RETURNING id, name, salary, address, description, url
        """
        cursor.execute(query,values)
        result = cursor.fetchone()
        self.connection.commit()
        columns = [col[0] for col in cursor.description]
        return dict(zip(columns, result))


    def update(self, values):
        cursor = self.connection.cursor()
        query = """
                UPDATE vacancy 
                SET name = %s,
                    salary = %s,
                    address = %s,
                    description = %s,
                    url = %s
                WHERE id = %s
                RETURNING id, name, salary, address, description, url
                """
        cursor.execute(query, values)
        result = cursor.fetchone()
        self.connection.commit()
        columns = [col[0] for col in cursor.description]
        return dict(zip(columns, result))

    def delete(self, vacancy_id: UUID):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM vacancy WHERE id = %s", (str(vacancy_id),))
        self.connection.commit()

    def get(self, vacancy_id: UUID):
        cursor = self.connection.cursor()
        query = """
            SELECT id, name, salary, address, description, url
            FROM vacancy
            WHERE id = %s
            """
        cursor.execute(query, (str(vacancy_id), ))
        result = cursor.fetchone()
        self.connection.commit()
        columns = [col[0] for col in cursor.description]
        return dict(zip(columns, result))

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM vacancy")
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


vacancy_repo = VacancyRepository(connection=connection)
