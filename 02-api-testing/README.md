# 02 API Testing

Interactive API testing of Restful-booker with Postman. The requests were executed manually against the public instance; the test cases and results are in [`01-manual-testing/test-cases.csv`](../01-manual-testing/test-cases.csv).

## Contents
- [`postman-collection.json`](postman-collection.json): exported Postman collection

## How to use
1. Import the collection into Postman (Import → select the JSON file).
2. Base URL: `https://restful-booker.herokuapp.com`
3. Run the token request first (`POST /auth`), then create a booking and use its `bookingid` in the read, update and delete requests.
4. Protected requests (PUT, PATCH, DELETE) need the token in a `Cookie: token=<value>` header.

The instance is shared and is reset from time to time, so a booking can disappear within minutes. Create a fresh booking before each update or delete test.

## Coverage
| Endpoint | Method | Covered | Test cases |
|---|---|---|---|
| /ping | GET | Yes | TC-001 |
| /auth | POST | Yes | TC-002, TC-003 |
| /booking | GET | Yes | TC-004, TC-014 |
| /booking/{id} | GET | Yes | TC-005, TC-006 |
| /booking | POST | Yes | TC-007, TC-008, TC-009 |
| /booking/{id} | PUT | Yes | TC-010, TC-011 |
| /booking/{id} | PATCH | Yes | TC-012 |
| /booking/{id} | DELETE | Yes | TC-013 |
