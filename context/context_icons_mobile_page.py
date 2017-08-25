# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from logic.logic_base_page import LogBase
from logic.logic_click_base import LogClickBase
from logic.logic_locate_base import LogLocateBase
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from context_base_page import ContextBase


class ContextIconsMobile(ContextBase):
    """Context/Fixtures of mobile version web-app tests"""

    def setup_class(cls):
        """Actions before test class"""
        # Driver profile
        cls.profile = FirefoxProfile()
        cls.profile.set_preference(
            "browser.download.folderList", 2)
        cls.profile.set_preference(
            "browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference(
            "browser.download.dir", ContextIconsMobile.download_folder_path)
        cls.profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            '''application/x-msdos-program, application/octet-stream,
            image/png, image/svg+xml, application/postscript,
            text/plain, application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(ContextIconsMobile.wait_time)

        # Open home page
        cls.driver.get(ContextBase.home_page_icons_mobile)
        cls.driver.set_window_size(750, 1334)

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
        try:
            time.sleep(1)
            self.base.open_home_page(ContextBase.home_page_icons_mobile)
        except:
            time.sleep(1)
            self.base.open_home_page(ContextBase.home_page_icons_mobile)
