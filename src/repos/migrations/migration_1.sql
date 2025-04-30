BEGIN;
CREATE TABLE IF NOT EXISTS vacancy(
    id_vacancy SERIAL PRIMARY KEY,
    name_vacancy VARCHAR(50) NOT NULL,
    salary INT,
    address VARCHAR(100),
    description TEXT NOT NULL,
    url VARCHAR(100)
);

COMMIT;
