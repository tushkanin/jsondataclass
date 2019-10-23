from abc import abstractmethod
from typing import Any, Collection, Dict, Generic, List, Optional, Tuple, Type, TypeVar

from .config import Config
from .exceptions import TupleTypeMatchError
from .utils import extract_generic_args, extract_generic_origin, is_generic, is_subclass, type_check

T = TypeVar("T")


class Serializer(Generic[T]):
    def __init__(self, serializer_factory: "SerializerFactory" = None, config: Config = None, *args, **kwargs):
        if config is None:
            config = Config()
        if serializer_factory is None:
            serializer_factory = SerializerFactory(config)
        self._serializer_factory = serializer_factory
        self._config = config

    @abstractmethod
    def serialize(self, data: T) -> Any:
        ...

    @abstractmethod
    def deserialize(self, data: Any, type_: Type[T]) -> T:
        ...


class DefaultSerializer(Serializer[Any]):
    def serialize(self, data: Any) -> Any:
        return data

    def deserialize(self, data: Any, type_: Type) -> Any:
        return data


class StringSerializer(Serializer[str]):
    def serialize(self, data: Any) -> str:
        return str(data)

    def deserialize(self, data: Any, type_: Type[str]) -> str:
        return str(data)


def _serialize_collection(data: Collection, serializer_factory: "SerializerFactory") -> List:
    result = []
    for value in data:
        serializer = serializer_factory.get_serializer(type(value))
        result.append(serializer.serialize(value))
    return result


class ListSerializer(Serializer[List]):
    def serialize(self, data: List) -> List:
        return _serialize_collection(data, self._serializer_factory)

    def deserialize(self, data: list, type_: Type[List]) -> List:
        type_check(data, list)
        if not is_generic(type_):
            return list(data)
        item_type = extract_generic_args(type_)[0]
        serializer = self._serializer_factory.get_serializer(item_type)
        return list(serializer.deserialize(item, item_type) for item in data)


class TupleSerializer(Serializer[Tuple]):
    def serialize(self, data: Tuple) -> List:
        return _serialize_collection(data, self._serializer_factory)

    def _deserilize_generic(self, data: list, type_: Type[Tuple]) -> Tuple:
        item_types = extract_generic_args(type_)
        if len(item_types) == 0:
            return tuple(data)
        if len(item_types) == 2 and item_types[1] is Ellipsis:
            item_type = item_types[0]
            serializer = self._serializer_factory.get_serializer(item_type)
            return tuple(serializer.deserialize(item, item_type) for item in data)
        if len(item_types) != len(data):
            raise TupleTypeMatchError(type_, data)
        result = []
        for item, item_type in zip(data, item_types):
            serializer = self._serializer_factory.get_serializer(item_type)
            result.append(serializer.deserialize(item, item_type))
        return tuple(result)

    def deserialize(self, data: list, type_: Type[Tuple]) -> Tuple:
        type_check(data, list)
        if not is_generic(type_):
            return tuple(data)
        return self._deserilize_generic(data, type_)


class DictSerializer(Serializer[Dict]):
    def serialize(self, data: Dict) -> Dict:
        result = {}
        for key, value in data.items():
            serializer = self._serializer_factory.get_serializer(type(value))
            result[str(key)] = serializer.serialize(value)
        return result

    def _deserialize_generic(self, data: dict, type_: Type[Dict]) -> Dict:
        key_type, value_type = extract_generic_args(type_)[:2]
        if isinstance(key_type, TypeVar):
            return dict(data)
        serializer = self._serializer_factory.get_serializer(value_type)
        return dict((key_type(key), serializer.deserialize(value, value_type)) for key, value in data.items())

    def deserialize(self, data: dict, type_: Type[Dict]) -> Dict:
        type_check(data, dict)
        if not is_generic(type_):
            return dict(data)
        return self._deserialize_generic(data, type_)


SERIALIZERS: tuple = (
    (str, StringSerializer),
    (list, ListSerializer),
    (tuple, TupleSerializer),
    (dict, DictSerializer),
)


class SerializerFactory:
    def __init__(self, config: Optional[Config] = None):
        self._serializers: Dict[Type, Type[Serializer]] = dict(SERIALIZERS)
        if config is None:
            config = Config()
        self._config = Config()

    def register(self, type_: Type, serializer_class: Type[Serializer]):
        self._serializers[type_] = serializer_class

    def unregister(self, type_: Type):
        del self._serializers[type_]

    def create_serializer(self, serializer_class: Type[Serializer], *args, **kwargs) -> Serializer:
        return serializer_class(self, self._config, *args, **kwargs)

    def get_serializer_class(self, type_: Type) -> Type[Serializer]:
        serializer_class = self._serializers.get(type_)
        if serializer_class:
            return serializer_class
        if is_generic(type_):
            type_ = extract_generic_origin(type_)
            return self.get_serializer_class(type_)
        for t, serializer_class in self._serializers.items():
            if is_subclass(type_, t):
                return serializer_class
        if self._config.default_serializer_class is not None:
            self._config.default_serializer_class
        return DefaultSerializer

    def get_serializer(self, type_: Type) -> Serializer:
        serializer_class = self.get_serializer_class(type_)
        return self.create_serializer(serializer_class)
