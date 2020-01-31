import tests
from danger_python.plugins import DangerPlugin


class FirstPlugin(DangerPlugin):
    def fancy_method_returning_sum(self, a: int, b: int) -> int:
        return a + b


def test_that_plugin_method_is_registered_in_global_namespace():
    """
    Test that plguin method is autoregistered in global namespace of
    the package containing the method.
    """

    result = tests.fancy_method_returning_sum(8, 7)

    assert result == 15
