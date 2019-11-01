from dataclasses import dataclass
from jsondataclass import from_dict, DataClassMapper


@dataclass
class User:
    id: int
    name: str


dict_obj = {"id": 1, "name": "John Doe"}

mapper = DataClassMapper()
user = mapper.from_dict(dict_obj, User)
print(user)
# User(id=1, name='John Doe')

# or
user = from_dict(dict_obj, User)
print(user)
# User(id=1, name='John Doe')
