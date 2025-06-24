from pages.page_actions import PageActions
from locators.locators import Locators
import allure


class OrderPage:

    def __init__(self, driver, user_data):
        self.driver = driver
        self.user_data = user_data
        self.page_actions = PageActions(driver)

    @allure.step('Кликаем на кнопку: "Заказать"')
    def start_new_order(self, order_button):
        self.page_actions.scroll_to_element(order_button)
        self.page_actions.click_on_element(order_button)

    @allure.step('Заполняем Имя пользователя')
    def fill_in_user_first_name(self):
        self.page_actions.enter_text(Locators.FIRST_NAME_INPUT, self.user_data['first_name'])

    @allure.step('Заполняем Фамилию пользователя')
    def fill_in_user_last_name(self):
        self.page_actions.enter_text(Locators.LAST_NAME_INPUT, self.user_data['last_name'])
    
    @allure.step('Заполняем Адрес пользователя')
    def fill_in_user_address(self):
        self.page_actions.enter_text(Locators.ADDRESS_INPUT, self.user_data['address'])

    @allure.step('Выбираем Станцию Метро')
    def select_subway_station(self):
        self.page_actions.enter_text(Locators.SUBWAY_STATION_INPUT, self.user_data['subway_station'])
        self.page_actions.click_on_element(Locators.SUBWAY_STATION_CONFIRM)

    @allure.step('Заполняем Номер Телефона пользователя')
    def fill_in_user_phone_number(self):
        self.page_actions.enter_text(Locators.PHONE_NUMBER_INPUT, self.user_data['phone_number'])

    @allure.step('Переходим к следующей части оформления заказа')
    def move_forward_with_order(self):
        self.page_actions.click_on_element(Locators.BUTTON_NEXT)

    @allure.step('Выбираем Дату Доставки')
    def select_delivery_date(self):
        self.page_actions.enter_text(Locators.EXPECTED_DATE_INPUT, self.user_data['date'])
        self.page_actions.dismiss_a_modal()

    @allure.step('Выбираем Срок Аренды')
    def select_duration(self):
        self.page_actions.click_on_element(Locators.RENT_DURATION_OPEN_DROPDOWN)
        self.page_actions.click_on_element(Locators.RENT_DURATION_ONE_DAY)

    @allure.step('Выбираем Цвет') 
    def pick_a_color(self):
        self.page_actions.click_on_element(Locators.COLOR_PICKER_BLACK)

    @allure.step('Заполняем Комментарий к заказу')
    def enter_order_comment(self):
        self.page_actions.enter_text(Locators.COMMENTS_INPUT, self.user_data['comment'])

    @allure.step('Нажимаем на кнопку оформления заказа')
    def place_order(self):
        self.page_actions.click_on_element(Locators.CREATE_ORDER_BUTTON)

    @allure.step('Подтверждаем Оформление Заказа')
    def confirm_order_creation(self):
        self.page_actions.click_on_element(Locators.ORDER_CONFIRMATION_ACCEPT_BUTTON)

    @allure.step('Заказали Самокат')
    def order_scooter(self, order_button):
        self.start_new_order(order_button)
        self.fill_in_user_first_name()
        self.fill_in_user_last_name()
        self.fill_in_user_address()
        self.select_subway_station()
        self.fill_in_user_phone_number()
        self.move_forward_with_order()
        self.select_delivery_date()
        self.select_duration()
        self.pick_a_color()
        self.enter_order_comment()
        self.place_order()
        self.confirm_order_creation()
        return self.page_actions.get_page_element_text(Locators.ORDER_CONFIRMATION_TEXT)
    