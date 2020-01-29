from dataclasses import InitVar, dataclass, field
from typing import Any, List, Optional, Set, Tuple


@dataclass
class SchemaItem:
    name: str


@dataclass
class SchemaObject(SchemaItem):
    properties: List["SchemaItem"] = field(default_factory=list)


@dataclass
class SchemaValue(SchemaItem):
    value_types: List[str] = field(default_factory=list)
    value_type: InitVar[str] = None

    def __post_init__(self, value_type: Optional[str]):
        if value_type:
            self.value_types = [value_type]


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

    @property
    def formatted_type(self) -> str:
        prefixes = {"List[", "Optional["}
        prefix = next(filter(lambda p: self.value_type.startswith(p), prefixes), None)

        if self.known_type:
            return self.value_type
        elif prefix:
            stripped = self.value_type[len(prefix) : -1]
            return f"{prefix}'{stripped}']"
        else:
            return f"'{self.value_type}'"

    @property
    def non_reserved_name(self) -> str:
        reserved_names = {"from", "self"}
        return f"{self.name}_" if self.name in reserved_names else self.name


@dataclass
class TypeDefinition:
    name: str
    depends_on: Set["TypeDefinition"] = field(default_factory=set)


@dataclass
class ClassDefinition(TypeDefinition):
    properties: List[PropertyDefinition] = field(default_factory=list)


@dataclass
class EnumDefinition(TypeDefinition):
    values: List[Tuple[str, str]] = field(default_factory=list)
