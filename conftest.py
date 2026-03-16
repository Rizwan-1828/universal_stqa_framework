import pytest
import os
import json
import allure
from utils.driver_setup import create_chrome_driver
from utils.logger import log, current_log_file

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        return json.load(f)

def pytest_addoption(parser):
    """Add command-line options that can override config.json settings."""
    config = load_config()
    parser.addoption(
        "--base-url",
        action="store",
        default=config.get("base_url", "https://www.saucedemo.com/"),
        help="Base URL for the application under test"
    )

@pytest.fixture(scope="session")
def base_url(request):
    """Fixture to retrieve the base URL from CLI or config."""
    url = request.config.getoption("--base-url")
    log.info(f"Session Base URL set to: {url}")
    return url

@pytest.fixture(scope="function")
def driver(request, base_url):
    """Pytest fixture to initialize and yield the WebDriver instance."""
    log.info(f"\n--- Starting Test: {request.node.name} ---")
    driver_instance = create_chrome_driver()
    
    # Expose driver to request object for screenshot hooking
    request.node.driver = driver_instance
    
    yield driver_instance
    
    log.info(f"--- Finished Test: {request.node.name}. Tearing down driver. ---\n")
    driver_instance.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to attach screenshots to Allure reports and save locally on failure."""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        test_name = item.name.replace("_", " ").title()
        log.error(f"Test Failed: {test_name}. Capturing screenshot...")
        
        # Save absolute local path screenshot
        driver = getattr(item, 'driver', None)
        if driver:
            try:
                os.makedirs("screenshots", exist_ok=True)
                screenshot_path = os.path.join(os.getcwd(), "screenshots", f"{item.name}_failed.png")
                driver.save_screenshot(screenshot_path)
                
                # Attach screenshot to Allure report
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"🚨 Failed Test Detail: {test_name}",
                    attachment_type=allure.attachment_type.PNG
                )
                log.info(f"Screenshot saved to: {screenshot_path}")
            except Exception as e:
                log.error(f"Failed to capture screenshot for {test_name}: {str(e)}")

# pytest_sessionfinish removed to fix Allure KeyError crash on teardown.
