from typing import List


class Thing:
    name: str
    weight: int

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight


class Bag:
    max_weight: int
    __things: List[Thing]
    _current_weight: int = 0

    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__things = []

    def add_thing(self, thing: Thing):
        if self._current_weight + thing.weight <= self.max_weight:
            self.__things.append(thing)
            self._current_weight += thing.weight

    def remove_thing(self, indx: int):
        if indx < len(self.things):
            self.__things.pop(indx)

    def get_total_weight(self) -> int:
        return sum(thing.weight for thing in self.things)

    @property
    def things(self) -> List[Thing]:
        return self.__things


if __name__ == '__main__':
    bag = Bag(121)
    bag.add_thing(Thing("Книга по Python", 100))
    bag.add_thing(Thing("Котелок", 500))
    bag.add_thing(Thing("Спички", 20))
    bag.add_thing(Thing("Бумага", 100))
    w = bag.get_total_weight()

    for t in bag.things:
        print(f"{t.name}: {t.weight}")

