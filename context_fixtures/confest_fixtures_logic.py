# -*- coding: utf-8 -*-
import pytest
from logic.logic_base_page import LogBase
from logic.logic_click_base import LogClickBase
from logic.logic_locate_base import LogLocateBase
from context_fixtures.confest_fixtures_drivers import current_browser


@pytest.fixture(scope="class")
def click(request):
    """Return click logic class instance"""
    browser = current_browser()
    click_cls = LogClickBase(browser)
    return click_cls


@pytest.fixture(scope="class")
def base(request):
    """Return base logic class instance"""
    browser = current_browser()
    base_cls = LogBase(browser)
    return base_cls


@pytest.fixture(scope="class")
def locate(request):
    """Return locate logic class instance"""
    browser = current_browser()
    locate_cls = LogLocateBase(browser)
    return locate_cls
