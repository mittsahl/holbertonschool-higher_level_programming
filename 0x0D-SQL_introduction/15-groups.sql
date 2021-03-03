--Groups by number of appearances in the table
-- db given as arg
SELECT score, COUNT(score) AS `number` FROM second_table GROUP BY score
ORDER BY number DESC;
