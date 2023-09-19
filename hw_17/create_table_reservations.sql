CREATE TABLE IF NOT EXISTS reservations (
    id SERIAL PRIMARY KEY,
    room_id INTEGER REFERENCES rooms(id),
    guest_id INTEGER REFERENCES users(id),
    check_in_date DATE NOT NULL,
    check_out_date DATE NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO reservations (guest_id, check_in_date, check_out_date)
VALUES
    (1, '2023-09-20', '2023-09-25'),
    (2, '2023-10-05', '2023-10-10'),
    (3, '2023-11-15', '2023-11-20'),
    (1, '2023-12-01', '2023-12-05'),
    (2, '2024-01-10', '2024-01-15'),
    (3, '2024-02-20', '2024-02-25');