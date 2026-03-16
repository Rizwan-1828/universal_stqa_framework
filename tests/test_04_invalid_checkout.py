import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Checkout Flow")
@allure.story("Invalid Checkout")
@allure.title("TC04 - Fail checkout when missing required information")
def test_invalid_checkout(driver, base_url):
    """
    Test that submitting empty information during checkout displays a validation error.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    
    # Login
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    # Add item and navigate to checkout
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page.proceed_to_checkout()
    
    # Submit empty form
    with allure.step("Submit checkout information form with empty fields"):
        checkout_page.continue_checkout()
        
    # Validation
    with allure.step("Verify validation error is displayed"):
        error_msg = checkout_page.get_error_message()
        assert "Error: First Name is required" in error_msg, f"Unexpected error: {error_msg}"