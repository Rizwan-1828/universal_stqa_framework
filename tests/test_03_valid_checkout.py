import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@allure.feature("Checkout Flow")
@allure.story("Valid Checkout")
@allure.title("TC03 - Successfully finish checkout process")
def test_valid_checkout(driver, base_url):
    """
    Test adding an item to the cart and successfully completing the checkout flow.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    
    # Login
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    # Add item and go to cart
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    
    with allure.step("Verify Cart Badge is '1'"):
        assert inventory_page.get_cart_badge_count() == "1"
        
    inventory_page.go_to_cart()
    
    # Checkout steps
    cart_page.proceed_to_checkout()
    checkout_page.fill_information("John", "Doe", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()
    
    # Assert Order Complete
    with allure.step("Verify order completion message"):
        assert checkout_page.is_order_complete(), "Checkout completion header not found"
        assert "THANK YOU FOR YOUR ORDER" in checkout_page.get_completion_text().upper()