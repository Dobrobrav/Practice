from typing import Tuple, Callable


class Vector:
    _coords: Tuple[float, ...]

    def __init__(self, *args: float):
        self._coords = args

    def __add__(self, other: 'Vector') -> 'Vector':
        self._check_operand(other)
        return self._get_operation_result(other, lambda x1, x2: x1 + x2)

    def __sub__(self, other: 'Vector') -> 'Vector':
        self._check_operand(other)
        return self._get_operation_result(other, lambda x1, x2: x1 - x2)

    def get_coords(self) -> Tuple[float, ...]:
        return self._coords

    def _check_operand(self, operand: 'Vector'):
        self._check_if_vector(operand)
        self._check_if_sizes_equal(operand)

    def _check_if_sizes_equal(self, other_vector: 'Vector'):
        if len(self._coords) != len(other_vector._coords):
            raise TypeError('размерности векторов не совпадают')

    @staticmethod
    def _check_if_vector(value: 'Vector'):
        if not isinstance(value, Vector):
            raise TypeError('операнд должен быть объектом Vector '
                            'или его подкласса')

    def _get_operation_result(self, vector: 'Vector',
                              operation: Callable) -> 'Vector':
        new_coords = (operation(x1, x2)
                      for x1, x2 in zip(self._coords, vector._coords))
        vector_class = self._get_class_for_new_vector(vector)
        return vector_class(*new_coords)

    def _get_class_for_new_vector(self, vector: 'Vector') -> type:
        return self.__class__


class VectorInt(Vector):
    def __init__(self, *args: int):
        self._check_coords(*args)
        super().__init__(*args)

    @staticmethod
    def _check_coords(*args: int):
        if any(type(coord) is not int for coord in args):
            raise ValueError('координаты должны быть целыми числами')

    def _get_class_for_new_vector(self, vector: 'Vector') -> type:
        if any(isinstance(coord, float)
               for coord in self._coords + vector._coords):
            return Vector
        return self.__class__
