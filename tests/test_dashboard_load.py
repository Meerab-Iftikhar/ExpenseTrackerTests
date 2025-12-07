# selenium-tests/tests/test_dashboard_load.py
from test_setup import get_driver, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dashboard_cards():
    driver = get_driver()
    try:
        login(driver)
        wait = WebDriverWait(driver, 8)
        # Wait for budget-box or expense-list to appear
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "budget-box")))
        assert "Budget" in driver.page_source or "Recent Expenses" in driver.page_source
    finally:
        driver.quit()
