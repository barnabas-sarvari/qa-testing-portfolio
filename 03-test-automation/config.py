"""Settings shared by the fixtures and the tests."""
import os

BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
TIMEOUT = 30  # seconds

# Public demo credentials from the Restful-booker documentation
USERNAME = "admin"
PASSWORD = "password123"
