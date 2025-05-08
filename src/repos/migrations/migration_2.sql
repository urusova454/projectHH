BEGIN;

ALTER TABLE vacancy RENAME COLUMN name_vacancy TO name;
ALTER TABLE vacancy RENAME COLUMN id_vacancy TO id;
ALTER TABLE vacancy ALTER COLUMN id TYPE VARCHAR(36);

INSERT INTO migration VALUES ('migration_2.sql');

COMMIT;
