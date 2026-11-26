-- SQL queries for the tasks below.
-- Each query returns exactly the columns named in the task, in that order.
-- Tables: rooms, guests, bookings (see database.sql).

-- Q1 Bookings of Jim Brown
-- Task: list the booking_id of every booking made by the guest Jim Brown, ordered by booking_id.
-- Columns: booking_id
SELECT b.booking_id
FROM bookings b
JOIN guests g ON g.guest_id = b.guest_id
WHERE g.firstname = 'Jim' AND g.lastname = 'Brown'
ORDER BY b.booking_id;


-- Q2 Expensive bookings
-- Task: list the bookings with a total_price above 300, the highest price first (same price: lower booking_id first).
-- Columns: booking_id, total_price
SELECT booking_id, total_price
FROM bookings
WHERE total_price > 300
ORDER BY total_price DESC, booking_id;


-- Q3 Bookings without deposit
-- Task: list the booking_id of every booking where the deposit is not paid, ordered by booking_id.
-- Columns: booking_id
SELECT booking_id
FROM bookings
WHERE deposit_paid = 0
ORDER BY booking_id;


-- Q4 Bookings without additional needs
-- Task: list the booking_id of every booking that has no additional needs (the value is NULL), ordered by booking_id.
-- Columns: booking_id
SELECT booking_id
FROM bookings
WHERE additional_needs IS NULL
ORDER BY booking_id;


-- Q5 Invalid dates
-- Task: find the bookings where the checkout is not after the checkin (invalid data, the same problem as BUG-002 in the API). Order by booking_id.
-- Columns: booking_id
SELECT booking_id
FROM bookings
WHERE checkout <= checkin
ORDER BY booking_id;


-- Q6 Bookings with guest names
-- Task: list every booking together with the first and last name of the guest, ordered by booking_id.
-- Columns: booking_id, firstname, lastname
SELECT b.booking_id, g.firstname, g.lastname
FROM bookings b
JOIN guests g ON g.guest_id = b.guest_id
ORDER BY b.booking_id;


-- Q7 Bookings per room
-- Task: count the bookings of each room. Show only rooms that have bookings, ordered by room_name.
-- Columns: room_name, booking_count
SELECT r.room_name, COUNT(*) AS booking_count
FROM rooms r
JOIN bookings b ON b.room_id = r.room_id
GROUP BY r.room_id, r.room_name
ORDER BY r.room_name;


-- Q8 Revenue per room
-- Task: add up the total_price of the bookings of each room, the highest revenue first.
-- Columns: room_name, total_revenue
SELECT r.room_name, SUM(b.total_price) AS total_revenue
FROM rooms r
JOIN bookings b ON b.room_id = r.room_id
GROUP BY r.room_id, r.room_name
ORDER BY total_revenue DESC;


-- Q9 Guests without bookings
-- Task: find the guests who have no booking at all.
-- Columns: firstname, lastname
SELECT g.firstname, g.lastname
FROM guests g
LEFT JOIN bookings b ON b.guest_id = g.guest_id
WHERE b.booking_id IS NULL;


-- Q10 Busy rooms
-- Task: list the rooms that have more than 4 bookings, the room with the most bookings first.
-- Columns: room_name, booking_count
SELECT r.room_name, COUNT(*) AS booking_count
FROM rooms r
JOIN bookings b ON b.room_id = r.room_id
GROUP BY r.room_id, r.room_name
HAVING COUNT(*) > 4
ORDER BY booking_count DESC;
