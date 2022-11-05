from copy import copy
from typing import Iterable, Any


class ListInteger(list):
    def __init__(self, iterable: Iterable[int]):
        self._validate_iterable(iterable)
        super().__init__(iterable)

    def __setitem__(self, key: int, value: int):
        self._validate_type(value)
        super().__setitem__(key, value)

    def append(self, __object: int):
        self._validate_type(__object)
        super().append(__object)

    def _validate_iterable(self, iterable: Iterable[int]):
        for value in copy(iterable):
            self._validate_type(value)

    @staticmethod
    def _validate_type(value: Any, type_=int):
        if type(value) is not type_:
            raise TypeError('можно передавать только целочисленные значения')
