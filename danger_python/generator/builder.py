from typing import Any, Iterable, List, Optional

from toposort import toposort_flatten

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
    classes_by_names = {_class.name: _class for _class, _ in built_classes}
    sorted_classes = toposort_flatten(
        {_class.name: set(reference) for _class, reference in built_classes}
    )

    return list(map(lambda n: classes_by_names[n], sorted_classes))


def _build_class(object: SchemaObject) -> (ClassDefinition, List[str]):
    properties, references = unzip(
        (_build_property(property) for property in object.properties)
    )

    return (
        ClassDefinition(name=object.name, properties=list(properties)),
        list(filter(None, references)),
    )


def _build_property(item: SchemaItem) -> (PropertyDefinition, Optional[str]):
    if isinstance(item, SchemaReference):
        return (_property_from_reference(item), item.reference)

    return (_property_from_value(item), None)


def _property_from_value(value: SchemaValue) -> PropertyDefinition:
    mappings = {"string": "str", "boolean": "bool", "number": "int"}
    return PropertyDefinition(name=value.name, value_type=mappings[value.value_type])


def _property_from_reference(reference: SchemaReference) -> PropertyDefinition:
    return PropertyDefinition(name=reference.name, value_type=reference.reference)
