class Body:
    """ Class that represents a physical body with name, density and volume.
    Class implements '==', '>' and '<' operations between its instances
    or its instances and numeric types.
    """

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
        if not isinstance(other, (Body, int, float)):
            return NotImplemented
        return self.mass == other.mass if isinstance(other, Body) else other

    def __lt__(self, other: object):
        if not isinstance(other, (Body, int, float)):
            return NotImplemented
        return self.mass < other.mass if isinstance(other, Body) else other


class Foo:
    def __eq__(self, other):
        return NotImplemented


if __name__ == '__main__':
    b1 = Body("sdf", 15, 34)
    b2 = Body("sdf", 15, 34)
    f = Foo()

    a = b1 == f

    print(a)
