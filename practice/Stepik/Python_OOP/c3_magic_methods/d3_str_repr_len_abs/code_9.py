from typing import List, Tuple


class Ingredient:
    """ A class used to represent ingredients for recipes. """

    name: str
    volume: float
    measure: str

    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    """ A class used to represent recipes consisting of 0+ ingredients. """

    _ingredients: List[Ingredient]

    def __init__(self, *args: Ingredient):
        self._ingredients = list(args)

    def add_ingredient(self, ing: Ingredient) -> None:
        self._ingredients.append(ing)

    def remove_ingredient(self, ing: Ingredient) -> None:
        self._ingredients.remove(ing)

    def get_ingredients(self) -> Tuple[Ingredient, ...]:
        return tuple(self._ingredients)

    def __len__(self):
        return len(self._ingredients)
