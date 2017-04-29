# -*- coding: utf-8 -*-

import time
from context.context_sleeklogos_page import ContextSleekLogos
from locators.locators_sleeklogos_page import LocSleekLogos


class TestSleekLogos(ContextSleekLogos):
    """Tests of SleekLogos
    https://sleeklogos.design/web-app/new-icons/all
    """

    def test_platforms(self):
        """Tests presents of all platforms and platforms resuilt"""
        for platform in LocSleekLogos.platform_list:
            self.logBase.click_text(platform)
            self.logBase.locate_xpath(LocSleekLogos.platform_search_name % platform)
            self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)

    def test_category(self):
        """Tests presents of all categories and category resuilt"""
        for category_num in range(1, 28):
            self.logBase.click_xpath(LocSleekLogos.category_list % category_num)
            self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)

    def test_search_icons(self):
        """Tests search and presents search resuilt"""
        self.logBase.input_text_to_xpath(LocSleekLogos.search_text, LocSleekLogos.search_field)
        self.logBase.click_xpath(LocSleekLogos.search_button)
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)

    def test_grid_nolabel(self):
        """Tests grid nolabel"""
        self.logBase.click_xpath(LocSleekLogos.grid_nolabel)
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)
        assert self.logBase.displayed_xpath(LocSleekLogos.label) == False

    def test_grid_label(self):
        """Tests grid label"""
        self.logBase.click_xpath(LocSleekLogos.grid_label)
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)
        assert self.logBase.displayed_xpath(LocSleekLogos.label) == True

    def tests_more_icons_button(self):
        """Tests 'More icons' button"""
        self.logBase.click_xpath(LocSleekLogos.grid_label)
        self.logBase.click_text('More Icons')
        assert 'icons8.com' in self.logBase.current_url()

    def tests_my_account(self):
        """Tests 'My account' information"""
        self.logBase.click_text_part('My Account')
        self.logBase.locate_text('Account')
        self.logBase.locate_text(LocSleekLogos.login)

    def tests_change_email_or_password(self):
        """Tests change of email or password"""
        self.logBase.click_text_part('My Account')
        self.logBase.click_text_part('change email or password')
        self.logBase.locate_text_part('username')
        self.logBase.locate_text_part('new password')
        self.logBase.click_value('Save Profile')

    def tests_login(self):
        """Tests login"""
        self.logBase.click_xpath(LocSleekLogos.logout)
        self.logBase.open_home_page(LocSleekLogos.home_page_sleeklogos)
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

    def tests_register(self):
        """Tests register"""
        self.logBase.click_xpath(LocSleekLogos.logout)
        self.logBase.open_home_page(LocSleekLogos.home_page_sleeklogos)
        self.logBase.click_xpath(LocSleekLogos.register_button)
        self.logBase.locate_text_part('Register at SleekLogos')
        self.logBase.locate_text('email')
        self.logBase.locate_text('password')
        self.logBase.locate_xpath(LocSleekLogos.show_pass)
        self.logBase.input_text_to_xpath(self.logBase.random_email(), LocSleekLogos.email_field)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocSleekLogos.password_field)
        self.logBase.click_value('Register')
        self.logBase.locate_text_part('My Account')

    def tests_icon_page(self):
        """Tests Icon Info Page"""
        self.logBase.click_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.click_xpath(LocSleekLogos.icon_name)
        self.logBase.locate_xpath(LocSleekLogos.icon_name_in_icon_page)
        self.logBase.locate_xpath(LocSleekLogos.icon_info_in_icon_page)
        self.logBase.locate_xpath(LocSleekLogos.icon_in_icon_page)

    def test_add_collections(self):
        """Tests new colletions"""
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

    def test_generate_html(self):
        """Tests generate HTML"""
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.click_xpath(LocSleekLogos.generate_html)
        self.logBase.locate_text_part('2 ways to insert icons')
        self.logBase.locate_text_part('To show the icon')
        self.logBase.locate_text_part('To use the icons for free please')
        self.logBase.click_text_part('Our CDN')
        self.logBase.locate_text_part('Icons are served from our CDN')

    def test_color_panel(self):
        """Tests color Panel"""
        self.logBase.locate_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.click_xpath(LocSleekLogos.open_color_panel)
        self.logBase.locate_xpath(LocSleekLogos.grayscale)
        self.logBase.locate_xpath(LocSleekLogos.color)
        self.logBase.click_xpath(LocSleekLogos.color_palette)
        self.logBase.locate_xpath(LocSleekLogos.canvas)

    def test_icon_editor(self):
        """icon editor"""
        self.logBase.click_xpath(LocSleekLogos.open_icon_editor)
        for ui_num in range(1, 9):
            self.logBase.click_xpath(LocSleekLogos.editor_ui % ui_num)
        self.logBase.locate_xpath(LocSleekLogos.icon_window)
        self.logBase.locate_xpath(LocSleekLogos.size_show_icon)
        self.logBase.locate_text('Save Effects')
        self.logBase.locate_text('Cancel')

    def test_icon_editor_icon_color_popup(self):
        """Tests color icon editor pop-up in icon editor"""
        self.logBase.click_xpath(LocSleekLogos.open_icon_editor)
        self.logBase.click_xpath(LocSleekLogos.icon_color_edit)
        self.logBase.locate_xpath(LocSleekLogos.grayscale)
        self.logBase.locate_xpath(LocSleekLogos.color)
        self.logBase.click_xpath(LocSleekLogos.color_palette)
        self.logBase.locate_xpath(LocSleekLogos.canvas)

    def test_icon_editor_overlay_color_popup(self):
        """Tests color overlay editor pop-up in icon editor"""
        self.logBase.click_xpath(LocSleekLogos.open_icon_editor)
        self.logBase.click_xpath(LocSleekLogos.overlay_color_edit)
        self.logBase.locate_xpath(LocSleekLogos.grayscale)
        self.logBase.locate_xpath(LocSleekLogos.color)
        self.logBase.click_xpath(LocSleekLogos.color_palette)
        self.logBase.locate_xpath(LocSleekLogos.canvas)

    def test_download_png_sml(self):
        """Tests download test PNG/Small size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.small_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.png_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.png')
        self.logBase.del_by_extension('.png')

    def test_download_png_mdl(self):
        """Tests download test PNG/Middle size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.middle_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.png_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.png')
        self.logBase.del_by_extension('.png')

    def test_download_png_big(self):
        """Tests Ddwnload test PNG/Big size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.big_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.png_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.png')
        self.logBase.del_by_extension('.png')

    def test_download_svg_sml(self):
        """Tests download test SVG/Small size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.small_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.svg_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.svg')
        self.logBase.del_by_extension('.svg')

    def test_download_svg_mdl(self):
        """Tests download test SVG/Middle size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.middle_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.svg_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.svg')
        self.logBase.del_by_extension('.svg')

    def test_download_svg_big(self):
        """Tests download test SVG/Big size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.big_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.svg_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.svg')
        self.logBase.del_by_extension('.svg')

    def test_download_esp_sml(self):
        """Tests download test ESP/Small size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.small_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.eps_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.eps')
        self.logBase.del_by_extension('.eps')

    def test_download_esp_mdl(self):
        """Tests download test ESP/Middle size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.middle_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.eps_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.eps')
        self.logBase.del_by_extension('.eps')

    def test_download_esp_big(self):
        """Tests download test ESP/Big size"""
        self.logBase.click_xpath(LocSleekLogos.download_popup)
        self.logBase.click_xpath(LocSleekLogos.big_size)
        self.logBase.move_mouse(LocSleekLogos.open_color_panel)
        self.logBase.click_xpath(LocSleekLogos.eps_type)
        self.logBase.click_xpath(LocSleekLogos.download)
        self.logBase.wait_presents_file('.eps')
        self.logBase.del_by_extension('.eps')

    def test_download_get_font(self):
        """Tests download test Get Font"""
        self.logBase.click_xpath(LocSleekLogos.collections)
        self.logBase.click_xpath(LocSleekLogos.create_collection)
        self.logBase.click_xpath(LocSleekLogos.collections)
        self.logBase.click_xpath(LocSleekLogos.rename_collection)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocSleekLogos.collection_name)
        self.logBase.click_xpath(LocSleekLogos.confirm_name)
        self.logBase.click_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.locate_xpath(LocSleekLogos.first_collection)
        self.logBase.click_xpath(LocSleekLogos.get_font)
        self.logBase.wait_presents_file('.zip')
        time.sleep(1)
        self.logBase.del_by_extension('.zip')
        self.logBase.click_xpath(LocSleekLogos.first_icon_in_collection)
        self.logBase.click_xpath(LocSleekLogos.delete_collection_icon)
        self.logBase.click_xpath(LocSleekLogos.confirm_delete_icon)
        self.logBase.click_xpath(LocSleekLogos.delete_menu_collections)
        self.logBase.click_all_and_confirm(LocSleekLogos.delete_collection, LocSleekLogos.confirm_delete_collection)

    def test_download_get_svg_set(self):
        """Tests download test Get SVG set"""
        self.logBase.click_xpath(LocSleekLogos.collections)
        self.logBase.click_xpath(LocSleekLogos.create_collection)
        self.logBase.click_xpath(LocSleekLogos.collections)
        self.logBase.click_xpath(LocSleekLogos.rename_collection)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocSleekLogos.collection_name)
        self.logBase.click_xpath(LocSleekLogos.confirm_name)
        self.logBase.click_xpath(LocSleekLogos.icons_resuilt)
        self.logBase.locate_xpath(LocSleekLogos.first_collection)
        self.logBase.click_xpath(LocSleekLogos.get_svg_set)
        self.logBase.wait_presents_file('.svg')
        self.logBase.del_by_extension('.svg')
        self.logBase.click_xpath(LocSleekLogos.first_icon_in_collection)
        self.logBase.click_xpath(LocSleekLogos.delete_collection_icon)
        self.logBase.click_xpath(LocSleekLogos.confirm_delete_icon)
        self.logBase.click_xpath(LocSleekLogos.delete_menu_collections)
        self.logBase.click_all_and_confirm(LocSleekLogos.delete_collection, LocSleekLogos.confirm_delete_collection)
































