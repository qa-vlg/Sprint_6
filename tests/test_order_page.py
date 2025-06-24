from pages.order_page import OrderPage
from locators.locators import Locators
from data import UserInfo
import allure
import pytest

class TestOrderPage:

    @allure.title('Оформление заказа Самоката')
    @allure.description('Проверяем создание заказа с разными наборами данных и из разных точек входа.')
    @pytest.mark.parametrize("order_button, user_data", [(Locators.TOP_ORDER_BUTTON, UserInfo.user_alex), 
                                                         (Locators.MID_ORDER_BUTTON, UserInfo.user_andrew)])
    def test_scooter_order_true(self, driver, order_button, user_data):
        order_page = OrderPage(driver, user_data)
        assert 'Заказ оформлен' in order_page.order_scooter(order_button)