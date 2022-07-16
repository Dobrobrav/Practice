from typing import Sequence, NamedTuple, Optional, TypeAlias

Matrix: TypeAlias = Sequence[Sequence[float]]


class Step(NamedTuple):
    vertical: int
    horizontal: int


class Size(NamedTuple):
    vertical: int
    horizontal: int


class MaxPooling:
    step: Step
    size: Size

    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = Step(*step)
        self.size = Size(*size)

    def __repr__(self):
        return (f"step: {self.step.vertical}, {self.step.horizontal}; "
                f"size: {self.size.vertical}, {self.step.horizontal}")

    def __call__(self, matrix: Matrix) -> list[list[float]]:
        """ Return the max-pooling matrix
         that process areas of the given size with given step. """
        if (any(type(value) not in (int, float)
                for row in matrix for value in row)
                or any(len(row) != len(matrix[0]) for row in matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        max_pooling = [
            [self._calc_area_max_value(matrix, i, j)
             for j in range(0, len(matrix[0]), self.step.horizontal)
             if self._calc_area_max_value(matrix, i, j) is not None]
            for i in range(0, len(matrix), self.step.vertical)
        ]
        # max_pooling = [row for row in max_pooling if row != []]
        max_pooling = filter(lambda row: row != [], max_pooling)
        return max_pooling

    def _calc_area_max_value(self, matrix: Matrix,
                             i: int, j: int) -> Optional[float]:
        """ Return the max value of the given area from the matrix. """
        sub_matrix = [
            row[j: j + self.size.horizontal]
            for row in matrix[i: i + self.size.vertical]
        ]
        area_of_sub_matrix = sum(len(row) for row in sub_matrix)

        if area_of_sub_matrix < self.size.horizontal * self.size.vertical:
            return None

        max_value = max(
            value
            for row in sub_matrix
            for value in row
        )
        return max_value
