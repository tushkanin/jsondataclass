from typing import Collection, Dict, List, Mapping, Optional, Union

from jsondataclass.utils import (
    extract_generic_args,
    extract_generic_origin,
    is_generic,
    is_optional,
    is_subclass,
    is_union,
)


def test_is_generic():
    assert is_generic(List[int]) is True
    assert is_generic(int) is False


def test_is_subclass():
    assert is_subclass(List, Collection)
    assert is_subclass(Dict, Mapping)


def test_is_optional():
    assert is_optional(Optional[int]) is True
    assert is_optional(int) is False


def test_is_union():
    assert is_union(Union[int, str]) is True
    assert is_union(int) is False


def test_extract_generic_args():
    assert extract_generic_args(List[int]) == (int,)


def test_extract_generic_origin():
    assert extract_generic_origin(List[int]) is list
