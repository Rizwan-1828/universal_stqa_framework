import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.feature("Cart Functionality")
@allure.story("Empty Cart")
@allure.title("TC06 - Verify cart is empty initially")
def test_invalid_cart(driver, base_url):
    """
    Test navigating directly to the cart without adding items ensures it is empty.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    
    # Login
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    # Go straight to cart without adding
    inventory_page.go_to_cart()
    
    # Verify empty cart
    with allure.step("Verify Cart is empty"):
        assert cart_page.is_on_cart_page(), "Failed to navigate to cart page"
        assert cart_page.get_item_count() == 0, "Cart should be empty, but has items"