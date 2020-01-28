from collections import OrderedDict
from itertools import chain
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

import stringcase
from toposort import toposort_flatten

from .models import (
    ClassDefinition,
    EnumDefinition,
    PropertyDefinition,
    SchemaAllOf,
    SchemaArray,
    SchemaEnum,
    SchemaItem,
    SchemaObject,
    SchemaReference,
    SchemaValue,
    TypeDefinition,
)


def build_types(schema: List[SchemaItem]) -> List[TypeDefinition]:
    built_types = list(chain.from_iterable(map(_build_types_for_item, schema)))
    types_by_names = {type.name: type for type in built_types}
    references_by_type_names = {type.name: type.depends_on for type in built_types}
    sorted_types = toposort_flatten(references_by_type_names)

    return list(map(lambda t: types_by_names[_normalize_typename(t)], sorted_types))


def _normalize_typename(typename: str) -> str:
    return typename[5:-1] if typename.startswith("List[") else typename


def _build_types_for_item(
    item: SchemaItem, prefix: Optional[str] = None
) -> List[TypeDefinition]:
    if isinstance(item, SchemaEnum):
        return _build_types_for_enum(item, prefix)
    elif isinstance(item, SchemaObject):
        return _build_types_for_class(item, prefix)
    else:
        return []


def _build_types_for_enum(
    schema: SchemaEnum, prefix: Optional[str] = None
) -> List[TypeDefinition]:
    type_name = _nested_object_name(schema, prefix)
    values = list(map(lambda v: (stringcase.constcase(v), v), schema.values))
    return [EnumDefinition(name=type_name, values=values, depends_on=set())]


def _build_types_for_class(
    object: SchemaObject, prefix: Optional[str] = None
) -> List[TypeDefinition]:
    class_name = _nested_object_name(object, prefix)
    properties = [_build_property(p, class_name) for p in object.properties]
    depends_on = map(
        lambda p: _normalize_typename(p.value_type),
        filter(lambda p: not p.known_type, properties),
    )
    definition = ClassDefinition(
        name=class_name, properties=properties, depends_on=set(depends_on)
    )

    types = [definition]
    types.extend(_build_nested_objects(object, class_name))

    return types


def _build_nested_objects(
    object: SchemaObject, parent_class_name: str
) -> Iterable[TypeDefinition]:
    return chain.from_iterable(
        map(
            lambda p: _build_types_for_item(_item_for_nesting(p), parent_class_name),
            object.properties,
        )
    )


def _item_for_nesting(item: SchemaItem) -> SchemaItem:
    if isinstance(item, SchemaArray):
        item.item.name = item.name
        return _item_for_nesting(item.item)
    if isinstance(item, SchemaAllOf):
        first_item = item.all_of[0]
        first_item.name = item.name
        return _item_for_nesting(first_item)
    else:
        return item


def _build_property(item: SchemaItem, parent_class_name: str) -> PropertyDefinition:
    if isinstance(item, SchemaReference):
        return _property(item.name, item.reference, False)
    if isinstance(item, SchemaEnum) or isinstance(item, SchemaObject):
        return _property_from_object(item, parent_class_name)
    if isinstance(item, SchemaAllOf):
        return _build_property(_item_for_nesting(item), parent_class_name)
    if isinstance(item, SchemaArray):
        return _property_from_array(item, parent_class_name)

    return _property_from_value(item)


def _property_from_value(value: SchemaValue) -> PropertyDefinition:
    mappings = {"string": "str", "boolean": "bool", "number": "int"}
    return _property(value.name, mappings[value.value_types[0]], True)


def _property_from_object(object: SchemaObject, parent_name: str) -> PropertyDefinition:
    type_name = _nested_object_name(object, parent_name)
    return _property(object.name, type_name, False)


def _property_from_array(object: SchemaArray, parent_name: str) -> PropertyDefinition:
    nested_property = _build_property(_item_for_nesting(object), parent_name)
    return _property(
        name=object.name,
        type_name=f"List[{nested_property.value_type}]",
        known_type=nested_property.known_type,
    )


def _property(name: str, type_name: str, known_type: bool) -> PropertyDefinition:
    return PropertyDefinition(
        name=stringcase.snakecase(name), value_type=type_name, known_type=known_type
    )


def _nested_object_name(parent_object: SchemaItem, prefix: Optional[str] = None) -> str:
    object_name = stringcase.pascalcase(parent_object.name)
    return f"{prefix}{object_name}" if prefix else object_name
