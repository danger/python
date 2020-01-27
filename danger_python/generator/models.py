from dataclasses import dataclass, field
from typing import Any, List, Tuple


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


@dataclass
class PropertyDefinition:
    name: str
    value_type: str
    known_type: bool


@dataclass
class TypeDefinition:
    name: str


@dataclass
class ClassDefinition(TypeDefinition):
    properties: List[PropertyDefinition] = field(default_factory=list)


@dataclass
class EnumDefinition(TypeDefinition):
    values: List[Tuple[str, str]] = field(default_factory=list)
