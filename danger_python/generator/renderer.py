import subprocess

from jinja2 import Environment, PackageLoader, select_autoescape

from .models import TypeDefinition


def render_classes(to_render: list[TypeDefinition]) -> str:
    template_environment = Environment(
        loader=PackageLoader("danger_python.generator", "templates"),
        autoescape=select_autoescape([]),
    )
    template = template_environment.get_template("dsl.py.jinja")
    rendered = template.render(types=to_render)
    # Format the generated source with Ruff (black was removed in the tooling
    # migration). `ruff format -` reads the module from stdin and writes the
    # formatted result to stdout, using the project's [tool.ruff] config.
    result = subprocess.run(
        ["ruff", "format", "-"],
        input=rendered.encode("utf-8"),
        capture_output=True,
    )
    return result.stdout.decode("utf-8")
