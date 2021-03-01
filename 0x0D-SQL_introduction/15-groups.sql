--Groups by number of appearances in the table
SELECT score, count(score) AS `number` FROM second_table GROUP BY score
ORDER BY number DESC;
