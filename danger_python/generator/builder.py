from typing import List

from .models import (
    ClassDefinition,
    PropertyDefinition,
    SchemaItem,
    SchemaObject,
    SchemaValue,
)


def build_classes(schema: List[SchemaObject]) -> List[ClassDefinition]:
    return [_build_class(schema_object) for schema_object in schema]


def _build_class(object: SchemaObject) -> ClassDefinition:
    return ClassDefinition(
        name=object.name,
        properties=[_build_property(property) for property in object.properties],
    )


def _build_property(item: SchemaItem) -> PropertyDefinition:
    if isinstance(item, SchemaValue):
        return _property_from_value(item)


def _property_from_value(value: SchemaValue) -> PropertyDefinition:
    mappings = {"string": "str", "boolean": "bool"}
    return PropertyDefinition(name=value.name, value_type=mappings[value.value_type])
