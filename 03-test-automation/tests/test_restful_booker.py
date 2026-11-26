"""Automated tests for the Restful-booker API.

Every test maps to a test case in 01-manual-testing/test-cases.csv

The fixtures used here (token, auth_headers, booking_data, booking_id)
are defined in conftest.py.
"""
import uuid

import pytest
import requests

from config import BASE_URL, HEADERS, PASSWORD, TIMEOUT, USERNAME

UNKNOWN_BOOKING_ID = 99999999


# --- Health check and authentication ---------------------------------------


def test_tc001_health_check():
    response = requests.get(f"{BASE_URL}/ping", timeout=TIMEOUT)

    assert response.status_code == 201
    assert response.text == "Created"


def test_tc002_get_token_with_valid_credentials():
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": USERNAME, "password": PASSWORD},
        headers=HEADERS,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    assert "token" in response.json()


def test_tc003_get_token_with_invalid_credentials():
    response = requests.post(
        f"{BASE_URL}/auth",
        json={"username": USERNAME, "password": "wrongpassword"},
        headers=HEADERS,
        timeout=TIMEOUT,
    )
    body = response.json()

    assert "token" not in body
    assert body["reason"] == "Bad credentials"


# --- Reading bookings -------------------------------------------------------


def test_tc004_list_all_booking_ids(booking_id):
    # the booking_id fixture makes sure at least one booking exists
    response = requests.get(f"{BASE_URL}/booking", headers=HEADERS, timeout=TIMEOUT)
    items = response.json()

    assert response.status_code == 200
    assert len(items) > 0
    assert "bookingid" in items[0]


def test_tc005_get_booking_by_valid_id(booking_id, booking_data):
    response = requests.get(
        f"{BASE_URL}/booking/{booking_id}", headers=HEADERS, timeout=TIMEOUT
    )

    assert response.status_code == 200
    assert response.json() == booking_data


def test_tc006_get_booking_with_non_existent_id():
    response = requests.get(
        f"{BASE_URL}/booking/{UNKNOWN_BOOKING_ID}", headers=HEADERS, timeout=TIMEOUT
    )

    assert response.status_code == 404


def test_tc014_filter_bookings_by_firstname(booking_data, auth_headers):
    unique_name = "Qa" + uuid.uuid4().hex[:8]  # a name no other booking has
    booking_data["firstname"] = unique_name
    created = requests.post(
        f"{BASE_URL}/booking", json=booking_data, headers=HEADERS, timeout=TIMEOUT
    )
    new_id = created.json()["bookingid"]

    response = requests.get(
        f"{BASE_URL}/booking",
        params={"firstname": unique_name},
        headers=HEADERS,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    assert response.json() == [{"bookingid": new_id}]

    requests.delete(
        f"{BASE_URL}/booking/{new_id}", headers=auth_headers, timeout=TIMEOUT
    )


# --- Creating bookings ------------------------------------------------------


def test_tc007_create_booking_with_valid_data(booking_data, auth_headers):
    response = requests.post(
        f"{BASE_URL}/booking", json=booking_data, headers=HEADERS, timeout=TIMEOUT
    )
    body = response.json()

    assert response.status_code == 200
    assert isinstance(body["bookingid"], int)
    assert body["booking"] == booking_data

    requests.delete(
        f"{BASE_URL}/booking/{body['bookingid']}",
        headers=auth_headers,
        timeout=TIMEOUT,
    )


# Known bug: the test describes the correct behaviour and is expected to fail.
@pytest.mark.xfail(
    reason="BUG-001: a missing lastname returns 500 instead of a 4xx validation error"
)
def test_tc008_create_booking_without_required_field(booking_data):
    del booking_data["lastname"]

    response = requests.post(
        f"{BASE_URL}/booking", json=booking_data, headers=HEADERS, timeout=TIMEOUT
    )

    assert 400 <= response.status_code < 500


# Known bug: the test describes the correct behaviour and is expected to fail.
@pytest.mark.xfail(
    reason="BUG-002: a booking with checkout before checkin is accepted (200 OK)"
)
def test_tc009_create_booking_with_checkout_before_checkin(booking_data):
    booking_data["bookingdates"] = {"checkin": "2026-12-10", "checkout": "2026-12-01"}

    response = requests.post(
        f"{BASE_URL}/booking", json=booking_data, headers=HEADERS, timeout=TIMEOUT
    )

    assert response.status_code >= 400


# --- Updating and deleting bookings -----------------------------------------


def test_tc010_update_booking_with_valid_token(booking_id, booking_data, auth_headers):
    updated = booking_data.copy()
    updated["firstname"] = "James"

    response = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=updated,
        headers=auth_headers,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    assert response.json() == updated


def test_tc011_update_booking_without_token(booking_id, booking_data):
    updated = booking_data.copy()
    updated["firstname"] = "James"

    response = requests.put(
        f"{BASE_URL}/booking/{booking_id}",
        json=updated,
        headers=HEADERS,  # no token
        timeout=TIMEOUT,
    )

    assert response.status_code == 403


def test_tc012_partial_update_of_firstname(booking_id, booking_data, auth_headers):
    response = requests.patch(
        f"{BASE_URL}/booking/{booking_id}",
        json={"firstname": "Alex"},
        headers=auth_headers,
        timeout=TIMEOUT,
    )

    expected = booking_data.copy()
    expected["firstname"] = "Alex"  # only the firstname should change

    assert response.status_code == 200
    assert response.json() == expected


def test_tc013_delete_booking_with_valid_token(booking_id, auth_headers):
    delete_response = requests.delete(
        f"{BASE_URL}/booking/{booking_id}", headers=auth_headers, timeout=TIMEOUT
    )
    get_response = requests.get(
        f"{BASE_URL}/booking/{booking_id}", headers=HEADERS, timeout=TIMEOUT
    )

    assert delete_response.status_code == 201
    assert get_response.status_code == 404
