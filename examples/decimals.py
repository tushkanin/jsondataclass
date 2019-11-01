from dataclasses import dataclass
from decimal import Decimal
from jsondataclass import from_json, to_json


@dataclass
class User:
    id: int
    name: str
    salary: Decimal


user = User(1, "John Doe", Decimal("11.22"))
json_str = to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe", "salary": "11.22"}

json_str = '{"id": 1, "name": "John Doe", "salary": "11.22"}'
user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe', salary=Decimal('11.22'))
