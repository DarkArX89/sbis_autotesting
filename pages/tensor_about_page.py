from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    def should_be_about_page(self):
        assert 'https://tensor.ru/about' == self.browser.current_url

    def should_be_block_working(self):
        assert self.is_element_present(
            *TensorAboutPageLocators.BLOCK_WORKING
        ), 'Block "Working" is not presented'

    def should_be_title_of_block_working(self):
        title = self.browser.find_element(
            *TensorAboutPageLocators.TITLE_WORKING).text
        assert 'Работаем' == title, \
            'Name of block "Working" is incorrect'

    @staticmethod
    def get_height_and_weight(photos):
        weight_set = set()
        height_set = set()
        for photo in photos:
            weight_set.add(photo.get_attribute('weight'))
            height_set.add(photo.get_attribute('height'))
        return len(weight_set), len(height_set)

    def should_be_same_height_and_width_of_photos(self):
        photos = self.browser.find_elements(
            *TensorAboutPageLocators.PHOTOS_WORKING)
        different_height, different_weight = self.get_height_and_weight(
            photos)
        assert different_height == different_weight == 1, \
            'Height and width of photos in block "Working" are not the same'
