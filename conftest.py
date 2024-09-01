import os
import random
import time
import logging
import json

import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera", "safari", "yandex"])
    parser.addoption("--url", default="http://10.0.2.15:8081")
    parser.addoption("--executor", action="store", default="172.18.0.2")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--yadriver", action="store_true", default="*/yandexdriver")
    parser.addoption("--run", action="store", default="remote", choices=["local", "remote"])


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call':
        if rep.outcome != 'passed':
            item._failed = True
        else:
            item._failed = False


@pytest.fixture
def browser(request):
    run_type = request.config.getoption("--run")
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    mobile = request.config.getoption("--mobile")

    if run_type == "local":
        if browser_name == "yandex":
            options = ChromeOptions()
            if headless_mode:
                options.add_argument("headless=new")
            options.binary_location = "*/yandex.exe"
            service = ChromeService(executable_path=yadriver)
            driver = webdriver.Chrome(service=service, options=options)
        elif browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--no-sandbox")
            # options.add_argument('--disable-blink-features=AutomationControlled')
            # options.add_argument('--remote-debugging-port=9222')
            # options.add_argument("--disable-dev-shm-usage")
            # options.add_argument("--disable-gpu")
            if headless_mode:
                options.add_argument("headless=new")
            driver = webdriver.Chrome(service=ChromeService(), options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless_mode:
                options.add_argument("--headless")
            driver = webdriver.Firefox(service=FFService(), options=options)
        else:
            raise ValueError(f"Browser {browser_name} not supported locally")

    else:

        executor_url = f"http://{executor}:4444/wd/hub"

        if browser_name == "chrome":
            options = ChromeOptions()
            # options.add_argument("--no-sandbox")
            # options.add_argument("--disable-dev-shm-usage")
            # options.add_argument("--disable-gpu")
            # options.add_argument("--headless")
            # options.add_argument("--remote-debugging-port=9222")
        elif browser_name == "firefox":
            options = FirefoxOptions()
            # options.headless = True
        elif browser_name == "opera":
            options = ChromeOptions()
        elif browser_name == "safari":
            options = SafariOptions()
        else:
            raise ValueError(f"Browser {browser_name} not supported remotely")

        caps = {
            "browserName": browser_name,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "name": request.node.name,
            #     "screenResolution": "1280x2000",
                "enableVideo": video,
            #     "enableLog": logs,
            #     "timeZone": "Europe/Moscow",
            #     "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
            },
            # "acceptInsecureCerts": True,
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

        if not mobile:
            driver.maximize_window()

    driver.test_name = request.node.name
    driver.log_level = logging.DEBUG

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )

    driver.set_window_size(1920, 1080)

    def finalizer():
        if hasattr(request.node, "_failed") and request.node._failed:
            allure.attach(
                name="failure_screenshot",
                body=driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            allure.attach(
                name="page_source",
                body=driver.page_source,
                attachment_type=allure.attachment_type.HTML
            )
        driver.quit()

    request.addfinalizer(finalizer)
    return driver


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


