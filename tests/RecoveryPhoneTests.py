import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelperHelper
from pages.RecoveryPhonePage import RecoveryPhonePageHelperHelper

BASE_URL = 'https://sn.rv-school.ru/'

@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка корректности кода страны при выборе случайной страны')
def test_recovery_phone_ramdom_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_forgot_password()
    RecoveryPage = RecoveryPageHelperHelper(browser)
    RecoveryPage.click_recovery_phone()
    RecoveryPhonePage = RecoveryPhonePageHelperHelper(browser)
    Selected_country_code = RecoveryPhonePage.select_random_country()
    Actual_country_code = RecoveryPhonePage.get_phone_field_placeholder()
    assert Selected_country_code == Actual_country_code
