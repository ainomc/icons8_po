# -*- coding: utf-8 -*-

from locators_base_page import LocatorsBase


class LocIconsMobile(LocatorsBase):
    """Locotors for SleekLogos tests"""

    desktop_version_button = './/span[text()="Desktop version"]'

    open_main_menu = ".//*[@id='__layout']/div/div[1]/div[1]"
    iMessage_stickers = '//span[contains(text(), "iMessage Stickers")]'

    first_icon = './/*[@class="set-icons cf"]/a[1]'
    change_lang = './/*[@class="app-menu-language-icon"]'

    search_field = './/input[@class="auto-complete-input"]'
    search_button = './/*[@class="app-search-icon"]'

    desktop_version_locator = './/*[@class="c-grid-btns"][1]'

    icon_name = './/*[@class="content"]/a[@class="title"]'
    icon_name_in_icon_page = './/*[@class="app-page-section"]/h1[@ class="app-page-title"][1]'
    icon_subtitle = './/*[@class="app-icon icon-page-icon is-custom-size"]'
    icon_in_icon_page = './/*[@class="app-icon icon-page-icon is-custom-size"]'
    icon_page_download_bu = './/*[@class="actions button-group"]/div[1]'
    icon_page_generate_html = './/*[@class="actions button-group"]/div[2]'

    icon_page_tags_list = './/*[@class="icon-tags"]'
    collections = './/*[@class="app-right-sidebar-tabs"]/*[2]'
    blog_list = '//*[@class="feed js-grid"]'

    open_platform_list = './/*[@class="app-left-sidebar-toggle"]'

