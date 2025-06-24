import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    driver.set_window_size(1440, 1100)
    yield driver
    driver.quit()

@pytest.fixture
def go_to_order_page(driver):
    driver.get(Urls.ORDER_URL)