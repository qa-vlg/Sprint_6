from pages.page_actions import PageActions
from locators.locators import Locators
import allure

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.page_actions = PageActions(driver)

    @allure.step('Нажимаем на Самокат')
    def home_logo_click(self):
        self.page_actions.click_on_element(Locators.SCOOTER_HOME_BUTTON)

    @allure.step('Нажимаем на Яндекс')
    def yandex_logo_click(self):
        self.page_actions.click_on_element(Locators.YANDEX_HOME_BUTTON)

    @allure.step('Переходим на Домашнюю страницу')
    def go_to_home_page(self):
        self.page_actions.scroll_to_the_top()
        self.home_logo_click()
        url = self.page_actions.get_page_url()
        return url

    @allure.step('Переходим на страницу Яндекс')
    def go_to_yandex_page(self):
        self.page_actions.scroll_to_the_top()
        self.yandex_logo_click()
        self.page_actions.switch_between_tabs(1)
        self.page_actions.wait_for_element_to_be_ready(Locators.DZEN_LOGO)
        url = self.page_actions.get_page_url()
        return url
        