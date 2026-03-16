from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    """Page Object for the Sauce Demo Shopping Cart Page"""
    
    # Locators
    CART_ITEMS_LIST = (By.CLASS_NAME, "cart_list")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    
    def _remove_button_for(self, item_name):
        return (By.ID, f"remove-{item_name}")

    @allure.step("Verify user is on Cart Page")
    def is_on_cart_page(self):
        # We ensure the list container is present
        return self.is_element_present(self.CART_ITEMS_LIST)
        
    @allure.step("Proceed to Checkout")
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        
    @allure.step("Continue Shopping")
    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    @allure.step("Remove Item from Cart Page: '{item_name}'")
    def remove_item(self, item_name):
        self.click(self._remove_button_for(item_name))
        
    @allure.step("Get number of distinct items in cart")
    def get_item_count(self):
        items = self.driver.find_elements(*self.CART_ITEM)
        return len(items)
