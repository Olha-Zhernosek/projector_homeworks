CREATE TABLE IF NOT EXISTS rooms (
    id SERIAL PRIMARY KEY,
    host_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    attribute_name VARCHAR(20) NOT NULL,
    attribute_value BOOLEAN,
    price DECIMAL(10,2),
    number_of_guests INTEGER NOT NULL,
    adress VARCHAR(250),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO rooms (host_id, attribute_name, attribute_value, price, number_of_guests, adress)
VALUES
    (1, 'Room 1', TRUE, 100.00, 2, '123 Main Street'),
    (2, 'Room 2', FALSE, 75.50, 3, '456 Elm Street'),
    (1, 'Room 3', TRUE, 120.75, 2, '789 Oak Avenue'),
    (3, 'Room 4', FALSE, 90.25, 4, '101 Pine Road'),
    (2, 'Room 5', TRUE, 110.00, 2, '222 Maple Lane'),
    (3, 'Room 6', TRUE, 95.00, 3, '333 Birch Boulevard');