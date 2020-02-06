from functools import reduce
from itertools import chain
from operator import attrgetter
from typing import Iterable, List, Optional

import stringcase

from .models import (
    ClassDefinition,
    EnumDefinition,
    PropertyDefinition,
    SchemaAllOf,
    SchemaAnyOf,
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
    return sorted(built_types, key=attrgetter("name"))


def _normalize_typename(typename: str) -> str:
    prefixes = {"List[", "Optional["}
    prefix = next(filter(lambda p: typename.startswith(p), prefixes), None)
    return typename[len(prefix) : -1] if prefix else typename


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
    def format_case(enum_case: str) -> str:
        return stringcase.constcase(enum_case.lower())

    type_name = _nested_object_name(schema, prefix)
    values = list(map(lambda v: (format_case(v), v), schema.values))
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

    types: List[TypeDefinition] = [definition]
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
    if isinstance(item, SchemaAnyOf):
        first_item = item.any_of[0]
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
    if isinstance(item, SchemaAnyOf):
        return _property_from_any_of(item, parent_class_name)
    if isinstance(item, SchemaValue):
        return _property_from_value(item)
    else:
        raise ValueError(f"Unknown SchemaItem type: {item.__class__.__name__}")


def _property_from_value(value: SchemaValue) -> PropertyDefinition:
    return _property(value.name, _resolve_type(value.value_types), True)


def _resolve_type(value_types: List[str]) -> str:
    mappings = {
        "string": "str",
        "boolean": "bool",
        "number": "int",
        "any": "Any",
        "null": "Any",
    }

    real_type = next(filter(lambda v: v != "null", value_types), "null")
    real_type = mappings[real_type]

    if "null" in value_types and len(value_types) > 1:
        real_type = f"Optional[{real_type}]"

    return real_type


def _property_from_object(object: SchemaItem, parent_name: str) -> PropertyDefinition:
    type_name = _nested_object_name(object, parent_name)
    return _property(object.name, type_name, False)


def _property_from_array(object: SchemaArray, parent_name: str) -> PropertyDefinition:
    nested_property = _build_property(_item_for_nesting(object), parent_name)
    return _property(
        name=object.name,
        type_name=f"List[{nested_property.value_type}]",
        known_type=nested_property.known_type,
    )


def _property_from_any_of(object: SchemaAnyOf, parent_name: str) -> PropertyDefinition:
    def is_null(item: SchemaItem) -> bool:
        return isinstance(item, SchemaValue) and item.value_types == ["null"]

    nested_property = _build_property(_item_for_nesting(object), parent_name)
    is_optional = any(map(is_null, object.any_of))

    if is_optional:
        return _property(
            name=object.name,
            type_name=f"Optional[{nested_property.value_type}]",
            known_type=nested_property.known_type,
        )
    else:
        return _property(name=object.name, type_name="Any", known_type=True)


def _property(name: str, type_name: str, known_type: bool) -> PropertyDefinition:
    name_patches = {"ID": "Id", "URL": "Url", "PR": "Pr", "DEFAULTS": "defaults"}
    patched_name = reduce(
        lambda n, p: n.replace(p[0], p[1]), name_patches.items(), name
    )
    return PropertyDefinition(
        name=stringcase.snakecase(patched_name),
        key=name,
        value_type=type_name,
        known_type=known_type,
    )


def _nested_object_name(parent_object: SchemaItem, prefix: Optional[str] = None) -> str:
    object_name = stringcase.pascalcase(parent_object.name)
    return f"{prefix}{object_name}" if prefix else object_name
