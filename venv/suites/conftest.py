import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose any language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(executable_path='binaries/chromedriver', options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
