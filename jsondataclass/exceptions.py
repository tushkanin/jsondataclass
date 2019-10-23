from dataclasses import Field
from typing import Any, Type


class JsonDataClassError(Exception):
    ...


class MissingDefaultValueError(JsonDataClassError):
    def __init__(self, field: Field):
        self._field = field

    def __str__(self) -> str:
        return f"Missing default value for field: {self._field!r}"


class WrongTypeError(JsonDataClassError):
    def __init__(self, expected_type: Type, value: Any):
        self._expected_type = expected_type
        self._value = value

    def __str__(self) -> str:
        return f"Expected value of a type: {self._expected_type!r}, but received: {type(self._value)!r}"
