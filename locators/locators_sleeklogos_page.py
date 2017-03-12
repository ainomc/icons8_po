
import random
from locators_base_page import LocatorsBase

class LocSleekLogos(LocatorsBase):
    platform_list = ['All', 'iOS 10', 'Windows 10', 'Windows 8', 'Material',
                     'Android 4', 'Color', 'Office']
    search_text_list = ['Google', 'Facebook', 'Icon', 'Game', 'Phone']
    search_text = random.choice(search_text_list)
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
    login_submit = './/*[@value="Login"]'



