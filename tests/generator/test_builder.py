from danger_python.generator.builder import build_classes
from danger_python.generator.models import (
    ClassDefinition,
    PropertyDefinition,
    SchemaObject,
    SchemaValue,
)


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
