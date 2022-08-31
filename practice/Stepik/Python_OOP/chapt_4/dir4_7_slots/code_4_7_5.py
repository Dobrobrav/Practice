from typing import Dict, Any


class MetaSingleton(type):
    _instances: Dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls) \
                .__call__(*args, **kwargs)

        return cls._instances[cls]


class Planet:
    _name: str
    _diametr: float
    _period_solar: float
    _period: float

    def __init__(self, name: str, diameter: float,
                 period_solar: float, period: float):
        self._name = name
        self._diametr = diameter
        self._period_solar = period_solar
        self._period = period


class SolarSystem(metaclass=MetaSingleton):
    __slots__ = ('_mercury', '_venus', '_earth', '_mars',
                 '_jupiter', '_saturn', '_uranus', '_neptune')

    def __init__(self):
        self._mercury = Planet("Меркурий", 4878, 87.97, 1407.5)
        self._venus = Planet("Венера", 12104, 224.7, 5832.45)
        self._earth = Planet("Земля", 12756, 365.3, 23.93)
        self._mars = Planet("Марс", 6794, 687, 24.62)
        self._jupiter = Planet("Юпитер", 142800, 4330, 9.9)
        self._saturn = Planet("Сатурн", 120660, 10753, 10.63)
        self._uranus = Planet("Уран", 51118, 30665, 17.2)
        self._neptune = Planet("Нептун", 49528, 60150, 16.1)


if __name__ == '__main__':
    s_system = SolarSystem()
