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
