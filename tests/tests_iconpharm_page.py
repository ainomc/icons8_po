# -*- coding: utf-8 -*-

import time
import pytest
from locators.locators_iconpharm_page import LocIconPharm


@pytest.mark.usefixtures("driver_iconpharm", "base", "click", "locate")
class TestIconPharm(object):
    """Tests of IconPharm
    https://iconpharm.com/web-app/new-icons/all
    """

    def test_platforms(self, iconpharm_pre, click, locate):
        """Tests presents of all platforms and platforms resuilt"""
        for type_num in range(1, 4):
            click.click_xpath(LocIconPharm.type % type_num)
            locate.locate_xpath(LocIconPharm.icons_resuilt)

    def test_category(self, iconpharm_pre, click, locate):
        """Tests presents of all categories and category resuilt"""
        for category_num in range(1, 28):
            click.click_xpath(LocIconPharm.category_list % category_num)
            locate.locate_xpath(LocIconPharm.icons_resuilt)

    def test_search_icons(self, iconpharm_pre, base, click, locate):
        """Tests input search and presents search resuilt"""
        base.input_text_to_xpath(LocIconPharm.search_text,
                                 LocIconPharm.search_field)
        click.click_xpath(LocIconPharm.search_button)
        locate.locate_xpath(LocIconPharm.icons_resuilt)

    def test_grid_nolabel(self, iconpharm_pre, click, locate):
        """Tests grid nolabel"""
        click.click_xpath(LocIconPharm.grid_nolabel)
        locate.locate_xpath(LocIconPharm.icons_resuilt)
        assert locate.displayed_xpath(LocIconPharm.label) is False

    def test_grid_label(self, iconpharm_pre, click, locate):
        """Tests grid label"""
        click.click_xpath(LocIconPharm.grid_label)
        locate.locate_xpath(LocIconPharm.icons_resuilt)
        assert locate.displayed_xpath(LocIconPharm.label) is True

    def tests_my_account(self, iconpharm_pre, login, click, locate):
        """Tests 'My account' information"""
        click.click_text_part('My Account')
        locate.locate_text('Account')
        locate.locate_text(login)

    def tests_change_email_or_password(self, iconpharm_pre, click, locate):
        """Tests check change email or password"""
        click.click_text_part('My Account')
        click.click_text_part('change email or password')
        locate.locate_text_part('username')
        locate.locate_text_part('new password')
        click.click_value('Save Profile')

    def tests_icon_page(self, iconpharm_pre, click, locate):
        """Tests icon info page"""
        click.click_xpath(LocIconPharm.icons_resuilt)
        click.click_xpath(LocIconPharm.icon_name)
        locate.locate_xpath(LocIconPharm.icon_name_in_icon_page)
        locate.locate_xpath(LocIconPharm.icon_info_in_icon_page)
        locate.locate_xpath(LocIconPharm.icon_in_icon_page)

    def test_add_collections(self, iconpharm_pre, base, click, locate):
        """Tests add and delete new colletion"""
        click.click_xpath(LocIconPharm.collections)
        click.click_xpath(LocIconPharm.create_collection)
        click.click_xpath(LocIconPharm.collections)
        click.click_xpath(LocIconPharm.rename_collection)
        base.input_text_to_xpath(base.random_text(4),
                                 LocIconPharm.collection_name)
        click.click_xpath(LocIconPharm.confirm_name)
        click.click_xpath(LocIconPharm.icons_resuilt)
        locate.locate_xpath(LocIconPharm.first_collection)
        click.click_xpath(LocIconPharm.first_icon_in_collection)
        click.click_xpath(LocIconPharm.delete_collection_icon)
        click.click_xpath(LocIconPharm.confirm_delete_icon)
        click.click_xpath(LocIconPharm.delete_menu_collections)
        click.click_all_and_confirm(LocIconPharm.delete_collection,
                                    LocIconPharm.confirm_delete_collection)

    def test_generate_html(self, iconpharm_pre, click, locate):
        """Tests generate HTML"""
        locate.locate_xpath(LocIconPharm.icons_resuilt)
        click.click_xpath(LocIconPharm.generate_html)
        locate.locate_text_part('2 ways to insert icons')
        locate.locate_text_part('To show the icon')
        locate.locate_text_part('To use the icons for free please')
        click.click_text_part('Our CDN')
        locate.locate_text_part('Icons are served from our CDN')

    def test_color_panel(self, iconpharm_pre, click, locate):
        """Tests color Panel"""
        click.click_xpath(LocIconPharm.open_color_panel)
        locate.locate_xpath(LocIconPharm.grayscale)
        locate.locate_xpath(LocIconPharm.color)
        click.click_xpath(LocIconPharm.color_palette)
        locate.locate_xpath(LocIconPharm.canvas)

    def test_icon_editor(self, iconpharm_pre, click, locate):
        """Test icon editor"""
        click.click_xpath(LocIconPharm.open_icon_editor)
        for ui_num in range(1, 8):
            click.click_xpath(LocIconPharm.editor_ui % ui_num)
        locate.locate_xpath(LocIconPharm.icon_window)
        locate.locate_xpath(LocIconPharm.size_show_icon)
        locate.locate_text('Save Effects')
        locate.locate_text('Cancel')

    def test_icon_editor_icon_color_popup(self, iconpharm_pre, click, locate):
        """Tests color icon editor pop-up in icon editor"""
        click.click_xpath(LocIconPharm.open_icon_editor)
        click.click_xpath(LocIconPharm.icon_color_edit)
        locate.locate_xpath(LocIconPharm.grayscale)
        locate.locate_xpath(LocIconPharm.color)
        click.click_xpath(LocIconPharm.color_palette)
        locate.locate_xpath(LocIconPharm.canvas)

    def test_icon_editor_overlay_color_popup(self, iconpharm_pre,
                                             base, click, locate):
        """Tests color overlay editor pop-up in icon editor"""
        click.click_xpath(LocIconPharm.open_icon_editor)
        click.click_xpath(LocIconPharm.overlay_color_edit)
        locate.locate_xpath(LocIconPharm.grayscale)
        locate.locate_xpath(LocIconPharm.color)
        click.click_xpath(LocIconPharm.color_palette)
        locate.locate_xpath(LocIconPharm.canvas)

    def test_download_png_sml(self, iconpharm_pre, base, click, locate):
        """Tests download test PNG/Small size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.small_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.png_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.png')
        base.del_by_extension('.png')

    def test_download_png_mdl(self, iconpharm_pre, base, click, locate):
        """Tests download test PNG/Middle size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.middle_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.png_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.png')
        base.del_by_extension('.png')

    def test_download_png_big(self, iconpharm_pre, base, click, locate):
        """Tests download test PNG/Big size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.big_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.png_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.png')
        base.del_by_extension('.png')

    def test_download_svg_sml(self, iconpharm_pre, base, click, locate):
        """Tests download test SVG/Small size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.small_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.svg_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.svg')
        base.del_by_extension('.svg')

    def test_download_svg_mdl(self, iconpharm_pre, base, click, locate):
        """Tests download test SVG/Middle size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.middle_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.svg_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.svg')
        base.del_by_extension('.svg')

    def test_download_svg_big(self, iconpharm_pre, base, click, locate):
        """Tests download test SVG/Big size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.big_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.svg_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.svg')
        base.del_by_extension('.svg')

    def test_download_esp_sml(self, iconpharm_pre, base, click, locate):
        """Test download test ESP/Small size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.small_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.eps_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.eps')
        base.del_by_extension('.eps')

    def test_download_esp_mdl(self, iconpharm_pre, base, click, locate):
        """Tests download test ESP/Middle size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.middle_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.eps_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.eps')
        base.del_by_extension('.eps')

    def test_download_esp_big(self, iconpharm_pre, base, click, locate):
        """Tests download test ESP/Big size"""
        click.click_xpath(LocIconPharm.download_popup)
        click.click_xpath(LocIconPharm.big_size)
        base.move_mouse(LocIconPharm.open_color_panel)
        click.click_xpath(LocIconPharm.eps_type)
        click.click_xpath(LocIconPharm.download)
        base.wait_presents_file('.eps')
        base.del_by_extension('.eps')

    def test_download_get_font(self, iconpharm_pre, base, click, locate):
        """Tests download test Get Font"""
        click.click_xpath(LocIconPharm.collections)
        click.click_xpath(LocIconPharm.create_collection)
        click.click_xpath(LocIconPharm.collections)
        click.click_xpath(LocIconPharm.rename_collection)
        base.input_text_to_xpath(base.random_text(4),
                                 LocIconPharm.collection_name)
        click.click_xpath(LocIconPharm.confirm_name)
        click.click_xpath(LocIconPharm.icons_resuilt)
        locate.locate_xpath(LocIconPharm.first_collection)
        click.click_xpath(LocIconPharm.get_font)
        base.wait_presents_file('.zip')
        time.sleep(1)
        base.del_by_extension('.zip')
        click.click_xpath(LocIconPharm.first_icon_in_collection)
        click.click_xpath(LocIconPharm.delete_collection_icon)
        click.click_xpath(LocIconPharm.confirm_delete_icon)
        click.click_xpath(LocIconPharm.delete_menu_collections)
        click.click_all_and_confirm(LocIconPharm.delete_collection,
                                    LocIconPharm.confirm_delete_collection)

    def test_download_get_svg_set(self, iconpharm_pre, base, click, locate):
        """Tests download test Get SVG set"""
        click.click_xpath(LocIconPharm.collections)
        click.click_xpath(LocIconPharm.create_collection)
        click.click_xpath(LocIconPharm.collections)
        click.click_xpath(LocIconPharm.rename_collection)
        base.input_text_to_xpath(base.random_text(4),
                                 LocIconPharm.collection_name)
        click.click_xpath(LocIconPharm.confirm_name)
        click.click_xpath(LocIconPharm.icons_resuilt)
        locate.locate_xpath(LocIconPharm.first_collection)
        click.click_xpath(LocIconPharm.get_svg_set)
        base.wait_presents_file('.svg')
        base.del_by_extension('.svg')
        click.click_xpath(LocIconPharm.first_icon_in_collection)
        click.click_xpath(LocIconPharm.delete_collection_icon)
        click.click_xpath(LocIconPharm.confirm_delete_icon)
        click.click_xpath(LocIconPharm.delete_menu_collections)
        click.click_all_and_confirm(LocIconPharm.delete_collection,
                                    LocIconPharm.confirm_delete_collection)

    def tests_login(self, iconpharm_pre, iconpharm_url, login,
                    password, base, click, locate):
        """Tests login"""
        click.click_xpath(LocIconPharm.logout)
        base.open_home_page(iconpharm_url)
        click.click_xpath(LocIconPharm.login_button)
        locate.locate_text_part('Login to IconPharm')
        locate.locate_text('email')
        locate.locate_text('password')
        locate.locate_text_part('Forgot password?')
        locate.locate_xpath(LocIconPharm.show_pass)
        base.input_text_to_xpath(login, LocIconPharm.email_field)
        base.input_text_to_xpath(password, LocIconPharm.password_field)
        click.click_value('Login')
        locate.locate_text_part('My Account')

    def tests_register(self, iconpharm_pre, iconpharm_url, base, click, locate):
        """Tests register"""
        click.click_xpath(LocIconPharm.logout)
        base.open_home_page(iconpharm_url)
        click.click_xpath(LocIconPharm.register_button)
        locate.locate_text_part('Register at IconPharm')
        locate.locate_text('email')
        locate.locate_text('password')
        locate.locate_xpath(LocIconPharm.show_pass)
        base.input_text_to_xpath(base.random_email(),
                                 LocIconPharm.email_field)
        base.input_text_to_xpath(base.random_text(4),
                                 LocIconPharm.password_field)
        click.click_value('Register')
        locate.locate_text_part('My Account')

    def tests_more_icons_button(self, iconpharm_pre, base, click, locate):
        """Click and check 'More icons' button"""
        click.click_xpath(LocIconPharm.grid_label)
        click.click_text('More Icons')
        assert 'icons8.com' in base.current_url()