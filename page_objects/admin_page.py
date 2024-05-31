from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/administration"
    USERNAME_INPUT = By.CSS_SELECTOR, "#input-username"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    SUBMIT_LOGIN_BUTTON = By.CSS_SELECTOR, ".btn.btn-primary"
    CATALOG_BUTTON = By.XPATH, "//*[text()=' Catalog']"
    PRODUCTS_BUTTON = By.XPATH, "//*[text()='Products']"
    ADD_PRODUCT_BUTTON = By.CSS_SELECTOR, '.btn.btn-primary'
    PRODUCT_NAME_INPUT = By.CSS_SELECTOR, "#input-name-1"
    META_TAG_INPUT = By.CSS_SELECTOR, "#input-meta-title-1"
    DATA_TAB = By.XPATH, "//*[text()='Data']"
    SEO_TAB = By.XPATH, "//*[text()='SEO']"
    INPUT_MODEL = By.CSS_SELECTOR, "#input-model"
    INPUT_SEO_NAME = By.CSS_SELECTOR, "#input-keyword-0-1"
    SAVE_PRODUCT_BUTTON = By.CSS_SELECTOR, ".fa-solid.fa-floppy-disk"
    LAST_PAGE = By.XPATH, "//*[text()='>|']"
    LAST_PRODUCT = By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(1) > input"
    POPUP_SUCCESS = By.XPATH, "//div[contains(text(),'Success: You have modified products!')]"

    def open(self, url):
        self.browser.get(url + self.PATH)

    def input_username(self, text):
        self.get_element(self.USERNAME_INPUT).clear()
        self.get_element(self.USERNAME_INPUT).send_keys(text)

    def input_password(self, text):
        self.get_element(self.PASSWORD_INPUT).clear()
        self.get_element(self.PASSWORD_INPUT).send_keys(text)

    def login(self, username, password):
        self.get_element(self.USERNAME_INPUT).clear()
        self.get_element(self.PASSWORD_INPUT).clear()
        self.input_value(self.USERNAME_INPUT, username)
        self.input_value(self.PASSWORD_INPUT, password)
        self.get_element(self.SUBMIT_LOGIN_BUTTON).click()

    def submit_login(self):
        self.get_element(self.SUBMIT_LOGIN_BUTTON).click()

    def title_username(self):
        self.get_element((By.CSS_SELECTOR, ".rounded-circle"))
        profile = self.get_element((By.CSS_SELECTOR, ".rounded-circle"))
        return profile.get_attribute("title")

    def alt_username(self):
        self.get_element((By.CSS_SELECTOR, ".rounded-circle"))
        profile = self.get_element((By.CSS_SELECTOR, ".rounded-circle"))
        return profile.get_attribute("alt")

    def select_catalog(self):
        self.get_element(self.CATALOG_BUTTON).click()

    def select_products(self):
        self.get_element(self.PRODUCTS_BUTTON).click()

    def add_product(self):
        self.get_element(self.ADD_PRODUCT_BUTTON).click()

    def add_product_name(self, text):
        self.input_value(self.PRODUCT_NAME_INPUT, text)

    def add_meta_tag(self, text):
        self.input_value(self.META_TAG_INPUT, text)

    def select_data_tab(self):
        self.get_element(self.DATA_TAB).click()

    def add_model(self, text):
        self.input_value(self.INPUT_MODEL, text)

    def select_seo_tab(self):
        self.get_element(self.SEO_TAB).click()

    def add_seo_name(self, text):
        self.input_value(self.INPUT_SEO_NAME, text)

    def save_product(self):
        self.get_element(self.SAVE_PRODUCT_BUTTON).click()

    def to_the_last_page(self):
        self.get_element(self.LAST_PAGE).click()

    def select_last_product(self):
        self.get_element(self.LAST_PRODUCT).click()

    def delete_product(self):
        self.get_element((By.CSS_SELECTOR, ".btn.btn-danger")).click()
        confirm_alert = self.browser.switch_to.alert
        confirm_alert.accept()

    def find_popup_success(self):
        self.get_element(self.POPUP_SUCCESS)
