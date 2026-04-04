import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Urls:
    HOME_PAGE_URL = "https://cerulean-praline-8e5aa6.netlify.app/"


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)

    driver.get(Urls.HOME_PAGE_URL)
    yield driver
    driver.quit()