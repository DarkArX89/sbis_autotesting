import time

from .base_page import BasePage
from .locators import DownloadPageLocators


class DownloadPage(BasePage):
    def should_be_plugin_chapter(self):
        assert self.is_element_present(
            *DownloadPageLocators.PLUGIN
        ), 'SBIS Plugin chapter is not presented'

    def go_to_plugin_chapter(self):
        link = self.browser.find_element(*DownloadPageLocators.PLUGIN)
        link.click()

    def should_be_download_web_setup(self):
        assert self.is_element_present(
            *DownloadPageLocators.DOWNLOAD_WEB_SETUP
        ), 'Link on download Web-setup is not presented'

    def download_web_setup(self):
        download_link = self.browser.find_element(
            *DownloadPageLocators.DOWNLOAD_WEB_SETUP).get_attribute("href")
        self.browser.get(download_link)
        # download_link.click()
        # self.browser.execute_script(
        #     'arguments[0].click();', download_link)
        time.sleep(5)
