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


def build_types(schema: List[SchemaObject]) -> List[TypeDefinition]:
    built_types = list(chain.from_iterable(map(_build_types_for_object, schema)))
    types_by_names = {type.name: type for type in built_types}
    references_by_type_names = {type.name: type.depends_on for type in built_types}
    sorted_types = toposort_flatten(references_by_type_names)

    return list(map(lambda t: types_by_names[t], sorted_types))


def _build_types_for_object(
    object: SchemaObject, prefix: Optional[str] = None
) -> List[TypeDefinition]:
    class_name = _nested_object_name(object, prefix)
    properties = [_build_property(p, class_name) for p in object.properties]
    definition = ClassDefinition(
        name=class_name,
        properties=properties,
        depends_on=set(
            map(lambda p: p.value_type, filter(lambda p: not p.known_type, properties))
        ),
    )

    types = [definition]
    types.extend(_build_nested_enums(object, class_name))
    types.extend(_build_nested_objects(object, class_name))

    return types


def _build_nested_enums(
    object: SchemaObject, parent_class_name: str
) -> Iterable[TypeDefinition]:
    def build_enum(schema: SchemaEnum) -> EnumDefinition:
        type_name = _nested_object_name(schema, parent_class_name)
        values = list(map(lambda v: (stringcase.constcase(v), v), schema.values))
        return EnumDefinition(name=type_name, values=values, depends_on=set())

    return map(
        build_enum, filter(lambda p: isinstance(p, SchemaEnum), object.properties)
    )


def _build_nested_objects(
    object: SchemaObject, parent_class_name: str
) -> Iterable[TypeDefinition]:
    return chain.from_iterable(
        map(
            lambda o: _build_types_for_object(o, parent_class_name),
            filter(lambda p: isinstance(p, SchemaObject), object.properties),
        )
    )


def _build_property(item: SchemaItem, parent_class_name: str) -> PropertyDefinition:
    if isinstance(item, SchemaReference):
        return _property(item.name, item.reference, False)
    if isinstance(item, SchemaEnum) or isinstance(item, SchemaObject):
        return _property_from_object(item, parent_class_name)

    return _property_from_value(item)


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
