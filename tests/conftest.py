# -*- coding: utf-8 -*-
import os
import time
import pytest

from locators.locators_landing_page import LocLandind
from logic.logic_base_page import LogBase
from logic.logic_click_base import LogClickBase
from logic.logic_locate_base import LogLocateBase

from context.confest_driver import *
from context.confest_parameters import *

wait_time = 12
# Path to download folder
path_to_download_folder = os.path.join(' ', 'download')
path_to_test_folder = os.getcwd()
download_folder_path = path_to_test_folder + path_to_download_folder[1:]


# Logic
@pytest.fixture(scope="class")
def click(request):
    browser = browser_x()
    click_cls = LogClickBase(browser)
    return click_cls


@pytest.fixture(scope="class")
def base(request):
    browser = browser_x()
    base_cls = LogBase(browser)
    return base_cls


@pytest.fixture(scope="class")
def locate(request):
    browser = browser_x()
    locate_cls = LogLocateBase(browser)
    return locate_cls


# Preconditions
@pytest.fixture()
def landing_pre(request):
    """Actions before tests"""
    # Open home page
    browser = browser_x()
    url = request.config.getoption("--landing_url")

    base = LogBase(browser)
    click = LogClickBase(browser)
    locate = LogLocateBase(browser)

    base.open_home_page(url)

    # Precondition actions
    click.click_xpath(LocLandind.first_result_icon)
    click.click_xpath(LocLandind.icon_name)

    try:
        locate.locate_text_part('Browse by tags')
    except:
        base.open_home_page(url)
        click.click_xpath(LocLandind.another_first_result_icon)
        click.click_xpath(LocLandind.icon_name)
        locate.locate_text_part('Browse by tags')


@pytest.fixture()
def sleeklogos_pre(request):
    """Actions before tests"""
    # Open home page
    browser = browser_x()
    url = request.config.getoption("--sleeklogos_url")

    base = LogBase(browser)
    base.open_home_page(url)


@pytest.fixture()
def iconpharm_pre(request):
    """Actions before tests"""
    # Open home page
    browser = browser_x()
    url = request.config.getoption("--iconpharm_url")

    base = LogBase(browser)
    base.open_home_page(url)


@pytest.fixture()
def mobile_pre(request):
    """Actions before tests"""
    # Open home page
    browser = browser_x()
    url = request.config.getoption("--icon8_mobile_url")
    try:
        time.sleep(1)
        browser.get(url)
    except:
        time.sleep(1)
        browser.get(url)


@pytest.fixture(scope="class", autouse=True)
def quit_driver():
    yield quit_driver
    browser = browser_x()
    browser.quit()

