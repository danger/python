from danger_python.generator.models import (
    ClassDefinition,
    EnumDefinition,
    PropertyDefinition,
)
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
                    name="string_val",
                    key="stringVal",
                    value_type="str",
                    known_type=True,
                ),
                PropertyDefinition(
                    name="int_val", key="intVal", value_type="int", known_type=True
                ),
            ],
        ),
    ]

    rendered_code = render_classes(to_render)

    assert rendered_code == (
        "from enum import Enum\n"
        "from typing import Any, List, Optional\n"
        "\n"
        "from pydantic import BaseModel\n"
        "\n"
        "\n"
        "class SomeNiceEnum(Enum):\n"
        '    FIRST_VALUE = "first_value"\n'
        '    SECOND_VALUE = "second_value"\n'
        "\n"
        "\n"
        "class APythonClass(BaseModel):\n"
        "    string_val: Optional[str]\n"
        "    int_val: Optional[int]\n"
        "\n"
        "    class Config:\n"
        "        fields = {\n"
        '            "string_val": "stringVal",\n'
        '            "int_val": "intVal",\n'
        "        }\n"
        "\n"
        "\n"
        "APythonClass.update_forward_refs()"
        "\n"
    )


def test_renderer_handles_empty_classes_and_enums():
    """
    Test renderer handles empty classes and enums.
    """
    to_render = [
        EnumDefinition(name="EmptyEnum", depends_on=set(), values=[]),
        ClassDefinition(name="EmptyClass", depends_on=set(), properties=[]),
    ]

    rendered_code = render_classes(to_render)

    assert rendered_code == (
        "from enum import Enum\n"
        "from typing import Any, List, Optional\n"
        "\n"
        "from pydantic import BaseModel\n"
        "\n"
        "\n"
        "class EmptyEnum(Enum):\n"
        "    pass\n"
        "\n"
        "\n"
        "class EmptyClass(BaseModel):\n"
        "    pass\n"
        "\n"
        "\n"
        "EmptyClass.update_forward_refs()"
        "\n"
    )


def test_renderer_renders_custom_attributes_correctly():
    """
    Test that renderer renders definitions correctly.
    """
    to_render = [
        ClassDefinition(
            name="ClassWithUnknownTypes",
            depends_on=set(),
            properties=[
                PropertyDefinition(
                    name="first_prop",
                    key="firstProp",
                    value_type="FirstUnknownType",
                    known_type=False,
                ),
                PropertyDefinition(
                    name="second_prop",
                    key="secondProp",
                    value_type="List[SecondUnknownType]",
                    known_type=False,
                ),
                PropertyDefinition(
                    name="third_prop",
                    key="thirdProp",
                    value_type="Optional[ThirdUnknownType]",
                    known_type=False,
                ),
                PropertyDefinition(
                    name="any_prop", key="anyProp", value_type="Any", known_type=True
                ),
            ],
        ),
    ]

    rendered_code = render_classes(to_render)

    assert rendered_code == (
        "from enum import Enum\n"
        "from typing import Any, List, Optional\n"
        "\n"
        "from pydantic import BaseModel\n"
        "\n"
        "\n"
        "class ClassWithUnknownTypes(BaseModel):\n"
        '    first_prop: Optional["FirstUnknownType"]\n'
        '    second_prop: Optional[List["SecondUnknownType"]]\n'
        '    third_prop: Optional["ThirdUnknownType"]\n'
        "    any_prop: Any\n"
        "\n"
        "    class Config:\n"
        "        fields = {\n"
        '            "first_prop": "firstProp",\n'
        '            "second_prop": "secondProp",\n'
        '            "third_prop": "thirdProp",\n'
        '            "any_prop": "anyProp",\n'
        "        }\n"
        "\n"
        "\n"
        "ClassWithUnknownTypes.update_forward_refs()"
        "\n"
    )


def test_renderer_aliases_properties():
    """
    Test that renderer aliases properties.
    """
    to_render = [
        ClassDefinition(
            name="ClassWithAliases",
            depends_on=set(),
            properties=[
                PropertyDefinition(
                    name="self", key="self", value_type="str", known_type=True
                ),
                PropertyDefinition(
                    name="from", key="from", value_type="int", known_type=True
                ),
                PropertyDefinition(
                    name="non_aliased",
                    key="nonAliased",
                    value_type="Optional[str]",
                    known_type=True,
                ),
            ],
        ),
    ]

    rendered_code = render_classes(to_render)

    assert rendered_code == (
        "from enum import Enum\n"
        "from typing import Any, List, Optional\n"
        "\n"
        "from pydantic import BaseModel\n"
        "\n"
        "\n"
        "class ClassWithAliases(BaseModel):\n"
        "    self_: Optional[str]\n"
        "    from_: Optional[int]\n"
        "    non_aliased: Optional[str]\n"
        "\n"
        "    class Config:\n"
        "        fields = {\n"
        '            "self_": "self",\n'
        '            "from_": "from",\n'
        '            "non_aliased": "nonAliased",\n'
        "        }\n"
        "\n"
        "\n"
        "ClassWithAliases.update_forward_refs()"
        "\n"
    )
