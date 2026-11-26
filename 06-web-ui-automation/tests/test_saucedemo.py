import pytest
from playwright.sync_api import expect

@pytest.fixture
def logged_in_page(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    return page


def test_login_with_valid_user(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    assert page.inner_text('[data-test="title"]') == "Products"


def test_login_with_wrong_password(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "wrong_password")
    page.click('[data-test="login-button"]')
    assert "do not match" in page.inner_text('[data-test="error"]')


def test_add_product_to_cart(logged_in_page):
    logged_in_page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    assert logged_in_page.inner_text('[data-test="shopping-cart-badge"]') == "1"

def test_cart_contains_added_product(logged_in_page):
    logged_in_page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    logged_in_page.click('[data-test="shopping-cart-link"]')
    assert logged_in_page.inner_text('[data-test="inventory-item-name"]') == "Sauce Labs Backpack"

def test_inventory_shows_six_products(logged_in_page):
    expect(logged_in_page.locator('[data-test="inventory-item"]')).to_have_count(6)

def test_remove_product_from_cart(logged_in_page):
    logged_in_page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    logged_in_page.click('[data-test="remove-sauce-labs-backpack"]')
    expect(logged_in_page.locator('[data-test="shopping-cart-badge"]')).to_have_count(0)

def test_login_with_locked_out_user(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "locked_out_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.click('[data-test="login-button"]')
    assert "locked out" in page.inner_text('[data-test="error"]')

def test_checkout_complete(logged_in_page):
    logged_in_page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    logged_in_page.click('[data-test="shopping-cart-link"]')
    logged_in_page.click('[data-test="checkout"]')
    logged_in_page.fill('[data-test="firstName"]', "Test")
    logged_in_page.fill('[data-test="lastName"]', "User")
    logged_in_page.fill('[data-test="postalCode"]', "1111")
    logged_in_page.click('[data-test="continue"]')
    logged_in_page.click('[data-test="finish"]')
    assert logged_in_page.inner_text('[data-test="complete-header"]') == "Thank you for your order!"
