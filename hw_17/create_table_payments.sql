CREATE TABLE IF NOT EXISTS payments (
    id SERIAL PRIMARY KEY,
    reservation_id INTEGER REFERENCES reservations(id) ON DELETE CASCADE,
    paid_amount DECIMAL(10,2),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO payments (reservation_id, paid_amount)
VALUES
    (1, 100.00),
    (2, 75.50),
    (3, 120.75),
    (4, 90.25),
    (5, 110.00),
    (6, 45.95);
