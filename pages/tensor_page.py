from .base_page import BasePage
from .locators import TensorPageLocators


class TensorPage(BasePage):
    def should_be_block_strength_in_people(self):
        assert self.is_element_present(
            *TensorPageLocators.BLOK_STRENGTH_IN_PEOPLE
        ), 'Block "Stregth in People" is not presented'

    def should_be_title_of_block_strength_in_people(self):
        title = self.browser.find_element(
            *TensorPageLocators.TITLE_STRENGTH_IN_PEOPLE).text
        assert 'Сила в людях' == title, \
            'Name of block "Stregth in People" is incorrect'

    def should_be_link_in_block_strength_in_people(self):
        assert self.is_element_present(
            *TensorPageLocators.ABOUT
        ), 'Link in block "Stregth in People" is not presented'

    def go_to_about_page(self):
        link = self.browser.find_element(*TensorPageLocators.ABOUT)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView(true);', link)
        link.click()
