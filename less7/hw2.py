import os
from zipfile import ZipFile

from selenium import webdriver
import requests
from selene import browser
from selene import query
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_text_in_downloaded_file():
    with os.mkdir('HW_zip'):
        DIR_HW_ZIP = os.path.abspath('HW_zip')
        options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": DIR_HW_ZIP,
            "download.prompt_for_download": False
        }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        browser.config.driver = driver

        browser.open('https://github.com/Persik78/Guru_HW/blob/master/less7/tmp/HW_zip_file_final.zip')
        download_url_HW = browser.element('[data-testid="raw-button"]').get(query.attribute('href'))

        download_zip = requests.get(url=download_url_HW).content

        with open('HW_zip/down_HW_zip.zip', 'wb') as zip_f:
            print('test')
            zip_f.write(download_zip)

        ZIP_DIR = os.path.join(DIR_HW_ZIP, 'down_HW_zip.zip')

        with ZipFile(ZIP_DIR) as zip_f:
            print(zip_f.namelist())