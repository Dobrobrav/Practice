class Protists:
    name: str
    weight: float
    old: int

    def __init__(self, name: str, weight: float, old: int):
        self.old = old
        self.weight = weight
        self.name = name


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Worms(Animals):
    pass


class Flowering(Plants):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


if __name__ == '__main__':
    lst_objs = [
        Monkey("мартышка", 30.4, 7),
        Monkey("шимпанзе", 24.6, 8),
        Person("Балакирев", 88, 34),
        Person("Верховный жрец", 67.5, 45),
        Flower("Тюльпан", 0.2, 1),
        Flower("Роза", 0.01, 1),
        Worm("червь", 0.01, 1),
        Worm("червь 2", 0.02, 1),
    ]

    lst_animals = [protist for protist in lst_objs
                   if isinstance(protist, Animals)]

    lst_plants = [protist for protist in lst_objs
                  if isinstance(protist, Plants)]

    lst_mammals = [protist for protist in lst_objs
                   if isinstance(protist, Mammals)]
