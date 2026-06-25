import re

from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.item_prices = page.locator('[data-test="inventory-item-price"]')

    def should_be_opened(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*inventory\.html"))
        expect(self.title).to_have_text("Products")

    def add_product_to_cart(self, product_id: str) -> None:
        self.page.locator(f'[data-test="add-to-cart-{product_id}"]').click()

    def remove_product_from_cart(self, product_id: str) -> None:
        self.page.locator(f'[data-test="remove-{product_id}"]').click()

    def should_have_cart_badge(self, expected_count: str) -> None:
        expect(self.cart_badge).to_have_text(expected_count)

    def should_not_have_cart_badge(self) -> None:
        expect(self.cart_badge).to_have_count(0)

    def open_cart(self) -> None:
        self.cart_link.click()

    def sort_by_price_low_to_high(self) -> None:
        self.sort_dropdown.select_option("lohi")

    def get_product_prices(self) -> list[float]:
        prices = []
        for price_text in self.item_prices.all_inner_texts():
            prices.append(float(price_text.replace("$", "")))
        return prices