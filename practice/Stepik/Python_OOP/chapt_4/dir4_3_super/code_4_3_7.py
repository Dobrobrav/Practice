# здесь объявляйте функцию-декоратор
from typing import Callable, Any, Optional


def _validate_args(*args: int):
    if any(type(arg) is not int for arg in args):
        raise TypeError("аргументы должны быть целыми числами")


def integer_params_decorated(func: Callable) -> Callable:
    def wrapper(self, *args: int) -> Optional[Any]:
        _validate_args(*args)
        return func(self, *args)

    return wrapper


def integer_params(cls: type):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    __coords: list

    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key: int, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]
