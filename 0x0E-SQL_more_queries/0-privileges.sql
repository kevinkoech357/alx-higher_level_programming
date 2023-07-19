-- Lists all priviledges of user_0d_1 and user_0d_2 on the server

CREATE USER user_0d_1@localhost;
CREATE USER user_0d_2@localhost;
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
