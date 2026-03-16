import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@allure.feature("Cart Functionality")
@allure.story("Valid Cart")
@allure.title("TC05 - Successfully add item and verify cart contents")
def test_valid_cart(driver, base_url):
    """
    Test adding an item to the cart and verifying it appears in the cart page.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    
    # Login
    login_page.open(base_url)
    login_page.login("standard_user", "secret_sauce")
    
    # Add item
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    assert inventory_page.get_cart_badge_count() == "1"
    
    # Go to cart
    inventory_page.go_to_cart()
    
    # Verify Cart
    with allure.step("Verify Cart contains the added item"):
        assert cart_page.is_on_cart_page(), "Failed to navigate to cart page"
        assert cart_page.get_item_count() == 1, "Expected 1 item in the cart"