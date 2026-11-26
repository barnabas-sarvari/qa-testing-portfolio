# Test Plan: Restful-booker API

## 1. Purpose
Verify that the Restful-booker booking API behaves as documented: authentication, creating, reading, updating and deleting bookings, including invalid input and missing authorization.

## 2. System under test
- Application: Restful-booker (public practice API)
- Base URL: https://restful-booker.herokuapp.com
- Documentation: https://restful-booker.herokuapp.com/apidoc/index.html

## 3. Scope

**In scope**
- Health check (`GET /ping`)
- Authentication (`POST /auth`)
- Booking operations: list, get, create, full update (PUT), partial update (PATCH), delete
- Response status codes and response body structure
- Validation of invalid and missing input
- Authorization (requests with and without a valid token)

**Out of scope**
- Performance and load testing
- Security testing beyond basic authorization checks

## 4. Test types
- Functional testing (positive and negative)
- Boundary and validation testing
- Authorization testing
- Regression checks (automated, see `03-test-automation/`)

## 5. Approach
1. Explore the API manually in Postman and compare behaviour with the documentation.
2. Design test cases (see [`test-cases.csv`](test-cases.csv)) covering positive, negative and boundary scenarios.
3. Execute the test cases and record actual results and status.
4. Report every confirmed defect as a separate bug report in `bug-reports/`.
5. Automate stable, repeatable cases with pytest and run them in CI.

## 6. Tools and environment
- Postman for manual API testing
- Python 3, pytest, requests for automation
- GitHub Actions for continuous execution
- Environment: public shared instance 

## 7. Entry criteria
- API is reachable (`GET /ping` returns a success status)
- API documentation is available
- Test data (valid credentials, example booking payload) is prepared

## 8. Exit criteria
- All planned test cases are executed
- All confirmed defects are documented with reproduction steps
- Automated tests run successfully in CI

## 9. Risks
| Risk | Impact | Mitigation |
|---|---|---|
| Shared public instance, data can be changed by others | Unstable or unexpected results | Create own test data in each test, avoid relying on existing bookings |
| API may be reset or unavailable | Test runs fail | Re-run, note the time of failure in the results |
