class Item:
    """ Class that represents purchased items
     with their names and prices (money). """

    name: str
    _money: int

    def __init__(self, name: str, money: float):
        self.name = name
        self.money = money

    def __add__(self, other: 'Item | float'):
        if type(other) in (int, float):
            total_money = self.money + other
        else:
            total_money = (self._money + other._money) / 100
        return total_money

    def __radd__(self, other: float):
        return self + other

    @property
    def money(self):
        return self._money / 100

    @money.setter
    def money(self, money: float):
        self._money = int(money * 100)


class Budget:
    """ Class, for keeping track of purchases, that contains
     list of purchased items and defines methods for work with it.
    """

    _items: list[Item]

    def __init__(self):
        self._items = []

    def add_item(self, it: 'Item') -> None:
        self._items.append(it)

    def remove_item(self, indx: int) -> None:
        self._items.pop(indx)

    def get_items(self) -> list[Item]:
        return self._items
