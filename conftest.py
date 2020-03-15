import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome",
                     help="Choose browser")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "Chrome":
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--browser should be Chrome")
    yield browser
    browser.quit()
