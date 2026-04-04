from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))
