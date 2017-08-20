# -*- coding: utf-8 -*-

from context_base_page import ContextBase
from locators.locators_landing_page import LocLandind


class ContextLandingPage(ContextBase):
    """Context/fixtures of Landing page tests"""

    def setup(self):
        """Actions before tests"""
        # Open home page
        self.base.open_home_page(ContextBase.url)

        # Precondition actions
        self.click.click_xpath(LocLandind.first_result_icon)
        self.click.click_xpath(LocLandind.icon_name)

        try:
            self.locate.locate_text_part('Browse by tags')
        except:
            self.base.open_home_page(ContextBase.url)
            self.click.click_xpath(LocLandind.another_first_result_icon)
            self.click.click_xpath(LocLandind.icon_name)
            self.locate.locate_text_part('Browse by tags')