# -*- coding: utf-8 -*-
import time
from context.context_sleeklogos_page import ContextSleekLogos
from logic.logic_base_page import LogBase
from locators.locators_sleeklogos_page import LocSleekLogos

class TestSleekLogos(ContextSleekLogos):
    # Presents of all platforms and platforms resuilt
    def test_platforms(self):
        for platform in LocSleekLogos.platform_list:
            self.logBase.click_text(platform)
            self.logBase.locate_xpath(LocSleekLogos.platform_search_name % platform)
            self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)

    # Presents of all categories and category resuilt
    def test_category(self):
        for category_num in range(1, 28):
            self.logBase.click_xpath(LocSleekLogos.category_list % category_num)
            self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)

    # Input search and presents search resuilt
    def test_search_icons(self):
        self.logBase.input_text_to_xpath(LocSleekLogos.search_text, LocSleekLogos.search_field)
        self.logBase.click_xpath(LocSleekLogos.search_button)
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)

    # Tests grid nolabel
    def test_grid_nolabel(self):
        self.logBase.click_xpath(LocSleekLogos.grid_nolabel)
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)
        assert self.logBase.displayed_xpath(LocSleekLogos.label) == False

    # Tests grid label
    def test_grid_label(self):
        self.logBase.click_xpath(LocSleekLogos.grid_label)
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)
        assert self.logBase.displayed_xpath(LocSleekLogos.label) == True

    # Click and check 'More icons' button
    def tests_more_icons_button(self):
        self.logBase.click_xpath(LocSleekLogos.grid_label)
        self.logBase.click_text('More Icons')
        assert 'icons8.com' in self.logBase.current_url()

    """
    # 'My account' information
    def tests_more_icons_button(self):
        self.logBase.click_text('My Account')
        self.logBase.locate_text('Account')
        self.logBase.locate_text(ContextSleekLogos.login)
    """














