# -*- coding: utf-8 -*-
import json
import os
from sys import platform
from selenium import webdriver
from logic.logic_base_page import LogBase
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

class ContextBase:

    path_to_download_folder = os.path.join(' ', 'download')
    path_to_test_folder = os.getcwd()
    download_folder_path = path_to_test_folder + path_to_download_folder[1:]

    my_data = json.loads(open("param.json").read())
    url = my_data['server']
    wait_time = int(my_data['time_for_wait'])
    home_page_iconpharm = my_data['server_iconpharm']
    home_page_sleeklogos = my_data['server_sleeklogos']
    login = my_data['login']
    password = my_data['password']

    def setup_class(cls):
        cls.profile = FirefoxProfile()
        cls.profile.set_preference("browser.download.folderList", 2)
        cls.profile.set_preference("browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference("browser.download.dir", ContextBase.download_folder_path)
        cls.profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   '''application/x-msdos-program, application/octet-stream,
                                   image/png, image/svg+xml, application/postscript,
                                   text/plain, application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(ContextBase.wait_time)
        cls.driver.get(ContextBase.url)
        cls.driver.maximize_window()
        cls.logBase = LogBase(cls.driver)

    def teardown_class(cls):
        cls.driver.close()

    def setup(self):
        self.logBase.open_home_page(ContextBase.url)

    def teardown(self):
        pass
