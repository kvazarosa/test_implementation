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


@pytest.fixture(scope="function")
def mobile_driver():
    options = Options()
    options.add_argument("--window-size=390,844")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 "
        "(KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(30)
    driver.get(Urls.HOME_PAGE_URL)
    yield driver
    driver.quit()
