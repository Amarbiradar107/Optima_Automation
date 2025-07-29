import time

from selenium.webdriver.common.by import By

class CustomerManagementPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    MENU = (By.XPATH, "//i[@class='bx bx-grid-alt bx-sm pt-1']")
    CUSTOMER_MANAGEMENT = (By.XPATH, "//ul[@class='list-unstyled list-group notification navs module-wise']//a[@routerlinkactive='active'][normalize-space()='Customer Management']")
    ADD_NEW_BUTTON = (By.XPATH, "//button[contains(text(),'Add New')]")
    CUSTOMER_NAME = (By.XPATH, "//input[@formcontrolname='customerName']")
    PARENT_COMPANY = (By.XPATH, "//input[@formcontrolname='parentCompany']")
    ADDRESS = (By.XPATH, "//input[@formcontrolname='address']")
    DEPARTMENT = (By.XPATH, "//input[@formcontrolname='department']")
    SUBSIDIARY = (By.XPATH, "//input[@formcontrolname='subsidiary']")
    LOCATION = (By.XPATH, "//input[@formcontrolname='location']")
    PHONE_NUMBER = (By.XPATH, "//input[@formcontrolname='phoneNumber']")
    EMAIL_ADDRESS = (By.XPATH, "//input[@formcontrolname='emailAddress']")
    COMMENTS = (By.XPATH, "//input[@formcontrolname='comments']")
    CONTACT_NAME = (By.XPATH, "//input[@formcontrolname='contactName']")
    CONTACT_PHONE = (By.XPATH, "//input[@formcontrolname='contactPhone']")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()='Cancel']")

    def navigate_to_customer_management(self):
        self.driver.find_element(By.XPATH, "//a[@href='/customer']").click()
        time.sleep(5)
        print("Navigated to Customer Management page")
