from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import allure


class HeaderElement(BasePage):
    CURRENCY_BUTTON = By.XPATH, "//*[text()='Currency']"
    CURRENCY_ICON = By.XPATH, "//strong"
    SEARCH_FIELD = By.CSS_SELECTOR, ".form-control.form-control-lg"
    SEARCH_BUTTON = By.CSS_SELECTOR, ".btn.btn-light.btn-lg"

    def open(self, url):
        with allure.step(f"Открываю {url}"):
            self.browser.get(url)

    @allure.step("Ищу товар")
    def search_product(self, text):
        self.input_value(self.SEARCH_FIELD,text)
        self.get_element(self.SEARCH_BUTTON).click()


    @allure.step("Кликаю на Валюты")
    def click_currency(self):
        self.get_element(self.CURRENCY_BUTTON).click()

    @allure.step("Выбираю евро")
    def select_euro(self):
        self.get_element((By.XPATH, "//*[text()='€ Euro']")).click()

    @allure.step("Выбираю фунт")
    def select_pound(self):
        self.get_element((By.XPATH, "//*[text()='£ Pound Sterling']")).click()

    @allure.step("Выбираю доллар")
    def select_dollar(self):
        self.get_element((By.XPATH, "//*[text()='$ US Dollar']")).click()

    @allure.step("Получаю иконку валюты")
    def get_currency_icon(self):
        icon = self.get_element(self.CURRENCY_ICON)
        icon_text = icon.text
        return icon_text