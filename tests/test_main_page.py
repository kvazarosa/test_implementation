import pytest
from pages.main_page import MainPage


class TestMainPage:
    @pytest.mark.parametrize("from_price, to_price", [
        ("100", "1000"),
        ("500", "5000"),
        ("10000", "100000"),
    ])
    def test_price_range_filter(self, driver, from_price, to_price):
        page = MainPage(driver)
        page.set_price_range(from_price, to_price)
        prices = page.get_all_prices_int()
        for price in prices:
            assert int(from_price) <= price <= int(to_price)

    def test_sort_by_price(self, driver):
        page = MainPage(driver)
        page.select_sort_by_price()
        prices = page.get_all_prices_int()
        assert prices == sorted(prices, reverse=True)

    def test_category_filter_animals(self, driver):
        page = MainPage(driver)
        page.select_category_animals()
        assert all(cat == "Животные" for cat in page.get_all_categories())

    def test_urgent_toggle_filter(self, driver):
        page = MainPage(driver)
        page.enable_urgent_only()
        assert page.get_all_urgent_badges_count() == len(page.get_all_prices_int())
