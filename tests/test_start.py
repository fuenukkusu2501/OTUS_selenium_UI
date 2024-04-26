from selenium.webdriver.common.by import By

def test_one(browser):
    browser.get("http://localhost:8081/")
    assert browser.title == "Your Store"
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg") # http://192.168.0.106:8081/en-gb?route=common/home
    assert browser.find_element(By.CSS_SELECTOR, "#input-password")
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg")
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg")
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg")
    browser.get("http://192.168.0.106:8081/en-gb/catalog/laptop-notebook")
    assert browser.find_element(By.CSS_SELECTOR, "#compare-total") #каталог http://192.168.0.106:8081/en-gb/catalog/laptop-notebook
    assert browser.find_element(By.CSS_SELECTOR, ".fa-solid.fa-shopping-cart")[0]
    assert browser.find_element(By.CSS_SELECTOR, "#button-list")
    assert browser.find_element(By.CSS_SELECTOR, "#button-grid")
    assert browser.find_element(By.CSS_SELECTOR, "#input-sort")
    browser.get("http://192.168.0.106:8081/en-gb/product/laptop-notebook/hp-lp3065")
    assert browser.find_element(By.CSS_SELECTOR, "#button-cart") # http://192.168.0.106:8081/en-gb/product/laptop-notebook/hp-lp3065
    assert browser.find_element(By.CSS_SELECTOR, ".price-new")
    assert browser.find_element(By.CSS_SELECTOR, ".nav-link.active")
    assert browser.find_element(By.CSS_SELECTOR, "#input-option-225")
    assert browser.find_element(By.CSS_SELECTOR, "#input-quantity") #h1
    browser.get("http://localhost:8081/index.php?route=account/register")
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    assert browser.find_element(By.CSS_SELECTOR, "#input-firstname")
    assert browser.find_element(By.CSS_SELECTOR, "#input-lastname")
    assert browser.find_element(By.CSS_SELECTOR, "#input-email")
    assert browser.find_element(By.CSS_SELECTOR, "#input-newsletter")
    browser.get("http://192.168.0.106:8081/administration/")
    assert browser.find_element(By.CSS_SELECTOR, "#input-username")
    assert browser.find_element(By.CSS_SELECTOR, "#input-password")
    assert browser.find_element(By.CSS_SELECTOR, ".fa-solid.fa-lock")[0]
    assert browser.find_element(By.CSS_SELECTOR, ".fa-solid.fa-lock")[1]
    assert browser.find_element(By.CSS_SELECTOR, ".card-body")

