-- Lists all records in second_table
-- Displays score and name
-- Doesnt list rows withoud a name value
-- Orders in descending manner

SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
