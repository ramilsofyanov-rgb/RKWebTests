from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

from pages.RegistrationPage import RegistrationPageLocators

class RegistrationPageLocators:
    TITLE = (By.ID, 'phone-step-1-title')

class RegistrationPhonePageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RegistrationPageLocators.TITLE)