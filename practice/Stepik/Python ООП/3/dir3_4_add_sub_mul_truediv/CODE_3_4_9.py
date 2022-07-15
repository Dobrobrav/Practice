from typing import Callable, Union


class Box3D:
    """ Class that represents rectangular parallelepiped
     and allows '+', '-', '*', '//', '%' operations with it. """

    width: float
    height: float
    depth: float

    def __init__(self, width: float, height: float, depth: float):
        self.width = width
        self.height = height
        self.depth = depth

    def __repr__(self):
        return str((self.width, self.height, self.depth))

    def __add__(self, other: 'Box3D') -> 'Box3D':
        return self.get_new_box(other, lambda x, y: x + y)

    def __sub__(self, other: 'Box3D') -> 'Box3D':
        return self.get_new_box(other, lambda x, y: x - y)

    def __mul__(self, other: float) -> 'Box3D':
        return self.get_new_box(other, lambda x, y: x * y)

    def __rmul__(self, other: float) -> 'Box3D':
        return self * other

    def __floordiv__(self, other: float) -> 'Box3D':
        return self.get_new_box(other, lambda x, y: x // y)

    def __mod__(self, other: float) -> 'Box3D':
        return self.get_new_box(other, lambda x, y: x % y)

    def get_new_box(self, operand: 'Union[float, Box3D]',
                    operation: Callable) -> 'Box3D':
        if type(operand) in (int, float):
            new_dimensions = (
                operation(dimension, operand)
                for dimension in (self.width, self.height, self.depth)
            )
        elif isinstance(operand, Box3D):
            self_dimensions = (self.width, self.height, self.depth)
            other_dimensions = (operand.width, operand.height, operand.depth)
            new_dimensions = (
                operation(dimension, other_dimension)
                for dimension, other_dimension in zip(self_dimensions,
                                                      other_dimensions)
            )
        else:
            raise TypeError('The operand must be of int, float or Box3D type')
        return Box3D(*new_dimensions)
