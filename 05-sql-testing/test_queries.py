"""Checks the SQL queries in queries.sql against the sample database."""
import sqlite3

import pytest


def read_file(name):
    with open(name, encoding="utf-8") as file:
        return file.read()


@pytest.fixture
def db():
    """An in-memory database with the tables and the data of database.sql."""
    connection = sqlite3.connect(":memory:")
    connection.executescript(read_file("database.sql"))
    yield connection
    connection.close()


def run_query(db, number):
    """Run query number 1-10 from queries.sql and return the rows it gives back."""
    queries = read_file("queries.sql").split(";")  # the queries are separated by ;
    return db.execute(queries[number - 1]).fetchall()


def test_q1_bookings_of_jim_brown(db):
    assert run_query(db, 1) == [(1,), (2,), (14,)]


def test_q2_expensive_bookings(db):
    expected = [(4, 1400), (13, 600), (15, 480), (7, 400), (11, 400), (5, 360), (1, 320)]
    assert run_query(db, 2) == expected


def test_q3_bookings_without_deposit(db):
    assert run_query(db, 3) == [(2,), (5,), (6,), (9,), (12,), (15,)]


def test_q4_bookings_without_additional_needs(db):
    assert run_query(db, 4) == [(2,), (3,), (6,), (8,), (10,), (12,), (14,)]


def test_q5_invalid_dates(db):
    assert run_query(db, 5) == [(6,), (9,)]


def test_q6_bookings_with_guest_names(db):
    expected = [
        (1, "Jim", "Brown"),
        (2, "Jim", "Brown"),
        (3, "Mary", "Jones"),
        (4, "Mary", "Jones"),
        (5, "Sally", "Smith"),
        (6, "John", "Doe"),
        (7, "Anna", "Kovacs"),
        (8, "Anna", "Kovacs"),
        (9, "Peter", "Nagy"),
        (10, "Peter", "Nagy"),
        (11, "Laura", "Meyer"),
        (12, "Laura", "Meyer"),
        (13, "Sally", "Smith"),
        (14, "Jim", "Brown"),
        (15, "John", "Doe"),
    ]
    assert run_query(db, 6) == expected


def test_q7_bookings_per_room(db):
    assert run_query(db, 7) == [("Deluxe", 5), ("Standard", 6), ("Suite", 4)]


def test_q8_revenue_per_room(db):
    assert run_query(db, 8) == [("Suite", 2800), ("Deluxe", 1440), ("Standard", 960)]


def test_q9_guests_without_bookings(db):
    assert run_query(db, 9) == [("Tom", "Wilson")]


def test_q10_busy_rooms(db):
    assert run_query(db, 10) == [("Standard", 6), ("Deluxe", 5)]
