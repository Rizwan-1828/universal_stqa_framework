from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class CheckoutPage(BasePage):
    """Page Object for the Sauce Demo Checkout Steps"""
    
    # Locators - Step 1
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    # Locators - Step 2 (Overview)
    FINISH_BUTTON = (By.ID, "finish")
    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    
    # Locators - Complete
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    @allure.step("Fill Checkout Information: {first_name} {last_name}, {zip_code}")
    def fill_information(self, first_name, last_name, zip_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, zip_code)
        
    @allure.step("Continue to Checkout Overview")
    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)
        
    @allure.step("Get Checkout Error Message")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
        
    @allure.step("Finish Checkout / Place Order")
    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
        
    @allure.step("Verify Order is Complete")
    def is_order_complete(self):
        return self.is_element_present(self.COMPLETE_HEADER)
        
    @allure.step("Get Order Completion Header Text")
    def get_completion_text(self):
        return self.get_text(self.COMPLETE_HEADER)
