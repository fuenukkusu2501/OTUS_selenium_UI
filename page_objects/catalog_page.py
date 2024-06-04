from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    PATH = "/en-gb/catalog/laptop-notebook"

    def open(self, url):
        self.browser.get(url + self.PATH)