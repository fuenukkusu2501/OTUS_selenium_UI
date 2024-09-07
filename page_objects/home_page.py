import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HomePage(BasePage):
    LISTING_CART_BUTTON = By.CSS_SELECTOR, "button[title='Add to Cart']"
    HOMEPAGE_CART_BUTTON = By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle"
    POP_UP_CLOSE_BUTTON = By.CSS_SELECTOR, ".btn-close"
    PRICE = By.CSS_SELECTOR, ".price-new"

    def open(self, url):
        with allure.step(f"Открываю {url}"):
            self.browser.get(url)

    @allure.step("Скроллю страницу вниз")
    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Скроллю страницу вверх")
    def scroll_up(self):
        self.browser.execute_script("window.scrollTo(1000, 0);")

    @allure.step("Добавляю товар в корзину")
    def add_product_to_cart(self):
        self.get_element_clickable(self.LISTING_CART_BUTTON).click()

    @allure.step("Получаю название товара в листинге")
    def get_product_name_listing(self):
        name_product_listing = self.get_element((By.CSS_SELECTOR, ".description a"))
        product_listing_text = name_product_listing.get_attribute('text')
        return product_listing_text

    @allure.step("Получаю название товара в корзине")
    def get_product_name_cart(self):
        name_product_cart = self.get_element((By.CSS_SELECTOR, ".text-start a"))
        product_cart_text = name_product_cart.get_attribute('text')
        return product_cart_text

    @allure.step("Нажимаю на корзину")
    def click_cart_button(self):
        self.get_element_clickable(self.HOMEPAGE_CART_BUTTON).click()

    @allure.step("Закрываю поп-ап")
    def close_pop_up(self):
        self.get_element_clickable(self.POP_UP_CLOSE_BUTTON).click()

    @allure.step("Получаю валюту цены товара")
    def get_price_value(self):
        prise = self.get_element(self.PRICE).text
        return prise

