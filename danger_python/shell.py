import json
import subprocess
import sys
import traceback
from types import TracebackType
from typing import List

from .danger import Danger, fail, markdown, message, serialize_results, warn
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
    command.extend(["-p", "danger-python", "-u"])
    return command


def execute_dangerfile(dangerfile: str):
    try:
        compiled = compile(dangerfile, "dangerfile.py", "exec")
        danger_globals = {
            "danger": Danger(),
            "fail": fail,
            "warn": warn,
            "markdown": markdown,
            "message": message,
        }
        exec(compiled, {}, danger_globals)
        assert Danger.results is not None
        print(json.dumps(serialize_results(Danger.results)))
    except Exception as error:
        _, _, trace = sys.exc_info()
        assert trace is not None
        exception_message = __format_exception(error, trace)
    else:
        return

    raise DangerfileException(exception_message)


def __format_exception(error: Exception, trace: TracebackType) -> str:
    trace_next = trace.tb_next
    error_class = error.__class__.__name__
    error_detail = error.args[0]

    if isinstance(error, SyntaxError):
        line_number = error.lineno
    else:
        assert trace_next is not None
        line_number = trace_next.tb_lineno

    message = (
        "There was an error when executing dangerfile.py:\n"
        f"{error_class} at line {line_number}: {error_detail}\n\n"
        "Stacktrace:\n"
        f"{''.join(traceback.format_tb(trace_next))}"
    )

    return message
