# -*- coding: utf-8 -*-
import random
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

my_data = json.loads(open("param.json").read())
url = my_data['server']
TIME_FOR_WAIT = int(my_data['time_for_wait'])

class LogBase(object):

    def __init__(self, driver):
        self.driver = driver

    positive_text = random.choice(['google', 'facebook', 'space', 'ball', 'car', 'word'])

    # Кликнуть на линк
    def click_xpath(self, xpath):
        WebDriverWait(self.driver, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        while True:
            try:
                self.driver.find_element_by_xpath(xpath).click()
                break
            except StaleElementReferenceException:
                continue

    # Найти видимиый xpath
    def locate_xpath(self, xpath):
        WebDriverWait(self.driver, TIME_FOR_WAIT).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        assert self.driver.find_element_by_xpath(xpath)

    # Кликнуть на линк
    def click_text(self, link):
        WebDriverWait(self.driver, TIME_FOR_WAIT).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="%s"]' % link)))
        while True:
            try:
                self.driver.find_element_by_xpath('//*[text()="%s"]' % link).click()
                break
            except StaleElementReferenceException:
                continue

    # Найти видимиый текст что содержит в себе
    def locate_text_part(self, text, time_for_search=TIME_FOR_WAIT):
        WebDriverWait(self.driver, time_for_search).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
        )
        assert self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)

    # Найти поле по xpath и ввести в него текст
    def input_text_to_xpath(self, text, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    # Then scroll to end of the page
    def open_home_page(self, url):
        self.driver.get(url)
