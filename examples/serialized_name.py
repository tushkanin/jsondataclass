from dataclasses import dataclass
from jsondataclass import from_json, to_json, jsonfield


@dataclass
class User:
    id: int = jsonfield("Id")
    name: str = jsonfield("Name")


json_str = '{"Id": 1, "Name": "John Doe"}'
user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe')

json_str = to_json(user)
print(json_str)
# {"Id": 1, "Name": "John Doe"}
