import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def window_size():
    browser.config.window_height = 700
    browser.config.window_width = 560
    yield
    browser.close_current_tab()

@pytest.fixture(scope='session', autouse=True)
def yandex_config():
    browser.config.window_height = 1000
    browser.config.window_width = 800
    yield
    browser.close_current_tab()
