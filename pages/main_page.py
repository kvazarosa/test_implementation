from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Loc


class MainPage(BasePage):
    def go_to_statistics(self):
        self.click(Loc.STATISTICS_BUTTON)

    def set_price_range(self, from_price: str, to_price: str):
        self.input_text(Loc.INPUT_FROM, from_price)
        self.input_text(Loc.INPUT_BEFORE, to_price)
        self.wait.until(lambda d: len(d.find_elements(*Loc.CARD_PRICE)) > 0)

    def select_sort_by_price(self):
        self.click(Loc.DROPDOWN_SORT_BY)
        self.click(Loc.SORT_BY_PRICE_OPTION)
        self.wait.until(lambda d: self.get_all_prices_int() == sorted(self.get_all_prices_int(), reverse=True))

    def select_category_animals(self):
        self.click(Loc.DROPDOWN_CATEGORY)
        self.click(Loc.ANIMALS_IN_CATEGORIES)
        self.wait.until(lambda d: all(cat == "Животные" for cat in self.get_all_categories()))

    def enable_urgent_only(self):
        self.click(Loc.URGENT_TOGGLE)
        self.wait.until(lambda d: self.get_all_urgent_badges_count() == len(self.get_all_prices_int()))

    def get_all_prices_int(self) -> list:
        price_elements = self.driver.find_elements(*Loc.CARD_PRICE)
        prices = []
        for el in price_elements:
            text = el.text
            price_text = ''.join([ch for ch in text if ch.isdigit()])
            if price_text:
                price = int(price_text)
                prices.append(price)
        return prices

    def get_all_categories(self) -> list:
        category_elements = self.driver.find_elements(*Loc.CARD_CATEGORY)
        return [el.text for el in category_elements]

    def get_all_urgent_badges_count(self) -> int:
        return len(self.driver.find_elements(*Loc.URGENT_BADGE))
