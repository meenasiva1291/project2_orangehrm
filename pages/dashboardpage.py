import time

from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import Basepage
from locators.locators import locators as Locators

class dashboard(Basepage):
    def logout(self):
        try:
            # Wait for logout menu and click
            logout_menu = self.wait.until(EC.visibility_of_element_located(Locators.logoutmenu_locator))
            logout_menu.click()

            # Wait for logout option and click
            logout_option = self.wait.until(EC.visibility_of_element_located(Locators.logout_locator))
            logout_option.click()

            print("User logged out successfully")
        except Exception as e:
            print(f"Error during logout: {e}")
