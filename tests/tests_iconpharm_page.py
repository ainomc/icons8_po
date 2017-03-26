# -*- coding: utf-8 -*-
import time
from context.context_iconpharm_page import ContextIconPharm
from locators.locators_iconpharm_page import LocIconPharm

class TestIconPharm(ContextIconPharm):

    def test_x(self):
        pass

    # Presents of all platforms and platforms resuilt
    def test_platforms(self):
        for type_num in range(1, 4):
            self.logBase.click_xpath(LocIconPharm.type % type_num)
            self.logBase.locate_xpath(LocIconPharm.icons_resuilt)

    # Presents of all categories and category resuilt
    def test_category(self):
        for category_num in range(1, 28):
            self.logBase.click_xpath(LocIconPharm.category_list % category_num)
            self.logBase.locate_xpath(LocIconPharm.icons_resuilt)

    # Input search and presents search resuilt
    def test_search_icons(self):
        self.logBase.input_text_to_xpath(LocIconPharm.search_text, LocIconPharm.search_field)
        self.logBase.click_xpath(LocIconPharm.search_button)
        self.logBase.locate_xpath(LocIconPharm.icons_resuilt)

    # Tests grid nolabel
    def test_grid_nolabel(self):
        self.logBase.click_xpath(LocIconPharm.grid_nolabel)
        self.logBase.locate_xpath(LocIconPharm.icons_resuilt)
        assert self.logBase.displayed_xpath(LocIconPharm.label) == False

    # Tests grid label
    def test_grid_label(self):
        self.logBase.click_xpath(LocIconPharm.grid_label)
        self.logBase.locate_xpath(LocIconPharm.icons_resuilt)
        assert self.logBase.displayed_xpath(LocIconPharm.label) == True

    # Click and check 'More icons' button
    def tests_more_icons_button(self):
        self.logBase.click_xpath(LocIconPharm.grid_label)
        self.logBase.click_text('More Icons')
        assert 'icons8.com' in self.logBase.current_url()

    # 'My account' information
    def tests_my_account(self):
        self.logBase.click_text_part('My Account')
        self.logBase.locate_text('Account')
        self.logBase.locate_text(LocIconPharm.login)

    # Check change email or password
    def tests_change_email_or_password(self):
        self.logBase.click_text_part('My Account')
        self.logBase.click_text_part('change email or password')
        self.logBase.locate_text_part('username')
        self.logBase.locate_text_part('new password')
        self.logBase.click_value('Save Profile')

    # Check login
    def tests_login(self):
        self.logBase.click_xpath(LocIconPharm.logout)
        self.logBase.open_home_page(LocIconPharm.home_page_iconpharm)
        self.logBase.click_xpath(LocIconPharm.login_button)
        self.logBase.locate_text_part('Login to IconPharm')
        self.logBase.locate_text('email')
        self.logBase.locate_text('password')
        self.logBase.locate_text_part('Forgot password?')
        self.logBase.locate_xpath(LocIconPharm.show_pass)
        self.logBase.input_text_to_xpath(LocIconPharm.login, LocIconPharm.email_field)
        self.logBase.input_text_to_xpath(LocIconPharm.password, LocIconPharm.password_field)
        self.logBase.click_value('Login')
        self.logBase.locate_text_part('My Account')

    # Check register
    def tests_register(self):
        self.logBase.click_xpath(LocIconPharm.logout)
        self.logBase.open_home_page(LocIconPharm.home_page_iconpharm)
        self.logBase.click_xpath(LocIconPharm.register_button)
        self.logBase.locate_text_part('Register at IconPharm')
        self.logBase.locate_text('email')
        self.logBase.locate_text('password')
        self.logBase.locate_xpath(LocIconPharm.show_pass)
        self.logBase.input_text_to_xpath(self.logBase.random_email(), LocIconPharm.email_field)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocIconPharm.password_field)
        self.logBase.click_value('Register')
        self.logBase.locate_text_part('My Account')

    # Icon Info Page
    def tests_icon_page(self):
        self.logBase.click_xpath(LocIconPharm.icons_resuilt)
        self.logBase.click_xpath(LocIconPharm.icon_name)
        self.logBase.locate_xpath(LocIconPharm.icon_name_in_icon_page)
        self.logBase.locate_xpath(LocIconPharm.icon_info_in_icon_page)
        self.logBase.locate_xpath(LocIconPharm.icon_in_icon_page)

    # Add and delete new colletion
    def test_add_collections(self):
        self.logBase.click_xpath(LocIconPharm.collections)
        self.logBase.click_xpath(LocIconPharm.create_collection)
        self.logBase.click_xpath(LocIconPharm.collections)
        self.logBase.click_xpath(LocIconPharm.rename_collection)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocIconPharm.collection_name)
        self.logBase.click_xpath(LocIconPharm.confirm_name)
        self.logBase.click_xpath(LocIconPharm.icons_resuilt)
        self.logBase.locate_xpath(LocIconPharm.first_collection)
        self.logBase.click_xpath(LocIconPharm.first_icon_in_collection)
        self.logBase.click_xpath(LocIconPharm.delete_collection_icon)
        self.logBase.click_xpath(LocIconPharm.confirm_delete_icon)
        self.logBase.click_xpath(LocIconPharm.delete_menu_collections)
        self.logBase.click_all_and_confirm(LocIconPharm.delete_collection, LocIconPharm.confirm_delete_collection)

    # Generate HTML
    def test_generate_html(self):
        self.logBase.locate_xpath(LocIconPharm.icons_resuilt)
        self.logBase.click_xpath(LocIconPharm.generate_html)
        self.logBase.locate_text_part('2 ways to insert icons')
        self.logBase.locate_text_part('To show the icon')
        self.logBase.locate_text_part('To use the icons for free please')
        self.logBase.click_text_part('Our CDN')
        self.logBase.locate_text_part('Icons are served from our CDN')

    # Color Panel
    def test_color_panel(self):
        self.logBase.locate_xpath(LocIconPharm.icons_resuilt)
        self.logBase.click_xpath(LocIconPharm.open_color_panel)
        self.logBase.locate_xpath(LocIconPharm.grayscale)
        self.logBase.locate_xpath(LocIconPharm.color)
        self.logBase.click_xpath(LocIconPharm.color_palette)
        self.logBase.locate_xpath(LocIconPharm.canvas)

    # Icon editor
    def test_icon_editor(self):
        self.logBase.click_xpath(LocIconPharm.open_icon_editor)
        for ui_num in range(1, 8):
            self.logBase.click_xpath(LocIconPharm.editor_ui % ui_num)
        self.logBase.locate_xpath(LocIconPharm.icon_window)
        self.logBase.locate_xpath(LocIconPharm.size_show_icon)
        self.logBase.locate_text('Save Effects')
        self.logBase.locate_text('Cancel')

    # color icon editor pop-up in icon editor
    def test_icon_editor_icon_color_popup(self):
        self.logBase.click_xpath(LocIconPharm.open_icon_editor)
        self.logBase.click_xpath(LocIconPharm.icon_color_edit)
        self.logBase.locate_xpath(LocIconPharm.grayscale)
        self.logBase.locate_xpath(LocIconPharm.color)
        self.logBase.click_xpath(LocIconPharm.color_palette)
        self.logBase.locate_xpath(LocIconPharm.canvas)

    # color overlay editor pop-up in icon editor
    def test_icon_editor_overlay_color_popup(self):
        self.logBase.click_xpath(LocIconPharm.open_icon_editor)
        self.logBase.click_xpath(LocIconPharm.overlay_color_edit)
        self.logBase.locate_xpath(LocIconPharm.grayscale)
        self.logBase.locate_xpath(LocIconPharm.color)
        self.logBase.click_xpath(LocIconPharm.color_palette)
        self.logBase.locate_xpath(LocIconPharm.canvas)

    # Download test PNG/Small size
    def test_download_png_sml(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.small_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.png_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.png')
        self.logBase.del_by_extension('.png')

    # Download test PNG/Middle size
    def test_download_png_mdl(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.middle_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.png_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.png')
        self.logBase.del_by_extension('.png')

    # Download test PNG/Big size
    def test_download_png_big(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.big_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.png_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.png')
        self.logBase.del_by_extension('.png')

    # Download test SVG/Small size
    def test_download_svg_sml(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.small_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.svg_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.svg')
        self.logBase.del_by_extension('.svg')

    # Download test SVG/Middle size
    def test_download_svg_mdl(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.middle_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.svg_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.svg')
        self.logBase.del_by_extension('.svg')

    # Download test SVG/Big size
    def test_download_svg_big(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.big_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.svg_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.svg')
        self.logBase.del_by_extension('.svg')

    # Download test ESP/Small size
    def test_download_esp_sml(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.small_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.eps_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.eps')
        self.logBase.del_by_extension('.eps')

    # Download test ESP/Middle size
    def test_download_esp_mdl(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.middle_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.eps_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.eps')
        self.logBase.del_by_extension('.eps')

    # Download test ESP/Big size
    def test_download_esp_big(self):
        self.logBase.click_xpath(LocIconPharm.download_popup)
        self.logBase.click_xpath(LocIconPharm.big_size)
        self.logBase.move_mouse(LocIconPharm.open_color_panel)
        self.logBase.click_xpath(LocIconPharm.eps_type)
        self.logBase.click_xpath(LocIconPharm.download)
        self.logBase.wait_presents_file('.eps')
        self.logBase.del_by_extension('.eps')

    # Download test Get Font
    def test_download_get_font(self):
        self.logBase.click_xpath(LocIconPharm.collections)
        self.logBase.click_xpath(LocIconPharm.create_collection)
        self.logBase.click_xpath(LocIconPharm.collections)
        self.logBase.click_xpath(LocIconPharm.rename_collection)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocIconPharm.collection_name)
        self.logBase.click_xpath(LocIconPharm.confirm_name)
        self.logBase.click_xpath(LocIconPharm.icons_resuilt)
        self.logBase.locate_xpath(LocIconPharm.first_collection)
        self.logBase.click_xpath(LocIconPharm.get_font)
        self.logBase.wait_presents_file('.zip')
        time.sleep(1)
        self.logBase.del_by_extension('.zip')
        self.logBase.click_xpath(LocIconPharm.first_icon_in_collection)
        self.logBase.click_xpath(LocIconPharm.delete_collection_icon)
        self.logBase.click_xpath(LocIconPharm.confirm_delete_icon)
        self.logBase.click_xpath(LocIconPharm.delete_menu_collections)
        self.logBase.click_all_and_confirm(LocIconPharm.delete_collection, LocIconPharm.confirm_delete_collection)

    # Download test Get SVG set
    def test_download_get_svg_set(self):
        self.logBase.click_xpath(LocIconPharm.collections)
        self.logBase.click_xpath(LocIconPharm.create_collection)
        self.logBase.click_xpath(LocIconPharm.collections)
        self.logBase.click_xpath(LocIconPharm.rename_collection)
        self.logBase.input_text_to_xpath(self.logBase.random_text(4), LocIconPharm.collection_name)
        self.logBase.click_xpath(LocIconPharm.confirm_name)
        self.logBase.click_xpath(LocIconPharm.icons_resuilt)
        self.logBase.locate_xpath(LocIconPharm.first_collection)
        self.logBase.click_xpath(LocIconPharm.get_svg_set)
        self.logBase.wait_presents_file('.svg')
        self.logBase.del_by_extension('.svg')
        self.logBase.click_xpath(LocIconPharm.first_icon_in_collection)
        self.logBase.click_xpath(LocIconPharm.delete_collection_icon)
        self.logBase.click_xpath(LocIconPharm.confirm_delete_icon)
        self.logBase.click_xpath(LocIconPharm.delete_menu_collections)
        self.logBase.click_all_and_confirm(LocIconPharm.delete_collection, LocIconPharm.confirm_delete_collection)
































