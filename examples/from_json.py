from dataclasses import dataclass
from jsondataclass import from_json, DataClassMapper


@dataclass
class User:
    id: int
    name: str


json_str = '{"id": 1, "name": "John Doe"}'

mapper = DataClassMapper()
user = mapper.from_json(json_str, User)
print(user)
# User(id=1, name='John Doe')

# or
user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe')
