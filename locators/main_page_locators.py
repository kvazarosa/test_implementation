from selenium.webdriver.common.by import By


class MainPageLocators:
    INPUT_FROM = (By.CSS_SELECTOR, "._filters__input_1iunh_20[placeholder='От']")
    INPUT_BEFORE = (By.CSS_SELECTOR, "._filters__input_1iunh_20[placeholder='До']")
    DROPDOWN_SORT_BY = (By.CSS_SELECTOR, "._filters__select_1iunh_21")
    DROPDOWN_PRICE = (By.XPATH, "//select[.//option[text()='Цене']]")
    DROPDOWN_CATEGORY = (By.XPATH, "//select[.//option[text()='Электроника']]")
    ANIMALS_IN_CATEGORIES = (By.CSS_SELECTOR, "option[value='5']")
    URGENT_TOGGLE = (By.CSS_SELECTOR, "_urgentToggle__slider_h1vv9_21")
    STATISTICS_BUTTON = (By.CSS_SELECTOR, "._link_14hw7_51 _link_active_14hw7_79")