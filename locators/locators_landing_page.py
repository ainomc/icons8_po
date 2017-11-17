# -*- coding: utf-8 -*-

import random
from locators_base_page import LocatorsBase


class LocLandind(LocatorsBase):
    """Locators for Landing page"""

    field = '//*[@placeholder="%s"]'
    search_field = field % 'search'
    search_button = '//*[@class="b-search-btn"]'
    icon_name = './/*[@class="content"]/a[@class="title"]'
    icon_category = './/a[@href="/icon/new-icons/all"]'
    icon_text = './/*[@class="app-page-section is-underline"][1]'
    icon = './/*[@class="app-icon icon-page-icon is-custom-size"]'
    download_button = './/*[@class="actions button-group"]/*[1]'
    choose_PNG_size = './/*[@class="app-popup popup"]'
    icon_download_sizes = './/*[@ class="format"]/div/div[%s]' \
                          % random.randint(1, 4)
    icon_download_format = './/*[@class="size"]/div/div[%s]' \
                           % random.randint(1, 4)

    tag = './/*[@class="app-tabs-header"]/div[1]'
    icon_in_tag = './/*[@class="set"]/a[1]'
    icons_result = './/div[@class="icon-grid"][1]/div/a[%s]' \
                   % random.randint(1, 5)