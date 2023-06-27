-- script that updates the score of Bob, the cheater, to 10 in the second_table
FROM second_table
WHERE name = 'Bob';
INSERT INTO second_table.score
VALUES (10);
