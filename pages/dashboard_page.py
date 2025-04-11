from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    LOGOUT_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_pim(self):
        self.click(self.PIM_MENU)

    def logout(self):
        self.click(self.LOGOUT_DROPDOWN)
        self.click(self.LOGOUT_BUTTON)