import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        driver.find_element(By.XPATH,"//input[@type='text']").send_keys("hp-amar")
        driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Amar@1234")
        driver.find_element(By.XPATH,"//input[@id='flexCheckDefault']").click()
        driver.find_element(By.XPATH,"//div[@class='mb-3 d-grid']").click()
        time.sleep(2)
        print("test passed")


    # def test_logout(self):
    #     driver = self.driver
    #     driver.find_element("xpath", "//a[@href='/logout']").click()
    #     assert "Login" in driver.title
