-- Shows all records sorted by score only if the score is greater than or equal to 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC