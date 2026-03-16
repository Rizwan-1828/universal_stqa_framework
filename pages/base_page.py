from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log
import allure
import time

class BasePage:
    """Base class for all Page Objects containing common Selenium interactions and logging"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    @allure.step("Navigate to URL: {url}")
    def open_url(self, url):
        log.info(f"Navigating to URL: {url}")
        self.driver.get(url)
        time.sleep(1)  # Allow page to render visibly
        
    def find(self, locator):
        """Wait for an element to be present and return it"""
        return self.wait.until(EC.presence_of_element_located(locator))
        
    def click(self, locator):
        """Wait for an element to be clickable and click it"""
        log.info(f"Clicking on element with locator: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        time.sleep(0.5)  # Add visible delay before click
        element.click()
        time.sleep(0.5)  # Add visible delay after click
        
    def type_text(self, locator, text):
        """Wait for an element to be present, clear it, and enter text"""
        log.info(f"Typing text '{text}' into element: {locator}")
        element = self.find(locator)
        element.clear()
        time.sleep(0.5)  # Add visible delay before typing
        element.send_keys(text)
        time.sleep(0.5)  # Add visible delay after typing
        
    def get_text(self, locator):
        """Wait for an element and retrieve its text"""
        text = self.find(locator).text
        log.info(f"Retrieved text '{text}' from element: {locator}")
        return text
        
    def is_element_present(self, locator):
        """Check if an element exists on the page"""
        try:
            self.find(locator)
            log.info(f"Element found present on page: {locator}")
            return True
        except Exception:
            log.warning(f"Element NOT found on page: {locator}")
            return False
