import sys


class DangerPlugin:
    def __init_subclass__(cls, **kwargs):
        parent_module = cls.__module__.split(".")[0]
        module = sys.modules[parent_module]
        instance = cls()

        for method_name in dir(cls):
            if method_name.startswith("__"):
                continue

            method = getattr(instance, method_name)
            setattr(module, method_name, method)
