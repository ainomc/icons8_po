# -*- coding: utf-8 -*-

import json
import random

class LocatorsBase(object):
    """Base locators"""


    my_data = json.loads(open("param.json").read())
    login = my_data['login']
    password = my_data['password']
    home_page_sleeklogos = my_data['server_sleeklogos']
    home_page_iconpharm = my_data['server_iconpharm']
    home_page_icons_mobile= my_data["server_icons_mobile"]
    platform_list = ['All', 'iOS 10', 'Windows 10', 'Windows 8', 'Material',
                     'Android 4', 'Color', 'Office']
    search_text_list = ['Google', 'Facebook', 'Icon', 'Game', 'Phone']
    search_text = random.choice(search_text_list)

    first_result_icon = '//div[@class="b-subcategory-wrapper"][1]/descendant::a[1]'
