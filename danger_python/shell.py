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
    danger_path = resolve_danger_path()
    commands = [danger_path]
    commands.extend(parameters)
    commands.extend(['-p', 'danger-python'])

    return subprocess.run(commands, capture_output=True)
