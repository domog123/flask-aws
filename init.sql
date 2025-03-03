CREATE DATABASE IF NOT EXISTS flaskdb;
USE flaskdb;

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    barangay VARCHAR(255) NOT NULL,
    precinct_number VARCHAR(50) NOT NULL
);
