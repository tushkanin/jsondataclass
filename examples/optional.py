from dataclasses import dataclass
from typing import Optional
from jsondataclass import from_json


@dataclass
class User:
    id: int
    name: str
    email: Optional[str]


json_str = '{"id": 1, "name": "John Doe"}'
user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe', email=None)
