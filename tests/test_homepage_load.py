# selenium-tests/tests/test_homepage_load.py
from test_setup import get_driver

def test_homepage_title():
    driver = get_driver()
    try:
        driver.get("http://localhost:5173/")
        assert "Expense" in driver.title
    finally:
        driver.quit()
