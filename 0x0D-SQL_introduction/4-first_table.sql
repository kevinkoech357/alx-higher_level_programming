-- Creates a table called first_table
-- Table has ID and NAME
-- If table exists, script will not fail

CREATE TABLE IF NOT EXISTS first_table (
  id INT;
  name VARCHAR(256);
);
