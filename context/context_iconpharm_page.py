# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from logic.logic_base_page import LogBase
from locators.locators_iconpharm_page import LocIconPharm
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from context_base_page import ContextBase

class ContextIconPharm(ContextBase):

    def setup_class(cls):
        cls.profile = FirefoxProfile()
        cls.profile.set_preference("browser.download.folderList", 2)
        cls.profile.set_preference("browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference("browser.download.dir", ContextIconPharm.download_folder_path)
        cls.profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   '''application/x-msdos-program, application/octet-stream,
                                   image/png, image/svg+xml, application/postscript,
                                   text/plain, application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(ContextIconPharm.wait_time)
        cls.driver.get(ContextIconPharm.home_page_iconpharm)
        cls.driver.maximize_window()
        cls.logBase = LogBase(cls.driver)
        cls.logBase.click_text('Login')
        cls.logBase.input_text_to_xpath(ContextIconPharm.login, LocIconPharm.email_field)
        cls.logBase.input_text_to_xpath(ContextIconPharm.password, LocIconPharm.password_field)
        cls.logBase.click_value('Login')

    def teardown_class(cls):
        cls.driver.close()

    def setup(self):
        self.logBase.open_home_page(ContextIconPharm.home_page_iconpharm)

    def teardown(self):
        pass
