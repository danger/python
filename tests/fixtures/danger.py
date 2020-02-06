from typing import Any, Dict

from jinja2 import Environment, PackageLoader, select_autoescape


def danger_input_file_fixture(**kwargs: Dict[str, Any]) -> str:
    template_environment = Environment(
        loader=PackageLoader("tests", "fixtures"), autoescape=select_autoescape([])
    )
    template = template_environment.get_template("typescript-34806.json.jinja")
    return template.render(
        modified_files=kwargs.get("modified_files", []),
        created_files=kwargs.get("created_files", []),
        deleted_files=kwargs.get("deleted_files", []),
    )
