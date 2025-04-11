from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        sleep(2)

    def get_error_message(self):
        return self.get_element_text(self.ERROR_MESSAGE)