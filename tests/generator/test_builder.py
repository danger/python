from danger_python.generator.builder import build_types
from danger_python.generator.models import (
    ClassDefinition,
    EnumDefinition,
    PropertyDefinition,
    SchemaEnum,
    SchemaObject,
    SchemaReference,
    SchemaValue,
)


def test_type_builder_builds_correct_model_for_simple_class():
    """
    Test type builder builds correct model for simple class.
    """
    schema = [
        SchemaObject(
            name="TestClass",
            properties=[
                SchemaValue(name="stringValue", value_type="string"),
                SchemaValue(name="booleanValue", value_type="boolean"),
            ],
        )
    ]

    build_result = build_types(schema)

    assert len(build_result) == 1
    assert build_result[0] == ClassDefinition(
        name="TestClass",
        properties=[
            PropertyDefinition(name="string_value", value_type="str", known_type=True),
            PropertyDefinition(
                name="boolean_value", value_type="bool", known_type=True
            ),
        ],
    )


def test_type_builder_handles_reference_types():
    """
    Test type builder handles reference types correctly.
    """
    schema = [
        SchemaObject(
            name="ObjectA",
            properties=[SchemaReference(name="refB", reference="ObjectB")],
        ),
        SchemaObject(
            name="ObjectB",
            properties=[SchemaReference(name="refC", reference="ObjectC")],
        ),
        SchemaObject(
            name="ObjectC",
            properties=[SchemaValue(name="intValue", value_type="number")],
        ),
    ]

    build_result = build_types(schema)

    assert len(build_result) == 3
    assert build_result[0] == ClassDefinition(
        name="ObjectC",
        properties=[
            PropertyDefinition(name="int_value", value_type="int", known_type=True)
        ],
    )
    assert build_result[1] == ClassDefinition(
        name="ObjectB",
        properties=[
            PropertyDefinition(name="ref_c", value_type="ObjectC", known_type=False)
        ],
    )
    assert build_result[2] == ClassDefinition(
        name="ObjectA",
        properties=[
            PropertyDefinition(name="ref_b", value_type="ObjectB", known_type=False)
        ],
    )


def test_type_builder_handles_enums():
    """
    Test type builder handles enums correctly.
    """
    schema = [
        SchemaObject(
            name="ClassWithEnums",
            properties=[
                SchemaValue(name="string_value", value_type="string"),
                SchemaEnum(
                    name="enumValue",
                    value_type="string",
                    values=["first", "second", "third"],
                ),
            ],
        )
    ]

    build_result = build_types(schema)

    assert len(build_result) == 2
    assert build_result[0] == EnumDefinition(
        name="ClassWithEnumsEnumValue",
        values=[("FIRST", "first"), ("SECOND", "second"), ("THIRD", "third")],
    )
    assert build_result[1] == ClassDefinition(
        name="ClassWithEnums",
        properties=[
            PropertyDefinition(name="string_value", value_type="str", known_type=True),
            PropertyDefinition(
                name="enum_value",
                value_type="ClassWithEnumsEnumValue",
                known_type=False,
            ),
        ],
    )


def test_type_builder_handles_nested_properties():
    """
    Test type builder handles nested properties correctly.
    """
    schema = [
        SchemaObject(
            name="ClassWithNestedClass",
            properties=[
                SchemaObject(
                    name="nestedValue",
                    properties=[
                        SchemaValue(name="string_value", value_type="string"),
                        SchemaEnum(
                            name="enum_value",
                            value_type="string",
                            values=["hey", "new", "value"],
                        ),
                    ],
                ),
            ],
        )
    ]

    build_result = build_types(schema)

    assert len(build_result) == 3
    assert build_result[0] == EnumDefinition(
        name="ClassWithNestedClassNestedValueEnumValue",
        values=[("HEY", "hey"), ("NEW", "new"), ("VALUE", "value")],
    )
    assert build_result[1] == ClassDefinition(
        name="ClassWithNestedClassNestedValue",
        properties=[
            PropertyDefinition(name="string_value", value_type="str", known_type=True),
            PropertyDefinition(
                name="enum_value",
                value_type="ClassWithNestedClassNestedValueEnumValue",
                known_type=False,
            ),
        ],
    )
    assert build_result[2] == ClassDefinition(
        name="ClassWithNestedClass",
        properties=[
            PropertyDefinition(
                name="nested_value",
                value_type="ClassWithNestedClassNestedValue",
                known_type=False,
            ),
        ],
    )
