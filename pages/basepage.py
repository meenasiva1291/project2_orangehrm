import time
import uuid

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:


    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def employee_name(self,locator):
        employee_name = self.wait_for_element(locator)
        employee_name.send_keys("a")
        time.sleep(6)  # Wait for suggestions to appear
        employee_name.send_keys(Keys.ARROW_DOWN)
        # time.sleep(5)
        employee_name.send_keys(Keys.ENTER)

    def enter_text(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        self.wait_for_clickable(locator).click()



    def get_text(self, locator):
        return self.wait_for_visibility(locator).text

    def is_displayed(self, locator):
        return self.wait_for_visibility(locator).is_displayed()

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        """Helper function to wait for an element to be clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element(self, locator, timeout=10):
        """Helper function to wait for an element to be present and visible."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def select_dropdown_option(self, dropdown_locator, list_locator, option_index=1):
        """Helper function to select an option from a dropdown."""
        try:
            dropdown = self.wait_for_element_to_be_clickable(dropdown_locator)
            dropdown.click()
            listbox = self.wait_for_element(list_locator)
            options = listbox.find_elements(By.XPATH, ".//div")
            options_list = list(options)
            if len(options_list) > 1:
                options_list[1].click()  # Click the second option (index 1)
                print("Selected option at index 1.")
            else:
                print("Option at index 1 not found.")

        except Exception as e:
            print(f"Error selecting dropdown option: {e}")

