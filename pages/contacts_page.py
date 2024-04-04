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
        print(current_region, region)
        assert current_region in region, 'Local region is incorrect'

    def should_be_correct_local_region_in_contacts(self, current_region):
        region = self.browser.find_element(
            *ContactsPageLocators.CURRENT_REGION).text
        print(current_region, region)
        assert current_region == region, 'Local region is incorrect'

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
        chooser = self.browser.find_element(
            *ContactsPageLocators.CURRENT_REGION)
        chooser.click()
        new_region = self.browser.find_element(
            *ContactsPageLocators.KAMCHATKA_REGION)
        # self.browser.execute_script(
        #     'arguments[0].scrollIntoView(true);', new_region)
        # new_region.click()
        self.browser.execute_script(
            'arguments[0].click();', new_region
        )
