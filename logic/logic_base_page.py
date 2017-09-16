# -*- coding: utf-8 -*-

import os
import random
import time
from selenium import webdriver
from os import listdir

# Read param.json with params
TIME_FOR_WAIT = 12

# Download folder
path_to_download_folder = os.path.join(' ', 'download')
path_to_test_folder = os.getcwd()
download_folder_path = path_to_test_folder + path_to_download_folder[1:]


class LogBase(object):
    """Base logic of tests"""

    def __init__(self, driver):
        self.driver = driver

    # Positive text for search
    positive_text = random.choice(['google', 'facebook', 'space',
                                   'ball', 'car', 'word'])

    def input_text_to_xpath(self, text, xpath):
        """Find field by xpath, clear and input text"""
        pass
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def open_home_page(self, url):
        """Open url"""
        self.driver.get(url)

    def current_url(self):
        """Return current url"""
        return self.driver.current_url

    def random_email(self):
        """Return +random email, like ______@gmail.com"""
        email = ''
        for x in range(6):
            email = email + random.choice(list('qwertyuiopasdfghjklzxcvbnm'))
        return email + '@gmail.com'

    def random_text(self, items_number):
        """Generate and return random text with amount of 'items_number' """
        text = ''
        symbols = 'qwertyuiopasdfghjklzxcvbnm' \
                  'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
        for x in range(items_number):
            text = text + \
                random.choice(
                    list(symbols))
        return text

    def move_mouse(self, xpath):
        """Move mouse on the xpath"""
        element = self.driver.find_element_by_xpath(xpath)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def del_by_extension(self, extension):
        """Del all files in folder with extension"""
        list_of_all_files = listdir(download_folder_path)
        elements_count = 0
        for item in list_of_all_files:
            if item.endswith(extension):
                elements_count += 1
                os.remove(os.path.join(download_folder_path, item))
        assert elements_count > 0

    def wait_presents_file(self, extension):
        """Wait presents of file with 'extension' """
        loop = True
        loop_timer = 0
        while loop is True:
            time.sleep(1)
            loop_timer += 1
            for item in listdir(download_folder_path):
                if item.endswith(extension):
                    loop = False
                    break
                else:
                    pass
            assert loop_timer != 15
