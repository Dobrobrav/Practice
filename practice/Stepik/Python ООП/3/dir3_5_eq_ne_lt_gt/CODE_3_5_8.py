from typing import Type, Optional


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money: 'Money'):
        money.cb = cls


class Money:
    __volume: int
    __cb: Optional[Type[CentralBank]] = None

    _literals_for_currency = {
        'MoneyD': 'dollar',
        'MoneyR': 'rub',
        'MoneyE': 'euro',
    }

    def __init__(self, volume: float = 0):
        self.volume = volume

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        this_money = self._get_rub_equivalent()
        other_money = other._get_rub_equivalent()
        return this_money * 0.9 <= other_money <= this_money * 1.1

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        this_money = self._get_rub_equivalent()
        other_money = other._get_rub_equivalent()
        return this_money < other_money and self != other

    def __ge__(self, other: object) -> bool:
        return self > other or self == other

    def __repr__(self):
        compared_rubles = self._get_rub_equivalent() if self.cb else 'unknown'
        literals = self._literals_for_currency[self.__class__.__name__]
        return f"{self.volume} {literals} ~ {compared_rubles} rub"

    def _get_rub_equivalent(self) -> float:
        if isinstance(self, MoneyR):
            return self.volume
        currency_literal = self._literals_for_currency[self.__class__.__name__]
        rub_equivalent = (self.volume * self.cb.rates[currency_literal]
                          * self.cb.rates['rub'])
        return rub_equivalent

    @property
    def volume(self) -> float:
        if self.__volume is None:
            raise ValueError("Неизвестен курс валют.")
        return self.__volume / 100

    @volume.setter
    def volume(self, volume: float):
        self.__volume = int(volume * 100)

    @property
    def cb(self) -> Optional[Type[CentralBank]]:
        return self.__cb

    @cb.setter
    def cb(self, cb: Type[CentralBank]):
        self.__cb = cb


class MoneyR(Money):
    pass


class MoneyD(Money):
    pass


class MoneyE(Money):
    pass


if __name__ == '__main__':
    money_e = MoneyE()
    money_d = MoneyD()
    money_r = MoneyR()

    CentralBank.register(money_r)
    CentralBank.register(money_e)
    CentralBank.register(money_d)

    money_r.volume = 65
    money_d.volume = 1

    res = money_r <= money_d

    print(res)
