# -*- coding: utf-8 -*-
import time
import random
from context.context_icons_mobile_page import ContextIconsMobile
from locators.locators_icons_mobile_page import LocIconsMobile

class TestIconsMobile(ContextIconsMobile):

    # Check desktop version button
    def test_desktop_version_button(self):
        self.logBase.click_xpath(LocIconsMobile.desktop_version_button)
        self.logBase.locate_xpath(LocIconsMobile.desktop_version_locator)

    def test_main_menu_items(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.locate_text("Icons")
        self.logBase.locate_text("Request")
        self.logBase.locate_text("Buy")
        self.logBase.locate_text("Icon Search AI")
        self.logBase.locate_text("Blog")
        self.logBase.locate_text_part("Register")
        self.logBase.locate_text_part("Login")

    def test_menu_icons_button(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_text("Icons")
        self.logBase.locate_xpath(LocIconsMobile.desktop_version_locator)

    def test_menu_request_button(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_text("Request")
        self.logBase.locate_text("Request Icons")

    def test_menu_buy_button(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_text("Buy")
        self.logBase.locate_text("Free")

    def test_menu_iMessage_button(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_xpath(LocIconsMobile.iMessage_stickers)

    def test_menu_AI_button(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        time.sleep(1)
        self.logBase.click_text("Icon Search AI")
        self.logBase.locate_text_part("Draw an icon")

    def test_menu_blog_button(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_text("Blog")
        self.logBase.locate_text("Subscribe")

    def test_menu_register_button(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.locate_text_part("Register")
        self.logBase.click_text_part("Register")
        self.logBase.locate_text("Register at Icons8")

    def test_menu_login_button(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.locate_text_part("Login")
        self.logBase.click_text_part("Login")
        self.logBase.locate_text_part("Forgot password?")

    def test_change_lang_popup(self):
        self.logBase.click_xpath(LocIconsMobile.open_main_menu)
        self.logBase.click_xpath(LocIconsMobile.change_lang)
        self.logBase.locate_text("    French ")

    def test_latest_icons(self):
        self.logBase.locate_text_part("Latest Icons")
        self.logBase.click_xpath(LocIconsMobile.first_icon)

    def test_search_hide(self):
        self.logBase.locate_xpath(LocIconsMobile.search_field)
        self.logBase.click_xpath(LocIconsMobile.search_hide)
        self.logBase.absent_xpath(LocIconsMobile.search_field)
        self.logBase.click_xpath(LocIconsMobile.search_hide)
        self.logBase.locate_xpath(LocIconsMobile.search_field)

    def test_platforms(self):
        for platform in LocIconsMobile.platform_list:
            self.logBase.locate_text(platform)

    def test_search(self):
        self.logBase.input_text_to_xpath(random.choice(LocIconsMobile.search_text_list),
                                         LocIconsMobile.search_field)
        self.logBase.click_xpath(LocIconsMobile.search_button)
        self.logBase.locate_xpath(LocIconsMobile.first_search_resuilt)






































