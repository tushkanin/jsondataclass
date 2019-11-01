from dataclasses import dataclass
from typing import Union
from jsondataclass import from_json, to_json


@dataclass
class User:
    id: Union[int, str]
    name: str


json_str = '{"id": 1, "name": "John Doe"}'
user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe')

json_str = to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe"}
