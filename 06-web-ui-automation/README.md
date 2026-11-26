# Web UI Automation

Automated browser tests for the demo shop [Sauce Demo](https://www.saucedemo.com), written with Python, pytest and Playwright.

## What is tested

| Test | What it checks |
|------|----------------|
| `test_login_with_valid_user` | A valid user can log in and sees the Products page |
| `test_login_with_wrong_password` | Wrong password shows an error message |
| `test_login_with_locked_out_user` | A locked out user cannot log in |
| `test_add_product_to_cart` | Adding a product shows 1 in the cart badge |
| `test_cart_contains_added_product` | The added product is listed in the cart |
| `test_inventory_shows_six_products` | The product list shows 6 products |
| `test_remove_product_from_cart` | Removing a product clears the cart badge |
| `test_checkout_complete` | A full order can be completed |

The login steps for the cart and checkout tests are in a pytest fixture (`logged_in_page`).

## How to run

```
cd 06-web-ui-automation
pip install -r requirements.txt
playwright install chromium
pytest -v
```

To watch the browser while the tests run:

```
pytest -v --headed --slowmo 1000
```
