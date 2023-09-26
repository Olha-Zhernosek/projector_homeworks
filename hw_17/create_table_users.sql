CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    user_type VARCHAR(20) NOT NULL,
    user_name VARCHAR(40) NOT NULL,
    user_email VARCHAR(64) NOT NULL,
    user_phone CHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO users (user_type, user_name, user_email, user_phone)
VALUES
    ('host', 'person_1', 'person_1@example.com', '+1-555-555-5555'),
    ('host', 'person_2', 'person_2@example.com', '+2-555-123-4567'),
    ('host', 'person_3', 'person_3@example.com', '+3-555-123-4567'),
    ('guest', 'person_4', 'person_4@example.com', '+4-555-123-4567'),
    ('guest', 'person_5', 'person_5@example.com', '+5-555-123-4567'),
    ('guest', 'person_6', 'person_6@example.com', '+6-555-987-6543');