# -*- coding: utf-8 -*-
# from allure import attach, attach_type
import time
import pytest
from locators.locators_icons_mobile_page import LocIconsMobile


@pytest.mark.usefixtures("driver_icon8_mobile", "base", "click", "locate")
class TestIconsMobile(object):
    """Tests of monile version of web-add
    https://demo.icons8.com/icons/
    """

    def test_main_menu_items(self, setup_mobile, click, locate):
        """Tests of main menu items"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        locate.locate_text("Icons")
        locate.locate_text("Request")
        locate.locate_text("Buy")
        locate.locate_text("Icon Search AI")
        locate.locate_text("Blog")
        locate.locate_text_part("Register")
        locate.locate_text_part("Login")

    def test_menu_icons_button(self, setup_mobile, click, locate):
        """Tests of main menu icon button"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        click.click_text("Icons")
        locate.locate_xpath(LocIconsMobile.desktop_version_locator)

    def test_menu_request_button(self, setup_mobile, click, locate):
        """Tests of main menu icon button"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        click.click_text("Request")
        locate.locate_text("Request Icons")

    def test_menu_buy_button(self, setup_mobile, click, locate):
        """Tests of main menu icon button"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        click.click_text("Buy")
        locate.locate_text("Free")

    def test_menu_imessage_button(self, setup_mobile, click, locate):
        """Tests of main menu icon button"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        click.click_xpath(LocIconsMobile.iMessage_stickers)

    def test_menu_ai_button(self, setup_mobile, click, locate):
        """Tests of main menu icon button"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        time.sleep(1)
        click.click_text("Icon Search AI")
        locate.locate_text_part("Draw an icon")

    def test_menu_blog_button(self, setup_mobile, click, locate):
        """Tests of main menu icon button"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        click.click_text("Blog")
        locate.locate_xpath(LocIconsMobile.blog_list)

    def test_menu_register_button(self, setup_mobile, click, locate):
        """Tests of main menu icon button"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        locate.locate_text_part("Register")
        click.click_text_part("Register")
        locate.locate_text("Register at Icons8")

    def test_menu_login_button(self, setup_mobile, click, locate):
        """Tests of main menu icon button"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        locate.locate_text_part("Login")
        click.click_text_part("Login")
        locate.locate_text_part("Forgot password?")

    def test_platforms(self, setup_mobile, locate):
        """Tests of main menu icon button"""
        for platform in LocIconsMobile.platform_list:
            locate.locate_text(platform)

    def test_change_lang_popup(self, setup_mobile, click, locate):
        """Tests of change language pop-up"""
        click.click_xpath(LocIconsMobile.open_main_menu)
        click.click_xpath(LocIconsMobile.change_lang)
        locate.locate_text("    French ")

    def test_search(self, setup_mobile, base, click, locate):
        """Tests of search"""
        base.input_text_to_xpath(LocIconsMobile.search_text,
                                         LocIconsMobile.search_field)
        click.click_xpath(LocIconsMobile.search_button)
        locate.locate_xpath(LocIconsMobile.first_result_icon)

    def test_icon_page(self, setup_mobile, icon8_mobile_url,
                       base, click, locate):
        """Tests of icon page"""
        click.click_xpath(LocIconsMobile.first_result_icon)
        click.click_xpath(LocIconsMobile.icon_name)

        try:
            locate.locate_text_part('Browse by tags')
        except:
            base.open_home_page(icon8_mobile_url)
            click.click_xpath(LocIconsMobile.another_first_result_icon)
            click.click_xpath(LocIconsMobile.icon_name)
            locate.locate_text_part('Browse by tags')
        locate.locate_xpath(LocIconsMobile.icon_name_in_icon_page)
        locate.locate_xpath(LocIconsMobile.icon_subtitle)
        locate.locate_xpath(LocIconsMobile.icon_page_download_bu)
        locate.locate_xpath(LocIconsMobile.icon_in_icon_page)
        locate.locate_xpath(LocIconsMobile.icon_page_generate_html)
        locate.locate_xpath(LocIconsMobile.icon_page_tags_list)

    def test_right_menu_bar(self, setup_mobile, click, locate):
        """Tests of right menu bar"""
        click.click_xpath(LocIconsMobile.first_result_icon)
        locate.locate_text('Download')
        locate.locate_text('Generate HTML')
        click.click_xpath(LocIconsMobile.collections)
        locate.locate_text('Download')
        locate.locate_text('Get Font')
        locate.locate_text('Get SVG Set')
