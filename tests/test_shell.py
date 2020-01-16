import subprocess
from unittest import mock

import pytest

from danger_python.exceptions import SystemConfigurationException
from danger_python.shell import resolve_danger_path
from tests.fixtures.shell import (danger_js_missing_path_fixture,
                                  danger_js_path_fixture, subprocess_fixture)


def test_danger_path_can_be_resolved_if_present():
    """
    Test that danger-js path can be resolved.
    """
    with subprocess_fixture(danger_js_path_fixture('/usr/bin/fake-danger-js \n \r')):
        resolved_path = resolve_danger_path()

    assert resolved_path == "/usr/bin/fake-danger-js"


def test_danger_path_resolver_throws_an_error_if_not_present():
    """
    Test that danger-js path resolver throws an error if not present.
    """
    with subprocess_fixture(danger_js_missing_path_fixture()):
        with pytest.raises(SystemConfigurationException) as config_exc:
            resolve_danger_path()

    assert config_exc.match("danger-js not found in PATH")
