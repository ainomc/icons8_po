# -*- coding: utf-8 -*-

from selenium import webdriver
from logic.logic_base_page import LogBase
from locators.locators_iconpharm_page import LocIconPharm
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from context_base_page import ContextBase


class ContextIconPharm(ContextBase):
    """Context/Fixtures of IconPharm tests"""

    def setup_class(cls):
        """Actions before class tests"""
        # Profile settings
        cls.profile = FirefoxProfile()
        cls.profile.set_preference(
            "browser.download.folderList", 2)
        cls.profile.set_preference(
            "browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference(
            "browser.download.dir", ContextIconPharm.download_folder_path)
        cls.profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            '''application/x-msdos-program, application/octet-stream,
            image/png, image/svg+xml, application/postscript,
            text/plain, application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(ContextIconPharm.wait_time)

        # Open url
        cls.driver.get(ContextIconPharm.home_page_iconpharm)
        cls.driver.maximize_window()

        # Login
        cls.logBase = LogBase(cls.driver)
        cls.logBase.click_text('Login')
        cls.logBase.input_text_to_xpath(ContextIconPharm.login,
                                        LocIconPharm.email_field)
        cls.logBase.input_text_to_xpath(ContextIconPharm.password,
                                        LocIconPharm.password_field)
        cls.logBase.click_value('Login')

    def teardown_class(cls):
        """Actions after class tests"""
        # Close/quit driver
        cls.driver.quit()

    def setup(self):
        """Actions before tests"""
        # Open home page
        self.logBase.open_home_page(ContextIconPharm.home_page_iconpharm)

    def teardown(self):
        """Actions after tests"""
        pass
