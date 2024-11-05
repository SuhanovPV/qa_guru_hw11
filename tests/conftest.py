import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def browser_set():

    selenoid_login = 'user1'
    selenoid_pass = '1234'
    selenoid_url = 'https://selenoid.autotests.cloud'


    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "120.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.close()