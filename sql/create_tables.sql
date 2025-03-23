CREATE DATABASE telecom;

USE telecom;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone_number VARCHAR(20) UNIQUE,
    pin_code VARCHAR(10),
    balance DECIMAL(10,2)
);

INSERT INTO users (phone_number, pin_code, balance) VALUES
('0600000001', '1234', 20.50),
('0600000002', '5678', 35.00);
