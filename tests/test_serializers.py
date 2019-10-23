from typing import List

from jsondataclass.serializers import DefaultSerializer, ListSerializer, SerializerFactory, StringSerializer


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
