from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class SchemaItem:
    name: str


@dataclass
class SchemaObject(SchemaItem):
    properties: List["SchemaItem"] = field(default_factory=list)


@dataclass
class SchemaValue(SchemaItem):
    value_type: str


@dataclass
class SchemaReference(SchemaItem):
    reference: str


@dataclass
class SchemaEnum(SchemaValue):
    values: List[Any] = field(default_factory=list)


@dataclass
class SchemaArray(SchemaItem):
    item: SchemaItem


@dataclass
class SchemaAllOf(SchemaItem):
    all_of: [SchemaItem]
