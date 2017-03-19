# -*- coding: utf-8 -*-
import json
import os
from selenium import webdriver
from logic.logic_base_page import LogBase
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from sys import platform


my_data = json.loads(open("param.json").read())
url = my_data['server']
TIME_FOR_WAIT = int(my_data['time_for_wait'])

if "win" in platform:
    path_to_download_folder = os.path.join(' ', 'download')
    path_to_test_folder = os.getcwd()
    download_folder_path = path_to_test_folder + path_to_download_folder[1:]
elif "linux" in platform:
    download_folder_path = "$WORKSPACE/var/lib/jenkins/workspace/Icons8Selenium/download"
    print (download_folder_path + " << download_folder_path")

class ContextBase:

    def setup_class(cls):
        cls.profile = FirefoxProfile()
        cls.profile.set_preference("browser.download.folderList", 2)
        cls.profile.set_preference("browser.download.manager.showWhenStarting", False)
        cls.profile.set_preference("browser.download.dir", download_folder_path)
        cls.profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   '''application/x-msdos-program, application/octet-stream,
                                   image/png, image/svg+xml, application/postscript,
                                   text/plain, application/download, application/zip''')
        cls.driver = webdriver.Firefox(firefox_profile=cls.profile)
        cls.driver.implicitly_wait(TIME_FOR_WAIT)
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.logBase = LogBase(cls.driver)

    def teardown_class(cls):
        cls.driver.close()

    def setup(self):
        self.logBase.open_home_page(url)

    def teardown(self):
        pass
