import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import url_to_be

from pages.basepage import Basepage
from locators.locators import locators as Locators
from tests.conftest import driver


class assign_leave(Basepage):
    def assign_leave_employee(self):
        try:
            self.wait_for_clickable(Locators.leave_option).click()
            self.wait_for_clickable(Locators.assign_leaves).click()
            assert url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave"),"URL Mismatch"
            self.employee_name(Locators.employee_name)
            self.select_dropdown_option(Locators.leave_type,Locators.list_locator)
            self.enter_text(Locators.from_date,"2025-12-31")
            # self.enter_text(Locators.to_date,"2025-03-12")
            self.enter_text(Locators.comments,"Assigning leave to employee")
            self.wait_for_clickable(Locators.assign_button).click()
            self.wait_for_clickable(Locators.confirm_button).click()
            self.get_text(Locators.success_message)


        except Exception as e:
            print(e)

