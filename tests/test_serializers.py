from typing import Dict, List, Tuple

from jsondataclass.serializers import (
    DefaultSerializer,
    DictSerializer,
    ListSerializer,
    SerializerFactory,
    StringSerializer,
    TupleSerializer,
)


def test_default_serializer():
    serializer = DefaultSerializer()
    assert serializer.deserialize(1, int) == 1
    assert serializer.serialize(1) == 1


def test_serializer_factory_create_serializer():
    factory = SerializerFactory()
    assert isinstance(factory.create_serializer(DefaultSerializer), DefaultSerializer)


def test_serializer_factory_get_serializer_class():
    factory = SerializerFactory()
    assert factory.get_serializer_class(int) is DefaultSerializer


def test_serializer_factory_get_default_serializer():
    factory = SerializerFactory()
    assert isinstance(factory.get_serializer(int), DefaultSerializer)


def test_serializer_factory_get_string_serializer():
    factory = SerializerFactory()
    assert isinstance(factory.get_serializer(str), StringSerializer)


def test_serializer_factory_get_list_serializer():
    factory = SerializerFactory()
    assert isinstance(factory.get_serializer(list), ListSerializer)
    assert isinstance(factory.get_serializer(List), ListSerializer)
    assert isinstance(factory.get_serializer(List[int]), ListSerializer)


def test_serializer_factory_get_tuple_serializer():
    factory = SerializerFactory()
    assert isinstance(factory.get_serializer(tuple), TupleSerializer)
    assert isinstance(factory.get_serializer(Tuple), TupleSerializer)
    assert isinstance(factory.get_serializer(Tuple[int, ...]), TupleSerializer)


def test_serializer_factory_get_dict_serializer():
    factory = SerializerFactory()
    assert isinstance(factory.get_serializer(dict), DictSerializer)
    assert isinstance(factory.get_serializer(Dict), DictSerializer)
    assert isinstance(factory.get_serializer(Dict[str, int]), DictSerializer)


def test_string_serializer():
    data = "foo"
    serializer = StringSerializer()
    assert serializer.deserialize(data, str) == data
    assert serializer.serialize(data) == data


def test_list_serializer():
    data = [1, 2, 3]
    serializer = ListSerializer()
    assert serializer.deserialize(data, list) == data
    assert serializer.deserialize(data, List) == data
    assert serializer.deserialize(data, List[int]) == data
    assert serializer.deserialize(data, List[str]) == ["1", "2", "3"]
    assert serializer.serialize(data) == data


def test_tuple_serializer():
    list_data = [1, 2, 3]
    tuple_data = (1, 2, 3)
    serializer = TupleSerializer()
    assert serializer.deserialize(list_data, tuple) == tuple_data
    assert serializer.deserialize(list_data, Tuple) == tuple_data
    assert serializer.deserialize(list_data, Tuple[int, ...]) == tuple_data
    assert serializer.deserialize(list_data, Tuple[int, int, int]) == tuple_data
    assert serializer.serialize(tuple_data) == list_data


def test_dict_serializer():
    data = {"a": 1, "b": 2, "c": 3}
    serializer = DictSerializer()
    assert serializer.deserialize(data, dict) == data
    assert serializer.deserialize(data, Dict) == data
    assert serializer.deserialize(data, Dict[str, int]) == data
    assert serializer.deserialize(data, Dict[str, str]) == {"a": "1", "b": "2", "c": "3"}
    assert serializer.serialize(data) == data
