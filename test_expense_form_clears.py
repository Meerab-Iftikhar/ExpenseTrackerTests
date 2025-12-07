# selenium-tests/tests/test_expense_form_clears.py
from test_setup import get_driver, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_expense_form_clears():
    driver = get_driver()
    try:
        # Step 1: Login first
        login(driver)
        wait = WebDriverWait(driver, 10)

        # Step 2: Go to Add Expense form
        add_expense_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-expense-btn")))
        add_expense_btn.click()

        # Step 3: Fill form fields
        description = driver.find_element(By.ID, "description")
        amount = driver.find_element(By.ID, "amount")
        description.send_keys("Test Expense")
        amount.send_keys("123")

        # Step 4: Submit the form
        submit_btn = driver.find_element(By.ID, "submit-expense-btn")
        submit_btn.click()

        # Step 5: Wait until the form is cleared
        wait.until(lambda d: description.get_attribute("value") == "" and amount.get_attribute("value") == "")

        # Step 6: Assert fields are empty
        assert description.get_attribute("value") == ""
        assert amount.get_attribute("value") == ""

    finally:
        driver.quit()
