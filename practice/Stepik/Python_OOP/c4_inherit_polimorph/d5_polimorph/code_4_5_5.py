from typing import Any
from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def _is_valid(self, data) -> bool: ...


class FloatValidator(Validator):
    MIN_VALUE: float
    MAX_VALUE: float

    def __init__(self, min_value: float, max_value: float):
        self.MIN_VALUE = min_value
        self.MAX_VALUE = max_value

    def __call__(self, value: Any):
        return self._is_valid(value)

    def _is_valid(self, data: Any) -> bool:
        return (isinstance(data, float)
                and self.MIN_VALUE <= data <= self.MAX_VALUE)
