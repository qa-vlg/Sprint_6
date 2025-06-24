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