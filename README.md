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

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
pytest

## CI/CD

The project uses GitHub Actions to run Playwright UI tests automatically.

The workflow is triggered on:

- push to `main`
- pull request to `main`
- manual run via `workflow_dispatch`

Pipeline steps:

1. Checkout repository
2. Set up Python
3. Install project dependencies
4. Install Playwright Chromium browser
5. Run Pytest tests
6. Upload Allure results and Playwright traces as artifacts