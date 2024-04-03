from .base_page import BasePage
from .locators import HomePageLocators


class HomePage(BasePage):
    def go_to_contacts_page(self):
        link = self.browser.find_element(*HomePageLocators.CONTACTS)
        link.click()

    def should_be_contacts_link(self):
        assert self.is_element_present(
            *HomePageLocators.CONTACTS
        ), 'Contacts link is not presented'
