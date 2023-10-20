-- shows records in the score that are the same in the second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC