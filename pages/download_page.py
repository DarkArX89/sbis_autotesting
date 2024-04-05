import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import DownloadPageLocators


class DownloadPage(BasePage):
    def should_be_plugin_chapter(self):
        plugin = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(DownloadPageLocators.PLUGIN)
        )
        assert plugin is not False, 'SBIS Plugin chapter is not presented'

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
        time.sleep(5)
