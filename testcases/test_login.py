import time
import pytest
<<<<<<< HEAD
from ddt import ddt, data
from selenium.webdriver.common.by import By
from utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestLogin:
    @data((Utils.read_dat_from_excel()))
    def test_login(self):
        driver = self.driver
        driver.find_element(By.XPATH,"//input[@type='text']").send_keys("hp-amar")
        driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Amar@1234")
        driver.find_element(By.XPATH,"//input[@id='flexCheckDefault']").click()
        driver.find_element(By.XPATH,"//div[@class='mb-3 d-grid']").click()
=======
from Optima_Automation.utilities.utils import utlis
from Optima_Automation.pages.login_page import LoginPage

test_data = utlis.read_data_from_excel("C:\\Users\\amar.biradar\\Desktop\\python\\Automation\\Optima_Automation\\usercradentials.xlsx", "Cradentials")


@pytest.mark.usefixtures("setup")
class TestLogin():
    @pytest.mark.parametrize("username,password", test_data)
    def test_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
>>>>>>> e3d75deff336ea2b6340be92dc8081d27a2723cf
        time.sleep(2)
        print("test passed")

    # def test_logout(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.logout()
    #     assert "Login" in self.driver.title
