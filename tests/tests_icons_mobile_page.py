# -*- coding: utf-8 -*-

import time
from context.context_icons_mobile_page import ContextIconsMobile
from locators.locators_icons_mobile_page import LocIconsMobile
from logic.logic_base_page import LogBase


class TestIconsMobile(ContextIconsMobile):
    """Tests of monile version of web-add
    https://demo.icons8.com/icons/
    """

    def test_main_menu_items(self):
        """Tests of main menu items"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.locate_text("Icons")
        self.logBase.locate_text("Request")
        self.logBase.locate_text("Buy")
        self.logBase.locate_text("Icon Search AI")
        self.logBase.locate_text("Blog")
        self.logBase.locate_text_part("Register")
        self.logBase.locate_text_part("Login")

    def test_menu_icons_button(self):
        """Tests of main menu icon button"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_text("Icons")
        self.logBase.locate_xpath(LocIconsMobile.desktop_version_locator)

    def test_menu_request_button(self):
        """Tests of main menu icon button"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_text("Request")
        self.logBase.locate_text("Request Icons")

    def test_menu_buy_button(self):
        """Tests of main menu icon button"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_text("Buy")
        self.logBase.locate_text("Free")

    def test_menu_imessage_button(self):
        """Tests of main menu icon button"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_xpath(LocIconsMobile.iMessage_stickers)

    def test_menu_ai_button(self):
        """Tests of main menu icon button"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        time.sleep(1)
        self.logBase.click_text("Icon Search AI")
        self.logBase.locate_text_part("Draw an icon")

    def test_menu_blog_button(self):
        """Tests of main menu icon button"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_text("Blog")
        self.logBase.locate_xpath(LocIconsMobile.blog_list)

    def test_menu_register_button(self):
        """Tests of main menu icon button"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.locate_text_part("Register")
        self.logBase.click_text_part("Register")
        self.logBase.locate_text("Register at Icons8")

    def test_menu_login_button(self):
        """Tests of main menu icon button"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.locate_text_part("Login")
        self.logBase.click_text_part("Login")
        self.logBase.locate_text_part("Forgot password?")

    def test_platforms(self):
        """Tests of main menu icon button"""
        for platform in LocIconsMobile.platform_list:
            self.logBase.locate_text(platform)

    def test_change_lang_popup(self):
        """Tests of change language pop-up"""
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_xpath(LocIconsMobile.change_lang)
        self.logBase.locate_text("    French ")

    def test_search(self):
        """Tests of search"""
        self.logBase.input_text_to_xpath(LocIconsMobile.search_text,
                                         LocIconsMobile.search_field)
        self.logBase.click_xpath(LocIconsMobile.search_button)
        self.logBase.locate_xpath(LocIconsMobile.first_result_icon)

    def test_icon_page(self):
        """Tests of icon page"""
        self.logBase.click_xpath(LocIconsMobile.first_result_icon)
        self.logBase.click_xpath(LocIconsMobile.icon_name)

        try:
            self.logBase.locate_text_part('Browse by tags')
        except:
            self.logBase.open_home_page(ContextIconsMobile.url)
            self.logBase.click_xpath(LocIconsMobile.another_first_result_icon)
            self.logBase.click_xpath(LocIconsMobile.icon_name)
            self.logBase.locate_text_part('Browse by tags')
        self.logBase.locate_xpath(LocIconsMobile.icon_name_in_icon_page)
        self.logBase.locate_xpath(LocIconsMobile.icon_subtitle)
        self.logBase.locate_xpath(LocIconsMobile.icon_page_download_bu)
        self.logBase.locate_xpath(LocIconsMobile.icon_in_icon_page)
        self.logBase.locate_xpath(LocIconsMobile.icon_page_generate_html)
        self.logBase.locate_xpath(LocIconsMobile.icon_page_tags_list)

    def test_right_menu_bar(self):
        """Tests of right menu bar"""
        self.logBase.click_xpath(LocIconsMobile.first_result_icon)
        self.logBase.locate_text('Download')
        self.logBase.locate_text('Generate HTML')
        self.logBase.click_xpath(LocIconsMobile.collections)
        self.logBase.locate_text('Download')
        self.logBase.locate_text('Get Font')
        self.logBase.locate_text('Get SVG Set')
