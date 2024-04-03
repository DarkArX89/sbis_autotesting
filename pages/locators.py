from selenium.webdriver.common.by import By


class HomePageLocators():
    CONTACTS = (By.CLASS_NAME, 'sbisru-Header__menu-item-1')


class ContactsPageLocators():
    BANNER_TENSOR = (
        By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor')
    CURRENT_REGION = (By.CLASS_NAME, 'sbis_ru-Region-Chooser__text')
    CONTACTS = (By.CLASS_NAME, 'sbisru-Contacts-List__name')
    KAMCHATKA_REGION = (
        By.CSS_SELECTOR, '.sbis_ru-link[title="Камчатский край"]')


class TensorPageLocators():
    BLOK_STRENGTH_IN_PEOPLE = (
        By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    ABOUT = (
        By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link')
    TITLE_STRENGTH_IN_PEOPLE = (
        By.CSS_SELECTOR,
        '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title'
    )


class TensorAboutPageLocators():
    BLOCK_WORKING = (By.CLASS_NAME, 'tensor_ru-About__block3')
    TITLE_WORKING = (
        By.CSS_SELECTOR,
        '.tensor_ru-About__block3 .tensor_ru-About__block-title'
    )
    PHOTOS_WORKING = (By.CLASS_NAME, 'tensor_ru-About__block3-image')
