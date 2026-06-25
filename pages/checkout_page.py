from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = page.locator('[data-test="complete-header"]')
        self.error_message = page.locator('[data-test="error"]')

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self) -> None:
        self.continue_button.click()

    def finish_order(self) -> None:
        self.finish_button.click()

    def should_show_success_message(self) -> None:
        expect(self.complete_header).to_have_text("Thank you for your order!")

    def should_show_error(self, expected_text: str) -> None:
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_text)