class ShopItem:
    """ Class that represents shop items with name, weight and price.

    Class implements method and operation:
     - .__hash__ - objects with the same name (case-insensitive),
       price and weight have the same hash
     - '==' - objects with the same hash are considered the same
    """

    name: str
    weight: float
    _price: int

    def __init__(self, name: str, weight: float, price: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __repr__(self):
        # return f"{self._name}: {self._weight} g;  {self.price} rub"
        return self.name

    @property
    def price(self) -> float:
        return self._price / 100

    @price.setter
    def price(self, price: float):
        self._price = int(price * 100)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ShopItem):
            return NotImplemented
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


if __name__ == '__main__':
    lst_in = [
        'Системный блок: 1500 75890.56',
        'Монитор Samsung: 2000 34000',
        'Клавиатура: 200.44 545',
        'Монитор Samsung: 2000 34000',
    ]

    shop_items = {}

    for line in lst_in:
        name = line.split(': ')[0]
        specs = line.split(': ')[1].split()
        weight = float(specs[0])
        price = float(specs[1])
        shop_item = ShopItem(name, weight, price)

        if shop_item not in shop_items:
            shop_items[shop_item] = [shop_item, 1]
        else:
            shop_items[shop_item][1] += 1

    print(shop_items)
