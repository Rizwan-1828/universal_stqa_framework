from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    """Page Object for the Sauce Demo Login Page"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    @allure.step("Open Login Page using Base URL: {base_url}")
    def open(self, base_url):
        self.open_url(base_url)
        # Verify page loaded
        self.find(self.USERNAME_INPUT)
        
    @allure.step("Login with Username: '{username}' and Password: '{password}'")
    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        
    @allure.step("Get Login Error Message")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
