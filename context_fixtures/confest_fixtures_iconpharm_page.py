import pytest
import time
from context_fixtures.confest_fixtures_drivers import current_browser
from locators.locators_iconpharm_page import LocIconPharm
from logic.logic_base_page import LogBase
from logic.logic_click_base import LogClickBase


@pytest.fixture(scope="class")
def setup_cls_iconpharm(request):
    """Precondition for test class of iconpharm page"""
    browser = current_browser()
    url = request.config.getoption("--iconpharm_url")
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")
    base = LogBase(browser)
    click = LogClickBase(browser)

    # Login
    click.click_text('Login')
    base.input_text_to_xpath(login, LocIconPharm.email_field)
    base.input_text_to_xpath(password, LocIconPharm.password_field)
    click.click_value('Login')
    time.sleep(2)
    base.open_home_page(url)



@pytest.fixture
def setup_iconpharm(request):
    """Precondition for each iconpharm page test"""
    # Open home page
    browser = current_browser()
    base = LogBase(browser)
    url = request.config.getoption("--iconpharm_url")

    # Open home page
    base.open_home_page(url)
