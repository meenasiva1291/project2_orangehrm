import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import locators as Locators


from pages.basepage import Basepage


class UserManagement(Basepage):
    def addnewuser(self):
        try:
            # Click Admin
            admin_button = self.wait_for_element_to_be_clickable(Locators.admin_locator)
            admin_button.click()

            # Click Add User
            adduser = self.wait_for_element_to_be_clickable(Locators.adduser_locator)
            adduser.click()

            # Select User Role
            self.select_dropdown_option(Locators.userrole_locator, Locators.list_locator)
            self.employee_name(Locators.employee_name)

            # Enter Employee Name
            # employee_name = self.wait_for_element(Locators.employee_name)
            # employee_name.send_keys("a")
            # time.sleep(6)  # Wait for suggestions to appear
            # employee_name.send_keys(Keys.ARROW_DOWN)
            # employee_name.send_keys(Keys.ENTER)
            # print("Employee name selected successfully.")

            # Select User Status
            self.select_dropdown_option(Locators.user_status, Locators.list_locator)

            # Enter Username
            admin_username = self.wait_for_element(Locators.admin_username)
            admin_username.send_keys("Test1234456")

            # Enter Password
            admin_password = self.wait_for_element(Locators.admin_password)
            admin_password.send_keys("abcde12_91")

            # Re-enter Password
            admin_reenter_password = self.wait_for_element(Locators.admin_repassword)
            admin_reenter_password.send_keys("abcde12_91")

            # Submit the form
            submit = self.wait_for_element_to_be_clickable(Locators.submit)
            submit.click()

            print("New user added successfully.")

            expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
            # Current URL
            self.wait.until(EC.url_to_be(expected_url))
            current_url = self.driver.current_url
            # Assert that the current URL matches the expected URL
            assert current_url == expected_url, f"URL mismatch: Expected {expected_url}, but got {current_url}"

        except Exception as e:
            print(f"An error occurred during the user creation process: {e}")
            # Take a screenshot for debugging if needed
            self.driver.save_screenshot('user_addition_failure.png')