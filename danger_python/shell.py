import json
import subprocess
import sys
import traceback
from types import TracebackType
from typing import List, Optional

from .exceptions import DangerfileException, SystemConfigurationException
from .models import DangerDSL


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
        compiled = compile(dangerfile, "dangerfile.py", "exec")
        exec(compiled)
    except Exception as error:
        _, _, trace = sys.exc_info()
        message = __format_exception(error, trace)
    else:
        return

    raise DangerfileException(message)


def __format_exception(error: Exception, trace: Optional[TracebackType]) -> str:
    trace = trace.tb_next
    error_class = error.__class__.__name__
    error_detail = error.args[0]

    if isinstance(error, SyntaxError):
        line_number = error.lineno
    else:
        line_number = trace.tb_lineno

    message = (
        "There was an error when executing dangerfile.py:\n"
        f"{error_class} at line {line_number}: {error_detail}\n\n"
        "Stacktrace:\n"
        f"{''.join(traceback.format_tb(trace))}"
    )

    return message


def load_dsl() -> DangerDSL:
    input_json = json.loads(sys.stdin.read())
    return DangerDSL.from_dict(input_json["danger"])
