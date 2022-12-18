from random import randint

import pytest
import requests

from configuration6 import SERVICE_URL


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
