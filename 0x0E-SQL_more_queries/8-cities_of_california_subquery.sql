-- Lists all cities of california
-- db passed as arg
SELECT id, name FROM cities
WHERE state_id = 
(SELECT id FROM states
WHERE name = 'California')
ORDER BY cities.id ASC;
