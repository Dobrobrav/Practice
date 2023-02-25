from abc import ABC, abstractmethod


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def population(self) -> int:
        ...

    @population.setter
    @abstractmethod
    def population(self, population: int):
        ...

    @property
    @abstractmethod
    def square(self) -> float:
        ...

    @square.setter
    @abstractmethod
    def square(self, square: float):
        ...

    @abstractmethod
    def get_info(self) -> str:
        ...


class Country(CountryInterface):
    _name: str
    _population: int
    _square: float

    def __init__(self, name: str, population: int, square: float):
        self._name = name
        self.population = population
        self.square = square

    @property
    def name(self) -> str:
        return self._name

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, population: int):
        self._population = population

    @property
    def square(self) -> float:
        return self._square

    @square.setter
    def square(self, square: float):
        self._square = square

    def get_info(self) -> str:
        return F"{self.name}: {self.square}, {self.population}"
