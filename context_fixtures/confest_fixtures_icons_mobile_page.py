import time
import pytest
from logic.logic_base_page import LogBase
from context_fixtures.confest_fixtures_drivers import current_browser


@pytest.fixture
def setup_mobile(request):
    """Precondition for each mobile page test"""
    browser = current_browser()
    url = request.config.getoption("--icon8_mobile_url")
    base = LogBase(browser)

    # Open home page
    try:
        time.sleep(1)
        base.open_home_page(url)
    except:
        time.sleep(1)
        base.open_home_page(url)
