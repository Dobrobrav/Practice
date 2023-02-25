class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name: str, massa: float, temp: float):
        self._name = name
        self._massa = massa
        self._temp = temp

    def foo(self):
        pass


class WhiteDwarf(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name: str, massa: float, temp: float,
                 type_star: str, radius: float):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class YellowDwarf(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name: str, massa: float, temp: float,
                 type_star: str, radius: float):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class RedGiant(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name: str, massa: float, temp: float,
                 type_star: str, radius: float):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class Pulsar(Star):
    __slots__ = ('_type_star', '_radius')

    def __init__(self, name: str, massa: float, temp: float,
                 type_star: str, radius: float):
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


if __name__ == '__main__':
    stars = [
        RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
        WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
        WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
        YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1)
    ]

    white_dwarfs = [star for star in stars if isinstance(star, WhiteDwarf)]
