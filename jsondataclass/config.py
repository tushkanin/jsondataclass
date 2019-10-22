from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .serializers import Serializer  # noqa: F401


def _default_serializer():
    from .serializers import DefaultSerializer

    return DefaultSerializer


@dataclass
class Config:
    default_serializer_class: "Serializer" = field(default_factory=_default_serializer)
