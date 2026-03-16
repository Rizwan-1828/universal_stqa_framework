import allure
from pages.login_page import LoginPage

@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.title("TC02 - Failed Login with invalid credentials")
def test_invalid_login(driver, base_url):
    """
    Test invalid login flow ensuring appropriate error message is shown.
    """
    login_page = LoginPage(driver)
    
    # Step 1: Open Login Page
    login_page.open(base_url)
    
    # Step 2: Attempt Login
    login_page.login("invalid_user", "wrong_pass")
    
    # Step 3: Verify Error Message
    with allure.step("Verify error message contains 'Epic sadface'"):
        error_text = login_page.get_error_message()
        assert "Epic sadface" in error_text, f"Expected 'Epic sadface' in error but got: '{error_text}'"