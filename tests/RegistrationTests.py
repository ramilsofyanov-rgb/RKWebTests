import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.RegistrationPage import RegistrationPageHelper, RegistrationPageLocators
from pages.RegistrationPhonePage import RegistrationPhonePageHelper

BASE_URL = "https://sn.rv-school.ru/register.html"

@allure.suite("Регистрация пользователя")
@allure.title("Переход к странице регистрации по телефону через скролл")
def test_registration_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    RegistrationPage = RegistrationPageHelper(browser)
    RegistrationPage.scrollToitem(RegistrationPageLocators.REGISTER_PHONE_BUTTON)
    RegistrationPhonePageHelper(browser)