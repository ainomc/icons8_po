# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LogLocateBase(object):

    def __init__(self, driver):
        self.driver = driver

    # Найти xpath
    def locate_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath)

    # Найти xpath
    def absent_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 4).until\
                (EC.visibility_of_element_located((By.XPATH, xpath)))
            assert False, 'Xpath present!!!'
        except TimeoutException:
            pass

    # Найти xpath и проверить видимость элемента. Возвращает True or False
    def displayed_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath).is_displayed()

    #  Найти видимиый текст что содержит в себе
    def locate_text(self, text):
        self.driver.find_element_by_xpath('//*[text()="%s"]' % text)

    # Найти видимиый текст что содержит в себе
    def locate_text_part(self, text):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
