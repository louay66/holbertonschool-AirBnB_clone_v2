-- CREATE DATABASE name hbnb_test_db
-- CREATE USER named hbnb_test and password hbnb_test_pwd
-- GRANT ALL PRIVILEGES
-- GRANT SELECT ON performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

USE hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';