import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.pydantic_schemas.pydantic_post import Post


def test_status_code_pydantic():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(Post)
