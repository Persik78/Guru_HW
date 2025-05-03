import os
import requests
import csv
from zipfile import ZipFile
from pypdf import PdfReader
from selenium import webdriver
from selene import browser
from selene import query
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl import load_workbook



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
    dir_list = zip_f.namelist()
    for i in range(len(dir_list)):
        ext = os.path.splitext(dir_list[i])
        if ext[1] == '.pdf':
            print('pdf')
            with zip_f.open(dir_list[i]) as pdfFileInRachive:
                content = pdfFileInRachive.read().decode('utf-8')
                print(content)

        elif ext[1] == '.xlsx':
            print('xlsx')
        elif ext[1] == '.csv':
            print('csv')
