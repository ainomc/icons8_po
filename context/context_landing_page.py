# -*- coding: utf-8 -*-

from context_base_page import ContextBase
from logic.logic_base_page import LogBase
from locators.locators_landing_page import LocLandind


class ContextLandingPage(ContextBase):
    """Context/fixtures of Landing page tests"""

    def setup(self):
        """Actions before tests"""
        # Open home page
        self.logBase.open_home_page(ContextBase.url)

        # Precondition actions
        self.logBase.click_xpath(LocLandind.first_result_icon)
        self.logBase.click_xpath(LocLandind.icon_name)

    def teardown(self):
        """Actions after tests"""
        pass