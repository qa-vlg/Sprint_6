from urls import Urls
import allure
from pages.home_page import HomePage

class TestHomePage:

    @allure.title('Переход на домашнюю страницу Самоката')
    @allure.description('Проверяем что пользователь переходит на страницу Самоката при нажатии на логотипю')
    def test_user_returns_to_home_page_true(self, driver, go_to_order_page):
        home_page = HomePage(driver)
        actual_url = home_page.go_to_home_page()
        assert Urls.BASE_URL == actual_url

    @allure.title('Переход на домашнюю страницу Яндекс')
    @allure.description('Проверяем что пользователь переходит на страницу Яндекс при нажатии на логотипю')
    def test_user_goes_to_yandex_page_true(self, driver):
        home_page = HomePage(driver)
        actual_url = home_page.go_to_yandex_page()
        assert 'dzen' in actual_url
        