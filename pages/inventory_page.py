from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class InventoryPage(BasePage):
    """Page Object for the Sauce Demo Products/Inventory Page"""
    
    # Locators
    TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    # Dynamic locator generation
    def _add_to_cart_locator_for(self, item_name):
        return (By.ID, f"add-to-cart-{item_name}")

    def _remove_from_cart_locator_for(self, item_name):
        return (By.ID, f"remove-{item_name}")

    @allure.step("Verify user is on Inventory Page")
    def is_on_inventory_page(self):
        return "Products" in self.get_text(self.TITLE)

    @allure.step("Add Item to cart: '{item_name}'")
    def add_item_to_cart(self, item_name):
        self.click(self._add_to_cart_locator_for(item_name))

    @allure.step("Remove Item from cart: '{item_name}'")
    def remove_item_from_cart(self, item_name):
        self.click(self._remove_from_cart_locator_for(item_name))

    @allure.step("Go to Shopping Cart")
    def go_to_cart(self):
        self.click(self.SHOPPING_CART_LINK)

    @allure.step("Get Cart Badge Count")
    def get_cart_badge_count(self):
        if self.is_element_present(self.SHOPPING_CART_BADGE):
            return self.get_text(self.SHOPPING_CART_BADGE)
        return "0"

    @allure.step("Logout of Application")
    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
