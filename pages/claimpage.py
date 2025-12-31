from locators.locators import locators as Locators
from pages.basepage import Basepage

class ClaimPage(Basepage):
    def create_claim(self):
        try:
            self.wait_for_clickable(Locators.claim_option).click()
            self.wait_for_clickable(Locators.submit_claim).click()
            self.wait_for_visibility(Locators.event_dropdown)
            self.select_dropdown_option(Locators.event_dropdown, Locators.list_locator)
            self.select_dropdown_option(Locators.currency_dropdown, Locators.list_locator)
            # click create button
            self.wait_for_clickable(Locators.create_button).click()
            #verify success toaster
            success_message = self.wait_for_visibility(Locators.success_toaster)
            assert "Success" in success_message.text
            print("success message displayed")
            get_reference = self.wait_for_visibility(Locators.reference_id)
            # final submit button
            self.wait_for_clickable(Locators.submit_button).click()
            # go to my claims tab
            self.wait_for_clickable(Locators.my_claims).click()
            # verify for the created claim display in  record
            assert self.is_text_present(Locators.claim_verify_record, get_reference)
            #take screenshot
            self.driver.save_screenshot("claim_verified.png")
            print("Claim displayed successfully in the table")

        except Exception as e:
            print(e)



