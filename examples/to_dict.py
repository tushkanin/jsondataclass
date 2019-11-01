from dataclasses import dataclass
from jsondataclass import to_dict, DataClassMapper


@dataclass
class User:
    id: int
    name: str


user = User(1, "John Doe")

mapper = DataClassMapper()
dict_obj = mapper.to_dict(user)
print(dict_obj)
# {'id': 1, 'name': 'John Doe'}

# or
dict_obj = to_dict(user)
print(dict_obj)
# {'id': 1, 'name': 'John Doe'}
