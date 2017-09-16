# -*- coding: utf-8 -*-

import json
import random


class LocatorsBase(object):
    """Base locators"""

    platform_list = ['All', 'iOS 10', 'Windows 10', 'Windows 8', 'Material',
                     'Android 4', 'Color', 'Office']
    search_text_list = ['Google', 'Facebook', 'Icon', 'Game', 'Phone']
    search_text = random.choice(search_text_list)

    first_result_icon = './/div[@class="b-subcategory-wrapper"][1]' \
                        '/descendant::a[1]'
    another_first_result_icon = './/div[@class="b-subcategory-wrapper"][2]/' \
                                'descendant::a[1]'
