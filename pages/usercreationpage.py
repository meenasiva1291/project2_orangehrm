import uuid
from ast import Bytes

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import locators as Locators

from pages.basepage import Basepage

# Generate unique username
new_username = f"TestUser_{uuid.uuid4().hex[:8]}"
# Generate unique password
new_password = f"{new_username}@123"

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

            # Select User Status
            self.select_dropdown_option(Locators.user_status, Locators.list_locator)

            # Enter Username
            admin_username = self.wait_for_element(Locators.admin_username)
            admin_username.clear()
            admin_username.send_keys(new_username)

            print(f"Generated Username: {new_username}")

            # Enter Password
            admin_password = self.wait_for_element(Locators.admin_password)
            admin_password.clear()
            admin_password.send_keys(new_password)

            print(f"Generated password: {new_password}")

            # Re-enter Password
            admin_reenter_password = self.wait_for_element(Locators.admin_repassword)
            admin_reenter_password.clear()
            admin_reenter_password.send_keys(new_password)

            print(f"Generated reenter_password: {new_password}")

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

    def login_asnewuser(self):
        try:
            self.enter_text(new_username)
            self.enter_text(new_password)


        except Exception as e:
            print(e)

