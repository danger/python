from typing import Any, Iterable, List, Optional

from .models import (
    ClassDefinition,
    PropertyDefinition,
    SchemaItem,
    SchemaObject,
    SchemaReference,
    SchemaValue,
)


def unzip(iterable: Iterable[Any]) -> Iterable[Any]:
    return zip(*iterable)


def build_classes(schema: List[SchemaObject]) -> List[ClassDefinition]:
    built_classes = list(_build_class(schema_object) for schema_object in schema)
    resolved = []
    resolved_names = set()

    while len(resolved) != len(built_classes):
        unresolved = filter(lambda b: b[0].name not in resolved_names, built_classes)
        for (_class, references) in unresolved:
            if all(map(lambda r: r in resolved_names, references)):
                resolved_names.add(_class.name)
                resolved.append(_class)

    return resolved


def _build_class(object: SchemaObject) -> (ClassDefinition, List[str]):
    properties, references = unzip(
        (_build_property(property) for property in object.properties)
    )

    return (
        ClassDefinition(name=object.name, properties=list(properties)),
        list(filter(None, references)),
    )


def _build_property(item: SchemaItem) -> (PropertyDefinition, Optional[str]):
    if isinstance(item, SchemaValue):
        return (_property_from_value(item), None)
    if isinstance(item, SchemaReference):
        return (_property_from_reference(item), item.reference)


def _property_from_value(value: SchemaValue) -> PropertyDefinition:
    mappings = {"string": "str", "boolean": "bool", "number": "int"}
    return PropertyDefinition(name=value.name, value_type=mappings[value.value_type])


def _property_from_reference(reference: SchemaReference) -> PropertyDefinition:
    return PropertyDefinition(name=reference.name, value_type=reference.reference)
