from dataclasses import dataclass
from typing import Literal

from jsondataclass import from_json, to_json


@dataclass
class Movie:
    name: str
    year: int
    rating: Literal[1, 2, 3, 4, 5]


movie = Movie("Terminator: Dark Fate", 2019, 5)
print(to_json(movie))
# > {"name": "Terminator: Dark Fate", "year": 2019, "rating": 5}

json_str = '{"name": "Terminator: Dark Fate", "year": 2019, "rating": 5}'
print(from_json(json_str, Movie))
# > Movie(name='Terminator: Dark Fate', year=2019, rating=5)
