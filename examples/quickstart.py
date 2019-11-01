from dataclasses import dataclass
from jsondataclass import to_json, from_json


@dataclass
class Movie:
    name: str
    year: int
    county: str


movie = Movie("Terminator: Dark Fate", 2019, "USA")
print(to_json(movie))
# > {"name": "Terminator: Dark Fate", "year": 2019, "county": "USA"}

json_str = '{"name": "Terminator: Dark Fate", "year": 2019, "county": "USA"}'
print(from_json(json_str, Movie))
# > Movie(name='Terminator: Dark Fate', year=2019, county='USA')
