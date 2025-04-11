from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from time import sleep

class EmployeeListPage(BasePage):
    # SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    # EMPLOYEE_NAME_IN_LIST = (By.XPATH, "//div[@class='oxd-table-card']//div[contains(@class, 'oxd-table-cell')][3]")
    

    # def __init__(self, driver):
    #     super().__init__(driver)

    # def search_employee(self, name):
    #     self.send_keys(self.SEARCH_INPUT, name)

    # def verify_employee_via_api(self, first_name, last_name):
    #     auth = ('Admin', 'admin123')  # Use your credentials
    #     response = requests.get(
    #         'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees',
    #         auth=auth,
    #         params={'name': f"{first_name} {last_name}"}
    #     )
    #     return any(
    #         emp['firstName'] == first_name and emp['lastName'] == last_name
    #         for emp in response.json()['data']
    #     )
    
    def __init__(self, driver):
        self.driver = driver
        
        # Locators
        self.SEARCH_NAME_INPUT = (By.XPATH, "//label[contains(text(),'Employee Name')]/following::input[1]")
        self.SEARCH_BUTTON = (By.XPATH, "//button[@type='submit'][contains(.,'Search')]")
        self.EMPLOYEE_ROW = (By.XPATH, "//div[@class='oxd-table-card']")
        self.FIRST_NAME_CELL = (By.XPATH, ".//div[contains(@class,'oxd-table-cell')][3]")
        self.LAST_NAME_CELL = (By.XPATH, ".//div[contains(@class,'oxd-table-cell')][4]")
        self.RESET_BUTTON = (By.XPATH, "//button[@type='reset'][contains(.,'Reset')]")

    def search_employee(self, first_name, last_name):
        """Enter name in search field and click search"""
        try:
            # Enter first name
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SEARCH_NAME_INPUT)
            ).send_keys(first_name)
            
            # Enter last name (some implementations need tab between names)
            self.driver.find_element(*self.SEARCH_NAME_INPUT).send_keys(" " + last_name)
            
            # Click search button
            self.driver.find_element(*self.SEARCH_BUTTON).click()
            sleep(2)  # Wait for results to load
            
        except Exception as e:
            print(f"Search failed: {e}")

    def reset_search(self):
        """Reset the search fields"""
        try:
            # Click reset button
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.RESET_BUTTON)
            ).click()
            
            # Clear input fields
            self.driver.find_element(*self.SEARCH_NAME_INPUT).clear()
            
        except Exception as e:
            print(f"Reset failed: {e}")        

    def verify_employee_in_list(self, first_name, last_name):
        """Verify employee appears in search results"""
        try:
            # Wait for results
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.EMPLOYEE_ROW)
            )
            
            # Check all visible rows
            rows = self.driver.find_elements(*self.EMPLOYEE_ROW)
            for row in rows:
                current_first = row.find_element(*self.FIRST_NAME_CELL).text.strip()
                current_last = row.find_element(*self.LAST_NAME_CELL).text.strip()
                
                if current_first == first_name and current_last == last_name:
                    print(f"Name Verified: {first_name} {last_name}")
                    return True
                    
            print(f"Employee not found: {first_name} {last_name}")
            return False
            
        except Exception as e:
            print(f"Verification error: {e}")
            return False