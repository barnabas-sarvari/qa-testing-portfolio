"""Fixtures for the Restful-booker API tests."""
import pytest
import requests

from config import BASE_URL, HEADERS, PASSWORD, TIMEOUT, USERNAME


@pytest.fixture(scope="session")
def token():
    """Authentication token, requested once for the whole test run."""
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": USERNAME, "password": PASSWORD},
        headers=HEADERS,
        timeout=TIMEOUT,
    )
    return response.json()["token"]


@pytest.fixture
def auth_headers(token):
    """Headers with a valid token, needed for update and delete requests."""
    headers = HEADERS.copy()
    headers["Cookie"] = f"token={token}"
    return headers


@pytest.fixture
def booking_data():
    """A valid booking. Every test gets its own copy, so it can be changed freely."""
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-12-01", "checkout": "2026-12-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def booking_id(booking_data, auth_headers):
    """Create a booking for the test, give back its id, delete it afterwards."""
    response = requests.post(
        f"{BASE_URL}/booking", json=booking_data, headers=HEADERS, timeout=TIMEOUT
    )
    new_id = response.json()["bookingid"]

    yield new_id

    requests.delete(
        f"{BASE_URL}/booking/{new_id}", headers=auth_headers, timeout=TIMEOUT
    )
