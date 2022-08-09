-- CREATE DATABASE name hbnb_dev_db
-- CREATE USER named hbnb_dev and password hbnb_dev_pwd
-- GRANT ALL PRIVILEGES
-- GRANT SELECT ON performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

USE hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
