# -*- coding: utf-8 -*-

import random
from locators_base_page import LocatorsBase


class LocSleekLogos(LocatorsBase):
    """Locators for SleekLogos"""


    icons_resuilt = './/*[@class="b-subcategory-wrapper"][1]/descendant::span[1]'
    category_list = './/*[@class="b-bar-menus-menu m-scrollable"]/descendant::a[%s]'
    platform_search_name = '//h1[@class="icons-set-title"][contains(text(), "%s")]'

    search_field = './/input[@itemprop="query-input"]'
    search_button = './/*[@class="icons-search__btn"]'

    grid_nolabel = '''.//*[@ng-click="clickBtn('noLabel')"]'''
    grid_label = '''.//*[@ng-click="clickBtn('label')"]'''
    label = './/*[@class="b-subcategory-wrapper"][1]/descendant::*[@class="icons-set__icon-title"][1]'

    email_field = '''.//*[@id='RegisterForm_email']'''
    password_field = '''.//*[@id='RegisterForm_password']'''
    login_button = './/*[@href="/login/"]'
    register_button = './/*[@href="/register/"]'
    logout = '//*[@href="/logout/"]'
    show_pass = '//*[@class="showPass"]'

    icon_name = './/*[@class="icon-preview__title"]'
    icon_name_in_icon_page = './/*[@ng-bind="viewCtrl.pageTitle"]'
    icon_info_in_icon_page = './/*[@ng-bind-html="mainSubtitleText"]'
    icon_in_icon_page = './/*[@class="col-md-4 m-full-width b-main-icon m-main-icon"]'

    collections = '//span[contains(., "Collections")]'
    create_collection = './/*[@class="b-collection-preview-create"]'
    collection_name = './/*[@ng-model="collsControl.newCollName"]'
    confirm_name = './/*[@ng-click="collsControl.renameCollection()"]'
    first_collection = '//*[@class="b-collections-container"]/div[1]'
    first_icon_in_collection = './/*[@class="icons-set__icon"]'
    delete_collection_icon = '//span[@class="c-btn m-transparent"]'
    confirm_delete_icon = '//div[@class="c-btn modal__action-confirm modal__action"]'
    delete_menu_collections = '''.//*[@ng-class="{'m-edit': collectionsEdit}"]'''
    delete_collection = './/*[@ng-repeat="coll in colls.colls"][%s]/*[@class="b-collection-delete"]'
    confirm_delete_collection = '//*[@class="c-btn modal__action-confirm modal__action"]'
    rename_collection = './/*[@ng-click="collsControl.showRenaming()"]'

    generate_html = '//*[@class="b-bar-btns m-icon m-single-btn"]/*[2]/btn'
    open_color_panel = '''.//*[@ng-include="'/template-icon.html'"][1]/descendant::*[@class="off-click-recolor"]'''
    grayscale = '//*[@class="colors"]/descendant::*[@ng-repeat="color_ in colorsGray"][%s]' % random.randint(1, 5)
    color = '//*[@class="colors-block"][2]/*[%s]' % random.randint(1, 10)
    color_palette = '//*[@class="colors"]/descendant::*[@ng-class="{active: showPicker}"]'
    canvas = '//*[@class="colors"]/descendant::*/canvas'

    download_popup = '''.//*[@ng-class="{'m-single-page': pageType === 'single', 'm-icon-state':iconState == 'icon'}"]/*[1]/span[1]'''
    right_bar = '''//*[@i8-scroll-commander="vm.scrollCommander"]'''

    small_size = '''.//*[@ng-controller="IconCtrl"]/descendant::li[@ng-show="isShowSize(size)"][1]'''
    middle_size = '''.//*[@ng-controller="IconCtrl"]/descendant::li[@ng-show="isShowSize(size)"][2]'''
    big_size = '''.//*[@ng-controller="IconCtrl"]/descendant::li[@ng-show="isShowSize(size)"][3]'''

    png_type = './/*[@class="c-list m-nooverflow b-format"]/*[1]'
    svg_type = './/*[@class="c-list m-nooverflow b-format"]/*[2]'
    eps_type = './/*[@class="c-list m-nooverflow b-format"]/*[3]'
    pdf_type = './/*[@class="c-list m-nooverflow b-format"]/*[4]'
    font_type = './/*[@class="c-list m-nooverflow b-format"]/*[5]'
    svg_set_type = './/*[@class="c-list m-nooverflow b-format"]/*[6]'

    download = './/*[@class="b-bar-btns m-icon m-single-btn"]/*[1]'

    get_font = '''//*[@popup-target="'generate-font'"]'''
    get_svg_set = '''.//*[@class="b-bar-btns m-collections"]/div[3]'''

    open_icon_editor = '''.//*[@ng-mouseleave="showTooltipEffect[effect] = false"][1]/*[@src="'/effectBtn/'+effect+'.html'"]'''
    editor_ui = './/*[@class="b-switch-effects-list"]/li[%s]'
    icon_window = './/*[@class="b-editor-canvas-container"]'
    size_show_icon = './/*[@class="b-preview f-right"]'
    icon_color_edit = './/*[@class="b-editor-icon-actions f-left"]/descendant::*[@class="b-editor-recoler b-editor-recoler-icon off-click-recolor"]'
    overlay_color_edit = './/*[@class="b-editor-icon-actions f-left"]/descendant::*[@class="b-editor-recoler off-click-recolor b-editor-recoler-overlay"]'




