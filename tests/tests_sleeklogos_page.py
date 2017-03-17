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

    # 'My account' information
    def tests_more_icons_button(self):
        self.logBase.click_text_part('My Account')
        self.logBase.locate_text('Account')
        self.logBase.locate_text(LocSleekLogos.login)
        #self.logBase.locate_text(ContextSleekLogos.login)

    # Check change email or password
    def tests_change_email_or_password(self):
        self.logBase.click_text_part('My Account')
        self.logBase.click_text_part('change email or password')
        self.logBase.locate_text_part('username')
        self.logBase.locate_text_part('new password')
        self.logBase.click_value('Save Profile')

    # Check login
    def tests_login(self):
        self.logBase.click_xpath(LocSleekLogos.logout)
        self.logBase.open_home_page(LocSleekLogos.home_page)
        self.logBase.click_xpath(LocSleekLogos.login_button)
        self.logBase.locate_text_part('Login to SleekLogos')
        self.logBase.locate_text('email')
        self.logBase.locate_text('password')
        self.logBase.locate_text_part('Forgot password?')
        self.logBase.locate_xpath(LocSleekLogos.show_pass)
        self.logBase.input_text_to_xpath(LocSleekLogos.login, LocSleekLogos.email_field)
        self.logBase.input_text_to_xpath(LocSleekLogos.password, LocSleekLogos.password_field)
        self.logBase.click_value('Login')
        self.logBase.locate_text_part('My Account')

    # Check register
    def tests_register(self):
        self.logBase.click_xpath(LocSleekLogos.logout)
        self.logBase.open_home_page(LocSleekLogos.home_page)
        self.logBase.click_xpath(LocSleekLogos.register_button)
        self.logBase.locate_text_part('Register at SleekLogos')
        self.logBase.locate_text('email')
        self.logBase.locate_text('password')
        self.logBase.locate_xpath(LocSleekLogos.show_pass)
        self.logBase.input_text_to_xpath(self.logBase.random_email(), LocSleekLogos.email_field)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocSleekLogos.password_field)
        self.logBase.click_value('Register')
        self.logBase.locate_text_part('My Account')

    # Icon Info Page
    def tests_icon_page(self):
        self.logBase.click_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.click_xpath(LocSleekLogos.icon_name)
        self.logBase.click_xpath(LocSleekLogos.icon_name_in_icon_page)
        self.logBase.click_xpath(LocSleekLogos.icon_info_in_icon_page)
        self.logBase.click_xpath(LocSleekLogos.icon_in_icon_page)


























