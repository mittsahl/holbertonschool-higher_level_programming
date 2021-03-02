-- Lists all cities of california
-- db passed as arg
SELECT id, name
FROM
	cities
WHERE
	state_id IN (SELECT
		id
	FROM
		states
	WHERE
		id = state_id);
