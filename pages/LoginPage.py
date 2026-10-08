import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'login-phone-email')
    PASSWORD_FIELD = (By.ID, 'login-password')
    LOGIN_BUTTON = (By.ID, 'login-submit-btn')
    SEARCH_INPUT = (By.ID, 'search-input')
    FORGOT_PASSWORD_LINK = (By.ID, 'forgot-password-link')
    HERO_REGISTER_BUTTON = (By.ID, 'hero-register-btn')
    QR_TAB = (By.ID, 'tabQr')
    LOGO = (By.ID, 'logo')
    SERVICES_DROPDOWN = (By.ID, 'header-services')
    COOKIE_INFO_LINK = (By.ID, 'cookie-info-link')
    COOKIE_ACCEPT_BUTTON = (By.ID, 'cookie-accept-btn')
    COOKIE_SETTING_BUTTON =(By.ID, 'cookie-settings-btn')
    PROMO_LINK = (By.ID, 'promo-link')
    HERO_LOGIN_BUTTON = (By.ID, 'hero-login-btn')
    LOGIN_TAB = (By.ID, 'tabLogin')
    LANGUAGE_SWITCH_LINK = (By.ID, 'nav-language')
    HOBBIES_LINK = (By.ID, 'nav-hobbies')
    GROUPS_LINK = (By.ID, 'nav-groups')
    PUBLICATIONS_LINK = (By.ID, 'nav-publications')
    PEOPLE_LINK = (By.ID, 'nav-people')
    VIDEO_LINK = (By.ID, 'nav-video')
    GIFTS_LINK = (By.ID, 'nav-gifts')
    GAMES_LINK= (By.ID, 'nav-games')
    ADVERTISERS_LINK = (By.ID, 'nav-advertisers')
    HELP_LINK = (By.ID, 'nav-help')
    NEWS_LINK = (By.ID, 'nav-news')
    VACANCIES_LINK = (By.ID, 'nav-jobs')
    ABOUT_COMPANY_LINK = (By.ID, 'nav-about')
    FOR_BUSINESS_LINK = (By.ID, 'nav-business')
    FOR_DEVELOPERS_LINK = (By.ID, 'nav-developers')
    AGREEMENTS_LINK = (By.ID, 'nav-policies')
    RECOMENDATIONS_MORE_LINK = (By.ID, 'footer-recommendations-link')
    ERROR_TEXT = (By.ID, 'login-error')
    RESTORE_LINK = (By.ID, 'lockout-recover-btn')
    GO_BACK_BUTTON = (By.ID, 'lockout-cancel-btn')
    LOCKOUT_REGISTER_BTN = (By.ID, 'lockout-register-btn')


class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.SEARCH_INPUT)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
        self.find_element(LoginPageLocators.HERO_REGISTER_BUTTON)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGO)
        self.find_element(LoginPageLocators.SERVICES_DROPDOWN)
        self.find_element(LoginPageLocators.COOKIE_INFO_LINK)
        self.find_element(LoginPageLocators.COOKIE_ACCEPT_BUTTON)
        self.find_element(LoginPageLocators.COOKIE_SETTING_BUTTON)
        self.find_element(LoginPageLocators.PROMO_LINK)
        self.find_element(LoginPageLocators.HERO_LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LANGUAGE_SWITCH_LINK)
        self.find_element(LoginPageLocators.HOBBIES_LINK)
        self.find_element(LoginPageLocators.GROUPS_LINK)
        self.find_element(LoginPageLocators.PUBLICATIONS_LINK)
        self.find_element(LoginPageLocators.PEOPLE_LINK)
        self.find_element(LoginPageLocators.VIDEO_LINK)
        self.find_element(LoginPageLocators.GIFTS_LINK)
        self.find_element(LoginPageLocators.GAMES_LINK)
        self.find_element(LoginPageLocators.ADVERTISERS_LINK)
        self.find_element(LoginPageLocators.HELP_LINK)
        self.find_element(LoginPageLocators.NEWS_LINK)
        self.find_element(LoginPageLocators.VACANCIES_LINK)
        self.find_element(LoginPageLocators.ABOUT_COMPANY_LINK)
        self.find_element(LoginPageLocators.FOR_BUSINESS_LINK)
        self.find_element(LoginPageLocators.FOR_DEVELOPERS_LINK)
        self.find_element(LoginPageLocators.AGREEMENTS_LINK)
        self.find_element(LoginPageLocators.RECOMENDATIONS_MORE_LINK)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Вводим логин')
    def enter_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_LINK).click()


