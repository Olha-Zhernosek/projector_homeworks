-- (Optional) Find a host with the best average rating. Return hostname and host_id

SELECT
    users.user_name AS host_name,
    users.id AS host_id,
    AVG(reviews.rating) AS average_rating
FROM
    users
LEFT JOIN
    reservations ON reservations.guest_id = users.id
LEFT JOIN
    payments ON payments.reservation_id = reservations.id
LEFT JOIN
    reviews ON reviews.payment_id = payments.id
GROUP BY
    users.user_name,
    users.id
ORDER BY
    average_rating DESC
LIMIT 1;


