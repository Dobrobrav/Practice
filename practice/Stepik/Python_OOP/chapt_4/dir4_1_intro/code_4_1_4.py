class Animal:
    name: str
    old: int

    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old

    def get_info(self):
        other_params_gen = (str(item[1]) for item in self.__dict__.items()
                            if item[0] not in {'name', 'old'})
        other_params_str = ', '.join(other_params_gen)
        return f"{self.name}: {self.old}, {other_params_str}"


class Cat(Animal):
    color: str
    weight: float

    def __init__(self, name: str, old: int, color: str, weight: float):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):
    breed: str
    size: tuple[float, float]

    def __init__(self, name: str, old: int,
                 breed: str, size: tuple[float, float]):
        super().__init__(name, old)
        self.breed = breed
        self.size = size


if __name__ == '__main__':
    cat = Cat('кот', 4, 'black', 2.25)
    print(cat.get_info())

    dog = Dog('собака', 3, 'хаски', (0.7, 1))
    print(dog.get_info())
