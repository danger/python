import subprocess
from typing import List

from .exceptions import SystemConfigurationException


def resolve_danger_path():
    process = subprocess.run(['which', 'danger'], capture_output=True) 

    if process.returncode == 0:
        path = process.stdout.decode('utf-8')
        return path.strip()
    else:
        raise SystemConfigurationException('danger-js not found in PATH')

def invoke_danger(parameters: List[str]) -> subprocess.CompletedProcess:
    command = build_danger_command(parameters)
    return subprocess.run(command, capture_output=True)

def build_danger_command(parameters: List[str]) -> List[str]:
    command = [resolve_danger_path()]
    command.extend(parameters)
    command.extend(['-p', 'danger-python'])
    return command
