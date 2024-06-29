import allure
from selenium.webdriver.common.by import By
from page_objects.admin_page import AdminPage
from page_objects.home_page import HomePage
from page_objects.header_element import HeaderElement
from page_objects.catalog_page import CatalogPage
from page_objects.registration_page import RegistrationPage
import logging

logger = logging.getLogger(__name__)

@allure.title("Наличие элементов")
def test_elements(browser, base_url):
    browser.get(base_url)
    assert browser.title == "Your Store"
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg")
    assert browser.find_element(By.CSS_SELECTOR, ".form-control.form-control-lg")
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    assert browser.find_element(By.CSS_SELECTOR, "#narbar-menu")
    assert browser.find_element(By.CSS_SELECTOR, ".row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4")
    browser.get(f"{base_url}/en-gb/catalog/laptop-notebook")
    assert browser.find_element(By.CSS_SELECTOR, "#compare-total")
    assert browser.find_elements(By.CSS_SELECTOR, ".fa-solid.fa-shopping-cart")[0]
    assert browser.find_element(By.CSS_SELECTOR, "#button-list")
    assert browser.find_element(By.CSS_SELECTOR, "#button-grid")
    assert browser.find_element(By.CSS_SELECTOR, "#input-sort")
    browser.get(f"{base_url}/en-gb/product/laptop-notebook/hp-lp3065")
    assert browser.find_element(By.CSS_SELECTOR, "#button-cart")
    assert browser.find_element(By.CSS_SELECTOR, ".price-new")
    assert browser.find_element(By.CSS_SELECTOR, ".nav-link.active")
    assert browser.find_element(By.CSS_SELECTOR, "#input-option-225")
    assert browser.find_element(By.CSS_SELECTOR, "#input-quantity")
    browser.get(f"{base_url}/index.php?route=account/register")
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    assert browser.find_element(By.CSS_SELECTOR, "#input-firstname")
    assert browser.find_element(By.CSS_SELECTOR, "#input-lastname")
    assert browser.find_element(By.CSS_SELECTOR, "#input-email")
    assert browser.find_element(By.CSS_SELECTOR, "#input-newsletter")
    browser.get(f"{base_url}/administration/")
    assert AdminPage(browser).USERNAME_INPUT
    assert AdminPage(browser).PASSWORD_INPUT
    assert browser.find_elements(By.CSS_SELECTOR, ".fa-solid.fa-lock")[0]
    assert browser.find_elements(By.CSS_SELECTOR, ".fa-solid.fa-lock")[1]
    assert browser.find_element(By.CSS_SELECTOR, ".card-body")

@allure.title("Авторизация (админка)")
def test_admin_login(browser, base_url):
    admin_page = AdminPage(browser)
    admin_page.open(base_url)
    admin_page.login("user", "bitnami")
    assert admin_page.title_username() == "user"
    assert admin_page.alt_username() == "John Doe"
    assert browser.current_url.__contains__(base_url)

@allure.title("Добавление товара в корзину")
def test_add_to_cart(browser, base_url):
    home_page = HomePage(browser)
    home_page.open(base_url)
    home_page.scroll_down()
    home_page.add_product_to_cart()
    product_name_listing = home_page.get_product_name_listing()
    home_page.scroll_up()
    home_page.click_cart_button()
    product_name_cart = home_page.get_product_name_cart()
    assert product_name_listing == product_name_cart

@allure.title("Смена валюты - главная страница")
def test_currency_change_home(browser, base_url):
    home_page = HomePage(browser)
    header = HeaderElement(browser)
    home_page.open(base_url)
    header.click_currency()
    header.select_euro()
    price = home_page.get_price_value()
    assert price.__contains__("€")
    assert not price.__contains__("$")

@allure.title("Смена валюты - каталог")
def test_currency_change_catalog(browser, base_url):
    catalog_page = CatalogPage(browser)
    header = HeaderElement(browser)
    catalog_page.open(base_url)
    header.click_currency()
    header.select_euro()
    price = HomePage(browser).get_price_value()
    assert price.__contains__("€")
    assert not price.__contains__("$")

@allure.title("Создать товар")
def test_add_product(browser, base_url):
    admin_page = AdminPage(browser)
    admin_page.open(base_url)
    admin_page.login("user", "bitnami")
    admin_page.select_catalog()
    admin_page.select_products()
    admin_page.add_product()
    admin_page.add_product_name("test item")
    admin_page.add_meta_tag("test")
    admin_page.select_data_tab()
    admin_page.add_model("12345")
    admin_page.select_seo_tab()
    admin_page.add_seo_name("12345")
    admin_page.save_product()
    admin_page.find_popup_success()

@allure.title("Удалить товар")
def test_delete_product(browser, base_url):
    admin_page = AdminPage(browser)
    admin_page.open(base_url)
    admin_page.login("user", "bitnami")
    admin_page.select_catalog()
    admin_page.select_products()
    HomePage(browser).scroll_down()
    admin_page.to_the_last_page()
    admin_page.select_last_product()
    HomePage(browser).scroll_up()
    admin_page.delete_product()
    admin_page.find_popup_success()

@allure.title("Регистрация")
def test_user_registration(browser, base_url):
    registration_page = RegistrationPage(browser)
    registration_page.open(base_url)
    registration_page.input_data("Oleg", "Ivanov", "123@gmail.com", "12345")
    registration_page.confirm_agreement()
    registration_page.complete_registration()
    title_text = registration_page.get_title_text()
    assert title_text == "Your Account Has Been Created!"

@allure.title("Смена валюты")
def test_change_currency(browser, base_url):
    header = HeaderElement(browser)
    HomePage(browser).open(base_url)
    header.click_currency()
    header.select_euro()
    currency_icon = header.get_currency_icon()
    assert currency_icon == "€"
    header.click_currency()
    header.select_pound()
    currency_icon = header.get_currency_icon()
    assert currency_icon == "£"
    header.click_currency()
    header.select_dollar()
    currency_icon = header.get_currency_icon()
    assert currency_icon == "$"
