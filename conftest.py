import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def webdriver_chrome_browser(user_language):
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    options.add_experimental_option(
        'prefs', {'download.default_directory': CURRENT_DIR,
                  'safebrowsing.enabled': True})
    browser = webdriver.Chrome(options=options)
    return browser


def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store', default='ru',
        help='Choose language: ru, en, etc.'
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    browser = webdriver_chrome_browser(user_language)
    print('\nStart browser for test..')
    yield browser
    print("\nQuit browser..")
    browser.quit()
