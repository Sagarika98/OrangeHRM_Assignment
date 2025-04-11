from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage(BasePage):
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class,'oxd-toast')]//p[contains(@class,'oxd-text')]")

    def __init__(self, driver):
        super().__init__(driver)

    def add_employee(self, first_name, last_name):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.click(self.SAVE_BUTTON)
        sleep(3)