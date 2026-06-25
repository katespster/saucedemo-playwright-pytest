import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_user_can_complete_checkout(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page

    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    cart_page = CartPage(inventory_page.page)
    cart_page.should_be_opened()
    cart_page.should_have_items_count(1)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(inventory_page.page)
    checkout_page.fill_customer_info("Ekaterina", "Komyagina", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_order()

    checkout_page.should_show_success_message()


@pytest.mark.regression
def test_checkout_requires_first_name(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page

    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    cart_page = CartPage(inventory_page.page)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(inventory_page.page)
    checkout_page.fill_customer_info("", "Komyagina", "12345")
    checkout_page.continue_checkout()

    checkout_page.should_show_error("First Name is required")