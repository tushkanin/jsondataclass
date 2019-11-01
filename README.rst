=============
jsondataclass
=============

.. start-badges

.. image:: https://badgen.net/pypi/v/jsondataclass
    :target: https://pypi.org/project/jsondataclass/
    :alt: Latest version

.. image:: https://travis-ci.org/tushkanin/jsondataclass.svg?branch=develop
    :target: https://travis-ci.org/tushkanin/jsondataclass

.. image:: https://badgen.net/badge/code%20style/black/000
    :target: https://github.com/ambv/black
    :alt: code style: black

.. end-badges

**jsondataclass** is a library that makes it easy for you to convert of dataclasses (`PEP 557`_) to and from JSON.

.. _`PEP 557`: https://www.python.org/dev/peps/pep-0557/

Installation
------------

``pip3 install jsondataclass``

Requirements
------------

* python>=3.7

Quick start
-----------

.. code-block:: python

    from dataclasses import dataclass
    from jsondataclass import to_json, from_json


    @dataclass
    class Movie:
        name: str
        year: int
        county: str


    movie = Movie("Terminator: Dark Fate", 2019, "USA")
    print(to_json(movie))
    # {"name": "Terminator: Dark Fate", "year": 2019, "county": "USA"}

    json_str = '{"name": "Terminator: Dark Fate", "year": 2019, "county": "USA"}'
    print(from_json(json_str, Movie))
    # Movie(name='Terminator: Dark Fate', year=2019, county='USA')

Supported types
---------------

* str, int, bool, dict, list, tuple

* nested dataclasses

* typing.List

* typing.Tuple

* typing.Dict

* typing.Optional

* typing.Union

* datetime.datetime

* datetime.date

* datetime.time

* timestamp

* Enum

Usage
-----

The primary functions to use are ``from_json`` and ``to_json``. There is also a class ``DataClassMapper`` with methods ``from_json`` and ``to_json`` available that can be used to configure conversion operations.

The ``DataClassMapper`` instance does not maintain any state while invoking Json operations. So, you are free to reuse the same object for multiple Json serialization and deserialization operations.

Dataclass to JSON
=========================

.. code-block:: python

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

Dataclass from JSON
===================

.. code-block:: python

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

Dataclass to dict
=================

.. code-block:: python

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

Dataclass from dict
===================

.. code-block:: python

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

Nested dataclass
================

.. code-block:: python

    from dataclasses import dataclass
    from jsondataclass import from_json, to_json


    @dataclass
    class ContactInfo:
        email: str
        phone_number: str


    @dataclass
    class User:
        id: int
        name: str
        info: ContactInfo


    user = User(1, "John Doe", ContactInfo("john@doe.com", "+19999999"))
    print(to_json(user))
    # {"id": 1, "name": "John Doe", "info": {"email": "john@doe.com", "phone_number": "+19999999"}}

    json_str = '{"id": 1, "name": "John Doe", "info": {"email": "john@doe.com", "phone_number": "+19999999"}}'
    print(from_json(json_str, User))
    # User(id=1, name='John Doe', info=ContactInfo(email='john@doe.com', phone_number='+19999999'))

Field serialized name
=====================

.. code-block:: python

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

Optional fields
===============

.. code-block:: python

    from dataclasses import dataclass
    from typing import Optional
    from jsondataclass import from_json


    @dataclass
    class User:
        id: int
        name: str
        email: Optional[str]


    json_str = '{"id": 1, "name": "John Doe"}'
    user = from_json(json_str, User)
    print(user)
    # User(id=1, name='John Doe', email=None)

Unions
======

.. code-block:: python

    from dataclasses import dataclass
    from typing import Union
    from jsondataclass import from_json, to_json


    @dataclass
    class User:
        id: Union[int, str]
        name: str


    json_str = '{"id": 1, "name": "John Doe"}'
    user = from_json(json_str, User)
    print(user)
    # User(id=1, name='John Doe')

    json_str = to_json(user)
    print(json_str)
    # {"id": 1, "name": "John Doe"}

Generic collections
===================

.. code-block:: python

    from dataclasses import dataclass
    from typing import List, Tuple, Dict
    from jsondataclass import from_json, to_json


    @dataclass
    class Movie:
        genres: List[str]
        rating: Tuple[float, int]
        name: Dict[str, str]


    movie = Movie(["comedy", "crime"], (5.6, 100), {"en": "WALL-E", "de": "WALL-E"})
    json_str = to_json(movie)
    print(json_str)
    # {"genres": ["comedy", "crime"], "rating": [5.6, 100], "name": {"en": "WALL-E", "de": "WALL-E"}}

    json_str = '{"genres": ["comedy", "crime"], "rating": [5.6, 100], "name": {"en": "WALL-E", "de": "WALL-E"}}'
    movie = from_json(json_str, Movie)
    print(movie)
    # Movie(genres=['comedy', 'crime'], rating=(5.6, 100), name={'en': 'WALL-E', 'de': 'WALL-E'})

Enums
=====

.. code-block:: python

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

datetime, date, time
====================

Serialization of ``datetime``, ``date`` and ``time`` objects are performed using `isoformat()`_, and `fromisoformat()`_ are used for deserialization.

.. _`isoformat()` : https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat

.. _`fromisoformat()` : https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat

.. code-block:: python

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

But you can specify format via ``DataClassMapper`` instance.

.. code-block:: python

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

Or via ``jsonfield`` function.

.. code-block:: python

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

Timestamp
=========

By default, deserialization of timestamp result datetime naive object.

.. code-block:: python

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

You can specify timezone using ``jsonfield`` function.

.. code-block:: python

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

Forward References
==================

.. code-block:: python

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

Custom Serialization and Deserialization
========================================

Sometimes default representation is not what you want.
``DataClassMapper`` allows you to register your own custom serializers.

.. code-block:: python

    from dataclasses import dataclass
    from typing import Type
    from jsondataclass import DataClassMapper, jsonfield, to_json, from_json
    from jsondataclass.serializers import Serializer


    class Rating:
        def __init__(self, rating, vote_count):
            self.rating = rating
            self.vote_count = vote_count

        def __repr__(self):
            return f"Rating(rating={self.rating}, vote_count={self.vote_count})"


    class RatingSerializer(Serializer[list]):
        def serialize(self, data: Rating) -> list:
            return [data.rating, data.vote_count]

        def deserialize(self, data: list, type_: Type[Rating]) -> Rating:
            return Rating(*data)


    @dataclass
    class Movie:
        name: str
        year: int
        rating: Rating


    movie = Movie("Terminator: Dark Fate", 2019, Rating(5, 100))
    mapper = DataClassMapper()
    mapper.register_serializer(Rating, RatingSerializer)
    json_str = mapper.to_json(movie)
    print(json_str)
    # {"name": "Terminator: Dark Fate", "year": 2019, "rating": [5, 100]}

    json_str = '{"name": "Terminator: Dark Fate", "year": 2019, "rating": [5, 100]}'
    movie = mapper.from_json(json_str, Movie)
    print(movie)
    # Movie(name='Terminator: Dark Fate', year=2019, rating=Rating(rating=5, vote_count=100))

Or you can set your serializer on per-field level.

.. code-block:: python

    @dataclass
    class Movie:
        name: str
        year: int
        rating: Rating = jsonfield(serializer_class=RatingSerializer)


    movie = Movie("Terminator: Dark Fate", 2019, Rating(5, 100))
    json_str = to_json(movie)
    print(json_str)
    # {"name": "Terminator: Dark Fate", "year": 2019, "rating": [5, 100]}

    json_str = '{"name": "Terminator: Dark Fate", "year": 2019, "rating": [5, 100]}'
    movie = from_json(json_str, Movie)
    print(movie)
    # Movie(name='Terminator: Dark Fate', year=2019, rating=Rating(rating=5, vote_count=100))

Also, you can override builtin serializers.

.. code-block:: python

    class UpperStringSerializer(Serializer[str]):
        def serialize(self, data: str) -> str:
            return data.upper()

        def deserialize(self, data: str, type_: Type[str]) -> str:
            return data.upper()


    @dataclass
    class Movie:
        name: str
        year: int


    movie = Movie("Terminator: Dark Fate", 2019)

    mapper = DataClassMapper()
    mapper.register_serializer(str, UpperStringSerializer)
    json_str = mapper.to_json(movie)
    print(json_str)
    # {"name": "TERMINATOR: DARK FATE", "year": 2019}

    json_str = '{"name": "Terminator: Dark Fate", "year": 2019}'
    movie = mapper.from_json(json_str, Movie)
    print(movie)
    # Movie(name='TERMINATOR: DARK FATE', year=2019)


    @dataclass
    class Movie:
        name: str = jsonfield(serializer_class=UpperStringSerializer)
        year: int


    movie = Movie("Terminator: Dark Fate", 2019)
    json_str = mapper.to_json(movie)
    print(json_str)
    # {"name": "TERMINATOR: DARK FATE", "year": 2019}

    json_str = '{"name": "Terminator: Dark Fate", "year": 2019}'
    movie = mapper.from_json(json_str, Movie)
    print(movie)
    # Movie(name='TERMINATOR: DARK FATE', year=2019)
