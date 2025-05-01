import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_manager():

    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.timeout = 10

    yield

    browser.close()