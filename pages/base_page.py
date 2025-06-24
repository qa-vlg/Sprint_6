from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_element_text(self, locator):
        text = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).text
        return text
    
    def wait_for_element_to_be_ready(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def get_page_url(self):
        return self.driver.current_url
    
    def scroll_to_the_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_the_top(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        element.click()

    def enter_text(self, locator, text):
         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
         element.send_keys(text)

    def switch_between_tabs(self, tab_index):
        open_tabs = self.driver.window_handles
        self.driver.switch_to.window(open_tabs[tab_index])

    def dismiss_a_modal(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()