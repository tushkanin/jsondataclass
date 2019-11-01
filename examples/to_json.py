from dataclasses import dataclass
from jsondataclass import to_json, DataClassMapper


@dataclass
class User:
    id: int
    name: str


user = User(1, "John Doe")

mapper = DataClassMapper()
json_str = mapper.to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe"}

# or
json_str = to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe"}
