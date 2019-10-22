from typing import Any, Optional, Tuple, Type, Union


def is_generic(type_: Type) -> bool:
    return hasattr(type_, "__origin__")


def is_subclass(type_a: Type, type_b: Type):
    try:
        return issubclass(type_a, type_b)
    except TypeError:
        return False


def is_union(type_: Type) -> bool:
    return is_generic(type_) and type_.__origin__ is Union


def is_optional(type_: Type) -> bool:
    if not is_union(type_) or not len(type_.__args__) == 2:
        return False
    return type(None) in type_.__args__


def extract_generic_args(type_: Type) -> Tuple[Type, ...]:
    if not is_generic(type_):
        raise TypeError(f"{type_} is not Generic")
    return type_.__args__


def extract_generic_origin(type_: Type[Any]) -> Any:
    if not is_generic(type_):
        raise TypeError(f"{type_} is not Generic")
    if is_optional(type_):
        return Optional
    return type_.__origin__
