from jsondataclass.serializers import DefaultSerializer, SerializerFactory


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
