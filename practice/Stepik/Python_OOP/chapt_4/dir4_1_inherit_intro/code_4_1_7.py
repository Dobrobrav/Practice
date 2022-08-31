from typing import Any, Dict


class MetaSingleton(type):
    _instances: Dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls)\
                .__call__(*args, **kwargs)

        return cls._instances[cls]


class Singleton(metaclass=MetaSingleton):
    pass


class Game(Singleton):
    name: str

    def __init__(self, name: str):
        self.name = name
