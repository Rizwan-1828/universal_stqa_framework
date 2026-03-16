from selenium import webdriver
import json
import os
from utils.logger import log

def load_config():
    """Load configuration from config.json"""
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
    try:
        with open(config_path, "r") as config_file:
            return json.load(config_file)
    except Exception as e:
        log.error(f"Failed to load config.json: {e}")
        return {}

def create_chrome_driver():
    """Initializes and returns a configured Chrome WebDriver"""
    config = load_config()
    is_headless = config.get("headless", False)
    
    log.info(f"Initializing Chrome Driver (Headless: {is_headless})")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")
    
    if not is_headless:
        options.add_argument("--start-maximized")
    else:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    
    # Disable Password Manager and Compromised Password Prompts
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-features=PasswordLeakDetection")

    # Selenium 4 auto-downloads matching ChromeDriver
    driver = webdriver.Chrome(options=options)
    
    # Apply implicit wait from config globally
    implicit_wait = config.get("implicit_wait", 10)
    driver.implicitly_wait(implicit_wait)
    
    log.info(f"Chrome Driver initialized successfully with {implicit_wait}s implicit wait")
    return driver