from typing import Any


class Validator:
    def __call__(self, data: Any):
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')

    @staticmethod
    def _is_valid(data: Any) -> bool:
        return True


class IntegerValidator(Validator):
    min_value: int
    max_value: int

    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: int):
        return (type(data) is int
                and self.min_value <= data <= self.max_value)


class FloatValidator(Validator):
    min_value: float
    max_value: float

    def __init__(self, min_value: float, max_value: float):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data: float):
        return (isinstance(data, float)
                and self.min_value <= data <= self.max_value)
