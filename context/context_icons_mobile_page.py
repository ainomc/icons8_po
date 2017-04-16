# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from logic.logic_base_page import LogBase
from locators.locators_icons_mobile_page import LocIconsMobile
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from context_base_page import ContextBase

class ContextIconsMobile(ContextBase):

    def setup_class(cls):
        cls.profile = FirefoxProfile()
        cls.profile.set_preference("browser.download.folderList", 2)
        cls.profile.set_preference("browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference("browser.download.dir", ContextIconsMobile.download_folder_path)
        cls.profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   '''application/x-msdos-program, application/octet-stream,
                                   image/png, image/svg+xml, application/postscript, application/eps,
                                   application/x-eps, image/eps, image/x-eps, text/plain,
                                   application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(ContextIconsMobile.wait_time)
        cls.driver.get(ContextBase.home_page_icons_mobile)
        cls.driver.set_window_size(750, 1334)
        cls.logBase = LogBase(cls.driver)

    def teardown_class(cls):
        cls.driver.quit()

    def setup(self):
        self.logBase.open_home_page(ContextBase.home_page_icons_mobile)

    def teardown(self):
        pass
