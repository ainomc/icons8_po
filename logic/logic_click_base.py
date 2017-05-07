# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogClickBase(object):
    """Click logic of tests"""

    def __init__(self, driver):
        self.driver = driver

    def click_xpath(self, xpath):
        """Click xpath"""
        try:
            WebDriverWait(self.driver, 1)\
                .until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except:
            self.driver.find_element_by_xpath(xpath).click()

    def click_text(self, link):
        """Click text"""
        try:
            WebDriverWait(self.driver, 1)\
                .until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[text()="%s"]' % link))).click()
        except:
            self.driver.find_element_by_xpath('//*[text()="%s"]' % link).click()

    def click_text_part(self, text):
        """Click contains text """
        try:
            WebDriverWait(self.driver, 1).\
                until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[contains(text(), "%s")]' % text))).click()
        except:
            self.driver.find_element_by_xpath(
                '//*[contains(text(), "%s")]' % text).click()

    def try_click_text_part(self, text):
        """Try click text what have part of 'text', if not - pass"""
        try:
            self.driver.find_element_by_xpath(
                '//*[contains(text(), "%s")]' % text).click()
        except:
            pass

    def click_value(self, value):
        """Click xpath with value='value' """
        self.driver.find_element_by_xpath(
            './/*[@value="%s"]' % value).click()

    def elements_count(self, xpath):
        """Return count of xpath"""
        count = 0
        elements_number = 1
        while True:
            try:
                self.driver.find_element_by_xpath(xpath % elements_number)
                count += 1
                elements_number += 1
            except NoSuchElementException:
                break
        return count

    def click_all_and_confirm(self, click_all_xpath, confirm_xpath):
        """Click on the all xpath and click on the confirm """
        count = self.elements_count(click_all_xpath)
        while count > 0:
            self.driver.find_element_by_xpath(click_all_xpath % count).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(confirm_xpath).click()
            count -= 1
