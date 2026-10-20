import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.AllServicesPage import AllServicesPageHelper

BASE_URL = 'https://sn.rv-school.ru/'


@allure.suite('Проверка тулбара')
@allure.title('Переход к сервисам СоцСети')
def test_open_services(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = LoginPageHelper(browser)
    current_window_id = LoginPage.get_windows_id(0)
    LoginPage.click_header_services()
    LoginPage.click_more_button()
    new_window_id = LoginPage.get_windows_id(1)
    LoginPage.switch_window(new_window_id)
    AllServicesPage = AllServicesPageHelper(browser)
    AllServicesPage.switch_window(current_window_id)
    LoginPageHelper(browser)


