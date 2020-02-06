import pytest

import tests
from danger_python.danger import Danger, DangerResults, Violation
from danger_python.plugins import DangerPlugin


class FirstPlugin(DangerPlugin):
    def fancy_method_returning_sum(self, a: int, b: int) -> int:
        return a + b


def test_that_plugin_method_is_registered_in_global_namespace():
    """
    Test that plugin method is autoregistered in global namespace of
    the package containing the method.
    """

    result = tests.fancy_method_returning_sum(8, 7)

    assert result == 15


class ModifiedFilesPrinterPlugin(DangerPlugin):
    def print_modified_files(self):
        methods = [self.message, self.markdown, self.warn, self.fail]

        for index, modified_file in enumerate(self.danger.git.modified_files):
            number_of_files = len(self.danger.git.modified_files)
            methods[index](f"Files modified: {number_of_files}", modified_file, index)


@pytest.mark.parametrize(
    "modified_files", [["message.py", "markdown.py", "warn.py", "fail.py"]]
)
def test_that_plugin_method_has_access_to_danger_and_reporting_methods(danger: Danger):
    """
    Test that plugin method has access to the danger DSL and also the methods
    for providing messages, markdowns, warnings and fails.
    """
    tests.print_modified_files()

    assert danger.results == DangerResults(
        fails=[Violation(message="Files modified: 4", file_name="fail.py", line=3)],
        warnings=[Violation(message="Files modified: 4", file_name="warn.py", line=2)],
        markdowns=[
            Violation(message="Files modified: 4", file_name="markdown.py", line=1)
        ],
        messages=[
            Violation(message="Files modified: 4", file_name="message.py", line=0)
        ],
    )
