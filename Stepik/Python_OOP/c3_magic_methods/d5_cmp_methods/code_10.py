from typing import List


class Thing:
    """ Class that represents things with name and mass.

    Class implements operations:
     - '==' and '!='
    """

    _name: str
    _mass: float

    def __init__(self, name: str, mass: float):
        self._name = name
        self._mass = mass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Thing):
            return NotImplemented
        return (self._name.lower() == other._name.lower()
                and self._mass == other._mass)


class Box:
    """ Class that represents container with things kept in a list.

    Class implements methods and operations:
     - .add_thing for adding things in the list
     - .get_things for getting the list of things
     - '==' and '!='
    """

    _things: List[Thing]

    def __init__(self):
        self._things = []

    def add_thing(self, obj: Thing):
        self._things.append(obj)

    def get_things(self) -> List[Thing]:
        return self._things

    def __eq__(self, other: object):
        if not isinstance(other, Box):
            return NotImplemented
        return all(other.get_things().count(elem) == 1
                   for elem in self.get_things())
