import pytest

from danger_python.generator.models import (
    SchemaAllOf,
    SchemaArray,
    SchemaEnum,
    SchemaObject,
    SchemaReference,
    SchemaValue,
)
from danger_python.generator.parser import parse_schema


def test_schema_parser_parses_definitions():
    """
    Test that schema parser parses definitions.
    """
    schema = """{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "definitions": {
            "BitBucketCloudCommitsLinks": {
                "properties": {
                    "html": {
                        "properties": {
                            "href": {
                                "type": "string"
                            }
                        },
                        "type": "object"
                    },
                    "ref_property": {
                        "$ref": "#/definitions/BitBucketCloudPRDSL"
                    }
                },
                "type": "object"
            },
            "EnumType": {
                "properties": {
                    "enum_property": {
                        "enum": [
                            "NORMAL",
                            "SERVICE"
                        ],
                        "type": "string"
                    },
                    "arr_property": {
                        "items": {
                            "$ref": "#/definitions/SomeDefinition"
                        },
                        "type": "array"
                    }
                },
                "type": "object"
            },
            "AllOfArrayType": {
                "properties": {
                    "all_of_array": {
                        "items": {
                            "allOf": [
                                {
                                    "$ref": "#/definitions/SomeReference"
                                },
                                {
                                    "properties": {
                                        "role": {
                                            "enum": [
                                                "AUTHOR"
                                            ],
                                            "type": "string"
                                        }
                                    },
                                    "type": "object"
                                }
                            ]
                        },
                        "type": "array"
                    }
                },
                "type": "object"
            }
        }
    }"""

    definitions = parse_schema(schema)

    assert len(definitions) == 3
    assert definitions == [
        SchemaObject(
            name="AllOfArrayType",
            properties=[
                SchemaArray(
                    name="all_of_array",
                    item=SchemaAllOf(
                        name="",
                        all_of=[
                            SchemaReference(name="", reference="SomeReference"),
                            SchemaObject(
                                name="",
                                properties=[
                                    SchemaEnum(
                                        name="role",
                                        value_type="string",
                                        values=["AUTHOR"],
                                    )
                                ],
                            ),
                        ],
                    ),
                )
            ],
        ),
        SchemaObject(
            name="BitBucketCloudCommitsLinks",
            properties=[
                SchemaObject(
                    name="html",
                    properties=[SchemaValue(name="href", value_type="string"),],
                ),
                SchemaReference(name="ref_property", reference="BitBucketCloudPRDSL"),
            ],
        ),
        SchemaObject(
            name="EnumType",
            properties=[
                SchemaArray(
                    name="arr_property",
                    item=SchemaReference(name="", reference="SomeDefinition"),
                ),
                SchemaEnum(
                    name="enum_property",
                    value_type="string",
                    values=["NORMAL", "SERVICE"],
                ),
            ],
        ),
    ]


def test_schema_parser_parses_real_schema():
    """
    Test schema parser parses real schema.
    """
    with open("tests/fixtures/input_schema.json", "r") as input_schema:
        parsed_schema = parse_schema(input_schema.read())

    assert len(parsed_schema) == 52
