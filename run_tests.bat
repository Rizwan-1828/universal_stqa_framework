@echo off
setlocal EnableDelayedExpansion
color 0a

echo ========================================================
echo        Universal STQA Automation Framework Runner
echo ========================================================

:: Check for URL argument
set BASE_URL=
if "%~1" neq "" (
    set BASE_URL=--base-url="%~1"
    echo Overriding config.json with target URL: %~1
) else (
    echo Note: No URL passed. Falling back to base_url inside config.json
)

echo.
echo [1] Cleaning old reports and screenshots...
if exist "reports\allure-results" (
    rmdir /S /Q "reports\allure-results"
)
if exist "screenshots" (
    del /S /Q "screenshots\*.png" >nul 2>&1
)
mkdir "reports\allure-results" 2>nul
echo Done.

echo.
echo [2] Running Test Suite...
echo ========================================================
python -m pytest tests/ %BASE_URL% --alluredir=reports/allure-results -v
echo ========================================================

echo.
echo [3] Packing environment details for Allure Report...
echo Browser=Chrome> "reports\allure-results\environment.properties"
echo Framework=Pytest-Selenium-POM>> "reports\allure-results\environment.properties"

echo.
echo [4] Launching Allure Report Dashboard...
allure serve reports/allure-results

endlocal
pause
