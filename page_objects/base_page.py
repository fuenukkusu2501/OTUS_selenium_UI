import logging
import os
import selenium

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    def __init__(self, browser, wait=3):
        self.wait = WebDriverWait(browser, wait)
        self.browser = browser
        self.actions = ActionChains(browser)
        self.__config_logger()

    def __config_logger(self, to_file=False):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    def _open(self, url):
        self.logger.info(f"Open {url}")
        self.browser.get(url)

    def get_element(self, locator: tuple, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple):
        self.logger.info(f"Click {locator}")
        ActionChains(self.browser).move_to_element(self.get_elements(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for i in text:
            self.get_element(locator).send_keys(i)
