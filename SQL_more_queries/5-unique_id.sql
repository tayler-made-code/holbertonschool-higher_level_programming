-- script that creates a table unique_id on your MySQL server
-- script that creates a table unique_id on your MySQL server
CREATE TABLE if NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE SET DEFAULT 1,
    name VARCHAR(256)
)
