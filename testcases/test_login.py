import time
import pytest
from selenium.webdriver.common.by import By
from Optima_Automation.utilities.utils import utlis

test_data = utlis.read_data_from_excel("C:\\Users\\amar.biradar\\Desktop\\python\\Automation\\Optima_Automation\\usercradentials.xlsx", "Cradentials")


@pytest.mark.usefixtures("setup")
class TestLogin():
    @pytest.mark.parametrize("username,password", test_data)
    def test_login(self, username, password):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@type='text']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='flexCheckDefault']").click()
        driver.find_element(By.XPATH, "//div[@class='mb-3 d-grid']").click()
        time.sleep(2)
        print("test passed")

    # def test_logout(self):
    #     driver = self.driver
    #     driver.find_element("xpath", "//a[@href='/logout']").click()
    #     assert "Login" in driver.title
