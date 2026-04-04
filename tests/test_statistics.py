from pages.main_page import MainPage
from pages.statistics_page import StatisticsPage


class TestStatistics:
    def test_refresh_button_updates_timer(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_statistics()
        stats_page = StatisticsPage(driver)
        stats_page.click_refresh()

    def test_pause_button_stops_auto_update(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_statistics()
        stats_page = StatisticsPage(driver)
        stats_page.click_pause()
        assert stats_page.is_auto_update_off_message_displayed()

    def test_play_button_starts_timer(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_statistics()
        stats_page = StatisticsPage(driver)
        stats_page.click_pause()
        stats_page.click_play()
        assert stats_page.is_timer_displayed()
