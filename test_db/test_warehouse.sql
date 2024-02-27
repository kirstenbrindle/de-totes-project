DROP DATABASE IF EXISTS test_warehouse;

CREATE DATABASE test_warehouse;
\c test_warehouse

CREATE TABLE test_currency (
    currency_id SERIAL PRIMARY KEY,
    currency_code VARCHAR(3) NOT NULL,
    currency_name VARCHAR(20) NOT NULL
);
