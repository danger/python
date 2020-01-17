import subprocess
import sys
import traceback
from typing import List

from .exceptions import DangerfileException, SystemConfigurationException


def resolve_danger_path():
    process = subprocess.run(["which", "danger"], capture_output=True)

    if process.returncode == 0:
        path = process.stdout.decode("utf-8")
        return path.strip()
    else:
        raise SystemConfigurationException("danger-js not found in PATH")


def invoke_danger(parameters: List[str]) -> subprocess.CompletedProcess:
    command = build_danger_command(parameters)
    return subprocess.run(command, capture_output=True)


def build_danger_command(parameters: List[str]) -> List[str]:
    command = [resolve_danger_path()]
    command.extend(parameters)
    command.extend(["-p", "danger-python"])
    return command


def execute_dangerfile(dangerfile: str):
    try:
        exec(dangerfile)
    except Exception as err:
        error_class = err.__class__.__name__
        detail = err.args[0]
        _, _, tb = sys.exc_info()
        tb = tb.tb_next
        line_number = err.lineno if isinstance(err, SyntaxError) else tb.tb_lineno
    else:
        return

    line_of_code = dangerfile.split("\n")[line_number - 1]
    message = (
        "There was an error when executing dangerfile.py:\n"
        f"{error_class} at line {line_number}: {detail}\n\n"
        "Offending line:\n"
        f"{line_of_code}\n\n"
        "Stacktrace:\n"
        f"{''.join(traceback.format_tb(tb))}"
    )
 
    raise DangerfileException(message)
