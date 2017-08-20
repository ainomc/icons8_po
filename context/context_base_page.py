# -*- coding: utf-8 -*-

import json
import os
# import pytest
# import allure
# from allure import attach, attach_type
from selenium import webdriver
from logic.logic_base_page import LogBase
from logic.logic_click_base import LogClickBase
from logic.logic_locate_base import LogLocateBase
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


class ContextBase(object):
    """Base Context/Fixtures"""

    # Path to download folder
    path_to_download_folder = os.path.join(' ', 'download')
    path_to_test_folder = os.getcwd()
    download_folder_path = path_to_test_folder + path_to_download_folder[1:]

    # Read param.json with tests parameters
    my_data = json.loads(open("param.json").read())
    url = my_data['server']
    wait_time = int(my_data['time_for_wait'])
    home_page_iconpharm = my_data['server_iconpharm']
    home_page_sleeklogos = my_data['server_sleeklogos']
    home_page_icons_mobile = my_data['server_icons_mobile']
    login = my_data['login']
    password = my_data['password']

    def setup_class(cls):
        """Actions before tests"""
        # Driver profile
        cls.profile = FirefoxProfile()
        cls.profile.set_preference(
            "browser.download.folderList", 2)
        cls.profile.set_preference(
            "browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference(
            "browser.download.dir", ContextBase.download_folder_path)
        cls.profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            '''application/x-msdos-program, application/octet-stream,
            image/png, image/svg+xml, application/postscript,
            text/plain, application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(ContextBase.wait_time)

        # Open icon8 home page url
        cls.driver.get(ContextBase.url)
        cls.driver.maximize_window()
        cls.base = LogBase(cls.driver)
        cls.click = LogClickBase(cls.driver)
        cls.locate = LogLocateBase(cls.driver)

    def teardown_class(cls):
        """Actions after test class"""
        # Close/quit driver
        cls.driver.quit()

    def setup(self):
        """Actions before each test"""
        # Open home page
        self.base.open_home_page(ContextBase.url)
    '''
    def teardown(self):
        """Actions after each tests"""
        attach('screenshot', self.driver.get_screenshot_as_png(), type=attach_type.PNG)
    '''