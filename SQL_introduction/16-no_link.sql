-- shows records in the score that are the same in the second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC