-- script that creates a table unique_id on your MySQL server
CREATE TABLE if NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE,
    name VARCHAR(256)
)
