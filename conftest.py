from pytest import fixture
from config import Config
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        help='On which browser run tests'
    )

@fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')
    

@fixture(scope='session')
def app_config(browser):
    cfg = Config(browser)
    return cfg

@fixture(scope='session')
def app_setup(app_config):
    browser = getattr(webdriver, app_config.which_browser)()
    yield browser
    browser.quit()

@fixture()
def task1_url():
    url = 'https://antycaptcha.amberteam.pl:5443/exercises/exercise1?seed=52a1bfe6-fd37-4587-a5cc-27a00a978d48'
    return url

@fixture()
def task2_url():
    url = 'https://antycaptcha.amberteam.pl:5443/exercises/exercise2?seed=45b24f59-6579-4087-ad13-f6f5949aace5'
    return url

@fixture()
def task3_url():
    url = 'https://antycaptcha.amberteam.pl:5443/exercises/exercise3?seed=97cb6030-c84a-43b8-94c3-99a39b0f54ef'
    return url

@fixture()
def task4_url():
    url = 'https://antycaptcha.amberteam.pl:5443/exercises/exercise4?seed=b80e6fa0-bf53-47ae-b34c-5d7037fe3f4f'
    return url