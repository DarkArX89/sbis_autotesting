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

    def should_be_download_local_version_link(self):
        assert self.is_element_present(
            *HomePageLocators.DOWNLOAD_LOCAL_VERSION
        ), 'Download Local Version link is not presented'

    def go_to_download_local_version_page(self):
        link = self.browser.find_element(
            *HomePageLocators.DOWNLOAD_LOCAL_VERSION)
        self.browser.execute_script(
            'arguments[0].scrollIntoView(true);', link)
        link.click()
