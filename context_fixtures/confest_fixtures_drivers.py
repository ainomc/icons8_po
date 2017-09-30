# -*- coding: utf-8 -*-
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


# Path to download folder
path_to_download_folder = os.path.join(' ', 'download')
path_to_test_folder = os.getcwd()
download_folder_path = path_to_test_folder + path_to_download_folder[1:]


def make_driver(url):
    """Create driver with profile parameters"""
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


@pytest.fixture(scope="class")
def driver_landing(request):
    """Create and return landing page test driver"""
    url = request.config.getoption("--landing_url")
    global browser
    browser = make_driver(url)
    return browser


@pytest.fixture(scope="class")
def driver_icon8_mobile(request):
    """Create and return icon8 mobile page test driver"""
    url = request.config.getoption("--icon8_mobile_url")
    global browser
    browser = make_driver(url)
    browser.set_window_size(750, 1334)
    return browser


@pytest.fixture(scope="class")
def driver_sleeklogos(request):
    """Create and return sleeklogos page test driver"""
    url = request.config.getoption("--sleeklogos_url")
    global browser
    browser = make_driver(url)
    return browser


@pytest.fixture(scope="class")
def driver_iconpharm(request):
    """Create and return iconpharm page test driver"""
    url = request.config.getoption("--iconpharm_url")
    # make_driver(url)
    global browser
    browser = make_driver(url)
    return browser


@pytest.fixture(scope="class", autouse=True)
def teardown_cls_quit_driver():
    """Close browser and quit driver"""
    yield teardown_cls_quit_driver
    browser = current_browser()
    browser.quit()


def current_browser():
    """Return current driver"""
    global browser
    return browser