from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HeaderElement(BasePage):
    CURRENCY_BUTTON = By.XPATH, "//*[text()='Currency']"
    CURRENCY_ICON = By.XPATH, "//strong"

    def open(self, url):
        self.browser.get(url)

    def click_currency(self):
        self.get_element(self.CURRENCY_BUTTON).click()

    def select_euro(self):
        self.get_element((By.XPATH, "//*[text()='€ Euro']")).click()

    def select_pound(self):
        self.get_element((By.XPATH, "//*[text()='£ Pound Sterling']")).click()

    def select_dollar(self):
        self.get_element((By.XPATH, "//*[text()='$ US Dollar']")).click()

    def get_currency_icon(self):
        icon = self.get_element(self.CURRENCY_ICON)
        icon_text = icon.text
        return icon_text