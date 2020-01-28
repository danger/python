from danger_python.generator.models import (ClassDefinition, EnumDefinition,
                                            PropertyDefinition, TypeDefinition)
from danger_python.generator.renderer import render_classes


def test_renderer_renders_definitions_correctly():
    """
    Test that renderer renders definitions correctly.
    """
    to_render = [
        EnumDefinition(
            name="SomeNiceEnum",
            depends_on=set(),
            values=[("FIRST_VALUE", "first_value"), ("SECOND_VALUE", "second_value")],
        ),
        ClassDefinition(
            name="APythonClass",
            depends_on=set(),
            properties=[
                PropertyDefinition(
                    name="string_val", value_type="str", known_type=True
                ),
                PropertyDefinition(name="int_val", value_type="int", known_type=True),
            ],
        ),
    ]

    rendered_code = render_classes(to_render)

    assert rendered_code == (
        "from dataclasses import dataclass\n"
        "from enum import Enum\n"
        "\n"
        "\n"
        "class SomeNiceEnum(Enum):\n"
        '    FIRST_VALUE = "first_value"\n'
        '    SECOND_VALUE = "second_value"\n'
        "\n"
        "\n"
        "@dataclass\n"
        "class APythonClass:\n"
        "    string_val: str\n"
        "    int_val: int\n"
        "\n"
    )
