import pytest

from src.baseclasses.response6 import Response
from src.pydantic_schemas.user import User


def test_getting_user_make(get_data, make_number):  # тоже что и первый но с фикстурой
    Response(get_data).assert_status_code(200).validate(User)


@pytest.mark.parametrize("firs_value, second_value, result", [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', 'b', 'bb')])
def test_calculator(firs_value, second_value, result, calculate):
    assert calculate(firs_value, second_value) == result


@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
def test_two():
    assert 1 == 1


@pytest.mark.development
def test_three():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.production
def test_five():
    assert 1 == 1
