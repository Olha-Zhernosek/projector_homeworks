--2. (Optional) Find a host who earned the biggest amount of money for the 
--last month. Return hostname and host_id

SELECT
    users.user_name AS host_name,
    users.id AS host_id,
    SUM(payments.paid_amount) AS total_paid
FROM
    users
LEFT JOIN
    reservations ON users.id = reservations.guest_id
LEFT JOIN
    payments ON reservations.id = payments.reservation_id
WHERE
    reservations.check_in_date >= '2023-08-01' 
    AND reservations.check_out_date <= '2023-08-31'
GROUP BY
    users.user_name,
    users.id
ORDER BY
    total_paid DESC
LIMIT 1;
