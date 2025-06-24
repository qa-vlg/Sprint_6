from pages.faq_page import FaqPage
from data import FaqText
import allure
import pytest

class TestFaqPage:

    @allure.title('Проверка ответов на часто задаваемые вопросы')
    @allure.description('Переходим в раздел: "Вопросы о важном" и проверям что каждому вопросу соответствует верный ответ.')
    @pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_view_answer_true(self, driver, index):
        faq_page = FaqPage(driver)
        expected_text = faq_page.get_answer(index)
        assert expected_text == FaqText.answers[index]
