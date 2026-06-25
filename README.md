# SauceDemo Playwright Pytest Automation

This is a portfolio UI test automation project for SauceDemo.

## Stack

- Python
- Pytest
- Playwright
- Page Object Model
- Allure Report
- GitHub Actions

## Covered scenarios

### Login

- Successful login
- Locked out user cannot login
- Empty credentials validation
- Wrong password validation

### Inventory and cart

- Add product to cart
- Remove product from cart
- Sort products by price: low to high

### Checkout

- Successful checkout
- Checkout validation for required first name

## How to run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
pytest