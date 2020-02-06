import os
import shutil

from danger_python.generator.builder import build_types
from danger_python.generator.parser import parse_schema
from danger_python.generator.renderer import render_classes


def main():
    with open("input_schema.json", "r") as schema_file:
        types = build_types(parse_schema(schema_file.read()))
        rendered = render_classes(types)

        with open("output_schema.py", "w") as output:
            output.write(rendered)
            base_path = os.path.dirname(os.path.realpath(__file__))
            shutil.move(
                os.path.join(base_path, "output_schema.py"),
                os.path.join("../danger_python/models.py"),
            )


if __name__ == "__main__":
    main()
