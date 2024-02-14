\c test_database
INSERT INTO department
(department_name, locations, manager, created_at, last_updated)
VALUES
('Sales', 'Manchester', 'Richard Roma', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Purchasing', 'Manchester', 'Naomi Lapaglia', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Production', 'Leeds', 'Chester Ming', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Dispatch', 'Leds', 'Mark Hanna', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Finance', 'Manchester', 'Jordan Belfort', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Facilities', 'Manchester', 'Shelley Levene', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'),  
('Communications', 'Leeds', 'Ann Blake', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('HR', 'Leeds', 'James Link', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO design 
(created_at, last_updated, design_name, file_location, file_name)
VALUES
('Wooden', '/usr', 'wooden-20220717-npgz.json', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Bronze', '/private', 'bronze-20221024-4dds.json', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Granite', '/private/var', 'granite-20220205-3vfw.json', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Bronze', '/lost+found', 'bronze-20230102-r904.json', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Soft', '/System', 'soft-20211001-cjaz.json', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO payment_type
(payment_type_name, created_at, last_updated)
VALUES
('SALES_RECEIPT', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('SALES_REFUND', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('PURCHASE_PAYMENT', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('PURCHASE_REFUND', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO currency
(currency_code, created_at, last_updated)
VALUES 
('GBP', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('USD', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('EUR', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO addresses 
(address_line_1, address_line_2, district, city, postal_code, country, phone, created_at, last_updated)
VALUES 
('6826 Herzog Via',	NULL, 'Avon',	'New Patienceburgh', '28441', 'Turkey', '1803 637401', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('179 Alexie Cliffs', NULL, NULL, 'Aliso Viejo', '99305-7380', 'San Marino', '9621 880720', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('148 Sincere Fort', NULL, NULL, 'Lake Charles', '89360', 'Samoa', '0730 783349', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('6102 Rogahn Skyway', NULL, 'Bedfordshire', 'Olsonside', '47518', 'Republic of Korea', '1239 706295', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('34177 Upton Track', NULL, NULL, 'Fort Shadburgh', '55993-8850', 'Bosnia and Herzegovina',	'0081 009772', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO counterparty (counterparty_legal_name, legal_address_id, commercial_contact, delivery_contact, created_at, last_updated)
VALUES 
('Fahey and Sons', 1, 'Micheal Toy', 'Mrs. Lucy Runolfsdottir', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Leannon, Predovic and Morar', 2, 'Melba Sanford', 'Jean Hane III', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Armstrong Inc', 3, 'Jane Wiza', 'Myra Kovacek', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Kohler Inc', 4, 'Taylor Haag', 'Alfredo Cassin II', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Frami, Yundt and Macejkovic', 5, 'Homer Mitchell', 'Ivan Balistreri', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO staff (first_name, last_name, department_id, email_address, created_at, last_updated)
VALUES
('Jeremie', 'Franey', 1, 'jeremie.franey@terrifictotes.com', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Deron	Beier', 2, 'deron.beier@terrifictotes.com', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Jeanette	Erdman', 3, 'jeanette.erdman@terrifictotes.com', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Ana	Glover', 4, 'ana.glover@terrifictotes.com', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
('Magdalena	Zieme', 5, 'magdalena.zieme@terrifictotes.com', '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO purchase_order (staff_id, counterparty_id, item_code, item_quantity, item_unit_price, currency_id, agreed_delivery_date, agreed_payment_date, agreed_delivery_location_id, created_at, last_updated)
VALUES 
(1,	1,	'ZDOI5EA', 371, 361.39, 2, '2022-11-09', '2022-11-07', 6'2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(2,	2,	'QLZLEXR', 286,	199.04,	2, '2022-11-04', '2022-11-07', 8'2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(3, 3, 'AN3D85L', 839, 658.58, 2, '2022-11-05', '2022-11-04', 16'2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(4, 4, 'I9MET53', 316, 803.82, 3, '2022-11-10', '2022-11-05', 2'2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(5, 5, 'QKQQ9IS', 597, 714.89, 2, '2022-12-03', '2022-12-03', 11, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO sales_order (created_at, last_updated, design_id, staff_id, counterparty_id, units_sold, unit_price, currency_id, agreed_delivery_date, agreed_payment_date, agreed_delivery_location_id)
VALUES 
(1, 1, 1, 84754, 2.43, 1, '2022-11-10', '2022-11-03', 4, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(2, 2, 2, 42972, 3.94, 2, '2022-11-07', '2022-11-08', 8, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(3, 3, 3, 65839, 2.91, 3, '2022-11-06', '2022-11-07', 19, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(4, 4, 4, 32069, 3.89, 1, '2022-11-05', '2022-11-07', 15, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(5, 5, 5, 49659, 2.41, 3, '2022-11-05', '2022-11-08', 25, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO transactions (transaction_type, sales_order_id, purchase_order_id, created_at, last_updated)
VALUES 
(PURCHASE, NULL, 2, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(PURCHASE, NULL, 3, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(SALE, 1, NULL, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(PURCHASE, NULL, 1, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(PURCHASE, NULL, 4, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');

INSERT INTO payment (transaction_id, counterparty_id, payment_amount, currency_id, payment_type_id, paid, payment_date, company_acc_number, counterparty_acc_number, created_at, last_updated)
VALUES 
(1, 1, 552548.62, 1, 3, false, '2022-11-04', 67305075, 31622269, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(2, 2, 205952.22, 3, 2, false, '2022-11-03', 81718079, 47839086, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(3, 3, 57067.20, 2, 3, false, '2022-11-06', 66213052, 91659548, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(4, 4, 254007.12, 3, 4, false, '2022-11-05', 32948439, 90135525, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962'), 
(5, 5, 250459.52, 2, 1, false, '2022-11-05', 34445327, 71673373, '2022-11-03 14:20:49.962', '2022-11-03 14:20:49.962');



