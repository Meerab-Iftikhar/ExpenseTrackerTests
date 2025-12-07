# selenium-tests/tests/test_expense_entry.py
from test_setup import get_driver, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_expense_entry():
    driver = get_driver()
    try:
        login(driver)
        wait = WebDriverWait(driver, 10)

        # wait for inputs
        wait.until(EC.presence_of_element_located((By.ID, "amount")))
        driver.find_element(By.ID, "title").send_keys("Test Expense")
        driver.find_element(By.ID, "amount").send_keys("500")
        driver.find_element(By.ID, "date").send_keys("2025-12-01")
        # select category by send_keys (option text)
        driver.find_element(By.ID, "category").send_keys("Food")

        driver.find_element(By.ID, "save-btn").click()

        # wait for the entry to appear in expense-list (simple check)
        time.sleep(1)
        assert "Test Expense" in driver.page_source or "500" in driver.page_source
    finally:
        driver.quit()
