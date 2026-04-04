from pages.base_page import BasePage
from locators.mobile_locators import MobileLocators


class MobilePage(BasePage):
    def click_theme_toggle(self):
        self.click(MobileLocators.THEME_TOGGLE)

    def get_background_color(self) -> str:
        body = self.driver.find_element(*MobileLocators.BODY)
        return body.value_of_css_property("background-color")
