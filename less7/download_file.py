import time
import pytest
from selenium import webdriver
import requests
from selene import browser
from selene import query
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from less7.script_os import TMP_DIR


def test_text_in_downloaded_file():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download" : False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver



    browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
    download_url = browser.element('[data-testid="raw-button"]').get(query.attribute('href'))
    print(download_url)

    content = requests.get(url=download_url).content

    with open('tmp/readme2.rst', 'wb') as file:
        file.write(content)

    with open('tmp/readme2.rst', 'r') as file:
        a = file.read()
        assert 'test_answer' in a

    #time.sleep(5)

