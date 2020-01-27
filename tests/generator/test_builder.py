from danger_python.generator.builder import build_classes
from danger_python.generator.models import (ClassDefinition,
                                            PropertyDefinition, SchemaObject,
                                            SchemaReference, SchemaValue)


def test_class_builder_builds_correct_model_for_simple_class():
    """
    Test class builder builds correct model for simple class.
    """
    schema = [
        SchemaObject(
            name="TestClass",
            properties=[
                SchemaValue(name="string_value", value_type="string"),
                SchemaValue(name="boolean_value", value_type="boolean"),
            ],
        )
    ]

    build_result = build_classes(schema)

    assert len(build_result) == 1
    assert build_result[0] == ClassDefinition(
        name="TestClass",
        properties=[
            PropertyDefinition(name="string_value", value_type="str"),
            PropertyDefinition(name="boolean_value", value_type="bool"),
        ],
    )


def test_class_builder_handles_reference_types():
    """
    Test class builder handles reference types correctly.
    """
    schema = [
        SchemaObject(
            name="ObjectA",
            properties=[SchemaReference(name="ref_b", reference="ObjectB")],
        ),
        SchemaObject(
            name="ObjectB",
            properties=[SchemaReference(name="ref_c", reference="ObjectC")],
        ),
        SchemaObject(
            name="ObjectC",
            properties=[SchemaValue(name="int_value", value_type="number")],
        ),
    ]

    build_result = build_classes(schema)

    assert len(build_result) == 3
    assert build_result[0] == ClassDefinition(
        name="ObjectC",
        properties=[PropertyDefinition(name="int_value", value_type="int")],
    )
    assert build_result[1] == ClassDefinition(
        name="ObjectB",
        properties=[PropertyDefinition(name="ref_c", value_type="ObjectC")],
    )
    assert build_result[2] == ClassDefinition(
        name="ObjectA",
        properties=[PropertyDefinition(name="ref_b", value_type="ObjectB")],
    )
