import pytest
import logging
import allure
import json
import os
from pytest import fixture

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="ch", choices=["ya", "ch", "ff"]
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--yadriver", action="store_true", default="*/yandexdriver"
    )
    parser.addoption(
        "--url", default="http://10.0.2.15:8081"
    )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")

    if browser_name == "ya":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        options.binary_location = "*/yandex.exe"
        service = Service(executable_path=yadriver)
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "ch":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        browser = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
        browser = webdriver.Firefox(service=FFService(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    browser.set_window_size(1920, 1080)
    # так же можно использовать browser.maximize_window()

    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON)

    browser.test_name = request.node.name
    browser.log_level = logging.DEBUG

    yield browser

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=browser.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
        allure.attach(
            name="page_source",
            body=browser.page_source,
            attachment_type=allure.attachment_type.HTML
        )

    browser.close()


@pytest.fixture
def base_url(request):
    url = request.config.getoption('--url')
    return url


