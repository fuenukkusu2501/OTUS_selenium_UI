import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage


class RegistrationPage(BasePage):
    PATH = "/en-gb?route=account/register"
    FIRSTMANE_INPUT = By.CSS_SELECTOR, "#input-firstname"
    LASTNAME_INPUT = By.CSS_SELECTOR, "#input-lastname"
    EMAIL_INPUT = By.CSS_SELECTOR, "#input-email"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    AGREEMENT_SWITCH = By.XPATH, "//*[@name='agree']"
    CONTINUE_BUTTON = By.CSS_SELECTOR, ".btn.btn-primary"
    TITLE = By.XPATH, "//h1"

    def open(self, url):
        with allure.step(f"Открываю {url + self.PATH}"):
            self.browser.get(url + self.PATH)

    @allure.step("Ввожу данные для регистрации")
    def input_data(self, firstname, lastname, email, password):
        self.input_value(self.FIRSTMANE_INPUT, firstname)
        self.input_value(self.LASTNAME_INPUT, lastname)
        self.input_value(self.EMAIL_INPUT, email)
        self.input_value(self.PASSWORD_INPUT, password)

    @allure.step("Подтверждаю соглашение")
    def confirm_agreement(self):
        self.get_element(self.AGREEMENT_SWITCH).click()

    @allure.step("Завершаб регистрацию нажатием на кнопку Continue")
    def complete_registration(self):
        self.get_element(self.CONTINUE_BUTTON).click()

    @allure.step("Получаю текст заголовка")
    def get_title_text(self):
        WebDriverWait(self.browser, 10).until(
        EC.url_contains("http://10.0.2.15:8081/en-gb?route=account/success&customer"))
        title = self.get_element(self.TITLE)
        title_text = title.text
        return title_text




