from dataclasses import Field


class JsonDataClassError(Exception):
    ...


class MissingDefaultValueError(JsonDataClassError):
    def __init__(self, field: Field):
        self._field = field

    def __str__(self) -> str:
        return f"Missing default value for field: {self._field!r}"
