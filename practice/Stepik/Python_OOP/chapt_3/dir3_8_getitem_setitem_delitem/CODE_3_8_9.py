class Thing:
    name: str
    weight: float

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"{self.name}: {self.weight}"


class Bag:
    _things: list[Thing]
    _max_weight: float
    _current_weight = 0

    def __init__(self, max_weight: float):
        self._max_weight = max_weight
        self._things = []

    def __repr__(self):
        return f"weight: {self._current_weight}/{self._max_weight} " \
               f"{self._things}"

    def add_thing(self, thing: Thing, index: int | None = None):
        weight_to_remove = 0 if index is None else self._things[index].weight
        self._check_weight(thing.weight, weight_to_remove)

        if index is not None:
            self._things[index] = thing
        else:
            self._things.append(thing)

        self._current_weight -= weight_to_remove
        self._current_weight += thing.weight

    def __setitem__(self, key: int, value: Thing):
        self._check_index(key)
        self.add_thing(value, key)

    def __getitem__(self, item: int) -> Thing:
        self._check_index(item)
        return self._things[item]

    def __delitem__(self, key: int):
        self._check_index(key)
        self._current_weight -= self._things[key].weight
        del self._things[key]

    def _check_weight(self, weight_to_add: float, weight_to_remove=0.0):
        if (self._current_weight + weight_to_add - weight_to_remove
                > self._max_weight):
            raise ValueError('превышен суммарный вес предметов')

    def _check_index(self, index: int):
        is_int = type(index) is int
        if not (is_int and (0 <= index < len(self._things)
                            or -len(self._things) <= index <= -1)):
            raise IndexError('неверный индекс')
