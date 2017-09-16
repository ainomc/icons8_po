# -*- coding: utf-8 -*-

import pytest
from locators.locators_landing_page import LocLandind
# python -m pytest -v tests/tests_landing_page.py -s -l


@pytest.mark.usefixtures("driver_landing", "base", "click", "locate")
class TestLandingPage(object):
    """ Tests of landing page (page of icon, what appear after
        when user clicked of the name of icon).
        """

    def test_landing_page_icon(self, landing_pre, click, locate):
        """Tests locate of main element of icon page"""

        locate.locate_xpath(LocLandind.icon_category)
        locate.locate_xpath(LocLandind.icon_text)
        locate.locate_xpath(LocLandind.icon)
        locate.locate_xpath(LocLandind.download_button)
        locate.locate_text_part('Generate HTML')
        click.click_xpath(LocLandind.choose_PNG_size)
        locate.locate_xpath(LocLandind.icon_download_sizes)
        locate.locate_xpath(LocLandind.icon_download_format)
        locate.locate_text_part('Download multiple sizes')
        locate.locate_text_part('Browse by tags')

    def test_landing_page_tag(self, landing_pre, click, locate):
        """Tests tags in icon page"""
        locate.locate_text_part('Browse by tags')
        click.click_xpath(LocLandind.tag)
        locate.locate_text_part('Here we go with the icons related')
        locate.locate_xpath(LocLandind.icon_in_tag)

    def test_landing_page_category(self, landing_pre, click, locate):
        """Tests category button in icon page
        For example: 'Free Icons › Web Icons › Arrows'
        If user click 'Arrows' must opened page with arrows categoryicons
        """
        locate.locate_text_part('Browse by tags')
        click.click_xpath(LocLandind.icon_category)
        locate.locate_xpath(LocLandind.icons_result)
        locate.locate_xpath(LocLandind.icon_in_result)
        locate.locate_xpath(LocLandind.category_title)
