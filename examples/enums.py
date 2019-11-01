from dataclasses import dataclass
from enum import Enum
from jsondataclass import from_json, to_json


class Role(Enum):
    ADMIN = 1
    STAFF = 2
    GUEST = 3


@dataclass
class User:
    id: int
    name: str
    role: Role


user = User(1, "John Doe", Role.ADMIN)
json_str = to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe", "role": 1}

json_str = '{"id": 1, "name": "John Doe", "role": 1}'
user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe', role=<Role.ADMIN: 1>)
