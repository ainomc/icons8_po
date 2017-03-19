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
    def tests_my_account(self):
        self.logBase.click_text_part('My Account')
        self.logBase.locate_text('Account')
        self.logBase.locate_text(LocSleekLogos.login)

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
        self.logBase.locate_xpath(LocSleekLogos.icon_name_in_icon_page)
        self.logBase.locate_xpath(LocSleekLogos.icon_info_in_icon_page)
        self.logBase.locate_xpath(LocSleekLogos.icon_in_icon_page)

    # Add and delete new colletion
    def test_add_collections(self):
        self.logBase.click_xpath(LocSleekLogos.collections)
        self.logBase.click_xpath(LocSleekLogos.create_collection)
        self.logBase.click_xpath(LocSleekLogos.collections)
        self.logBase.click_xpath(LocSleekLogos.rename_collection)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocSleekLogos.collection_name)
        self.logBase.click_xpath(LocSleekLogos.confirm_name)
        self.logBase.click_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.locate_xpath(LocSleekLogos.first_collection)
        self.logBase.click_xpath(LocSleekLogos.first_icon_in_collection)
        self.logBase.click_xpath(LocSleekLogos.delete_collection_icon)
        self.logBase.click_xpath(LocSleekLogos.confirm_delete_icon)
        self.logBase.click_xpath(LocSleekLogos.delete_menu_collections)
        self.logBase.click_all_and_confirm(LocSleekLogos.delete_collection, LocSleekLogos.confirm_delete_collection)

    # Generate HTML
    def test_generate_html(self):
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.click_xpath(LocSleekLogos.generate_html)
        self.logBase.locate_text_part('2 ways to insert icons')
        self.logBase.locate_text_part('To show the icon')
        self.logBase.locate_text_part('To use the icons for free please')
        self.logBase.click_text_part('Our CDN')
        self.logBase.locate_text_part('Icons are served from our CDN')

    # Color Panel
    def test_color_panel(self):
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.click_xpath(LocSleekLogos.open_color_panel)
        self.logBase.locate_xpath(LocSleekLogos.grayscale)
        self.logBase.locate_xpath(LocSleekLogos.color)
        self.logBase.click_xpath(LocSleekLogos.color_palette)
        self.logBase.locate_xpath(LocSleekLogos.canvas)

    # Download test PNG/Small size
    def test_download_png_sml(self):
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.move_mouse(LocSleekLogos.collections)
        self.logBase.click_xpath(LocSleekLogos.small_size)
        self.logBase.click_xpath(LocSleekLogos.png_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        time.sleep(3)
        self.logBase.del_by_extension('.png')



































