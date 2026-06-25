import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_successful_login(login_page, username, password):
    login_page.login(username, password)

    inventory_page = InventoryPage(login_page.page)
    inventory_page.should_be_opened()


@pytest.mark.regression
def test_locked_out_user_cannot_login(login_page, password):
    login_page.login("locked_out_user", password)

    login_page.should_show_error("Sorry, this user has been locked out.")


@pytest.mark.regression
def test_login_with_empty_credentials_shows_error(login_page):
    login_page.login("", "")

    login_page.should_show_error("Username is required")


@pytest.mark.regression
def test_login_with_wrong_password_shows_error(login_page, username):
    login_page.login(username, "wrong_password")

    login_page.should_show_error("Username and password do not match")