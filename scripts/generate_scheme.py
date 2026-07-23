import os
import shutil

from danger_python.generator.builder import build_types
from danger_python.generator.parser import parse_schema
from danger_python.generator.renderer import render_classes


def main():
    with open("input_schema.json", encoding="utf-8") as schema_file:
        types = build_types(parse_schema(schema_file.read()))
        rendered = render_classes(types)

    base_path = os.path.dirname(os.path.realpath(__file__))
    output_path = os.path.join(base_path, "output_schema.py")
    with open(output_path, "w", encoding="utf-8") as output:
        output.write(rendered)

    # Move only after the handle is closed; on Windows an open handle blocks the
    # unlink that shutil.move performs on the source file.
    shutil.move(output_path, os.path.join("../danger_python/models.py"))


if __name__ == "__main__":
    main()
