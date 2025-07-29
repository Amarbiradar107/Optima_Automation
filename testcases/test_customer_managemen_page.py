from Optima_Automation.pages.customer_management_page import CustomerManagementPage
from Optima_Automation.testcases.test_login import TestLogin

class TestCustomerManagement:
    def __init__(self, driver):
        self.driver = driver
        self.customer_page = CustomerManagementPage(driver)


    def test_customer_management(self):
        TestLogin.test_login()
        self.customer_page.navigate_to_customer_management()
