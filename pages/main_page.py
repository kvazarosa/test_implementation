from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def go_to_statistics(self):
        self.click(MainPageLocators.STATISTICS_BUTTON)

    def set_price_range(self, from_price: str, to_price: str):
        self.input_text(MainPageLocators.INPUT_FROM, from_price)
        self.input_text(MainPageLocators.INPUT_BEFORE, to_price)

    def select_sort_by_price(self):
        self.click(MainPageLocators.DROPDOWN_SORT_BY)
        self.click(MainPageLocators.SORT_BY_PRICE_OPTION)

    def select_category_animals(self):
        self.click(MainPageLocators.DROPDOWN_CATEGORY)
        self.click(MainPageLocators.ANIMALS_IN_CATEGORIES)

    def enable_urgent_only(self):
        self.click(MainPageLocators.URGENT_TOGGLE)

    def get_all_prices_int(self) -> list:
        price_elements = self.driver.find_elements(*MainPageLocators.CARD_PRICE)
        prices = []
        for el in price_elements:
            text = el.text
            price_text = ''.join([ch for ch in text if ch.isdigit()])
            if price_text:
                price = int(price_text)
                prices.append(price)
        return prices

    def get_all_categories(self) -> list:
        category_elements = self.driver.find_elements(*MainPageLocators.CARD_CATEGORY)
        return [el.text for el in category_elements if el.text]

    def get_all_urgent_badges_count(self) -> int:
        return len(self.driver.find_elements(*MainPageLocators.URGENT_BADGE))
