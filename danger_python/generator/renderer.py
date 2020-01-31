import subprocess
from typing import List

from jinja2 import Environment, PackageLoader, select_autoescape

from .models import TypeDefinition


def render_classes(to_render: List[TypeDefinition]) -> str:
    template_environment = Environment(
        loader=PackageLoader("danger_python.generator", "templates"),
        autoescape=select_autoescape([]),
    )
    template = template_environment.get_template("dsl.py.jinja")
    rendered = template.render(types=to_render)
    result = subprocess.run(["black", "-c", rendered], capture_output=True)
    return result.stdout.decode("utf-8")
