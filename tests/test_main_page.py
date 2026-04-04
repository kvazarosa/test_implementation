from pages.main_page import MainPage


class TestMainPage:
    def test_price_range_filter(self, driver):
        page = MainPage(driver)
        page.set_price_range("100", "1000")
        prices = page.get_all_prices_int()
        for price in prices:
            assert 100 <= price <= 1000, f"Цена {price} вне диапазона"

    def test_sort_by_price(self, driver):
        page = MainPage(driver)
        page.select_sort_by_price()
        prices = page.get_all_prices_int()
        assert prices == sorted(prices, reverse=True), "Цены не отсортированы по убыванию"

    def test_category_filter_animals(self, driver):
        page = MainPage(driver)
        page.select_category_animals()
        categories = page.get_all_categories()
        assert all(cat == "Животные" for cat in categories if cat), \
            f"Найдены другие категории: {set(categories)}"

    def test_urgent_toggle_filter(self, driver):
        page = MainPage(driver)
        page.enable_urgent_only()
        urgent_count = page.get_all_urgent_badges_count()
        cards_count = len(page.get_all_prices_int())
        assert urgent_count == cards_count, f"Срочных: {urgent_count}, всего: {cards_count}"
