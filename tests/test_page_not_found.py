# selenium-tests/tests/test_page_not_found.py
from test_setup import get_driver

def test_404_page():
    driver = get_driver()
    try:
        driver.get("http://localhost:5173/unknown-route")
        assert "404" in driver.page_source or "Not Found" in driver.page_source or "Page Not Found" in driver.page_source
    finally:
        driver.quit()
