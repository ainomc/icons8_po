# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from logic.logic_base_page import LogBase


my_data = json.loads(open("param.json").read())
url = my_data['server']

class ContextBase:

    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.logBase = LogBase(cls.driver)

    def teardown_class(cls):
        cls.driver.close()

    def setup(self):
        self.logBase.open_home_page(url)

    def teardown(self):
        pass
