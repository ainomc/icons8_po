import pytest
from context_fixtures.confest_fixtures_drivers import current_browser
from logic.logic_base_page import LogBase
from logic.logic_click_base import LogClickBase
from locators.locators_sleeklogos_page import LocSleekLogos


@pytest.fixture(scope="class")
def setup_cls_sleeklogos(request):
    """Precondition for test class of sleeklogos page"""
    browser = current_browser()
    url = request.config.getoption("--sleeklogos_url")
    base = LogBase(browser)
    click = LogClickBase(browser)
    login = request.config.getoption("--login")
    password = request.config.getoption("--password")

    # Login
    click.click_text('Login')
    base.input_text_to_xpath(login, LocSleekLogos.email_field)
    base.input_text_to_xpath(password, LocSleekLogos.password_field)
    click.click_value('Login')
    base.open_home_page(url)


@pytest.fixture
def setup_sleeklogos(request):
    """Precondition for each sleeklogos page test"""
    # Open home page
    browser = current_browser()
    url = request.config.getoption("--sleeklogos_url")
    base = LogBase(browser)

    # Open home page
    base.open_home_page(url)
