import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("Authentication")
@allure.story("Valid Login")
@allure.title("TC01 - Successful Login with valid credentials")
def test_valid_login(driver, base_url):
    """
    Test successful login flow and verify access to inventory page.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    # Step 1: Open Login Page
    login_page.open(base_url)
    
    # Step 2: Login
    login_page.login("standard_user", "secret_sauce")
    
    # Step 3: Verify Inventory Page presence
    with allure.step("Verify login redirects to Products page"):
        assert inventory_page.is_on_inventory_page(), "Failed to locate Products title after login."