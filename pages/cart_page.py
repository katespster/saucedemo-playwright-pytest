from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.cart_items = page.locator('[data-test="inventory-item"]')

    def should_be_opened(self) -> None:
        expect(self.title).to_have_text("Your Cart")

    def should_have_items_count(self, expected_count: int) -> None:
        expect(self.cart_items).to_have_count(expected_count)

    def proceed_to_checkout(self) -> None:
        self.checkout_button.click()