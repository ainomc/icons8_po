import pytest
from context_fixtures.confest_fixtures_drivers import current_browser
from logic.logic_base_page import LogBase
from logic.logic_click_base import LogClickBase
from logic.logic_locate_base import LogLocateBase
from locators.locators_landing_page import LocLandind


@pytest.fixture
def setup_landing(request):
    """Precondition for each landing page test"""
    # Open home page
    browser = current_browser()
    url = request.config.getoption("--landing_url")
    base = LogBase(browser)
    click = LogClickBase(browser)
    locate = LogLocateBase(browser)

    base.open_home_page(url)

    # Open landing page
    import time
    click.click_xpath(LocLandind.first_result_icon)
    time.sleep(1)
    click.click_xpath(LocLandind.icon_name)


    try:
        locate.locate_text_part('Browse by tags')
    except:
        base.open_home_page(url)
        click.click_xpath(LocLandind.another_first_result_icon)
        click.click_xpath(LocLandind.icon_name)
        locate.locate_text_part('Browse by tags')