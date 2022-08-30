from decimal import Decimal
from typing import Union


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    # здесь объявляйте еще один метод
    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)


# здесь объявляйте класс Money
class Money:
    _money: Decimal

    def __init__(self, value: Union[float, Decimal]):
        self.money = value

    @property
    def money(self) -> float:
        return float(self._money)

    @money.setter
    def money(self, value: Union[float, Decimal]):
        self._validate_money(value)
        self._money = value

    @staticmethod
    def _validate_money(value: Union[float, Decimal]):
        if type(value) not in (int, float, Decimal):
            raise TypeError('сумма должна быть числом')


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"
