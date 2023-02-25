def main():
    input_data = [
        (1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2),
        (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6),
    ]

    lst_tr = []
    for sides in input_data:
        try:
            lst_tr.append(Triangle(*sides))
        except (ValueError, TypeError):
            continue


class Triangle:
    _a: float
    _b: float
    _c: float

    def __init__(self, a: float, b: float, c: float):
        self._validate_sides(a, b, c)
        self._a = a
        self._b = b
        self._c = c

    def _validate_sides(self, a: float, b: float, c: float):
        self._check_if_positives(a, b, c)
        self._check_if_triangle(a, b, c)

    @staticmethod
    def _check_if_positives(a: float, b: float, c: float):
        if any(type(val) not in (int, float) or val <= 0
               for val in (a, b, c)):
            raise TypeError('стороны треугольника должны быть положительными числами')

    @staticmethod
    def _check_if_triangle(a: float, b: float, c: float):
        if a + b < c or b + c < a or c + a < b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')


if __name__ == '__main__':
    main()
