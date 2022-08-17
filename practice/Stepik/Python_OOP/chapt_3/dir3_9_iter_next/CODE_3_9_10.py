from typing import Any


class Matrix:
    _rows: int
    _cols: int
    _fill_value: float
    _table: list[list[float]]

    def __init__(self, *args):
        is_matrix = self._check_args(*args)
        self._set_up_table(*args, is_table=is_matrix)

    def __setitem__(self, key: tuple[int, int], value: float):
        self._check_index(key)
        self._check_value(value)
        i, j = key
        self._table[i][j] = value

    def __getitem__(self, item: tuple[int, int]):
        self._check_index(item)
        i, j = item
        return self._table[i][j]

    def __add__(self, other: object):
        return self._add(other)

    def __sub__(self, other: object):
        return self._add(other, subtract_instead=True)

    def _check_args(self, *args) -> bool:
        if len(args) not in (1, 3):
            raise TypeError
        if len(args) == 1:
            self._check_table(*args)
            return True
        else:  # len(args) == 3
            self._check_table_params(*args)
            return False

    def _set_up_table(self, *args, is_table: bool):
        if is_table:
            matrix = args[0]
        else:
            matrix = self._generate_table(*args)
        self._table = matrix

    def _add(self, other: object, subtract_instead=False) -> 'Matrix':
        if (not isinstance(other, (Matrix, int, float))
                or type(other) is bool):
            return NotImplemented
        if isinstance(other, Matrix):
            return self._add_matrix(other, subtract_instead=subtract_instead)
        else:
            return self._add_number(other, subtract_instead=subtract_instead)

    def _add_matrix(self, matrix: 'Matrix',
                    subtract_instead=False) -> 'Matrix':
        self._compare_matrix_sizes(matrix)
        return Matrix(self._get_sum_of_matrices(
            matrix,
            subtract_instead=subtract_instead
        ))

    def _add_number(self, number: float, subtract_instead=False) -> 'Matrix':
        def operation(x, y):
            return x - y if subtract_instead else x + y

        table = [[operation(a, number) for a in row]
                 for row in self._table]
        return Matrix(table)

    def _compare_matrix_sizes(self, other_matrix: 'Matrix'):
        if len(self._table) == len(other_matrix._table):
            if all(len(self_row) == len(other_row)
                   for self_row, other_row in zip(
                self._table, other_matrix._table
            )):
                return
        raise ValueError('операции возможны только с матрицами равных размеров')

    def _get_sum_of_matrices(self, matrix: 'Matrix',
                             subtract_instead=False) -> list[list[float]]:
        def operation(x, y):
            return x - y if subtract_instead else x + y

        table = [
            [operation(a, b) for a, b in zip(self_row, other_row)]
            for self_row, other_row in zip(self._table, matrix._table)
        ]
        return table

    @staticmethod
    def _generate_table(rows: int, cols: int,
                        fill_value: float) -> list[list[float]]:
        table = [[fill_value for _ in range(cols)] for _ in range(rows)]
        return table

    def _check_value(self, value: float):
        if not self._is_value_type_correct(value):
            raise TypeError('значения матрицы должны быть числами')

    def _check_index(self, index_pair: tuple[int, int]):
        if not (isinstance(index_pair, tuple)
                and len(index_pair) == 2
                and all(self._is_value_type_correct(i) for i in index_pair)
                and 0 <= index_pair[0] < len(self._table)
                and 0 <= index_pair[1] < len(self._table[0])):
            raise IndexError('недопустимые значения индексов')

    @staticmethod
    def _is_value_type_correct(
            value: Any,
            allowed_types: type | tuple[type, ...] = (int, float)
    ) -> bool:
        return isinstance(value, allowed_types)

    def _check_table(self, matrix: list[list[float]]):
        reference_length = len(matrix[0])
        is_table_rectangular = all(
            len(row) == reference_length for row in matrix
        )
        are_all_elements_numbers = all(
            all(self._is_value_type_correct(e) for e in row)
            for row in matrix
        )
        if not (is_table_rectangular and are_all_elements_numbers):
            raise TypeError('список должен быть прямоугольным, '
                            'состоящим из чисел')

    @staticmethod
    def _check_table_params(*args):
        rows, cols, fill_value = args
        if not (all(isinstance(arg, int) for arg in (rows, cols))
                and isinstance(fill_value, (int, float))):
            raise TypeError('аргументы rows, cols - целые числа; '
                            'fill_value - произвольное число')
