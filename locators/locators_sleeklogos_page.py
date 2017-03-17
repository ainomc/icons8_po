
import random
import json
from locators_base_page import LocatorsBase



class LocSleekLogos(LocatorsBase):

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


