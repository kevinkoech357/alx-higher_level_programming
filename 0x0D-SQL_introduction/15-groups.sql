-- Lists no.of records with the same score
-- Displays score and no.of records with that score
-- Orders by number of records in descending order

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
