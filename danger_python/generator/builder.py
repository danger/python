from collections import OrderedDict
from itertools import chain
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

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


def build_types(schema: List[SchemaObject]) -> List[TypeDefinition]:
    built_types = [(type, refs) for s in schema for type, refs in _build_types(s)]
    types_by_names = {type.name: type for type, _ in built_types}
    references_by_type_names = {type.name: refs for type, refs in built_types}
    sorted_types = toposort_flatten(references_by_type_names)

    return list(map(lambda t: types_by_names[t], sorted_types))


def _build_types(object: SchemaObject) -> List[Tuple[TypeDefinition, Set[str]]]:
    props, refs, enums = unzip(
        (_build_property(prop, object) for prop in object.properties)
    )
    definition = ClassDefinition(name=object.name, properties=list(props))
    types = [(definition, set(filter(None, refs)))]
    types.extend(map(lambda enum: (enum, set()), filter(None, enums)))

    return types


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
