BEGIN;
CREATE TABLE IF NOT EXISTS vacancy(
    id_vacancy SERIAL PRIMARY KEY,
    name_vacancy VARCHAR(50) NOT NULL,
    salary INT,
    address VARCHAR(100),
    description TEXT NOT NULL,
    url VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS migration(
    name VARCHAR(40)
);
INSERT INTO migration VALUES ('migration_1.sql');

COMMIT;
