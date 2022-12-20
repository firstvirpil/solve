from random import randint

import pytest
import requests

from configuration6 import SERVICE_URL
from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture(scope='function')
def say_hello():
    print("heLLO")
    return 15


@pytest.fixture
def get_data():
    response = requests.get(SERVICE_URL)
    return response


@pytest.fixture
def get_random_number():
    return randint(111, 999)


def _calculate(a, b):
    return a + b


@pytest.fixture
def calculate():
    return _calculate


@pytest.fixture
def make_number():
    print("I`m getting number")
    number = randint(111, 999)
    yield
    print(f"Number at home {number}")