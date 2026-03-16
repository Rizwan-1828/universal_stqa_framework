import allure
from pages.login_page import LoginPage

@allure.feature("UI Elements Verification")
@allure.story("Valid UI Elements")
@allure.title("TC07 - Verify presence of essential login elements")
def test_valid_ui_elements(driver, base_url):
    """
    Test that the login page contains the expected input fields and buttons.
    """
    login_page = LoginPage(driver)
    
    # Open Login Page
    login_page.open(base_url)
    
    # Verify core elements are present
    with allure.step("Verify Username input is present"):
        assert login_page.is_element_present(login_page.USERNAME_INPUT), "Username input not found"
        
    with allure.step("Verify Password input is present"):
        assert login_page.is_element_present(login_page.PASSWORD_INPUT), "Password input not found"
        
    with allure.step("Verify Login button is present"):
        assert login_page.is_element_present(login_page.LOGIN_BUTTON), "Login button not found"