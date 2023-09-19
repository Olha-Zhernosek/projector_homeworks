--1. Find a user who had the biggest amount ADD
--of reservations. Return user name and user_id

SELECT u.id, u.user_name
FROM users AS u
JOIN reservations r ON u.id = r.guest_id
GROUP BY u.id, u.user_name
ORDER BY COUNT(*) DESC
LIMIT 1;

