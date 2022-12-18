import requests
from jsonschema.validators import validate

from configuration import SERVICE_URL

from src.baseclasses.response import Response
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA


def test_validation():
    """
    Тест через jsonschema выносим эту логику в baseclasses/response.py class Response
    """
    res = requests.get(url=SERVICE_URL)
    receives_posts = res.json()
    for item in receives_posts:
        validate(item, POST_SCHEMA)


def test_status_code():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)


def test_count_posts():
    r = requests.get(url=SERVICE_URL)
    received_posts = r.json()
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value





# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
