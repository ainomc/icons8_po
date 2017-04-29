# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LogLocateBase(object):
    """Base logic"""

    def __init__(self, driver):
        self.driver = driver

    def locate_xpath(self, xpath):
        """Check locate of xpath"""
        self.driver.find_element_by_xpath(xpath)

    def absent_xpath(self, xpath):
        """Check absent of xpath"""
        try:
            WebDriverWait(self.driver, 4).until\
                (EC.visibility_of_element_located((By.XPATH, xpath)))
            assert False, 'Xpath present!!!'
        except TimeoutException:
            pass

    def displayed_xpath(self, xpath):
        """Check xpath displayed or not.
        Return True or False
        """
        return self.driver.find_element_by_xpath(xpath).is_displayed()

    def locate_text(self, text):
        """Check locate of text"""
        self.driver.find_element_by_xpath('//*[text()="%s"]' % text)

    def locate_text_part(self, text):
        """Check locate of contains text"""
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)
