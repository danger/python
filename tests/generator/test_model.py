from danger_python.generator.models import PropertyDefinition


def test_property_definition_formats_the_type_correctly():
    """
    Test that PropertyDefinition formats the type correctly.
    """
    optional_string = PropertyDefinition(
        name="", key="", value_type="Optional[str]", known_type=True
    )
    list_custom_type = PropertyDefinition(
        name="", key="", value_type="List[CustomType]", known_type=False
    )
    optional_custom_type = PropertyDefinition(
        name="", key="", value_type="Optional[TheType]", known_type=False
    )
    integer = PropertyDefinition(name="", key="", value_type="int", known_type=True)

    assert optional_string.formatted_type == "Optional[str]"
    assert list_custom_type.formatted_type == "List['CustomType']"
    assert optional_custom_type.formatted_type == "Optional['TheType']"
    assert integer.formatted_type == "int"


def test_property_definition_returns_non_reserved_name():
    """
    Test that PropertyDefinition returns non-reserved name.
    """
    from_string = PropertyDefinition(
        name="from", key="", value_type="str", known_type=True
    )
    self_custom_type = PropertyDefinition(
        name="self", key="", value_type="CustomType", known_type=False
    )
    id_int = PropertyDefinition(name="id", key="", value_type="int", known_type=True)

    assert from_string.non_reserved_name == "from_"
    assert self_custom_type.non_reserved_name == "self_"
    assert id_int.non_reserved_name == "id"


def test_patched_property_type_formats_the_type_correctly():
    """
    Test that patched properties are guaranteed to be of Optional type.
    """
    optional_string = PropertyDefinition(
        name="", key="", value_type="Optional[str]", known_type=True
    )
    list_custom_type = PropertyDefinition(
        name="", key="", value_type="List[CustomType]", known_type=False
    )
    custom_type = PropertyDefinition(
        name="", key="", value_type="TheType", known_type=False
    )
    integer = PropertyDefinition(name="", key="", value_type="int", known_type=True)
    any_type = PropertyDefinition(name="", key="", value_type="Any", known_type=True)

    assert optional_string.patched_type == "Optional[str]"
    assert list_custom_type.patched_type == "Optional[List['CustomType']]"
    assert custom_type.patched_type == "Optional['TheType']"
    assert integer.patched_type == "Optional[int]"
    assert any_type.patched_type == "Any"
