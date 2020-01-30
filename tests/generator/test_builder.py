from danger_python.generator.builder import build_types
from danger_python.generator.models import (
    ClassDefinition,
    EnumDefinition,
    PropertyDefinition,
    SchemaAllOf,
    SchemaAnyOf,
    SchemaArray,
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
                SchemaValue(name="anyValue", value_type="any"),
                SchemaValue(name="nullValue", value_type="null"),
                SchemaValue(name="optionalStringValue", value_types=["null", "string"]),
            ],
        )
    ]

    build_result = build_types(schema)

    assert len(build_result) == 1
    assert build_result[0] == ClassDefinition(
        name="TestClass",
        properties=[
            PropertyDefinition(
                name="string_value",
                key="stringValue",
                value_type="str",
                known_type=True,
            ),
            PropertyDefinition(
                name="boolean_value",
                key="booleanValue",
                value_type="bool",
                known_type=True,
            ),
            PropertyDefinition(
                name="any_value", key="anyValue", value_type="Any", known_type=True
            ),
            PropertyDefinition(
                name="null_value", key="nullValue", value_type="Any", known_type=True
            ),
            PropertyDefinition(
                name="optional_string_value",
                key="optionalStringValue",
                value_type="Optional[str]",
                known_type=True,
            ),
        ],
        depends_on=set(),
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
        name="ObjectA",
        properties=[
            PropertyDefinition(
                name="ref_b", key="refB", value_type="ObjectB", known_type=False
            )
        ],
        depends_on={"ObjectB"},
    )
    assert build_result[1] == ClassDefinition(
        name="ObjectB",
        properties=[
            PropertyDefinition(
                name="ref_c", key="refC", value_type="ObjectC", known_type=False
            )
        ],
        depends_on={"ObjectC"},
    )
    assert build_result[2] == ClassDefinition(
        name="ObjectC",
        properties=[
            PropertyDefinition(
                name="int_value", key="intValue", value_type="int", known_type=True
            )
        ],
        depends_on=set(),
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
    assert build_result[0] == ClassDefinition(
        name="ClassWithEnums",
        properties=[
            PropertyDefinition(
                name="string_value",
                key="string_value",
                value_type="str",
                known_type=True,
            ),
            PropertyDefinition(
                name="enum_value",
                key="enumValue",
                value_type="ClassWithEnumsEnumValue",
                known_type=False,
            ),
        ],
        depends_on={"ClassWithEnumsEnumValue"},
    )
    assert build_result[1] == EnumDefinition(
        name="ClassWithEnumsEnumValue",
        values=[("FIRST", "first"), ("SECOND", "second"), ("THIRD", "third")],
        depends_on=set(),
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
    assert build_result[0] == ClassDefinition(
        name="ClassWithNestedClass",
        properties=[
            PropertyDefinition(
                name="nested_value",
                key="nestedValue",
                value_type="ClassWithNestedClassNestedValue",
                known_type=False,
            ),
        ],
        depends_on={"ClassWithNestedClassNestedValue"},
    )
    assert build_result[1] == ClassDefinition(
        name="ClassWithNestedClassNestedValue",
        properties=[
            PropertyDefinition(
                name="string_value",
                key="string_value",
                value_type="str",
                known_type=True,
            ),
            PropertyDefinition(
                name="enum_value",
                key="enum_value",
                value_type="ClassWithNestedClassNestedValueEnumValue",
                known_type=False,
            ),
        ],
        depends_on={"ClassWithNestedClassNestedValueEnumValue"},
    )
    assert build_result[2] == EnumDefinition(
        name="ClassWithNestedClassNestedValueEnumValue",
        values=[("HEY", "hey"), ("NEW", "new"), ("VALUE", "value")],
        depends_on=set(),
    )


def test_type_builder_handles_all_of_references():
    """
    Test type builder handles all of references.
    """
    schema = [
        SchemaObject(
            name="ClassWithAllOf",
            properties=[
                SchemaAllOf(
                    name="authorValue",
                    all_of=[
                        SchemaReference(name="", reference="ReferencedObject"),
                        SchemaObject(
                            name="role",
                            properties=[
                                SchemaEnum(
                                    name="", value_type="string", values=["AUTHOR"]
                                ),
                            ],
                        ),
                    ],
                )
            ],
        ),
        SchemaObject(
            name="ReferencedObject",
            properties=[SchemaValue(name="stringValue", value_type="string")],
        ),
    ]

    build_result = build_types(schema)

    assert len(build_result) == 2
    assert build_result[0] == ClassDefinition(
        name="ClassWithAllOf",
        properties=[
            PropertyDefinition(
                name="author_value",
                key="authorValue",
                value_type="ReferencedObject",
                known_type=False,
            )
        ],
        depends_on={"ReferencedObject"},
    )
    assert build_result[1] == ClassDefinition(
        name="ReferencedObject",
        properties=[
            PropertyDefinition(
                name="string_value",
                key="stringValue",
                value_type="str",
                known_type=True,
            )
        ],
        depends_on=set(),
    )


def test_type_builder_handles_arrays():
    """
    Test that type builder handles arrays.
    """
    schema = [
        SchemaObject(
            name="ClassWithAllOfArray",
            properties=[
                SchemaArray(
                    name="authorsArray",
                    item=SchemaAllOf(
                        name="",
                        all_of=[
                            SchemaReference(name="", reference="SomeOtherObject"),
                            SchemaObject(
                                name="role",
                                properties=[
                                    SchemaEnum(
                                        name="",
                                        value_type="string",
                                        values=["PARTICIPANT"],
                                    )
                                ],
                            ),
                        ],
                    ),
                )
            ],
        ),
        SchemaObject(
            name="SomeOtherObject",
            properties=[SchemaValue(name="anyProperty", value_type="number")],
        ),
        SchemaObject(
            name="ClassWithPropertyArray",
            properties=[
                SchemaArray(
                    name="propertiesArray",
                    item=SchemaObject(
                        name="",
                        properties=[
                            SchemaValue(name="firstField", value_type="string"),
                            SchemaValue(name="secondField", value_type="number"),
                        ],
                    ),
                )
            ],
        ),
    ]

    build_result = build_types(schema)

    assert len(build_result) == 4
    assert build_result[0] == ClassDefinition(
        name="ClassWithAllOfArray",
        properties=[
            PropertyDefinition(
                name="authors_array",
                key="authorsArray",
                value_type="List[SomeOtherObject]",
                known_type=False,
            )
        ],
        depends_on={"SomeOtherObject"},
    )
    assert build_result[1] == ClassDefinition(
        name="ClassWithPropertyArray",
        properties=[
            PropertyDefinition(
                name="properties_array",
                key="propertiesArray",
                value_type="List[ClassWithPropertyArrayPropertiesArray]",
                known_type=False,
            )
        ],
        depends_on={"ClassWithPropertyArrayPropertiesArray"},
    )
    assert build_result[2] == ClassDefinition(
        name="ClassWithPropertyArrayPropertiesArray",
        properties=[
            PropertyDefinition(
                name="first_field", key="firstField", value_type="str", known_type=True
            ),
            PropertyDefinition(
                name="second_field",
                key="secondField",
                value_type="int",
                known_type=True,
            ),
        ],
        depends_on=set(),
    )
    assert build_result[3] == ClassDefinition(
        name="SomeOtherObject",
        properties=[
            PropertyDefinition(
                name="any_property",
                key="anyProperty",
                value_type="int",
                known_type=True,
            )
        ],
        depends_on=set(),
    )


def test_type_builder_handles_top_level_enumerations():
    """
    Test type builder handles top-level enumerations.
    """
    schema = [
        SchemaEnum(name="TestEnum", value_type="string", values=["a", "b", "c"]),
    ]

    build_result = build_types(schema)

    assert len(build_result) == 1
    assert build_result[0] == EnumDefinition(
        name="TestEnum", values=[("A", "a"), ("B", "b"), ("C", "c")], depends_on=set(),
    )


def test_type_builder_handles_enumerations_with_uppercase_values():
    """
    Test type builder handles enumerations with uppercase values.
    """
    schema = [
        SchemaEnum(
            name="UppercaseEnum",
            value_type="string",
            values=["HELLO_WORLD", "UPPERCASE_VALUE", "SOME_VALUE"],
        ),
    ]

    build_result = build_types(schema)

    assert len(build_result) == 1
    assert build_result[0] == EnumDefinition(
        name="UppercaseEnum",
        values=[
            ("HELLO_WORLD", "HELLO_WORLD"),
            ("UPPERCASE_VALUE", "UPPERCASE_VALUE"),
            ("SOME_VALUE", "SOME_VALUE"),
        ],
        depends_on=set(),
    )


def test_type_builder_handles_optional_references():
    """
    Test type builder handles optional references.
    """
    schema = [
        SchemaObject(
            name="ObjectA",
            properties=[
                SchemaAnyOf(
                    name="refB",
                    any_of=[
                        SchemaReference(name="refB", reference="ObjectB"),
                        SchemaValue(name="refB", value_type="null"),
                    ],
                )
            ],
        ),
        SchemaObject(
            name="ObjectB",
            properties=[SchemaValue(name="strField", value_type="string")],
        ),
    ]

    build_result = build_types(schema)

    assert len(build_result) == 2
    assert build_result[0] == ClassDefinition(
        name="ObjectA",
        properties=[
            PropertyDefinition(
                name="ref_b",
                key="refB",
                value_type="Optional[ObjectB]",
                known_type=False,
            )
        ],
        depends_on={"ObjectB"},
    )
    assert build_result[1] == ClassDefinition(
        name="ObjectB",
        properties=[
            PropertyDefinition(
                name="str_field", key="strField", value_type="str", known_type=True
            )
        ],
        depends_on=set(),
    )


def test_type_builder_resolves_union_types_to_any():
    """
    Test type builder resolves union types to Any.
    """
    schema = [
        SchemaObject(
            name="ObjectA",
            properties=[
                SchemaAnyOf(
                    name="refB",
                    any_of=[
                        SchemaReference(name="refB", reference="ObjectB"),
                        SchemaValue(name="refB", value_type="str"),
                    ],
                )
            ],
        ),
        SchemaObject(
            name="ObjectB",
            properties=[SchemaValue(name="strField", value_type="string")],
        ),
    ]

    build_result = build_types(schema)

    assert len(build_result) == 2
    assert build_result[0] == ClassDefinition(
        name="ObjectA",
        properties=[
            PropertyDefinition(
                name="ref_b", key="refB", value_type="Any", known_type=True,
            )
        ],
        depends_on=set(),
    )
    assert build_result[1] == ClassDefinition(
        name="ObjectB",
        properties=[
            PropertyDefinition(
                name="str_field", key="strField", value_type="str", known_type=True
            )
        ],
        depends_on=set(),
    )
