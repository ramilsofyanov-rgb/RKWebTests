import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class AllServicesPageLocators:
    TITLE_LABEL = (By.ID, 'services-title')


class AllServicesPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем загрузку страницы "Все сервисы"'):
            self.attach_screenshot()
        self.find_element(AllServicesPageLocators.TITLE_LABEL)
