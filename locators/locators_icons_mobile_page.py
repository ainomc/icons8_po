# -*- coding: utf-8 -*-

from locators_base_page import LocatorsBase


class LocIconsMobile(LocatorsBase):
    """Locotors for SleekLogos tests"""

    desktop_version_button = './/span[text()="Desktop version"]'

    open_main_menu = './/*[@class="b-menu-toggle"]'
    iMessage_stickers = '//span[contains(text(), "iMessage Stickers")]'

    first_icon = './/*[@class="set-icons cf"]/a[1]'
    change_lang = './/*[@id="Ð¡Ð»Ð¾Ð¹_1"]'

    search_field = './/input[@ng-model="search.term"]'
    search_button = './/*[@class="icons-search__btn"]'

    desktop_version_locator = './/*[@class="c-grid-btns"][1]'

    icon_name = './/*[@class="c-pretty-link m-inline"]'
    icon_name_in_icon_page = './/*[@ng-bind="vm.pageTitle"]'
    icon_subtitle = './/*[@ng-bind-html="vm.mainSubtitleText"]'
    icon_in_icon_page = './/*[@ class="m-color-icon"]'
    icon_page_download_bu = './/button[@class="c-button red"]'
    icon_page_generate_html = '''.//*[@classes="'c-button white'"]'''
    icon_page_tab_list = './/*[@class="b-categories-tabs' \
                         ' c-tabs m-responsive m-narrow"]'
    icon_page_tags_list = './/*[@class="b-tags-list"]'
    collections = './/span[@class="b-tab m-active"]'

