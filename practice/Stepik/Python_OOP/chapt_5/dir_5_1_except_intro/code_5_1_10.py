from abc import ABC

from typing import Type, Any, Iterable, Sequence, Union


def main():
    fv = FloatValidator(0, 10.5)
    iv = IntegerValidator(-10, 20)
    lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)],
                       validators=[fv, iv])  # [1, 4.5]

    print(lst_out)


def is_valid(lst: Iterable, validators: Sequence['NumericValidator']) -> list:
    validated = []
    for value in lst:
        for validator in validators:
            try:
                validator(value)
            except ValueError:
                continue
            else:
                validated.append(value)

    return validated


class NumericValidator(ABC):
    min_value: float
    max_value: float

    def __init__(self, min_value: float, max_value: float):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, *args, **kwargs):
        ...

    def _validate(self, value: Any, type_: Type[Union[int, float]]):
        if not (type(value) is type_
                and self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class FloatValidator(NumericValidator):
    def __call__(self, value: float):
        self._validate(value, float)


class IntegerValidator(NumericValidator):
    def __call__(self, value: int):
        self._validate(value, int)


if __name__ == '__main__':
    main()
