# QA Testing Portfolio

A hands-on testing project covering manual testing, API testing, test automation, mobile testing, SQL testing and web UI automation. The system under test for the API work is [Restful-booker](https://restful-booker.herokuapp.com/), a public booking API built for testing practice. The web UI tests run against [Sauce Demo](https://www.saucedemo.com), a demo shop built for automation practice.

## Overview

| Area | Tools | Folder | Result |
|---|---|---|---|
| Manual testing | Test plan, test cases, bug reports | [`01-manual-testing/`](01-manual-testing/) | 14 test cases executed: 12 passed, 2 failed, 2 bugs reported |
| API testing | Postman | [`02-api-testing/`](02-api-testing/) | All 8 endpoint/method combinations covered |
| Test automation | Python, pytest, requests, GitHub Actions | [`03-test-automation/`](03-test-automation/) | 14 automated tests in CI: 12 pass, 2 expected failures for known bugs |
| Mobile testing | Manual testing on an Android emulator (IMDb app) | [`04-mobile-testing/`](04-mobile-testing/) | 10 test cases executed: 10 passed |
| SQL testing | SQL, SQLite, pytest | [`05-sql-testing/`](05-sql-testing/) | 10 queries checked by automated tests |
| Web UI automation | Python, pytest, Playwright | [`06-web-ui-automation/`](06-web-ui-automation/) | 8 browser tests run in CI |

## How the areas connect

1. **Manual testing** defines what to test: a test plan, test cases and reported defects.
2. **API testing** explores and verifies the endpoints interactively in Postman.
3. **Test automation** turns the stable test cases into automated pytest checks. The `Automated` column in the test case list links each case to its test.
4. **Mobile testing** applies the same approach (test cases, bug reports) to a mobile application.
5. **SQL testing** checks data with queries; one of them finds the invalid dates described in BUG-002.
6. **Web UI automation** automates browser checks of a web application (Sauce Demo) with Playwright.

## Repository structure

```
qa-testing-portfolio/
├── 01-manual-testing/      test plan, test cases, bug reports
├── 02-api-testing/         Postman collection and API test notes
├── 03-test-automation/     pytest + requests automated tests
├── 04-mobile-testing/      mobile test cases and bug reports
├── 05-sql-testing/         SQL queries checked by automated tests
├── 06-web-ui-automation/   browser tests with Playwright
└── .github/workflows/      CI: automated tests run on every push
```

## Tech stack

Python, pytest, requests, Playwright, Postman, SQL, GitHub Actions, Markdown / CSV for test documentation.

## How to run the automated tests

```
cd 03-test-automation
pip install -r requirements.txt
pytest -v

```
See [`03-test-automation/`](03-test-automation/) for details.

The SQL and web UI tests have their own instructions in [05-sql-testing/](05-sql-testing/) and [06-web-ui-automation/](06-web-ui-automation/).
