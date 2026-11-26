# 03 Test Automation

Automated API tests for Restful-booker, written in Python with pytest and requests. They automate the test cases from [`01-manual-testing/test-cases.csv`](../01-manual-testing/test-cases.csv).

## Structure
```
03-test-automation/
├── tests/
│   └── test_restful_booker.py   14 tests, one per test case
├── config.py                    base URL, headers, timeout, demo credentials
├── conftest.py                  fixtures shared by the tests
├── pytest.ini                   pytest settings
├── requirements.txt             dependencies
└── README.md
```

## How to run
```
pip install -r requirements.txt
pytest -v
```
The base URL defaults to `https://restful-booker.herokuapp.com` and can be changed with the `BASE_URL` environment variable.

## How the tests are built
- Every test sends a request with `requests` and checks the result with `assert` (status code and response body).
- Four fixtures in `conftest.py` prepare what the tests need:
  - `token`: an authentication token, requested once per test run
  - `auth_headers`: request headers that contain the token (needed for update and delete)
  - `booking_data`: a valid booking, a fresh copy for every test
  - `booking_id`: creates a booking before the test and deletes it after the test (`yield`)
- Tests that create their own data delete it at the end, because the public instance is shared and reset from time to time.
- The test name contains the id of the matching test case (e.g. `test_tc007_...` automates `TC-007`).

## Known bugs
Two tests describe the correct behaviour and currently fail because of the bugs found during manual testing. They are marked as expected failures (`xfail`) with the bug id, so the run stays green while the bugs are documented. If a bug gets fixed, the test shows up as `XPASS` in the summary.

| Test | Bug |
|---|---|
| `test_tc008_create_booking_without_required_field` | [BUG-001](../01-manual-testing/bug-reports/BUG-001.md) |
| `test_tc009_create_booking_with_checkout_before_checkin` | [BUG-002](../01-manual-testing/bug-reports/BUG-002.md) |

## CI
The GitHub Actions workflow [`tests.yml`](../.github/workflows/tests.yml) runs the tests on every push to `main`, on pull requests and on demand.
