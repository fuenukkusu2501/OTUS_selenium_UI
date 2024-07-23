import allure
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    PATH = "/en-gb/catalog/laptop-notebook"

    def open(self, url):
        with allure.step(f"Открываю {url + self.PATH}"):
            self.browser.get(url + self.PATH)