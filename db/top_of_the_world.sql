DROP TABLE attractions;
DROP TABLE countries;
DROP TABLE cities;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    visited BOOLEAN,
    notes TEXT
);

CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cost FLOAT,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE 
);