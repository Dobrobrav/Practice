from typing import Callable


class Vector:
    """ Implements '==', '!=', '+', '+=', '-', '-=', '*', '*=' operations.
    Multiplication and equality operations only support vector as 2nd operand,
    whereas other operations also support numbers as 2nd operand.
    """

    coords: list[float]

    def __init__(self, *args: float):
        self.coords = list(args)

    def __eq__(self, other: object):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(other.coords) != len(self.coords):
            raise ArithmeticError('размерности векторов не совпадают')

        return all(a == b for a, b in zip(self.coords, other.coords))

    def __add__(self, other: object):
        if not isinstance(other, (Vector, int, float)):
            return NotImplemented
        return Vector(*self._get_resulting_coords(other, lambda x, y: x + y))

    def __iadd__(self, other: object):
        if not isinstance(other, (Vector, int, float)):
            return NotImplemented
        self.coords = self._get_resulting_coords(other, lambda x, y: x + y)
        return self

    def __sub__(self, other: object):
        if not isinstance(other, (Vector, int, float)):
            return NotImplemented
        return Vector(*self._get_resulting_coords(other, lambda x, y: x - y))

    def __isub__(self, other: object):
        if not isinstance(other, (Vector, int, float)):
            return NotImplemented
        self.coords = self._get_resulting_coords(other, lambda x, y: x - y)
        return self

    def __mul__(self, other: object):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(*self._get_resulting_coords(other, lambda x, y: x * y))

    def __imul__(self, other: object):
        if not isinstance(other, Vector):
            return NotImplemented
        self.coords = self._get_resulting_coords(other, lambda x, y: x * y)
        return self

    def __repr__(self):
        return str(self.coords)

    def _get_resulting_coords(self, other: 'Vector | float',
                              operation: Callable) -> list[float]:
        if not isinstance(other, (int, float, Vector)):  # not essential here
            raise TypeError('incorrect type of operand')

        coords = []
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
            is_vector = True
        else:
            is_vector = False

        for i, coord in enumerate(self.coords):
            operand = other.coords[i] if is_vector else other
            coords.append(operation(coord, operand))
        return coords
