# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from logic.logic_base_page import LogBase
from locators.locators_sleeklogos_page import LocSleekLogos
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from context_base_page import ContextBase

class ContextSleekLogos(ContextBase):

    def setup_class(cls):
        cls.profile = FirefoxProfile()
        cls.profile.set_preference("browser.download.folderList", 2)
        cls.profile.set_preference("browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference("browser.download.dir", ContextSleekLogos.download_folder_path)
        cls.profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   '''application/x-msdos-program, application/octet-stream,
                                   image/png, image/svg+xml, application/postscript, application/eps,
                                   application/x-eps, image/eps, image/x-eps, text/plain,
                                   application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(ContextSleekLogos.wait_time)
        cls.driver.get(ContextSleekLogos.home_page_sleeklogos)
        cls.driver.maximize_window()
        cls.logBase = LogBase(cls.driver)
        cls.logBase.click_text('Login')
        cls.logBase.input_text_to_xpath(ContextSleekLogos.login, LocSleekLogos.email_field)
        cls.logBase.input_text_to_xpath(ContextSleekLogos.password, LocSleekLogos.password_field)
        cls.logBase.click_value('Login')

    def teardown_class(cls):
        cls.driver.quit()

    def setup(self):
        self.logBase.open_home_page(ContextSleekLogos.home_page_sleeklogos)

    def teardown(self):
        pass
