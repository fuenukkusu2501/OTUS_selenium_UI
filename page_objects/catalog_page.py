import allure
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    PATH = "/en-gb/catalog/laptop-notebook"
    DESCRIPTION_PRODUCT = By.CSS_SELECTOR, ".description h4"

    def open(self, url):
        with allure.step(f"Открываю {url + self.PATH}"):
            self.browser.get(url + self.PATH)

    @allure.step("Получаю текст наименования товара")
    def get_description_text(self):
        return self.get_element(self.DESCRIPTION_PRODUCT).text