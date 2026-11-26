# 01 Manual Testing

Test documentation for the Restful-booker API.

## Contents
- [`test-plan.md`](test-plan.md): purpose, scope and approach
- [`test-cases.csv`](test-cases.csv): designed and executed test cases, with actual results and status
- [`bug-reports/`](bug-reports/): one file per confirmed defect

## Summary
| Metric | Value |
|---|---|
| Test cases designed | 14 |
| Test cases executed | 14 |
| Passed / Failed | 12 / 2 |
| Bugs reported | 2 |

## Bugs found
| ID | Title | Severity | Test case |
|---|---|---|---|
| [BUG-001](bug-reports/BUG-001.md) | Server returns 500 when a booking is created without the required lastname | Medium | TC-008 |
| [BUG-002](bug-reports/BUG-002.md) | Booking is accepted with a checkout date before the checkin date | Medium | TC-009 |

