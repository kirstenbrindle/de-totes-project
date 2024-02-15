DROP DATABASE IF EXISTS test_database;

CREATE DATABASE test_database;
\c test_database

CREATE TABLE department (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR NOT NULL,
    locations VARCHAR,
    manager VARCHAR,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE design (
    design_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL,
    design_name VARCHAR NOT NULL,
    file_location VARCHAR NOT NULL,
    file_name VARCHAR NOT NULL
);

CREATE TABLE payment_type (
    payment_type_id SERIAL PRIMARY KEY,
    payment_type_name VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE currency (
    currency_id SERIAL PRIMARY KEY,
    currency_code VARCHAR(3) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE addresses (
    address_id SERIAL PRIMARY KEY,
    address_line_1 VARCHAR NOT NULL,
    address_line_2 VARCHAR,
    district VARCHAR,
    city VARCHAR NOT NULL,
    postal_code VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    phone VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE counterparty (
    counterparty_id SERIAL PRIMARY KEY,
    counterparty_legal_name VARCHAR NOT NULL,
    legal_address_id INT REFERENCES addresses(address_id) NOT NULL,
    commercial_contact VARCHAR,
    delivery_contact VARCHAR,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    department_id INT REFERENCES department(department_id),
    email_address VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE purchase_order (
    purchase_order_id SERIAL PRIMARY KEY,
    staff_id INT REFERENCES staff(staff_id) NOT NULL,
    counterparty_id INT REFERENCES counterparty(counterparty_id) NOT NULL,
    item_code VARCHAR NOT NULL,
    item_quantity INT NOT NULL,
    item_unit_price NUMERIC NOT NULL,
    currency_id INT REFERENCES currency(currency_id) NOT NULL,
    agreed_delivery_date VARCHAR NOT NULL,
    agreed_payment_date VARCHAR NOT NULL,
    agreed_delivery_location_id INT REFERENCES addresses(address_id) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);


CREATE TABLE sales_order (
    sales_order_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL,
    design_id INT,
    staff_id INT REFERENCES staff(staff_id) NOT NULL,
    counterparty_id INT REFERENCES counterparty(counterparty_id) NOT NULL,
    units_sold INT NOT NULL,
    unit_price NUMERIC NOT NULL,
    currency_id INT REFERENCES currency(currency_id) NOT NULL,
    agreed_delivery_date VARCHAR NOT NULL,
    agreed_payment_date VARCHAR NOT NULL,
    agreed_delivery_location_id INT REFERENCES addresses(address_id) NOT NULL
);

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    transaction_type VARCHAR NOT NULL,
    sales_order_id INT REFERENCES sales_order(sales_order_id),
    purchase_order_id INT REFERENCES purchase_order(purchase_order_id),
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);

CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    transaction_id INT REFERENCES transactions(transaction_id) NOT NULL,
    counterparty_id INT REFERENCES counterparty(counterparty_id) NOT NULL,
    payment_amount NUMERIC NOT NULL,
    currency_id INT REFERENCES currency(currency_id) NOT NULL,
    payment_type_id INT REFERENCES payment_type(payment_type_id) NOT NULL,
    paid BOOLEAN NOT NULL,
    payment_date VARCHAR NOT NULL,
    company_acc_number INT NOT NULL,
    counterparty_acc_number INT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_updated TIMESTAMP NOT NULL
);


