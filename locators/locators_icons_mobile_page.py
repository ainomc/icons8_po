
import random
from locators_base_page import LocatorsBase

class LocIconsMobile(LocatorsBase):

    desktop_ver_button = './/span[text()="Desktop version"]'

    open_main_menu = './/*[@class="b-menu-toggle"]'
    iMessage_stickers = '//span[contains(text(), "iMessage Stickers")]'

    first_icon = './/*[@class="set-icons cf"]/a[1]'
    change_lang = './/*[@class="b-select-lang ng-scope"]/*[1]'

    search_hide = './/*[@class="c-btn-search-mobile"]'
    search_field = './/input[@ng-model="search.term"]'
    search_button = './/*[@class="c-btn show ng-binding"]'
    first_search_resuilt = './/*[@ng-if="term"]/descendant::a[@class="set-icon ng-scope"][1]'


