from selenium.webdriver.common.by import By
import allure
from pages.login_page import LoginPage

@allure.feature("UI Elements Verification")
@allure.story("Invalid UI Elements")
@allure.title("TC08 - Verify non-existent element check")
def test_invalid_ui_elements(driver, base_url):
    """
    Test that checking for a non-existent element correctly returns False instead of crashing.
    """
    login_page = LoginPage(driver)
    
    # Open Login Page
    login_page.open(base_url)
    
    fake_element_locator = (By.ID, "non-existent-element")
    
    # Verify fake element is NOT present
    with allure.step("Verify fake element is not present on the page"):
        assert not login_page.is_element_present(fake_element_locator), "Found an element that should not exist"