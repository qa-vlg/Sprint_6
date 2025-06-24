from pages.base_page import BasePage
from locators.locators import Locators
import allure

class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на Самокат')
    def home_logo_click(self):
        self.click_on_element(Locators.SCOOTER_HOME_BUTTON)

    @allure.step('Нажимаем на Яндекс')
    def yandex_logo_click(self):
        self.click_on_element(Locators.YANDEX_HOME_BUTTON)

    @allure.step('Переходим на Домашнюю страницу')
    def go_to_home_page(self):
        self.scroll_to_the_top()
        self.home_logo_click()
        url = self.get_page_url()
        return url

    @allure.step('Переходим на страницу Яндекс')
    def go_to_yandex_page(self):
        self.scroll_to_the_top()
        self.yandex_logo_click()
        self.switch_between_tabs(1)
        self.wait_for_element_to_be_ready(Locators.DZEN_LOGO)
        url = self.get_page_url()
        return url
        