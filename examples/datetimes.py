# flake8: noqa
from dataclasses import dataclass
from datetime import datetime, date, time
from jsondataclass import from_json, to_json, DataClassMapper, jsonfield


@dataclass
class User:
    id: int
    name: str
    last_login: datetime
    birthday: date
    local_time: time


user = User(1, "John Doe", datetime.now(), date(2000, 1, 1), time(0, 0, 0, 0))
json_str = to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe", "last_login": "2019-10-31T18:53:47.615534", "birthday": "2000-01-01", "local_time": "00:00:00"}

user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe', last_login=datetime.datetime(2019, 10, 31, 18, 54, 35, 688288), birthday=datetime.date(2000, 1, 1), local_time=datetime.time(0, 0))

mapper = DataClassMapper()
mapper.datetime_format = "%m/%d/%y %H:%M:%S"
mapper.date_format = "%m/%d/%y"
mapper.time_format = "%H:%M"

user = User(1, "John Doe", datetime.now(), date(2000, 1, 1), time(0, 0, 0, 0))
json_str = mapper.to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe", "last_login": "10/31/19 18:59:11", "birthday": "01/01/00", "local_time": "00:00"}

user = mapper.from_json(json_str, User)
print(user)
# User(id=1, name='John Doe', last_login=datetime.datetime(2019, 10, 31, 18, 59, 11), birthday=datetime.date(2000, 1, 1), local_time=datetime.time(0, 0))


@dataclass
class User:
    id: int
    name: str
    last_login: datetime = jsonfield(serializer_args=("%y/%m/%d %H:%M:%S",))
    birthday: date = jsonfield(serializer_args=("%y/%m/%d",))
    local_time: time = jsonfield(serializer_args=("%I:%M %p",))


user = User(1, "John Doe", datetime.now(), date(2000, 1, 1), time(0, 0, 0, 0))
json_str = to_json(user)
print(json_str)
# {"id": 1, "name": "John Doe", "last_login": "19/10/31 19:00:58", "birthday": "00/01/01", "local_time": "12:00 AM"}

user = from_json(json_str, User)
print(user)
# User(id=1, name='John Doe', last_login=datetime.datetime(2019, 10, 31, 19, 0, 58), birthday=datetime.date(2000, 1, 1), local_time=datetime.time(0, 0))
