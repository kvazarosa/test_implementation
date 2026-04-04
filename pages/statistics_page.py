from pages.base_page import BasePage
from locators.statistics_locators import StatisticsLocators as Loc


class StatisticsPage(BasePage):
    def click_refresh(self):
        old_value = self.get_timer_value()
        self.click(Loc.REFRESH_BUTTON)
        self.wait.until(lambda d: self.get_timer_value() != old_value)

    def click_pause(self):
        self.click(Loc.PAUSE_BUTTON)
        self.wait.until(lambda d: self.is_auto_update_off_message_displayed())

    def click_play(self):
        self.click(Loc.PLAY_BUTTON)
        self.wait.until(lambda d: not self.is_auto_update_off_message_displayed())
        self.wait.until(lambda d: self.is_timer_displayed())

    def get_timer_value(self) -> str:
        return self.get_text(Loc.TIMER)

    def is_auto_update_off_message_displayed(self) -> bool:
        return self.is_visible(Loc.AUTO_UPDATE_OFF_MESSAGE)

    def is_timer_displayed(self) -> bool:
        return self.is_visible(Loc.TIMER)
