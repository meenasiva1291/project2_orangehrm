import time
from asyncio import wait_for

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import Basepage
from locators.locators import locators as Locators

class myinfo(Basepage):

    def myinfo_menu_displayandfunction(self):
        try:
            print("\n===== MENU NAVIGATION DETAILS =====\n")

            # Wait for the menu items to load (implicitly wait will help, but let's be explicit here)
            self.wait_for_element_to_be_clickable(Locators.myinfo_locator).click()

            # Get the my_info menu items
            self.wait_for_visibility(Locators.myinfo_menu)
            # menu_items: list[WebElement] = self.wait_for_element_to_be_clickable(Locators.myinfo_menu)
            menu_items: list[WebElement] = self.driver.find_elements(By.XPATH,"//div[contains(@class,'orangehrm-tabs')]/div")

            for index in range(len(menu_items)):

                # Re-fetch the menu items list to avoid stale element reference
                menu_items = self.driver.find_elements(By.XPATH,"//div[contains(@class,'orangehrm-tabs')]/div")
                menu_item = menu_items[index]
                # Get menu name
                menu_name = menu_item.text.strip()
                # Scroll into view and click the menu item
                self.driver.execute_script("arguments[0].scrollIntoView(true);", menu_item)
                self.wait_for_clickable(menu_item)
                # time.sleep(3)

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
                # self.driver.back()

                # Wait until the page is back on the dashboard (you could use a specific element or title check here)
                self.wait.until(EC.title_is("OrangeHRM"))

        except Exception as e:
            print(f"Error during menu navigation: {e}")


