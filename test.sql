BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> d3d4db8de1c6

CREATE TABLE countries (
    id SERIAL NOT NULL, 
    country_name VARCHAR(255) NOT NULL, 
    status INTEGER, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    updated_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_countries_id ON countries (id);

INSERT INTO alembic_version (version_num) VALUES ('d3d4db8de1c6') RETURNING alembic_version.version_num;

-- Running upgrade d3d4db8de1c6 -> fc42fa693ec3

CREATE TABLE states (
    id SERIAL NOT NULL, 
    state_name VARCHAR(255) NOT NULL, 
    countries_id INTEGER, 
    status INTEGER, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    updated_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(countries_id) REFERENCES countries (id)
);

CREATE INDEX ix_states_id ON states (id);

UPDATE alembic_version SET version_num='fc42fa693ec3' WHERE alembic_version.version_num = 'd3d4db8de1c6';

COMMIT;

