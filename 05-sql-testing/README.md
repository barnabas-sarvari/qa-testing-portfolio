# 05 SQL Testing

SQL queries for checking and validating booking data. A small sample database holds hotel bookings, similar to the Restful-booker domain, and automated tests check that every query returns the expected result.

## Contents
- [`database.sql`](database.sql): the tables (`rooms`, `guests`, `bookings`) and the sample data
- [`queries.sql`](queries.sql): 10 tasks, each with its SQL query
- [`test_queries.py`](test_queries.py): runs every query against the database and compares the result with the expected rows
- [`requirements.txt`](requirements.txt): dependencies

## Tasks
| # | Task | SQL used |
|---|---|---|
| Q1 | Bookings of one guest | JOIN, WHERE, ORDER BY |
| Q2 | Bookings above a price | WHERE, ORDER BY (two columns, descending) |
| Q3 | Bookings without deposit | WHERE |
| Q4 | Bookings without additional needs | IS NULL |
| Q5 | Bookings with invalid dates (checkout not after checkin) | WHERE, comparing columns |
| Q6 | Bookings with guest names | JOIN |
| Q7 | Number of bookings per room | JOIN, GROUP BY, COUNT |
| Q8 | Revenue per room | JOIN, GROUP BY, SUM |
| Q9 | Guests without bookings | LEFT JOIN, IS NULL |
| Q10 | Rooms with more than 4 bookings | GROUP BY, HAVING |

Q5 connects to the API testing: [BUG-002](../01-manual-testing/bug-reports/BUG-002.md) shows that the API accepts a booking with a checkout date before the checkin date, and this query finds such records in the data.

## How to run
Run the tests inside this folder:
```
cd 05-sql-testing
pip install -r requirements.txt
pytest -v
```
A query that returns a different result than expected makes its test fail and shows the difference.

## Database
```
rooms (room_id, room_name, price_per_night)
guests (guest_id, firstname, lastname)
bookings (booking_id, guest_id, room_id, checkin, checkout, total_price, deposit_paid, additional_needs)
```
`bookings.guest_id` refers to `guests`, `bookings.room_id` refers to `rooms`.
