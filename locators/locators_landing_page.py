
import random
from locators_base_page import LocatorsBase

class LocLandind(LocatorsBase):
    field = '//*[@placeholder="%s"]'
    search_field = field % 'search'
    search_button = '//*[@class="b-search-btn"]'
    icon_name = '//*[@class="c-pretty-link m-inline"]'
    icon_category = '//*[@class="c-breadcrumbs"]/*[3]'
    icon_text = './/*[@ng-bind-html="vm.mainSubtitleText"]'
    icon = '//*[@class="col-md-4 m-full-width b-main-icon m-main-icon"]/*'
    download_button = '//button[contains(text(), "Download")]'
    choose_PNG_size = '//*[@class="icon-format-item icon-format-dropdown off-click-dropdownsize m-center"]'
    icon_download_sizes = '//ul[@class="c-list m-nooverflow"]/*[%s]' % random.randint(1, 4)
    icon_download_format = '//*[@class="c-list m-nooverflow b-format"]/*[%s]' % random.randint(1, 4)

    tag ='//*[@class="b-tags-list"]/a[1]'
    icon_in_tag = '//span[@class="icons-set_element"][1]'
    icons_result = '//*[@class="icons-set"]/descendant::span[%s]' % random.randint(1, 5)
    icon_in_result = '//div[@class="b-subcategory-wrapper"][1]/descendant::a[%s]' % random.randint(1, 5)
    category_title = '//*[@ng-bind-html="vm.category.title"]'




