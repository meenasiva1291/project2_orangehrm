from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import url_to_be
from pages.basepage import Basepage
from locators.locators import locators as Locators

class LoginPage(Basepage):
    def credentials_validation(self, username, password):
        try:
            username_field = self.wait_for_visibility(Locators.username_input)
            assert username_field.is_displayed(), "username field not displayed"
            assert username_field.is_enabled(),"username field not enabled"
            username_field.send_keys(username)

            password_field = self.wait_for_visibility(Locators.password_input)
            assert password_field.is_displayed(),"password field not displayed"
            assert password_field.is_enabled(),"password field not enabled"
            password_field.send_keys(password)

            self.wait_for_element_to_be_clickable(Locators.loginbutton_click).click()
            assert url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"), "URL mismatch"

            error_message = self.wait_for_element(Locators.errormessage_text)
            print(error_message.text)

        except Exception as e:
            print(e)

    def forgot_password(self,username):
        try:
            self.wait_for_element_to_be_clickable(Locators.forgotpassword_locator).click()
            self.wait_for_visibility(Locators.username_input).send_keys(username)
            self.wait_for_clickable(Locators.resetlink_locator).click()
            resetpassword_text = self.wait_for_element(Locators.resetpasswordtext_locator)
            print(resetpassword_text.text)

        except Exception as e:
            print(e)

    def multipleuserlogin(self, username, password):
        try:
            valid_username = self.wait_for_visibility(Locators.username_input)
            valid_username.send_keys(username)
            self.wait_for_visibility(Locators.password_input).send_keys(password)
            self.wait_for_element_to_be_clickable(Locators.loginbutton_click).click()
            assert url_to_be(
                "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"), "URL mismatch"
            # print("user logged in successfully and redirected to dashboard page")

        except Exception as e:
            print(e)
