from selenium.webdriver.support import expected_conditions as EC
from locators.locators import locators as Locators


from pages.basepage import Basepage


class claim(Basepage):
    def create_claim(self):
        self.wait_for_clickable(Locators.claim_option).click()
        self.wait_for_clickable(Locators.submit_claim).click()
        self.select_dropdown_option(Locators.event_dropdown,Locators.list_locator)
        self.select_dropdown_option(Locators.currency_dropdown,Locators.list_locator)
        self.wait_for_clickable(Locators.create_button).click()
        self.wait_for_clickable(Locators.submit_button).click()