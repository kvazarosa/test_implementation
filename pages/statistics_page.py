from pages.base_page import BasePage
from locators.statistics_locators import StatisticsLocators


class StatisticsPage(BasePage):
    def click_refresh(self):
        self.click(StatisticsLocators.REFRESH_BUTTON)

    def click_pause(self):
        self.click(StatisticsLocators.PAUSE_BUTTON)

    def click_play(self):
        self.click(StatisticsLocators.PLAY_BUTTON)

    def get_timer_value(self) -> str:
        return self.get_text(StatisticsLocators.TIMER)

    def is_auto_update_off_message_displayed(self) -> bool:
        return self.is_visible(StatisticsLocators.AUTO_UPDATE_OFF_MESSAGE)

    def is_timer_displayed(self) -> bool:
        return self.is_visible(StatisticsLocators.TIMER)
