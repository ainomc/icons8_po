# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from logic.logic_base_page import LogBase
from locators.locators_sleeklogos_page import LocSleekLogos

my_data = json.loads(open("param.json").read())
home_page = my_data['server_sleeklogos']
login = my_data['login']
password = my_data['password']
TIME_FOR_WAIT = int(my_data['time_for_wait'])

class ContextSleekLogos:

    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(TIME_FOR_WAIT)
        cls.driver.get(home_page)
        cls.driver.maximize_window()
        cls.logBase = LogBase(cls.driver)
        cls.logBase.click_text('Login')
        cls.logBase.input_text_to_xpath(login, LocSleekLogos.email_field)
        cls.logBase.input_text_to_xpath(password, LocSleekLogos.password_field)
        cls.logBase.click_xpath(LocSleekLogos.login_submit)

    def teardown_class(cls):
        cls.driver.close()

    def setup(self):
        self.logBase.open_home_page(home_page)

    def teardown(self):
        pass
