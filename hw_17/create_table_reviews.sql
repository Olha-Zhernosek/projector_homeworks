CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    payment_id INTEGER REFERENCES payments(id),
    review_type VARCHAR(20) NOT NULL,
    rating DECIMAL(3,1) NOT NULL,
    comment TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO reviews (payment_id, review_type, rating, comment)
VALUES
    (1, 'Positive', 4.5, 'Great experience overall.'),
    (2, 'Negative', 2.0, 'Could be better.'),
    (3, 'Positive', 4.8, 'Highly recommended.'),
    (4, 'Positive', 5.0, 'Excellent service.'),
    (5, 'Negative', 3.5, 'Average experience.'),
    (6, 'Positive', 4.7, 'Very satisfied.');