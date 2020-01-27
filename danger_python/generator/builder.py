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


def _build_types(
    object: SchemaObject, prefix: Optional[str] = None
) -> List[Tuple[TypeDefinition, Set[str]]]:
    class_name = _nested_object_name(object, prefix)
    props, refs, enums = unzip(
        (_build_property(prop, class_name) for prop in object.properties)
    )
    definition = ClassDefinition(name=class_name, properties=list(props))
    types = [(definition, set(filter(None, refs)))]
    types.extend(map(lambda enum: (enum, set()), filter(None, enums)))

    nested_objects = filter(lambda p: isinstance(p, SchemaObject), object.properties)
    for object in nested_objects:
        types.extend(_build_types(object, prefix=class_name))

    return types


def _build_property(
    item: SchemaItem, class_name: str
) -> (PropertyDefinition, Optional[str], Optional[EnumDefinition]):
    if isinstance(item, SchemaReference):
        return (_property_from_reference(item), item.reference, None)
    if isinstance(item, SchemaEnum):
        property, enum = _property_from_enum(item, class_name)
        return (property, enum.name, enum)
    if isinstance(item, SchemaObject):
        property, reference = _property_from_object(item, class_name)
        return (property, reference, None)

    return (_property_from_value(item), None, None)


def _property_from_value(value: SchemaValue) -> PropertyDefinition:
    mappings = {"string": "str", "boolean": "bool", "number": "int"}
    return _property(value.name, mappings[value.value_type])


def _property_from_reference(reference: SchemaReference) -> PropertyDefinition:
    return _property(reference.name, reference.reference)


def _property_from_enum(
    enum: SchemaEnum, class_name: str
) -> (PropertyDefinition, EnumDefinition):
    type_name = _nested_object_name(enum, class_name)
    values = list(map(lambda v: (stringcase.constcase(v), v), enum.values))

    return (
        _property(enum.name, type_name),
        EnumDefinition(name=type_name, values=values),
    )


def _property_from_object(
    object: SchemaObject, prefix: str
) -> (PropertyDefinition, str):
    type_name = _nested_object_name(object, prefix)
    return (_property(object.name, type_name), type_name)


def _property(name: str, type_name: str) -> PropertyDefinition:
    return PropertyDefinition(name=stringcase.snakecase(name), value_type=type_name)


def _nested_object_name(parent_object: SchemaItem, prefix: Optional[str] = None) -> str:
    object_name = stringcase.pascalcase(parent_object.name)

    if prefix:
        return f"{prefix}{object_name}"
    else:
        return object_name
