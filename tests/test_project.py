import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC, wait

from pages.claimpage import claim
from pages.leavepage import assign_leave
from pages.loginpage import LoginPage
from pages.dashboardpage import dashboard
from pages.myinfopage import myinfo
from pages.usercreationpage import UserManagement, new_username, new_password
from tests.read_data_from_xl import read_data, write_result
import faulthandler
faulthandler.disable()

#TC-01 validate multiple user credentials data from excel
@pytest.mark.parametrize("username,password,row", read_data())
def test_login_data_fromXL(driver, username, password, row):
    login = LoginPage(driver)
    # Attempt login
    login.multipleuserlogin(username, password)
    print(driver.current_url)
    current_url = driver.current_url

    if current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
        write_result(row, "Login Success")
        # Logout only if login successful
        dashboardpage = dashboard(driver)
        dashboardpage.logout()

    elif current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login":
        write_result(row, "Login Fail[Invalid credentials]")

#TC01 - verify error message text when  login with invalid username and password
def test_testcase2_unsuccessful_login(driver):
    invalid_credentials = LoginPage(driver)
    invalid_credentials.credentials_validation("test123", "admin123")

# TC02,TC03- Below test validate username,password fields are displayed and enabled, successful login with valid credentials
def test_testcase1_successful_login_logout(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin", "admin123")
    user_logout = dashboard(driver)
    user_logout.logout()

#TC-04 validate visibility and clickability of main menu items after login
def test_menu_validation(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin", "admin123")
    dashboard_menu = dashboard(driver)
    dashboard_menu.menuitems_displayandfunction()

#TC-05 create new user and validate login
def test_new_user_creation(driver):
    #Login with admin credentials
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin", "admin123")
    #Add new user
    new_user_creation = UserManagement(driver)
    new_user_creation.addnewuser()
    # logout from the current user
    dashboard_page = dashboard(driver)
    dashboard_page.logout()
    #validating login with newly created username and password
    valid_credentials.credentials_validation(new_username,new_password)
    print(f"New user created and logged in successfully: {new_username} / {new_password}")

#TC-06 presence of newly created user in admin user list
def test_newuserintable(driver):
    # Login with admin credentials
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("Admin", "admin123")
    # Add new user
    new_user_creation = UserManagement(driver)
    new_user_creation.addnewuser()
    dashboard_page = dashboard(driver)
    dashboard.is_username_present_in_table(new_username)

#TC07 verify forgot password functionality
def test_forgotpassword(driver):
    forgotpassword = LoginPage(driver)
    forgotpassword.forgot_password("Admin")

#TC-08 validate menu items under "My info"
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

def test_claim(driver):
    valid_credentials = LoginPage(driver)
    valid_credentials.credentials_validation("mahalakshmi", "Easyway@12")
    claim_creation = claim(driver)
    claim_creation.create_claim()
