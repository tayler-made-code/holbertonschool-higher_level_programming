-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT city.name FROM city
WHERE city.id IN (SELECT city_id FROM state WHERE name = 'California')
SORT BY city.id ASC;
