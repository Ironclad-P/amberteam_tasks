from pytest import fixture
from config import Config


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