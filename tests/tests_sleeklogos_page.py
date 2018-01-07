# -*- coding: utf-8 -*-

import time
import pytest
from locators.locators_sleeklogos_page import LocSleekLogos


@pytest.mark.usefixtures("driver_sleeklogos", "setup_cls_sleeklogos",
                         "base", "click", "locate")
class TestSleekLogos(object):
    """Tests of SleekLogos
    https://sleeklogos.design/web-app/new-icons/all
    """

    def tests_login(self, setup_sleeklogos, sleeklogos_url, login,
                    password, base, click, locate):
        """Tests login"""
        click.click_xpath(LocSleekLogos.logout)
        base.open_home_page(sleeklogos_url)
        click.click_xpath(LocSleekLogos.login_button)
        locate.locate_text_part('Login to SleekLogos')
        locate.locate_text('email')
        locate.locate_text('password')
        locate.locate_text_part('Forgot password?')
        locate.locate_xpath(LocSleekLogos.show_pass)
        base.input_text_to_xpath(login, LocSleekLogos.email_field)
        base.input_text_to_xpath(password, LocSleekLogos.password_field)
        click.click_value('Login')
        locate.locate_text_part('My Account')

    def tests_register(self, setup_sleeklogos, sleeklogos_url,
                       base, click, locate):
        """Tests register"""
        click.click_xpath(LocSleekLogos.logout)
        base.open_home_page(sleeklogos_url)
        click.click_xpath(LocSleekLogos.register_button)
        locate.locate_text_part('Register at SleekLogos')
        locate.locate_text('email')
        locate.locate_text('password')
        locate.locate_xpath(LocSleekLogos.show_pass)
        base.input_text_to_xpath(base.random_email(),
                                 LocSleekLogos.email_field)
        base.input_text_to_xpath(base.random_text(4),
                                 LocSleekLogos.password_field)
        click.click_value('Register')
        locate.locate_text_part('My Account')

    def tests_icon_page(self, setup_sleeklogos, click, locate):
        """Tests Icon Info Page"""
        click.click_xpath(LocSleekLogos.icons_resuilt)
        click.click_xpath(LocSleekLogos.icon_name)
        locate.locate_xpath(LocSleekLogos.icon_name_in_icon_page)
        locate.locate_xpath(LocSleekLogos.icon_info_in_icon_page)
        locate.locate_xpath(LocSleekLogos.icon_in_icon_page)

    def test_add_collections(self, setup_sleeklogos, base, click, locate):
        """Tests new colletions"""
        click.click_xpath(LocSleekLogos.collections)
        click.click_xpath(LocSleekLogos.create_collection)
        click.click_xpath(LocSleekLogos.collections)
        click.click_xpath(LocSleekLogos.rename_collection)
        base.input_text_to_xpath(base.random_text(4),
                                 LocSleekLogos.collection_name)
        click.click_xpath(LocSleekLogos.confirm_name)
        click.click_xpath(LocSleekLogos.icons_resuilt)
        locate.locate_xpath(LocSleekLogos.first_collection)
        click.click_xpath(LocSleekLogos.first_icon_in_collection)
        click.click_xpath(LocSleekLogos.delete_collection_icon)
        click.click_xpath(LocSleekLogos.confirm_delete_icon)
        click.click_xpath(LocSleekLogos.delete_menu_collections)
        click.click_all_and_confirm(LocSleekLogos.delete_collection,
                                    LocSleekLogos.confirm_delete_collection)

    def test_generate_html(self, setup_sleeklogos, click, locate):
        """Tests generate HTML"""
        locate.locate_xpath(LocSleekLogos.icons_resuilt)
        click.click_xpath(LocSleekLogos.generate_html)
        locate.locate_text_part('2 ways to insert icons')
        locate.locate_text_part('To show the icon')
        locate.locate_text_part('To use the icons for free please')
        click.click_text_part('Our CDN')
        locate.locate_text_part('Icons are served from our CDN')

    def test_color_panel(self, setup_sleeklogos, click, locate):
        """Tests color Panel"""
        locate.locate_xpath(LocSleekLogos.icons_resuilt)
        click.click_xpath(LocSleekLogos.open_color_panel)
        locate.locate_xpath(LocSleekLogos.grayscale)
        locate.locate_xpath(LocSleekLogos.color)
        click.click_xpath(LocSleekLogos.color_palette)
        locate.locate_xpath(LocSleekLogos.canvas)

    def test_icon_editor(self, setup_sleeklogos, click, locate):
        """icon editor"""
        click.click_xpath(LocSleekLogos.open_icon_editor)
        for ui_num in range(1, 9):
            click.click_xpath(LocSleekLogos.editor_ui % ui_num)
        locate.locate_xpath(LocSleekLogos.icon_window)
        locate.locate_xpath(LocSleekLogos.size_show_icon)
        locate.locate_text('Save Effects')
        locate.locate_text('Cancel')

    def test_icon_editor_icon_color_popup(self, setup_sleeklogos,
                                          click, locate):
        """Tests color icon editor pop-up in icon editor"""
        click.click_xpath(LocSleekLogos.open_icon_editor)
        click.click_xpath(LocSleekLogos.icon_color_edit)
        locate.locate_xpath(LocSleekLogos.grayscale)
        locate.locate_xpath(LocSleekLogos.color)
        click.click_xpath(LocSleekLogos.color_palette)
        locate.locate_xpath(LocSleekLogos.canvas)

    def test_icon_editor_overlay_color_popup(self, setup_sleeklogos,
                                             click, locate):
        """Tests color overlay editor pop-up in icon editor"""
        click.click_xpath(LocSleekLogos.open_icon_editor)
        click.click_xpath(LocSleekLogos.overlay_color_edit)
        locate.locate_xpath(LocSleekLogos.grayscale)
        locate.locate_xpath(LocSleekLogos.color)
        click.click_xpath(LocSleekLogos.color_palette)
        locate.locate_xpath(LocSleekLogos.canvas)

    def test_download_png_sml(self, setup_sleeklogos, base, click, locate):
        """Tests download test PNG/Small size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.small_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.png_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.png')
        base.del_by_extension('.png')

    def test_download_png_mdl(self, setup_sleeklogos, base, click, locate):
        """Tests download test PNG/Middle size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.middle_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.png_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.png')
        base.del_by_extension('.png')

    def test_download_png_big(self, setup_sleeklogos, base, click, locate):
        """Tests Ddwnload test PNG/Big size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.big_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.png_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.png')
        base.del_by_extension('.png')

    def test_download_svg_sml(self, setup_sleeklogos, base, click, locate):
        """Tests download test SVG/Small size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.small_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.svg_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.svg')
        base.del_by_extension('.svg')

    def test_download_svg_mdl(self, setup_sleeklogos, base, click, locate):
        """Tests download test SVG/Middle size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.middle_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.svg_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.svg')
        base.del_by_extension('.svg')

    def test_download_svg_big(self, setup_sleeklogos, base, click, locate):
        """Tests download test SVG/Big size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.big_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.svg_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.svg')
        base.del_by_extension('.svg')

    def test_download_esp_sml(self, setup_sleeklogos, base, click, locate):
        """Tests download test ESP/Small size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.small_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.eps_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.eps')
        base.del_by_extension('.eps')

    def test_download_esp_mdl(self, setup_sleeklogos, base, click, locate):
        """Tests download test ESP/Middle size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.middle_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.eps_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.eps')
        base.del_by_extension('.eps')

    def test_download_esp_big(self, setup_sleeklogos, base, click, locate):
        """Tests download test ESP/Big size"""
        click.click_xpath(LocSleekLogos.download_popup)
        click.click_xpath(LocSleekLogos.big_size)
        base.move_mouse(LocSleekLogos.open_color_panel)
        click.click_xpath(LocSleekLogos.eps_type)
        click.click_xpath(LocSleekLogos.download)
        base.wait_presents_file('.eps')
        base.del_by_extension('.eps')

    def test_download_get_font(self, setup_sleeklogos, base, click, locate):
        """Tests download test Get Font"""
        click.click_xpath(LocSleekLogos.collections)
        click.click_xpath(LocSleekLogos.create_collection)
        click.click_xpath(LocSleekLogos.collections)
        click.click_xpath(LocSleekLogos.rename_collection)
        base.input_text_to_xpath(base.random_text(4),
                                 LocSleekLogos.collection_name)
        click.click_xpath(LocSleekLogos.confirm_name)
        click.click_xpath(LocSleekLogos.icons_resuilt)
        locate.locate_xpath(LocSleekLogos.first_collection)
        click.click_xpath(LocSleekLogos.get_font)
        base.wait_presents_file('.zip')
        time.sleep(1)
        base.del_by_extension('.zip')
        click.click_xpath(LocSleekLogos.first_icon_in_collection)
        click.click_xpath(LocSleekLogos.delete_collection_icon)
        click.click_xpath(LocSleekLogos.confirm_delete_icon)
        click.click_xpath(LocSleekLogos.delete_menu_collections)
        click.click_all_and_confirm(LocSleekLogos.delete_collection,
                                    LocSleekLogos.confirm_delete_collection)

    def test_download_get_svg_set(self, setup_sleeklogos, base, click, locate):
        """Tests download test Get SVG set"""
        click.click_xpath(LocSleekLogos.collections)
        click.click_xpath(LocSleekLogos.create_collection)
        click.click_xpath(LocSleekLogos.collections)
        click.click_xpath(LocSleekLogos.rename_collection)
        base.input_text_to_xpath(base.random_text(4),
                                 LocSleekLogos.collection_name)
        click.click_xpath(LocSleekLogos.confirm_name)
        click.click_xpath(LocSleekLogos.icons_resuilt)
        locate.locate_xpath(LocSleekLogos.first_collection)
        click.click_xpath(LocSleekLogos.get_svg_set)
        base.wait_presents_file('.svg')
        base.del_by_extension('.svg')
        click.click_xpath(LocSleekLogos.first_icon_in_collection)
        click.click_xpath(LocSleekLogos.delete_collection_icon)
        click.click_xpath(LocSleekLogos.confirm_delete_icon)
        click.click_xpath(LocSleekLogos.delete_menu_collections)
        click.click_all_and_confirm(LocSleekLogos.delete_collection,
                                    LocSleekLogos.confirm_delete_collection)


    def test_platforms(self, setup_sleeklogos, click, locate):
        """Tests presents of all platforms and platforms resuilt"""
        for platform in LocSleekLogos.platform_list:
            click.click_text(platform)
            locate.locate_xpath(LocSleekLogos.platform_search_name % platform)
            locate.locate_xpath(LocSleekLogos.icons_resuilt)

    def test_category(self, setup_sleeklogos, click, locate):
        """Tests presents of all categories and category resuilt"""
        for category_num in range(1, 28):
            click.click_xpath(LocSleekLogos.category_list % category_num)
            locate.locate_xpath(LocSleekLogos.icons_resuilt)

    def test_search_icons(self, setup_sleeklogos, base, click, locate):
        """Tests search and presents search resuilt"""
        base.input_text_to_xpath(LocSleekLogos.search_text,
                                 LocSleekLogos.search_field)
        click.click_xpath(LocSleekLogos.search_button)
        locate.locate_xpath(LocSleekLogos.icons_resuilt)

    def test_grid_nolabel(self, setup_sleeklogos, click, locate):
        """Tests grid nolabel"""
        click.click_xpath(LocSleekLogos.grid_nolabel)
        locate.locate_xpath(LocSleekLogos.icons_resuilt)
        assert locate.displayed_xpath(LocSleekLogos.label) is False

    def test_grid_label(self, setup_sleeklogos, click, locate):
        """Tests grid label"""
        click.click_xpath(LocSleekLogos.grid_label)
        locate.locate_xpath(LocSleekLogos.icons_resuilt)
        assert locate.displayed_xpath(LocSleekLogos.label) is True

    def tests_more_icons_button(self, setup_sleeklogos, base, click, locate):
        """Tests 'More icons' button"""
        click.click_xpath(LocSleekLogos.grid_label)
        click.click_text('More Icons')
        assert 'icons8.com' in base.current_url()

    def tests_my_account(self, setup_sleeklogos, login, click, locate):
        """Tests 'My account' information"""
        click.click_text_part('My Account')
        locate.locate_text('Account')
        locate.locate_text(login)

    def tests_change_email_or_password(self, setup_sleeklogos, click, locate):
        """Tests change of email or password"""
        click.click_text_part('My Account')
        click.click_text_part('change email or password')
        locate.locate_text_part('username')
        locate.locate_text_part('new password')
        click.click_value('Save Profile')
