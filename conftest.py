import os

import pytest
from dotenv import load_dotenv

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


load_dotenv()


@pytest.fixture
def app_base_url() -> str:
    return os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com/")


@pytest.fixture
def username() -> str:
    return os.getenv("SAUCEDEMO_USERNAME", "standard_user")


@pytest.fixture
def password() -> str:
    return os.getenv("SAUCEDEMO_PASSWORD", "secret_sauce")


@pytest.fixture
def login_page(page, app_base_url) -> LoginPage:
    login_page = LoginPage(page)
    login_page.open(app_base_url)
    return login_page


@pytest.fixture
def logged_in_inventory_page(page, app_base_url, username, password) -> InventoryPage:
    login_page = LoginPage(page)
    login_page.open(app_base_url)
    login_page.login(username, password)
    return InventoryPage(page)
