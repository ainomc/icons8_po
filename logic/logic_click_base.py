# -*- coding: utf-8 -*-
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogClickBase(object):

    def __init__(self, driver):
        self.driver = driver

    # Кликнуть на линк
    def click_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 1).until \
                (EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except:
            self.driver.find_element_by_xpath(xpath).click()

    # Кликнуть на линк
    def click_text(self, link):
        try:
            WebDriverWait(self.driver, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "%s")]' % link))).click()
        except:
            self.driver.find_element_by_xpath('//*[text()="%s"]' % link).click()

    # Кликнуть на линк
    def click_text_part(self, text):
        try:
            WebDriverWait(self.driver, 1).until \
                (EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "%s")]' % text))).click()
        except:
            self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text).click()

    # Кликнуть на линк
    def try_click_text_part(self, text):
        try:
            self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text).click()
        except:
            pass

    # Кликнуть на линк
    def click_value(self, value):
        self.driver.find_element_by_xpath('.//*[@value="%s"]' % value).click()

    # Возвращае колличество єлементов
    def elements_count(self, xpath):
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

    # Кликает на все найденные элементы и потом еще кликает на кнопку
    def click_all_and_confirm(self, click_all_xpath, confirm_xpath):
        count = self.elements_count(click_all_xpath)
        while count > 0:
            self.driver.find_element_by_xpath(click_all_xpath % count).click()
            time.sleep(3)
            self.driver.find_element_by_xpath(confirm_xpath).click()
            count -= 1

