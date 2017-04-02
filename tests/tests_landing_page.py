# -*- coding: utf-8 -*-
from context.context_base_page import ContextBase
from logic.logic_base_page import LogBase
from locators.locators_landing_page import LocLandind

class TestLandingPage(ContextBase):


    # landing page icon
    def test_landingPageIcon(self):
        self.logBase.input_text_to_xpath(LogBase.positive_text, LocLandind.search_field)
        self.logBase.click_xpath(LocLandind.search_button)
        self.logBase.click_xpath(LocLandind.first_result_icon)
        self.logBase.click_xpath(LocLandind.icon_name)
        self.logBase.locate_xpath(LocLandind.icon_category)
        self.logBase.locate_xpath(LocLandind.icon_text)
        self.logBase.locate_xpath(LocLandind.icon)
        self.logBase.locate_xpath(LocLandind.download_button)
        self.logBase.locate_text_part('Generate HTML')
        self.logBase.click_xpath(LocLandind.choose_PNG_size)
        self.logBase.locate_xpath(LocLandind.icon_download_sizes)
        self.logBase.locate_xpath(LocLandind.icon_download_format)
        self.logBase.locate_text_part('Download multiple sizes')
        self.logBase.locate_text_part('Browse by tags')

    # landing page tag
    def test_landingPageTag(self):
        self.logBase.input_text_to_xpath(LogBase.positive_text, LocLandind.search_field)
        self.logBase.click_xpath(LocLandind.search_button)
        self.logBase.click_xpath(LocLandind.first_result_icon)
        self.logBase.click_xpath(LocLandind.icon_name)
        self.logBase.locate_text_part('Browse by tags')
        self.logBase.click_xpath(LocLandind.tag)
        self.logBase.locate_text_part('This page contains')
        self.logBase.click_xpath(LocLandind.icon_in_tag)
        self.logBase.locate_text_part('Browse by tags')

    # landing page category
    def test_landingPageCategory(self):
        self.logBase.input_text_to_xpath(LogBase.positive_text, LocLandind.search_field)
        self.logBase.click_xpath(LocLandind.search_button)
        self.logBase.click_xpath(LocLandind.first_result_icon)
        self.logBase.click_xpath(LocLandind.icon_name)
        self.logBase.locate_text_part('Browse by tags')
        self.logBase.click_xpath(LocLandind.icon_category)
        self.logBase.locate_xpath(LocLandind.icons_result)
        self.logBase.locate_xpath(LocLandind.icon_in_result)
        self.logBase.locate_xpath(LocLandind.category_title)
