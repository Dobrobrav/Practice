from abc import ABC, abstractmethod


class Digit:
    _value: float

    def __init__(self, value: float):
        self._validate(value)
        self._value = value

    def __repr__(self):
        return str(self._value)

    @staticmethod
    def _validate(value: float):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def _validate(self, value: float):
        super()._validate(value)
        if type(value) is not int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def _validate(self, value: float):
        super()._validate(value)
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def _validate(self, value: float):
        super()._validate(value)
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def _validate(self, value: float):
        super()._validate(value)
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


if __name__ == '__main__':
    digits = [
        PrimeNumber(6), PrimeNumber(2), PrimeNumber(345),
        FloatPositive(3.4), FloatPositive(2.3), FloatPositive(6.0)
    ]

    # lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
    lst_positive = [x for x in digits if isinstance(x, Positive)]

    # lst_float = list(filter(lambda x: isinstance(x, Float), digits))
    lst_float = [x for x in digits if isinstance(x, Float)]
