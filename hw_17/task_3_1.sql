--1. Find a user who had the biggest amount ADD
--of reservations. Return user name and user_id

SELECT users.user_name, users.id, COUNT(reservations.id) AS reservation_count
FROM users
LEFT JOIN reservations ON users.id = reservations.guest_id
GROUP BY users.user_name, users.id
ORDER BY reservation_count DESC
LIMIT 1;

