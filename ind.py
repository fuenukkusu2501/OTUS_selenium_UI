import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "*/yandex.exe"
service = Service(executable_path="*/yandexdriver")
browser = webdriver.Chrome(service=service, options=options)

browser.get("https://google.com")

time.sleep(5)