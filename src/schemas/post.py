POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"type": "string"}
    },
    "required": ["id"]  # обязательный параметр
}


# {'id': 1, 'title': 'Post 1'}