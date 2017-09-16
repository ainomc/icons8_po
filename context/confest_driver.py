# -*- coding: utf-8 -*-
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from logic.logic_base_page import LogBase
from logic.logic_click_base import LogClickBase
from locators.locators_sleeklogos_page import LocSleekLogos
from locators.locators_iconpharm_page import LocIconPharm

# Path to download folder
path_to_download_folder = os.path.join(' ', 'download')
path_to_test_folder = os.getcwd()
download_folder_path = path_to_test_folder + path_to_download_folder[1:]


def make_driver(url):
    profile = FirefoxProfile()
    profile.set_preference(
        "browser.download.folderList", 2)
    profile.set_preference(
        "browser.download.manager.showWhenStarting", False)
    profile.set_preference(
        "browser.download.dir", download_folder_path)
    profile.set_preference(
        "browser.helperApps.neverAsk.saveToDisk",
        '''application/x-msdos-program, application/octet-stream,
        image/png, image/svg+xml, application/postscript,
        text/plain, application/download, application/zip''')
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(url)
    driver.implicitly_wait(12)
    driver.maximize_window()
    return driver


# Page Driver
@pytest.fixture(scope="class")
def driver_landing(request):
    url = request.config.getoption("--landing_url")
    global browser
    browser = make_driver(url)
    return browser


@pytest.fixture(scope="class")
def driver_icon8_mobile(request):
    url = request.config.getoption("--icon8_mobile_url")
    global browser
    browser = make_driver(url)
    browser.set_window_size(750, 1334)
    return browser


@pytest.fixture(scope="class")
def driver_sleeklogos(request):
    url = request.config.getoption("--sleeklogos_url")
    global browser
    browser = make_driver(url)

    base = LogBase(browser)
    click = LogClickBase(browser)
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")

    click.click_text('Login')
    base.input_text_to_xpath(login, LocSleekLogos.email_field)
    base.input_text_to_xpath(password, LocSleekLogos.password_field)
    click.click_value('Login')

    return browser


@pytest.fixture(scope="class")
def driver_iconpharm(request):
    url = request.config.getoption("--iconpharm_url")
    # make_driver(url)
    global browser
    browser = make_driver(url)

    url = request.config.getoption("--iconpharm_url")
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    base = LogBase(browser)
    click = LogClickBase(browser)

    base.open_home_page(url)

    click.click_text('Login')
    base.input_text_to_xpath(login, LocIconPharm.email_field)
    base.input_text_to_xpath(password, LocIconPharm.password_field)
    click.click_value('Login')

    return browser


def browser_x():
    global browser
    return browser
