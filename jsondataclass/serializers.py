from abc import abstractmethod
from typing import Any, Dict, Generic, Optional, Type, TypeVar

from .config import Config
from .utils import extract_generic_origin, is_generic, is_subclass

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


SERIALIZERS: tuple = tuple()


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
