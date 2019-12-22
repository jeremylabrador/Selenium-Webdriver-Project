"""
Conftest:

Adds a command line browser option and defines the
fixture functions used across multiple test files.
"""
import pytest
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from base.webdriver_setup import WebDriverSetup


@pytest.yield_fixture()
def setup():
    print("Running method level setup")
    yield
    print("Running method level teardown")


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("Running one time setup")
    wds = WebDriverSetup(browser)
    driver = wds.get_webdriver_instance()
    lp = LoginPage(driver)
    nav = NavigationPage(driver)
    nav.click_login_link()
    lp.login("tester123@gmail.com", "123456")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
