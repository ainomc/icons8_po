# -*- coding: utf-8 -*-
import pytest


# Parameters
def pytest_addoption(parser):
    parser.addoption("--login", action="store",
                     default="po_tests@gmail.com", help="login")
    parser.addoption("--password", action="store",
                     default="123", help="password")
    parser.addoption("--server", action="store",
                     default="demo", help="server")

    parser.addoption("--landing_url", action="store",
                     default="https://demo.icons8.com/icon/",
                     help="landing_url")
    parser.addoption("--icon8_mobile_url", action="store",
                     default="https://demo.icons8.com/icons/",
                     help="icon8_mobile_url")
    parser.addoption("--sleeklogos_url", action="store",
                     default="https://sleeklogos.design/web-app/new-icons/all",
                     help="sleeklogos_url")
    parser.addoption("--iconpharm_url", action="store",
                     default="https://iconpharm.com/web-app/new-icons/all",
                     help="iconpharm_url")


# Parameters
@pytest.fixture(scope="module")
def login(request):
    return request.config.getoption("--login")


@pytest.fixture(scope="module")
def password(request):
    return request.config.getoption("--password")


@pytest.fixture(scope="module")
def server(request):
    return request.config.getoption("--server")


@pytest.fixture(scope="module")
def landing_url(request):
    return request.config.getoption("--landing_url")


@pytest.fixture(scope="module")
def icon8_mobile_url(request):
    return request.config.getoption("--icon8_mobile_url")


@pytest.fixture(scope="module")
def sleeklogos_url(request):
    return request.config.getoption("--sleeklogos_url")


@pytest.fixture(scope="module")
def iconpharm_url(request):
    return request.config.getoption("--iconpharm_url")