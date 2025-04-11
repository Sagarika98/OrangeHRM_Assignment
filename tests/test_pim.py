import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage
from utilities.config import BASE_URL, USERNAME, PASSWORD
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(USERNAME, PASSWORD)
    yield driver
    # driver.quit()

def test_add_and_verify_employee(driver):
    dashboard_page = DashboardPage(driver)
    pim_page = PIMPage(driver)
    add_employee_page = AddEmployeePage(driver)
    employee_list_page = EmployeeListPage(driver)

    # Navigate to PIM → Add Employee
    dashboard_page.navigate_to_pim()
    # pim_page.click_add_employee()

    # Add 3 Employees
    employees = [("testing-firstname", "testing-lastname"), ("testing-firstname1", "testing-lastname2"),
                  ("testing-firstname3", "testing-lastname3")]
    for first_name, last_name in employees:
        pim_page.click_add_employee()
        add_employee_page.add_employee(first_name, last_name)
        # assert "Successfully Saved" in add_employee_page.get_success_message()
        sleep(3)
        assert "viewPersonalDetails" in driver.current_url, f"Failed to add {first_name} {last_name}"
        pim_page.click_employee_list()

    # Verify in Employee List
    pim_page.click_employee_list()
    sleep(3)
    for first_name, last_name in employees:
       
        employee_list_page.reset_search()
        sleep(3)
        employee_list_page.search_employee(first_name, last_name)
        assert employee_list_page.verify_employee_in_list(first_name, last_name), \
               f"Employee {first_name} {last_name} not found after search"

    # Logout
    dashboard_page.logout()
    sleep(2)
    assert "auth/login" in driver.current_url