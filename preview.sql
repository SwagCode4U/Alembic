CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 2bdd9aadc755

CREATE INDEX ix_courses_id ON courses (id);

CREATE INDEX ix_students_id ON students (id);

INSERT INTO alembic_version (version_num) VALUES ('2bdd9aadc755');

-- Running upgrade 2bdd9aadc755 -> d2dd4f1e4925

ALTER TABLE students MODIFY phone VARCHAR(30) NULL;

UPDATE alembic_version SET version_num='d2dd4f1e4925' WHERE alembic_version.version_num = '2bdd9aadc755';

-- Running upgrade d2dd4f1e4925 -> 96291d49a1bc

UPDATE alembic_version SET version_num='96291d49a1bc' WHERE alembic_version.version_num = 'd2dd4f1e4925';

-- Running upgrade 96291d49a1bc -> 4dbe53e15cf5

UPDATE alembic_version SET version_num='4dbe53e15cf5' WHERE alembic_version.version_num = '96291d49a1bc';

-- Running upgrade 4dbe53e15cf5 -> 0ff61a0b9b16

ALTER TABLE students MODIFY phone VARCHAR(30) NULL;

UPDATE alembic_version SET version_num='0ff61a0b9b16' WHERE alembic_version.version_num = '4dbe53e15cf5';

-- Running upgrade 0ff61a0b9b16 -> 9efaac1c83fb

UPDATE alembic_version SET version_num='9efaac1c83fb' WHERE alembic_version.version_num = '0ff61a0b9b16';

