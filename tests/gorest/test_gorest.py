import requests

from configuration6 import SERVICE_URL
from src.baseclasses.response6 import Response
from src.pydantic_schemas.user import User


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)


def test_getting_user_fi(get_data, get_random_number):  # тоже что и первый но с фикстурой
    Response(get_data).assert_status_code(200).validate(User)
    print(get_random_number)


def test_getting_user_fu(get_data, calculate):  # тоже что и первый но с фикстурой
    Response(get_data).assert_status_code(200).validate(User)
    print(calculate)
    print(calculate(1, 2))

def test_getting_user_make(get_data, make_number):  # тоже что и первый но с фикстурой
    Response(get_data).assert_status_code(200).validate(User)
    print(make_number)
