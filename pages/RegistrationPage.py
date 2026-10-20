from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import allure

from pages.BasePage import BasePageHelper

class RegistrationPageLocators:
    INPUT_NAME = (By.ID, 'display-name')
    INPUT_LOGIN = (By.ID, 'username')
    INPUT_EMAIL = (By.ID, 'email')
    INPUT_PHONE = (By.ID, 'phone')
    INPUT_PASSWORD = (By.ID, 'register-password')
    INPUT_CONFIRM_PASSWORD = (By.ID, 'confirm-password')
    CREATE_ACCOUNT_BUTTON = (By.ID, 'register-submit-btn')
    REGISTER_PHONE_BUTTON = (By.ID, 'register-phone-toggle')
    LOGIN_LINK = (By.ID, 'login-link-anchor')

class RegistrationPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.INPUT_NAME)
        self.find_element(RegistrationPageLocators.INPUT_LOGIN)
        self.find_element(RegistrationPageLocators.INPUT_EMAIL)
        self.find_element(RegistrationPageLocators.INPUT_PHONE)
        self.find_element(RegistrationPageLocators.INPUT_PASSWORD)
        self.find_element(RegistrationPageLocators.INPUT_CONFIRM_PASSWORD)
        self.find_element(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        self.find_element(RegistrationPageLocators.LOGIN_LINK)
        self.find_element(RegistrationPageLocators.REGISTER_PHONE_BUTTON)

    def scrollToitem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()