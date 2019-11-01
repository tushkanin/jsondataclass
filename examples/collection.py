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
