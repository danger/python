import json
from typing import Any, Dict, List, Optional

from .models import (
    SchemaAllOf,
    SchemaAnyOf,
    SchemaArray,
    SchemaEnum,
    SchemaItem,
    SchemaObject,
    SchemaReference,
    SchemaValue,
)


def parse_schema(schema: str) -> List[SchemaItem]:
    objects = json.loads(schema).get("definitions", {})
    return _parse_items(objects)


def _parse_items(json: Dict[str, Any]) -> List[SchemaItem]:
    keys = sorted(json.keys())
    return list(filter(None, (_parse_item(name, json[name]) for name in keys)))


def _parse_item(name: str, json: Dict[str, Any]) -> SchemaItem:
    parsers = (
        _parse_object,
        _parse_enum,
        _parse_reference,
        _parse_array,
        _parse_all_of,
        _parse_any_of,
        _parse_value,
    )
    values = filter(None, map(lambda p: p(name, json), parsers))
    return next(values)


def _parse_object(name: str, json: Dict[str, Any]) -> Optional[SchemaObject]:
    if json.get("type", None) == "object":
        properties = _parse_items(json.get("properties", {}))
        return SchemaObject(name=name, properties=properties)

    return None


def _parse_value(name: str, json: Dict[str, Any]) -> SchemaValue:
    value_types = json.get("type", None)
    if value_types:
        value_types = value_types if isinstance(value_types, list) else [value_types]
        return SchemaValue(name=name, value_types=value_types)

    return SchemaValue(name=name, value_type="any")


def _parse_reference(name: str, json: Dict[str, Any]) -> Optional[SchemaReference]:
    if json.get("$ref", None):
        reference = json["$ref"].split("#/definitions/")[-1]
        return SchemaReference(name=name, reference=reference)

    return None


def _parse_enum(name: str, json: Dict[str, Any]) -> Optional[SchemaEnum]:
    if json.get("enum", None):
        return SchemaEnum(name=name, value_type=json["type"], values=json["enum"])

    return None


def _parse_array(name: str, json: Dict[str, Any]) -> Optional[SchemaArray]:
    if json.get("type", None) == "array":
        return SchemaArray(name=name, item=_parse_item("", json.get("items", {})))

    return None


def _parse_all_of(name: str, json: Dict[str, Any]) -> Optional[SchemaAllOf]:
    if json.get("allOf", None):
        items = [_parse_item(name, item) for item in json["allOf"]]
        return SchemaAllOf(name=name, all_of=items)

    return None


def _parse_any_of(name: str, json: Dict[str, Any]) -> Optional[SchemaAnyOf]:
    if json.get("anyOf", None):
        items = [_parse_item(name, item) for item in json["anyOf"]]
        return SchemaAnyOf(name=name, any_of=items)

    return None
