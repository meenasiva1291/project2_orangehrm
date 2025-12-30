import time
from asyncio import wait_for
from operator import truediv

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v136.tracing import record_clock_sync_marker
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import Basepage
from locators.locators import locators as Locators
from pages.usercreationpage import new_username


class dashboard(Basepage):
    def logout(self):
        try:
            # Wait for logout menu and click
            logout_menu = self.wait_for_element_to_be_clickable(Locators.logoutmenu_locator)
            # logout_menu = self.wait.until(EC.visibility_of_element_located(Locators.logoutmenu_locator))
            logout_menu.click()


            # Wait for logout option and click
            logout_option = self.wait.until(EC.visibility_of_element_located(Locators.logout_locator))
            logout_option.click()

            print("User logged out successfully")
        except Exception as e:
            print(f"Error during logout: {e}")

    def menuitems_displayandfunction(self):
        try:
            print("\n===== MENU NAVIGATION DETAILS =====\n")

            # Wait for the menu items to load (implicitly wait will help, but let's be explicit here)
            self.wait_for_visibility(Locators.menu_locator)

            # Get the first 8 menu items
            menu_items: list[WebElement] = self.driver.find_elements(
                By.XPATH, "//ul/li[contains(@class,'oxd-main-menu-item-wrapper')]"
            )[:8]

            for index in range(len(menu_items)):
                # Re-fetch the menu items list to avoid stale element reference
                menu_items = self.driver.find_elements(
                    By.XPATH, "//ul/li[contains(@class,'oxd-main-menu-item-wrapper')]"
                )

                menu_item = menu_items[index]

                # Get menu name
                menu_name = menu_item.text.strip()

                # Scroll into view and click the menu item
                self.driver.execute_script("arguments[0].scrollIntoView(true);", menu_item)
                menu_item.click()

                # Wait for page title or another specific condition (e.g., wait for a page element to load)
                self.wait.until(EC.title_is("OrangeHRM"))

                # Get page details
                page_title = self.driver.title
                page_url = self.driver.current_url

                # Print menu option, page title, and URL
                print(f"Menu Option : {menu_name}")
                print(f"Page Title : {page_title}")
                print(f"Page URL   : {page_url}")
                print("-" * 50)

                # Navigate back to the dashboard
                self.driver.back()

                # Wait until the page is back on the dashboard (you could use a specific element or title check here)
                self.wait.until(EC.title_is("OrangeHRM"))

        except Exception as e:
            print(f"Error during menu navigation: {e}")

    def is_username_present_in_table(self):
        # Enter username
        search_input = self.wait_for_visibility(
            Locators.search_username_input
        )
        search_input.clear()
        search_input.send_keys(new_username)

        # Click Search
        self.wait_for_element_to_be_clickable(
            Locators.user_search_button
        ).click()

        #1 record found should display
        record_table = self.wait_for_visibility(Locators.record_found)
        if record_table.is_displayed():
            print("New user displayed in table successfully")
        else:
            print("New user not displayed")

