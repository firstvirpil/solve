import pytest


@pytest.fixture
def say_hello():
    print("Это фикструра в папке something")
