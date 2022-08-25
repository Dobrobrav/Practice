class Food:
    _name: str
    _weight: float
    _calories: int

    def __init__(self, name: str, weight: float, calories: int):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    _white: bool

    def __init__(self, name: str, weight: float, calories: int, white: bool):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    _dietary: bool

    def __init__(self, name: str, weight: float, calories: int, dietary: bool):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    _fish: str

    def __init__(self, name: str, weight: float, calories: int, fish: str):
        super().__init__(name, weight, calories)
        self._fish = fish
