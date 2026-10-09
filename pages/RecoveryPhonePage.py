import allure
import random
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RecoveryPhonePageLocators:
    PHONE_INPUT = (By.ID, 'phone-input')
    COUNTRY_LIST = (By.ID, 'country-select-btn')
    COUNTRY_ITEM = (By.XPATH, '//*[@class="custom-select-option-code"]')
    GET_CODE_BUTTON = (By.ID, 'phone-submit-btn')

class RecoveryPhonePageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
            self.find_element(RecoveryPhonePageLocators.PHONE_INPUT)
            self.find_element(RecoveryPhonePageLocators.COUNTRY_LIST)
            self.find_element(RecoveryPhonePageLocators.GET_CODE_BUTTON)

    def select_random_country(self):
        self.find_element(RecoveryPhonePageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RecoveryPhonePageLocators.COUNTRY_ITEM)
        random_number = random.randint(0, len(country_items) - 1)
        country_code = country_items[random_number].get_attribute('data-value')
        country_items[random_number].click()
        return country_code

    def get_phone_field_placeholder(self):
        return self.find_element(RecoveryPhonePageLocators.PHONE_INPUT).get_attribute('data-value')

