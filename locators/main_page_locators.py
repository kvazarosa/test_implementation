from selenium.webdriver.common.by import By


class MainPageLocators:
    INPUT_FROM = (By.CSS_SELECTOR, "._filters__input_1iunh_20[placeholder='От']")
    INPUT_BEFORE = (By.CSS_SELECTOR, "._filters__input_1iunh_20[placeholder='До']")
    DROPDOWN_SORT_BY = (By.CSS_SELECTOR, "._filters__select_1iunh_21")
    SORT_BY_PRICE_OPTION = (By.XPATH, "//option[text()='Цене']")
    DROPDOWN_CATEGORY = (By.XPATH, "//select[.//option[text()='Электроника']]")
    ANIMALS_IN_CATEGORIES = (By.CSS_SELECTOR, "option[value='5']")
    URGENT_TOGGLE = (By.CSS_SELECTOR, "._urgentToggle__slider_h1vv9_21")
    STATISTICS_BUTTON = (By.XPATH, "//a[.//span[text()='Статистика']]")
    CARD_PRICE = (By.CSS_SELECTOR, "._card__price_15fhn_241")
    CARD_CATEGORY = (By.CSS_SELECTOR, "._card__category_15fhn_259")
    URGENT_BADGE = (By.CSS_SELECTOR, "._card__priority_15fhn_172")
