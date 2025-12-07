# selenium-tests/tests/test_login_valid.py
from test_setup import get_driver, login
from selenium.webdriver.common.by import By

def test_valid_login():
    driver = get_driver()
    try:
        # login helper will use TEST_EMAIL / TEST_PASSWORD env vars
        login(driver)
        assert "/dashboard" in driver.current_url or "Recent Expenses" in driver.page_source
    finally:
        driver.quit()
