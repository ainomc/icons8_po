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
        self.driver.find_element_by_xpath(xpath).click()

    # Найти xpath
    def locate_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath)

    # Найти xpath и проверить видимость элемента. Возвращает True or False
    def displayed_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath).is_displayed()

    # Кликнуть на линк
    def click_text(self, link):
        self.driver.find_element_by_xpath('//*[text()="%s"]' % link).click()

    #  Найти видимиый текст что содержит в себе
    def locate_text(self, text):
        self.driver.find_element_by_xpath('//*[text()="%s"]' % text)

    # Кликнуть на линк
    def click_text_part(self, text):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text).click()

    # Кликнуть на линк
    def click_value(self, value):
        self.driver.find_element_by_xpath('.//*[@value="%s"]' % value).click()

    # Найти видимиый текст что содержит в себе
    def locate_text_part(self, text):
        self.driver.find_element_by_xpath('//*[contains(text(), "%s")]' % text)

    # Найти поле по xpath и ввести в него текст
    def input_text_to_xpath(self, text, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    # Then scroll to end of the page
    def open_home_page(self, url):
        self.driver.get(url)

    # Return current url
    def current_url(self):
        return self.driver.current_url

    # Генерирует рандомное имейл из 6 значений из списка и + '@gmail.com'
    def random_email(self):
        email = ''
        for x in range(6):
            email = email + random.choice(list('qwertyuiopasdfghjklzxcvbnm'))
        return email + '@gmail.com'

    # Генерирует рандомный текст
    def random_text(self, number_of_testItems):
        text = ''
        symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
        for x in range(number_of_testItems):
            text = text + \
                random.choice(
                    list(symbols))
        return text

