import time

import pytest

from pages.leavepage import assign_leave
from pages.loginpage import LoginPage
from pages.dashboardpage import dashboard
from pages.myinfopage import myinfo
from pages.usercreationpage import UserManagement
from tests.read_data_from_xl import read_data
import faulthandler
faulthandler.disable()


# Below test validate username,password fields are displayed and enabled, successful login with valid credentials
# Coverage - TC02,TC03
def test_testcase1_successful_login_logout(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin","admin123")
    user_logout = dashboard(driver)
    user_logout.logout()

# verify error message text when  login with invalid username and password
# Coverage - TC01
def test_testcase2_unsuccessful_login(driver):
    invalid_credentials = LoginPage(driver)
    invalid_credentials.credentials_validation("test123","admin123")

# verify forgot password functionality
# Coverage - TC07
def test_forgotpassword(driver):
    forgotpassword = LoginPage(driver)
    forgotpassword.forgot_password("Admin")

# verify with multiple login data from XL
# Coverage - TC01
@pytest.mark.parametrize("username,password", read_data())
def test_login_data_fromXL(username, password, driver):
    multiple_login = LoginPage(driver)
    multiple_login.multipleuserlogin(username ,password)
    user_logout = dashboard(driver)
    user_logout.logout()

# verify dashboard menu items
# Coverage - TC04
def test_menu_validation(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin","admin123")
    dashboard_menu = dashboard(driver)
    dashboard_menu.menuitems_displayandfunction()

# verify new usercreation
# Coverage - TC04
def test_new_user_creation(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin","admin123")
    new_user_creation = UserManagement(driver)
    new_user_creation.addnewuser()

def test_myinfo(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin", "admin123")
    validate_myinfo = myinfo(driver)
    validate_myinfo.myinfo_menu_displayandfunction()

def test_assignleave(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin", "admin123")
    assignleave_employee = assign_leave(driver)
    assignleave_employee.assign_leave_employee()


