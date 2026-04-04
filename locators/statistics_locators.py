from selenium.webdriver.common.by import By


class StatisticsLocators:
    REFRESH_BUTTON = (By.CSS_SELECTOR, "._refreshButton_ir5wu_16")
    PAUSE_BUTTON = (By.CSS_SELECTOR, "._toggleButton_ir5wu_69._toggleButton_active_ir5wu_89")
    PLAY_BUTTON = (By.CSS_SELECTOR, "._toggleButton_ir5wu_69")
    TIMER = (By.CSS_SELECTOR, "._timeValue_ir5wu_112")
    AUTO_UPDATE_OFF_MESSAGE = (By.XPATH, "//span[text()='Автообновление выключено']")
