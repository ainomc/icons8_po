# -*- coding: utf-8 -*-
import os
import random
import json
import time
from selenium import webdriver
from os import listdir

from logic_click_base import LogClickBase
from logic_locate_base import LogLocateBase

my_data = json.loads(open("param.json").read())
url = my_data['server']
TIME_FOR_WAIT = int(my_data['time_for_wait'])

path_to_download_folder = os.path.join(' ', 'download')
path_to_test_folder = os.getcwd()
download_folder_path = path_to_test_folder + path_to_download_folder[1:]

class LogBase(LogClickBase, LogLocateBase):

    positive_text = random.choice(['google', 'facebook', 'space', 'ball', 'car', 'word'])

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

    # Перемещает мышь та элемент
    def move_mouse(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    # Удаляет все файлы с окончание или расширением (extension)
    def del_by_extension(self, extension):
        list_of_all_files = listdir(download_folder_path)
        #print(str(list_of_all_files) + " << all files")
        elements_count = 0
        for item in list_of_all_files:
            if item.endswith(extension):
                elements_count += 1
                os.remove(os.path.join(download_folder_path, item))
        assert elements_count > 0

    # Ждёт пока не появиться файл
    def wait_presents_file(self, extension):
        loop = True
        loop_timer = 0
        while loop == True:
            time.sleep(1)
            loop_timer += 1
            for item in listdir(download_folder_path):
                if item.endswith(extension):
                    loop = False
                    break
                else:
                    pass
            assert loop_timer != 15



