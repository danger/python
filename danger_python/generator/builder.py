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
    props, refs = unzip(
        (_build_property(prop, class_name) for prop in object.properties)
    )
    definition = ClassDefinition(name=class_name, properties=list(props))
    references = set(
        map(lambda p: p.value_type, filter(lambda p: not p.known_type, props))
    )

    types = [(definition, references)]
    types.extend(_build_nested_enums(object, class_name))
    types.extend(_build_nested_objects(object, class_name))

    return types


def _build_nested_enums(
    object: SchemaObject, parent_class_name: str
) -> Iterable[Tuple[TypeDefinition, Set[str]]]:
    def build_enum(schema: SchemaEnum) -> EnumDefinition:
        type_name = _nested_object_name(schema, parent_class_name)
        values = list(map(lambda v: (stringcase.constcase(v), v), schema.values))
        return EnumDefinition(name=type_name, values=values)

    return map(
        lambda e: (e, set()),
        map(build_enum, filter(lambda p: isinstance(p, SchemaEnum), object.properties)),
    )


def _build_nested_objects(
    object: SchemaObject, parent_class_name: str
) -> Iterable[Tuple[TypeDefinition, Set[str]]]:
    return chain.from_iterable(
        map(
            lambda o: _build_types(o, parent_class_name),
            filter(lambda p: isinstance(p, SchemaObject), object.properties),
        )
    )


def _build_property(
    item: SchemaItem, class_name: str
) -> (PropertyDefinition, Optional[str]):
    if isinstance(item, SchemaReference):
        property = _property(item.name, item.reference, False)
        return (property, property.value_type)
    if isinstance(item, SchemaEnum) or isinstance(item, SchemaObject):
        property = _property_from_object(item, class_name)
        return (property, property.value_type)

    return (_property_from_value(item), None)


def _property_from_value(value: SchemaValue) -> PropertyDefinition:
    mappings = {"string": "str", "boolean": "bool", "number": "int"}
    return _property(value.name, mappings[value.value_type], True)


def _property_from_object(object: SchemaObject, parent_name: str) -> PropertyDefinition:
    type_name = _nested_object_name(object, parent_name)
    return _property(object.name, type_name, False)


def _property(name: str, type_name: str, known_type: bool) -> PropertyDefinition:
    return PropertyDefinition(
        name=stringcase.snakecase(name), value_type=type_name, known_type=known_type
    )


def _nested_object_name(parent_object: SchemaItem, prefix: Optional[str] = None) -> str:
    object_name = stringcase.pascalcase(parent_object.name)
    return f"{prefix}{object_name}" if prefix else object_name
