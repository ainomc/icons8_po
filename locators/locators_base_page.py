# -*- coding: utf-8 -*-

import json
import random


class LocatorsBase(object):
    """Base locators"""

    platform_list = ['All', 'iOS', 'Windows 10', 'iOS Glyphs', 'Material',
                     'Office', 'Nolan']
    search_text_list = ['Google', 'Facebook', 'Icon', 'Game', 'Phone']
    search_text = random.choice(search_text_list)

    first_result_icon = './/div[@class="icon-grid"][1]/div/a[1]'
    another_first_result_icon = './/div[@class="b-subcategory-wrapper"][2]/' \
                                'descendant::a[1]'
