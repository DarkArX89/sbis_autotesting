import pytest

from pages.home_page import HomePage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage
from pages.tensor_about_page import TensorAboutPage
from pages.download_page import DownloadPage


link = "https://sbis.ru/"

my_region = ['66-sverdlovskaya-oblast', 'Свердловская обл.', 23]
kamchatka_region = ['41-kamchatskij-kraj', 'Камчатский край', 1]


def test_guest_scenario_1(browser):
    home_page = HomePage(browser, link)
    home_page.open()
    home_page.should_be_contacts_link()
    home_page.go_to_contacts_page()
    contacts_page = ContactsPage(browser, browser.current_url)
    contacts_page.open()
    contacts_page.should_be_banner_tensor()
    contacts_page.go_to_tensor_page()
    tensor_page = TensorPage(browser, browser.current_url)
    tensor_page.open()
    tensor_page.switch_next()
    tensor_page.should_be_block_strength_in_people()
    tensor_page.should_be_title_of_block_strength_in_people()
    tensor_page.should_be_link_in_block_strength_in_people()
    tensor_page.go_to_about_page()
    about_page = TensorAboutPage(browser, browser.current_url)
    about_page.open()
    about_page.should_be_about_page()
    about_page.should_be_block_working()
    about_page.should_be_title_of_block_working()
    about_page.should_be_same_height_and_width_of_photos()


def test_guest_scenario_2(browser):
    home_page = HomePage(browser, link)
    home_page.open()
    home_page.should_be_contacts_link()
    home_page.go_to_contacts_page()
    contacts_page = ContactsPage(browser, browser.current_url)
    contacts_page.open()
    contacts_page.should_be_correct_local_region_in_contacts(my_region[1])
    contacts_page.should_be_correct_local_region_in_url(my_region[0])
    contacts_page.should_be_list_of_contacts(my_region[2])
    contacts_page.change_local_region()
    contacts_page.should_be_correct_local_region_in_contacts(
        kamchatka_region[1])
    contacts_page.should_be_correct_local_region_in_url(kamchatka_region[0])
    contacts_page.should_be_list_of_contacts(kamchatka_region[2])


@pytest.mark.skip
def test_guest_scenario_3(browser):
    home_page = HomePage(browser, link)
    home_page.open()
    home_page.should_be_download_local_version_link()
    home_page.go_to_download_local_version_page()
    download_page = DownloadPage(browser, browser.current_url)
    download_page.open()
    download_page.should_be_plugin_chapter()
    download_page.go_to_plugin_chapter()
    download_page.should_be_download_web_setup()
    download_page.download_web_setup()
