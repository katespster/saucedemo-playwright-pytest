import pytest


@pytest.mark.smoke
def test_user_can_add_product_to_cart(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page

    inventory_page.should_be_opened()
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    inventory_page.should_have_cart_badge("1")


@pytest.mark.regression
def test_user_can_remove_product_from_cart(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page

    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.should_have_cart_badge("1")

    inventory_page.remove_product_from_cart("sauce-labs-backpack")
    inventory_page.should_not_have_cart_badge()


@pytest.mark.regression
def test_sort_products_by_price_low_to_high(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page

    inventory_page.sort_by_price_low_to_high()
    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices), f"Prices are not sorted: {prices}"