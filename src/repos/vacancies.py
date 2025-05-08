

class VacancyRepo:

    def __init__(self, connection):
        self.connection = connection

    def create(self, values):
        cursor = self.connection.cursor()
        query = """ 
        INSERT INTO vacancy(id, name, salary, address, description, url)
        VALUES (%s,%s,%s,%s,%s,%s)
        RETURNING id, name, salary, address, description, url
        """
        cursor.execute(query, values)
        result = cursor.fetchone()
        self.connection.commit()
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, result))


    def update(self, vacancy_id, new_values):
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
        values = new_values + (vacancy_id, )
        cursor.execute(query, values)
        result = cursor.fetchone()
        self.connection.commit()
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, result))

    def delete(self, vacancy_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM vacancy WHERE id = %s", (vacancy_id,))
        self.connection.commit()

    def get(self, vacancy_id):
        cursor = self.connection.cursor()
        query = """
            SELECT id, name, salary, address, description, url
            FROM vacancy
            WHERE id = %s
            """
        cursor.execute(query, (vacancy_id, ))
        result = cursor.fetchone()
        self.connection.commit()
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, result))

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM vacancy")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]

    def create_test(self, values):
        cursor = self.connection.cursor()
        query = """ 
                INSERT INTO vacancy(id, name, salary, address, description, url)
                VALUES (%s,%s,%s,%s,%s,%s)
                ON CONFLICT (id)
                DO UPDATE SET
                name = excluded.name,
                salary = excluded.salary,
                address = excluded.address,
                description = excluded.description,
                url = excluded.url
                RETURNING id, name, salary, address, description, url
                """
        cursor.execute(query, values)
        result = cursor.fetchone()
        self.connection.commit()
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, result))



