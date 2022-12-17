from pydantic import BaseModel, validator, Field

"""
можно использовать Field
"""


class Post(BaseModel):
    id: int # = Field(le=3) это можно раскоментить и закоментить все что после @validator
    title: str
#    name: str = Field(alias="_name")

    @validator("id")
    def check_that_id_is_less_than_two(cls, v):
        if v > 3:
            raise ValueError("Id is not less than two")
        else:
            return v

## {'id': 1, 'title': 'Post 1', '_name': "Igor"}
