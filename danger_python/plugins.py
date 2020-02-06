import sys

from .danger import Danger, fail, markdown, message, warn


class DangerPlugin:
    def __init__(self):
        self._danger = None
        self.message = message
        self.markdown = markdown
        self.warn = warn
        self.fail = fail

    def __init_subclass__(cls, **kwargs):
        parent_module = cls.__module__.split(".")[0]
        module = sys.modules[parent_module]
        instance = cls()

        for method_name in dir(cls):
            if method_name.startswith("__") or method_name in set(dir(DangerPlugin)):
                continue

            method = getattr(instance, method_name)
            setattr(module, method_name, method)

    @property
    def danger(self):
        if not self._danger:
            self._danger = Danger()

        return self._danger
