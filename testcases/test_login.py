import time
import pytest
from Optima_Automation.utilities.utils import utlis
from Optima_Automation.pages.login_page import LoginPage

test_data = utlis.read_data_from_excel("C:\\Users\\amar.biradar\\Desktop\\python\\Automation\\Optima_Automation\\usercradentials.xlsx", "Cradentials")


@pytest.mark.usefixtures("setup")
class TestLogin():
    @pytest.mark.parametrize("username,password", test_data)
    def test_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        time.sleep(2)
        print("test passed")

    # def test_logout(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.logout()
    #     assert "Login" in self.driver.title
