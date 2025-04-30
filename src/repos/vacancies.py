from launch import connection

class Vacancy:

    def __init__(self, connection):
        self.connection = connection

    def create(self, values):
        cursor = self.connection.cursor()
        query = """ 
        INSERT INTO vacancy(name_vacancy, salary, address, description, url)
        VALUES (%s,%s,%s,%s,%s)
        """
        cursor.execute(query, values)
        self.connection.commit()

    def update(self, vacancy_id, new_values):
        cursor = self.connection.cursor()
        query = """
                UPDATE vacancy 
                SET name_vacancy = %s,
                    salary = %s,
                    address = %s,
                    description = %s,
                    url = %s
                WHERE id_vacancy = %s
                """
        values = new_values + (vacancy_id, )
        cursor.execute(query, values)
        self.connection.commit()

    def delete(self, vacancy_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM vacancy WHERE id_vacancy = %s", (vacancy_id,))
        self.connection.commit()

    def get(self, vacancy_id):
        cursor = self.connection.cursor()
        query = """
            SELECT id_vacancy, name_vacancy, salary, address, description, url
            FROM vacancy
            WHERE id_vacancy = %s
            """
        cursor.execute(query, (vacancy_id, ))
        result = cursor.fetchone()
        self.connection.commit()
        return result

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM vacancy")
        return cursor.fetchall()


vacancy_repo = Vacancy(connection=connection)
