import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ContactsPageLocators


class ContactsPage(BasePage):
    def go_to_tensor_page(self):
        link = self.browser.find_element(*ContactsPageLocators.BANNER_TENSOR)
        link.click()

    def should_be_banner_tensor(self):
        assert self.is_element_present(
            *ContactsPageLocators.BANNER_TENSOR
        ), 'Banner "Tensor" is not presented'

    def should_be_correct_local_region_in_url(self, current_region):
        region = self.browser.current_url
        assert current_region in region, 'Local region is incorrect'

    def should_be_correct_local_region_in_contacts(self, current_region):
        region = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(
                ContactsPageLocators.CURRENT_REGION, current_region))
        assert region is True, 'Local region is incorrect'

    @staticmethod
    def compare_title_and_name(contacts):
        for contact in contacts:
            title = contact.get_attribute('title')
            name = contact.text
            assert title == name, 'Title and name do not match'

    def should_be_list_of_contacts(self, amount):
        contacts_list = self.browser.find_elements(
            *ContactsPageLocators.CONTACTS)
        assert len(contacts_list) > 0, 'Contacts List is not presented'
        assert len(contacts_list) == amount, 'Contacts List is incorrect'
        self.compare_title_and_name(contacts_list)

    def change_local_region(self):
        '''
        До изменения формы выбора региона для клика работал следующий код:
        self.browser.execute_script(
            'arguments[0].scrollIntoView(true);', new_region)
        new_region.click()
        После изменения он был заменён на:
        self.browser.execute_script(
            'arguments[0].click();', new_region
        )
        '''
        chooser = self.browser.find_element(
            *ContactsPageLocators.CURRENT_REGION)
        current_region = chooser.text
        chooser.click()
        new_region = self.browser.find_element(
            *ContactsPageLocators.KAMCHATKA_REGION)
        self.browser.execute_script(
            'arguments[0].click();', new_region
        )
        while chooser.text == current_region:
            chooser = self.browser.find_element(
                *ContactsPageLocators.CURRENT_REGION)
            time.sleep(1)
