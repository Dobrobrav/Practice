from typing import Tuple


class Thing:
    name: str
    weight: float

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    author: str
    date: str

    def __init__(self, name: str, weight: float, author: str, date: str):
        super(ArtObject, self).__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    memory: int
    cpu: str

    def __init__(self, name: str, weight: float, memory: int, cpu: str):
        super(Computer, self).__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    dims: Tuple[float, float, float]

    def __init__(self, name: str, weight: float,
                 dims: Tuple[float, float, float]):
        super(Auto, self).__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    model: str
    old: int

    def __init__(self, name: str, weight: float,
                 dims: Tuple[float, float, float], model: str, old: int):
        super(Mercedes, self).__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    model: str
    wheel: bool

    def __init__(self, name: str, weight: float,
                 dims: Tuple[float, float, float], model: str, wheel: bool):
        super(Toyota, self).__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel
