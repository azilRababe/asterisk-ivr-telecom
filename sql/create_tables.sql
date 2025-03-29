CREATE DATABASE asterisk;

USE asterisk;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phone VARCHAR(20) UNIQUE,
    pin VARCHAR(10),
    balance DECIMAL(10,2)
);

INSERT INTO users (phone, pin, balance) VALUES
('0600000001', '1234', 20.50),
('0600000002', '5678', 35.00);
