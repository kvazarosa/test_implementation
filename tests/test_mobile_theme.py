from pages.mobile_page import MobilePage


class TestMobileTheme:
    def test_theme_changes_on_mobile(self, mobile_driver):
        page = MobilePage(mobile_driver)
        bg_before = page.get_background_color()
        page.click_theme_toggle()
        page.wait.until(lambda d: page.get_background_color() != bg_before)
        bg_after = page.get_background_color()
        assert bg_before != bg_after, "Цвет не изменился"
