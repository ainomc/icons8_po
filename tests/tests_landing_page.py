# -*- coding: utf-8 -*-

from context.context_landing_page import ContextLandingPage
from locators.locators_landing_page import LocLandind


class TestLandingPage(ContextLandingPage):
    """ Tests of landing page (page of icon, what appear after
        when user clicked of the name of icon).
        """

    def test_landing_page_icon(self):
        """Tests locate of main element of icon page"""
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

    def test_landing_page_tag(self):
        """Tests tags in icon page"""
        self.logBase.locate_text_part('Browse by tags')
        self.logBase.click_xpath(LocLandind.tag)
        self.logBase.locate_text_part('Here we go with the icons related')
        self.logBase.click_xpath(LocLandind.icon_in_tag)
        self.logBase.locate_text_part('Browse by tags')

    def test_landing_page_category(self):
        """Tests category button in icon page
        For example: 'Free Icons › Web Icons › Arrows'
        If user click 'Arrows' must opened page with arrows categoryicons
        """
        self.logBase.locate_text_part('Browse by tags')
        self.logBase.click_xpath(LocLandind.icon_category)
        self.logBase.locate_xpath(LocLandind.icons_result)
        self.logBase.locate_xpath(LocLandind.icon_in_result)
        self.logBase.locate_xpath(LocLandind.category_title)
