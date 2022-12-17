# пробуем сделать через pydantic комментируем  from jsonschema import validate

from src.enums.global_enums import GlobalErrorMessages


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        """
        Тест через jsonschema
        """
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
                #validate(item, schema)
        else:
            schema.parse_obj(self.response_json)
            #validate(self.response_json, schema)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
