# Universal STQA Pytest Framework 🧪

This is a robust, data-driven, and highly configurable UI test automation framework built on **Python**, **Selenium**, **Pytest**, and **Allure Reports**. It is designed using the **Page Object Model (POM)** architecture to be universally adaptable for testing *any* web application.

## 🚀 Features
- **Centralized Configuration:** Define target URLs and browser behaviors in `config.json`.
- **1-Click Execution:** Run the entire suite and automatically generate a gorgeous HTML report using `run_tests.bat`.
- **Deep Logging:** Every UI interaction (click, type, wait) is logged to timestamped files and automatically attached to the final test report.
- **Auto-Screenshots:** Automatically captures and attaches screenshots of the browser state anytime a test fails.

---

## 💻 Setup Instructions

### 1. Requirements
Ensure you have the following installed on your machine:
- **Python 3.10+**
- **Google Chrome** (Selenium automatically downloads the matching driver)
- **Node.js** (Required to view the Allure HTML reports)

### 2. Installation
Open your terminal in the framework root folder and install the dependencies:
```cmd
pip install -r requirements.txt
npm install -g allure-commandline
```

---

## 🎯 How to Test Your Own Project

You can use this framework to test any live website (like `https://google.com`) or a project running locally on your machine (like `http://localhost:3000`).

### Method 1: Using the Configuration File (Recommended)
1. Open `config.json` in the root directory.
2. Change the `"base_url"` to your application's URL.
   - *Example for Live:* `"base_url": "https://my-live-app.com/"*
   - *Example for Local:* `"base_url": "http://localhost:5173/"*
3. Double-click **`run_tests.bat`** (or execute it in the terminal). The tests will run against your provided URL and automatically open the Allure report when finished!

### Method 2: Command Line Override
If you are integrating this into a CI/CD pipeline, you don't need to change `config.json`. You can pass the URL directly into the runner script:
```cmd
.\run_tests.bat "https://staging.my-app.com/"
```

---

## 🧩 Building New Tests (Page Object Model)

To write tests for your own application, follow these two steps:

### 1. Create a Page Object
Inside the `pages/` folder, create a new python file for representing a page (e.g., `checkout_page.py`). Inherit from `BasePage` to get access to the universal logged actions.

```python
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class MyCustomPage(BasePage):
    # 1. Define Locators
    SUBMIT_BUTTON = (By.ID, "submit-btn")
    
    # 2. Define Actions
    @allure.step("Clicking the submit button on custom page")
    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)
```

### 2. Write the Test
Inside the `tests/` folder, create a new file starting with `test_` (e.g., `test_my_feature.py`). Use the `base_url` and `driver` fixtures.

```python
import allure
from pages.my_custom_page import MyCustomPage

@allure.title("TC01 - Verify Custom Page Submission")
def test_submission(driver, base_url):
    page = MyCustomPage(driver)
    
    # The base_url comes automatically from config.json or the CLI tag!
    page.open_url(base_url) 
    page.click_submit()
    assert True
```

---

## 📂 Framework Structure
```text
📁 STQA-Framework/
 ┣ 📄 config.json         <-- Edit your URLs and timeouts here
 ┣ 📄 run_tests.bat       <-- 1-Click execution script
 ┣ 📁 pages/              <-- Store Page Objects (Locators + Actions)
 ┃ ┗ 📄 base_page.py      <-- Universal selenium controls and logging
 ┣ 📁 tests/              <-- Store Pytest files
 ┣ 📁 utils/
 ┃ ┣ 📄 driver_setup.py   <-- Chrome initialization handling (Headless configuration)
 ┃ ┗ 📄 logger.py         <-- Internal logging engine
 ┣ 📄 conftest.py         <-- Pytest hooks (Screenshot triggers, Allure attachment)
 ┗ 📄 requirements.txt
```
