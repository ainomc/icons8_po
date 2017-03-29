# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from logic.logic_base_page import LogBase
from locators.locators_sleeklogos_page import LocSleekLogos
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

my_data = json.loads(open("param.json").read())
home_page = my_data['server_sleeklogos']
login = my_data['login']
password = my_data['password']
TIME_FOR_WAIT = int(my_data['time_for_wait'])

class ContextSleekLogos:

    def setup_class(cls):
        cls.profile = FirefoxProfile()
        cls.profile.set_preference("browser.download.folderList", 2)
        cls.profile.set_preference("browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference("browser.download.dir", ContextSleekLogos.download_folder_path)
        cls.profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   '''application/x-msdos-program, application/octet-stream,
                                   image/png, image/svg+xml, application/postscript,
                                   text/plain, application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(TIME_FOR_WAIT)
        cls.driver.get(home_page)
        cls.driver.maximize_window()
        cls.logBase = LogBase(cls.driver)
        cls.logBase.click_text('Login')
        cls.logBase.input_text_to_xpath(login, LocSleekLogos.email_field)
        cls.logBase.input_text_to_xpath(password, LocSleekLogos.password_field)
        cls.logBase.click_value('Login')

    def teardown_class(cls):
        cls.driver.close()

    def setup(self):
        self.logBase.open_home_page(home_page)

    def teardown(self):
        pass
