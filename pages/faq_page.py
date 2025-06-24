from pages.page_actions import PageActions
from locators.locators import Locators
import allure

class FaqPage:

    open_answers = [
        Locators.ANSWER_0_DROPDOWN, Locators.ANSWER_1_DROPDOWN, Locators.ANSWER_2_DROPDOWN,
        Locators.ANSWER_3_DROPDOWN, Locators.ANSWER_4_DROPDOWN, Locators.ANSWER_5_DROPDOWN,
        Locators.ANSWER_6_DROPDOWN, Locators.ANSWER_7_DROPDOWN
    ]
    answers_text = [
        Locators.ANSWER_0_TEXT, Locators.ANSWER_1_TEXT, Locators.ANSWER_2_TEXT, Locators.ANSWER_3_TEXT,
        Locators.ANSWER_4_TEXT, Locators.ANSWER_5_TEXT, Locators.ANSWER_6_TEXT, Locators.ANSWER_7_TEXT
    ]
    def __init__(self, driver):
        self.driver = driver
        self.page_actions = PageActions(driver)

    @allure.step('Переходим к Вопросам')
    def go_to_faq_section(self):
        self.page_actions.scroll_to_the_bottom()

    @allure.step('Смотрим ответ на Вопрос')
    def view_answer(self, index):
        self.page_actions.click_on_element(self.open_answers[index])
    
    @allure.step('Получаем ответ на Вопрос')
    def get_answer(self, index):
        self.go_to_faq_section()
        self.view_answer(index)
        return self.page_actions.get_page_element_text(self.answers_text[index])
    