from dataclasses import dataclass
from datetime import datetime, timezone
from jsondataclass import from_json, to_json, jsonfield


@dataclass
class User:
    id: int
    name: str
    last_login: datetime.timestamp


user = User(1, "John Doe", datetime.now())
json_str = to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe", "last_login": 1572541610}

user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe', last_login=datetime.datetime(2019, 10, 31, 19, 7, 41))


@dataclass
class User:
    id: int
    name: str
    last_login: datetime.timestamp = jsonfield(serializer_kwargs={"timezone": timezone.utc})


user = User(1, "John Doe", datetime.now())
json_str = to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe", "last_login": 1572541956}

user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe', last_login=datetime.datetime(2019, 10, 31, 17, 12, 36, tzinfo=datetime.timezone.utc))
