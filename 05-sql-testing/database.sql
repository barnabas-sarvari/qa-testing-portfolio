-- Sample database for the SQL exercises (SQLite).
-- Hotel booking data, similar to the Restful-booker domain.

CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY,
    room_name TEXT NOT NULL,
    price_per_night INTEGER NOT NULL
);

CREATE TABLE guests (
    guest_id INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL
);

CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY,
    guest_id INTEGER NOT NULL REFERENCES guests (guest_id),
    room_id INTEGER NOT NULL REFERENCES rooms (room_id),
    checkin TEXT NOT NULL,           -- date, format YYYY-MM-DD
    checkout TEXT NOT NULL,          -- date, format YYYY-MM-DD
    total_price INTEGER NOT NULL,
    deposit_paid INTEGER NOT NULL,   -- 1 = paid, 0 = not paid
    additional_needs TEXT            -- can be NULL
);

INSERT INTO rooms (room_id, room_name, price_per_night) VALUES
    (1, 'Standard', 80),
    (2, 'Deluxe', 120),
    (3, 'Suite', 200),
    (4, 'Attic', 60);

INSERT INTO guests (guest_id, firstname, lastname) VALUES
    (1, 'Jim', 'Brown'),
    (2, 'Mary', 'Jones'),
    (3, 'Sally', 'Smith'),
    (4, 'John', 'Doe'),
    (5, 'Anna', 'Kovacs'),
    (6, 'Peter', 'Nagy'),
    (7, 'Laura', 'Meyer'),
    (8, 'Tom', 'Wilson');

INSERT INTO bookings
    (booking_id, guest_id, room_id, checkin, checkout, total_price, deposit_paid, additional_needs)
VALUES
    (1, 1, 1, '2026-12-01', '2026-12-05', 320, 1, 'Breakfast'),
    (2, 1, 2, '2026-12-10', '2026-12-12', 240, 0, NULL),
    (3, 2, 1, '2026-12-03', '2026-12-04', 80, 1, NULL),
    (4, 2, 3, '2026-12-20', '2026-12-27', 1400, 1, 'Late checkout'),
    (5, 3, 2, '2026-11-25', '2026-11-28', 360, 0, 'Extra bed'),
    (6, 4, 1, '2026-12-15', '2026-12-14', 80, 0, NULL),
    (7, 5, 3, '2026-12-01', '2026-12-03', 400, 1, 'Breakfast'),
    (8, 5, 1, '2027-01-05', '2027-01-08', 240, 1, NULL),
    (9, 6, 2, '2026-12-24', '2026-12-24', 120, 0, 'Parking'),
    (10, 6, 2, '2027-01-10', '2027-01-12', 240, 1, NULL),
    (11, 7, 3, '2026-12-28', '2026-12-30', 400, 1, 'Breakfast'),
    (12, 7, 1, '2026-11-10', '2026-11-12', 160, 0, NULL),
    (13, 3, 3, '2027-02-01', '2027-02-04', 600, 1, 'Airport transfer'),
    (14, 1, 1, '2027-02-10', '2027-02-11', 80, 1, NULL),
    (15, 4, 2, '2027-03-01', '2027-03-05', 480, 0, 'Breakfast');
