DROP DATABASE IF EXISTS test_warehouse;

CREATE DATABASE test_warehouse;
\c test_warehouse

CREATE TABLE test_currency (
    currency_id INT PRIMARY KEY,
    currency_code VARCHAR(3) NOT NULL,
    currency_name VARCHAR(50) NOT NULL
);
