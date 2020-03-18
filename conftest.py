import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="Chrome",
                     help="Choose browser: Chrome or Firefox")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "Chrome":
        browser = webdriver.Chrome()
    elif browser_name == "Firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser should be Chrome or Firefox")
    yield browser
    browser.quit()
