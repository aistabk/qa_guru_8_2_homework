import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def user():
    print("тоже выполняюсь перед тестом")
    yield
    print("выполняюсь после теста тоже")


browser.open('https://google.com')
