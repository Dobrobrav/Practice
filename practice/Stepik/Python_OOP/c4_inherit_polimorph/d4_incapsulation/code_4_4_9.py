# здесь объявляйте декоратор и все что с ним связано
from typing import Callable, List


class FuncLogDecorator:
    _log_list: list

    def __init__(self, log_list: list):
        self._log_list = log_list

    def __call__(self, func: Callable, *args, **kwargs):
        def _wrapper(*args, **kwargs):
            self._log_list.append(func.__name__)
            return func(*args, **kwargs)

        return _wrapper


def _decorate_class_methods(cls: type, func_decorator: Callable):
    funcs_of_cls = ((key, value) for key, value in cls.__dict__.items()
                    if callable(value))
    for key, func in funcs_of_cls:
        setattr(cls, key, func_decorator(func))


def class_log(log_list: list) -> Callable:
    def _cls_decorator(cls: type) -> type:
        func_decorator = FuncLogDecorator(log_list)
        _decorate_class_methods(cls, func_decorator)
        return cls

    return _cls_decorator


vector_log: List[str] = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    __coords: List[float]

    def __init__(self, *args: float):
        self.__coords = list(args)

    def __getitem__(self, item: int):
        return self.__coords[item]

    def __setitem__(self, key: int, value: float):
        self.__coords[key] = value
