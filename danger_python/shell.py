import subprocess


def resolve_danger_path():
    process = subprocess.run(['which', 'danger'], capture_output=True)

    if process.returncode == 0:
        path = process.stdout.decode('utf-8')
        return path.strip()
