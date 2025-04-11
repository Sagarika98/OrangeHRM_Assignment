from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMPage(BasePage):
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//button[text()=' Add ']")
    EMPLOYEE_LIST_BUTTON = (By.XPATH, "//a[text()='Employee List']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

    def click_employee_list(self):
        self.click(self.EMPLOYEE_LIST_BUTTON)