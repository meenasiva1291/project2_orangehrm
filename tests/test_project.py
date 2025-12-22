import time

import pytest

from pages.loginpage import LoginPage
from pages.dashboardpage import dashboard
from tests.read_data_from_xl import read_data


# 1.Below test validate username,password fields are displayed and enabled, successful login with valid credentials
def test_testcase1_successful_login_logout(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin","admin123")
    user_logout = dashboard(driver)
    user_logout.logout()

# 2.verify error message text when  login with invalid username and password
def test_testcase2_unsuccessful_login(driver):
    invalid_credentials = LoginPage(driver)
    invalid_credentials.credentials_validation("test123","admin123")

#3 verify forgot password functionality
def test_forgotpassword(driver):
    forgotpassword = LoginPage(driver)
    forgotpassword.forgot_password("Admin")

@pytest.mark.parametrize("username,password", read_data())
def test_login_data_fromXL(username, password, driver):
    multiple_login = LoginPage(driver)
    multiple_login.multipleuserlogin(username ,password)
    user_logout = dashboard(driver)
    user_logout.logout()






