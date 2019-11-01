from dataclasses import dataclass
from jsondataclass import from_json, to_json
from jsondataclass.utils import set_forward_refs


@dataclass
class User:
    id: int
    name: str
    info: "ContactInfo"


@dataclass
class ContactInfo:
    email: str
    phone_number: str


set_forward_refs(User, {"ContactInfo": ContactInfo})

user = User(1, "John Doe", ContactInfo("john@doe.com", "+19999999"))
print(to_json(user))
# {"id": 1, "name": "John Doe", "info": {"email": "john@doe.com", "phone_number": "+19999999"}}

json_str = '{"id": 1, "name": "John Doe", "info": {"email": "john@doe.com", "phone_number": "+19999999"}}'
print(from_json(json_str, User))
# User(id=1, name='John Doe', info=ContactInfo(email='john@doe.com', phone_number='+19999999'))
