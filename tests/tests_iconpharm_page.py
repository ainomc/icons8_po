# -*- coding: utf-8 -*-

import time
from context.context_iconpharm_page import ContextIconPharm
from locators.locators_iconpharm_page import LocIconPharm


class TestIconPharm(ContextIconPharm):
    """Tests of IconPharm
    https://iconpharm.com/web-app/new-icons/all
    """

    def test_platforms(self):
        """Tests presents of all platforms and platforms resuilt"""
        for type_num in range(1, 4):
            self.click.click_xpath(LocIconPharm.type % type_num)
            self.locate.locate_xpath(LocIconPharm.icons_resuilt)

    def test_category(self):
        """Tests presents of all categories and category resuilt"""
        for category_num in range(1, 28):
            self.click.click_xpath(LocIconPharm.category_list % category_num)
            self.locate.locate_xpath(LocIconPharm.icons_resuilt)

    def test_search_icons(self):
        """Tests input search and presents search resuilt"""
        self.base.input_text_to_xpath(LocIconPharm.search_text, LocIconPharm.search_field)
        self.click.click_xpath(LocIconPharm.search_button)
        self.locate.locate_xpath(LocIconPharm.icons_resuilt)

    def test_grid_nolabel(self):
        """Tests grid nolabel"""
        self.click.click_xpath(LocIconPharm.grid_nolabel)
        self.locate.locate_xpath(LocIconPharm.icons_resuilt)
        assert self.locate.displayed_xpath(LocIconPharm.label) is False

    def test_grid_label(self):
        """Tests grid label"""
        self.click.click_xpath(LocIconPharm.grid_label)
        self.locate.locate_xpath(LocIconPharm.icons_resuilt)
        assert self.locate.displayed_xpath(LocIconPharm.label) is True

    def tests_more_icons_button(self):
        """Click and check 'More icons' button"""
        self.click.click_xpath(LocIconPharm.grid_label)
        self.click.click_text('More Icons')
        assert 'icons8.com' in self.base.current_url()

    def tests_my_account(self):
        """Tests 'My account' information"""
        self.click.click_text_part('My Account')
        self.locate.locate_text('Account')
        self.locate.locate_text(LocIconPharm.login)

    def tests_change_email_or_password(self):
        """Tests check change email or password"""
        self.click.click_text_part('My Account')
        self.click.click_text_part('change email or password')
        self.locate.locate_text_part('username')
        self.locate.locate_text_part('new password')
        self.click.click_value('Save Profile')

    def tests_login(self):
        """Tests login"""
        self.click.click_xpath(LocIconPharm.logout)
        self.base.open_home_page(LocIconPharm.home_page_iconpharm)
        self.click.click_xpath(LocIconPharm.login_button)
        self.locate.locate_text_part('Login to IconPharm')
        self.locate.locate_text('email')
        self.locate.locate_text('password')
        self.locate.locate_text_part('Forgot password?')
        self.locate.locate_xpath(LocIconPharm.show_pass)
        self.base.input_text_to_xpath(LocIconPharm.login, LocIconPharm.email_field)
        self.base.input_text_to_xpath(LocIconPharm.password, LocIconPharm.password_field)
        self.click.click_value('Login')
        self.locate.locate_text_part('My Account')

    def tests_register(self):
        """Tests register"""
        self.click.click_xpath(LocIconPharm.logout)
        self.base.open_home_page(LocIconPharm.home_page_iconpharm)
        self.click.click_xpath(LocIconPharm.register_button)
        self.locate.locate_text_part('Register at IconPharm')
        self.locate.locate_text('email')
        self.locate.locate_text('password')
        self.locate.locate_xpath(LocIconPharm.show_pass)
        self.base.input_text_to_xpath(self.base.random_email(), LocIconPharm.email_field)
        self.base.input_text_to_xpath(self.base.random_text(4), LocIconPharm.password_field)
        self.click.click_value('Register')
        self.locate.locate_text_part('My Account')

    def tests_icon_page(self):
        """Tests icon info page"""
        self.click.click_xpath(LocIconPharm.icons_resuilt)
        self.click.click_xpath(LocIconPharm.icon_name)
        self.locate.locate_xpath(LocIconPharm.icon_name_in_icon_page)
        self.locate.locate_xpath(LocIconPharm.icon_info_in_icon_page)
        self.locate.locate_xpath(LocIconPharm.icon_in_icon_page)

    def test_add_collections(self):
        """Tests add and delete new colletion"""
        self.click.click_xpath(LocIconPharm.collections)
        self.click.click_xpath(LocIconPharm.create_collection)
        self.click.click_xpath(LocIconPharm.collections)
        self.click.click_xpath(LocIconPharm.rename_collection)
        self.base.input_text_to_xpath(self.base.random_text(4), LocIconPharm.collection_name)
        self.click.click_xpath(LocIconPharm.confirm_name)
        self.click.click_xpath(LocIconPharm.icons_resuilt)
        self.locate.locate_xpath(LocIconPharm.first_collection)
        self.click.click_xpath(LocIconPharm.first_icon_in_collection)
        self.click.click_xpath(LocIconPharm.delete_collection_icon)
        self.click.click_xpath(LocIconPharm.confirm_delete_icon)
        self.click.click_xpath(LocIconPharm.delete_menu_collections)
        self.click.click_all_and_confirm(LocIconPharm.delete_collection, LocIconPharm.confirm_delete_collection)

    def test_generate_html(self):
        """Tests generate HTML"""
        self.locate.locate_xpath(LocIconPharm.icons_resuilt)
        self.click.click_xpath(LocIconPharm.generate_html)
        self.locate.locate_text_part('2 ways to insert icons')
        self.locate.locate_text_part('To show the icon')
        self.locate.locate_text_part('To use the icons for free please')
        self.click.click_text_part('Our CDN')
        self.locate.locate_text_part('Icons are served from our CDN')

    def test_color_panel(self):
        """Tests color Panel"""
        self.locate.locate_xpath(LocIconPharm.icons_resuilt)
        self.click.click_xpath(LocIconPharm.open_color_panel)
        self.locate.locate_xpath(LocIconPharm.grayscale)
        self.locate.locate_xpath(LocIconPharm.color)
        self.click.click_xpath(LocIconPharm.color_palette)
        self.locate.locate_xpath(LocIconPharm.canvas)

    def test_icon_editor(self):
        """Test icon editor"""
        self.click.click_xpath(LocIconPharm.open_icon_editor)
        for ui_num in range(1, 8):
            self.click.click_xpath(LocIconPharm.editor_ui % ui_num)
        self.locate.locate_xpath(LocIconPharm.icon_window)
        self.locate.locate_xpath(LocIconPharm.size_show_icon)
        self.locate.locate_text('Save Effects')
        self.locate.locate_text('Cancel')

    def test_icon_editor_icon_color_popup(self):
        """Tests color icon editor pop-up in icon editor"""
        self.click.click_xpath(LocIconPharm.open_icon_editor)
        self.click.click_xpath(LocIconPharm.icon_color_edit)
        self.locate.locate_xpath(LocIconPharm.grayscale)
        self.locate.locate_xpath(LocIconPharm.color)
        self.click.click_xpath(LocIconPharm.color_palette)
        self.locate.locate_xpath(LocIconPharm.canvas)

    def test_icon_editor_overlay_color_popup(self):
        """Tests color overlay editor pop-up in icon editor"""
        self.click.click_xpath(LocIconPharm.open_icon_editor)
        self.click.click_xpath(LocIconPharm.overlay_color_edit)
        self.locate.locate_xpath(LocIconPharm.grayscale)
        self.locate.locate_xpath(LocIconPharm.color)
        self.click.click_xpath(LocIconPharm.color_palette)
        self.locate.locate_xpath(LocIconPharm.canvas)

    def test_download_png_sml(self):
        """Tests download test PNG/Small size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.small_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.png_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.png')
        self.base.del_by_extension('.png')

    def test_download_png_mdl(self):
        """Tests download test PNG/Middle size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.middle_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.png_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.png')
        self.base.del_by_extension('.png')

    def test_download_png_big(self):
        """Tests download test PNG/Big size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.big_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.png_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.png')
        self.base.del_by_extension('.png')

    def test_download_svg_sml(self):
        """Tests download test SVG/Small size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.small_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.svg_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.svg')
        self.base.del_by_extension('.svg')

    def test_download_svg_mdl(self):
        """Tests download test SVG/Middle size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.middle_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.svg_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.svg')
        self.base.del_by_extension('.svg')

    def test_download_svg_big(self):
        """Tests download test SVG/Big size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.big_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.svg_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.svg')
        self.base.del_by_extension('.svg')

    def test_download_esp_sml(self):
        """Test download test ESP/Small size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.small_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.eps_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.eps')
        self.base.del_by_extension('.eps')

    def test_download_esp_mdl(self):
        """Tests download test ESP/Middle size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.middle_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.eps_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.eps')
        self.base.del_by_extension('.eps')

    def test_download_esp_big(self):
        """Tests download test ESP/Big size"""
        self.click.click_xpath(LocIconPharm.download_popup)
        self.click.click_xpath(LocIconPharm.big_size)
        self.base.move_mouse(LocIconPharm.open_color_panel)
        self.click.click_xpath(LocIconPharm.eps_type)
        self.click.click_xpath(LocIconPharm.download)
        self.base.wait_presents_file('.eps')
        self.base.del_by_extension('.eps')

    def test_download_get_font(self):
        """Tests download test Get Font"""
        self.click.click_xpath(LocIconPharm.collections)
        self.click.click_xpath(LocIconPharm.create_collection)
        self.click.click_xpath(LocIconPharm.collections)
        self.click.click_xpath(LocIconPharm.rename_collection)
        self.base.input_text_to_xpath(self.base.random_text(4), LocIconPharm.collection_name)
        self.click.click_xpath(LocIconPharm.confirm_name)
        self.click.click_xpath(LocIconPharm.icons_resuilt)
        self.locate.locate_xpath(LocIconPharm.first_collection)
        self.click.click_xpath(LocIconPharm.get_font)
        self.base.wait_presents_file('.zip')
        time.sleep(1)
        self.base.del_by_extension('.zip')
        self.click.click_xpath(LocIconPharm.first_icon_in_collection)
        self.click.click_xpath(LocIconPharm.delete_collection_icon)
        self.click.click_xpath(LocIconPharm.confirm_delete_icon)
        self.click.click_xpath(LocIconPharm.delete_menu_collections)
        self.click.click_all_and_confirm(LocIconPharm.delete_collection, LocIconPharm.confirm_delete_collection)

    def test_download_get_svg_set(self):
        """Tests download test Get SVG set"""
        self.click.click_xpath(LocIconPharm.collections)
        self.click.click_xpath(LocIconPharm.create_collection)
        self.click.click_xpath(LocIconPharm.collections)
        self.click.click_xpath(LocIconPharm.rename_collection)
        self.base.input_text_to_xpath(self.base.random_text(4), LocIconPharm.collection_name)
        self.click.click_xpath(LocIconPharm.confirm_name)
        self.click.click_xpath(LocIconPharm.icons_resuilt)
        self.locate.locate_xpath(LocIconPharm.first_collection)
        self.click.click_xpath(LocIconPharm.get_svg_set)
        self.base.wait_presents_file('.svg')
        self.base.del_by_extension('.svg')
        self.click.click_xpath(LocIconPharm.first_icon_in_collection)
        self.click.click_xpath(LocIconPharm.delete_collection_icon)
        self.click.click_xpath(LocIconPharm.confirm_delete_icon)
        self.click.click_xpath(LocIconPharm.delete_menu_collections)
        self.click.click_all_and_confirm(LocIconPharm.delete_collection, LocIconPharm.confirm_delete_collection)
