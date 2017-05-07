# -*- coding: utf-8 -*-

from locators_sleeklogos_page import LocSleekLogos


class LocIconPharm(LocSleekLogos):
    """Locators for IconPharm"""

    type = './/*[@class="b-bar-menus m-fix-c-list"]/*[1]/*[%s]'
    overlay_color_edit = './/*[@class="b-editor-icon-actions f-left"]' \
                         '/descendant::*[@class="b-editor-recoler' \
                         ' off-click-recolor b-editor-recoler-text"]'
