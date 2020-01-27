from collections import OrderedDict
from itertools import chain
from typing import Any, Dict, Iterable, List, Optional, Set

import stringcase
from toposort import toposort_flatten

from .models import (
    ClassDefinition,
    EnumDefinition,
    PropertyDefinition,
    SchemaEnum,
    SchemaItem,
    SchemaObject,
    SchemaReference,
    SchemaValue,
    TypeDefinition,
)


def unzip(iterable: Iterable[Any]) -> Iterable[Any]:
    return zip(*iterable)


def build_classes(schema: List[SchemaObject]) -> List[TypeDefinition]:
    classes, references, enums = unzip(map(_build_class, schema))
    references_by_names = _group_references_by_names(classes, references)
    types_by_names = _group_types_by_names(classes, enums)
    references_by_type_names = {
        type_name: references_by_names.get(type_name, set())
        for type_name in types_by_names
    }

    sorted_types = toposort_flatten(references_by_type_names)
    return list(map(lambda t: types_by_names[t], sorted_types))


def _group_references_by_names(
    classes: List[ClassDefinition], references: List[List[str]]
) -> Dict[str, Set[str]]:
    return {_class.name: set(refs) for _class, refs in zip(classes, references)}


def _group_types_by_names(
    classes: List[ClassDefinition], enums: List[List[EnumDefinition]]
) -> Dict[str, TypeDefinition]:
    class_names = map(lambda _class: (_class.name, _class), classes)
    enum_names = map(
        lambda enum: (enum.name, enum), [enum for inner in enums for enum in inner]
    )
    return OrderedDict(chain(class_names, enum_names))


def _build_class(
    object: SchemaObject,
) -> (ClassDefinition, List[str], List[EnumDefinition]):
    properties, references, enums = unzip(
        (_build_property(property, object) for property in object.properties)
    )

    return (
        ClassDefinition(name=object.name, properties=list(properties)),
        list(filter(None, references)),
        list(filter(None, enums)),
    )


def _build_property(
    item: SchemaItem, object: SchemaObject
) -> (PropertyDefinition, Optional[str], Optional[EnumDefinition]):
    if isinstance(item, SchemaReference):
        return (_property_from_reference(item), item.reference, None)
    if isinstance(item, SchemaEnum):
        property, enum = _property_from_enum(item, object.name)
        return (property, enum.name, enum)

    return (_property_from_value(item), None, None)


def _property_from_value(value: SchemaValue) -> PropertyDefinition:
    mappings = {"string": "str", "boolean": "bool", "number": "int"}
    return PropertyDefinition(name=value.name, value_type=mappings[value.value_type])


def _property_from_reference(reference: SchemaReference) -> PropertyDefinition:
    return PropertyDefinition(name=reference.name, value_type=reference.reference)


def _property_from_enum(
    enum: SchemaEnum, class_name: str
) -> (PropertyDefinition, EnumDefinition):
    type_name = class_name + stringcase.pascalcase(enum.name)
    values = list(map(lambda v: (stringcase.constcase(v), v), enum.values))

    return (
        PropertyDefinition(name=enum.name, value_type=type_name),
        EnumDefinition(name=type_name, values=values),
    )
