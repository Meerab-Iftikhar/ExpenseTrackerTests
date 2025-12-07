# selenium-tests/tests/test_add_expense_form.py
from test_setup import get_driver, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_expense_button():
    driver = get_driver()
    try:
        login(driver)
        wait = WebDriverWait(driver, 8)
        add_btn = wait.until(EC.presence_of_element_located((By.ID, "save-btn")))
        assert add_btn.is_displayed()
    finally:
        driver.quit()
