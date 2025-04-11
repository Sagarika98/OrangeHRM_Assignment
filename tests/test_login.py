import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utilities.config import BASE_URL, USERNAME, PASSWORD

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
    assert "dashboard" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_pass")
    assert "Invalid credentials" in login_page.get_error_message()