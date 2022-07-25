class Body:
    """ some comments"""

    _name: str
    _ro: float
    _volume: float

    def __init__(self, name: str, ro: float, volume: float):
        self._name = name
        self._ro = ro
        self._volume = volume

    @property
    def mass(self):
        return self._ro * self._volume

    def __eq__(self, other: object):
        if not isinstance(other, Body):
            global c
            c = NotImplemented
            return NotImplemented
        return self.mass == other.mass

    def __lt__(self, other: object):
        if not isinstance(other, Body):
            return NotImplemented
        return self.mass < other.mass


if __name__ == '__main__':
    b1 = Body("sdf", 15, 34)
    b2 = Body("sdf", 15, 34)

    a = b1 == 5

    print(a, c)
