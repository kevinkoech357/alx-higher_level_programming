-- Creates a user user_0d_1 with all privileges
-- If user exists, script will not fail
-- Assigns a password user_0d_1_pwd

CREATE USER IF NOT EXISTS user_0d_1_pwd@localhost
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
