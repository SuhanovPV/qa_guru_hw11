import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_set():

    options = webdriver.FirefoxOptions()
    options.page_load_strategy = 'eager'

    browser.config.driver_options = options
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.close()