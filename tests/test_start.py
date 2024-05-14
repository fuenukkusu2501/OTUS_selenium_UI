from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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
    assert browser.find_element(By.CSS_SELECTOR, "#input-username")
    assert browser.find_element(By.CSS_SELECTOR, "#input-password")
    assert browser.find_elements(By.CSS_SELECTOR, ".fa-solid.fa-lock")[0]
    assert browser.find_elements(By.CSS_SELECTOR, ".fa-solid.fa-lock")[1]
    assert browser.find_element(By.CSS_SELECTOR, ".card-body")


def test_admin_login(browser, base_url):
    browser.get(f"{base_url}/administration/")
    """fill inputs and click login"""
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("user")
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    profile = browser.find_element(By.CSS_SELECTOR, ".rounded-circle")
    assert profile.get_attribute("title") == "user"
    assert profile.get_attribute("alt") == "John Doe"
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='Logout']"))).click()
    assert browser.current_url.__contains__('/administration/index.php?route=common/login')


def test_add_to_cart(browser, base_url):
    browser.get(f"{base_url}")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".fa-solid.fa-shopping-cart"))).click()
    name_product_listing = browser.find_element(By.CSS_SELECTOR, ".description a")
    product_listing_text = name_product_listing.get_attribute('text')
    time.sleep(1)
    browser.execute_script("window.scrollTo(1000, 0);")
    time.sleep(5)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle"))).click()
    name_product_cart = browser.find_element(By.CSS_SELECTOR, ".text-start a")
    product_cart_text = name_product_cart.get_attribute('text')
    assert product_listing_text == product_cart_text


def test_currency_change_home(browser, base_url):
    browser.get(f"{base_url}")
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='Currency']"))).click()
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='€ Euro']"))).click()
    price = browser.find_element(By.CSS_SELECTOR, ".price-new")
    price_text = price.text
    assert price_text.__contains__("€")
    assert not price_text.__contains__("$")


def test_currency_change_catalog(browser, base_url):
    browser.get(f"{base_url}/en-gb/catalog/laptop-notebook")
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='Currency']"))).click()
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='€ Euro']"))).click()
    price = browser.find_element(By.CSS_SELECTOR, ".price-new")
    price_text = price.text
    assert price_text.__contains__("€")
    assert not price_text.__contains__("$")
