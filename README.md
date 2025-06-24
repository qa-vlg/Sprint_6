## Проект Авто-тестов [Сервиса pfзаказа Самоката](https://qa-scooter.praktikum-services.ru/ "Самокат")
### Реализованные тесты:
1. Навигация пользователя:
  * test_user_returns_to_home_page_true
  * test_user_goes_to_yandex_page_true
2. Вопросы с Ответами:
  * test_view_answer_true
3. Заказ Самоката:
  * test_scooter_order_true

### Запустить тесты и сгенерировать Allure отчет:
  * `pytest tests/test_view_answer_true.py --alluredir=allure_results` пример запуска индивидуального теста
  * `pytest tests/ --alluredir=allure_results` пример запуска всех тестов последовательно
  * `allure serve allure_results` сгенерировать отчет, при условии что результаты тестов находятся в папке `allure_results`