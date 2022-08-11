from math import sqrt


class TriangleSide:
    """ Descriptor for triangle side.
    Values must be positive numeric type (if not, ValueError is raised).
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError('длины сторон треугольника '
                             'должны быть положительными числами')
        self.value = value

    def __get__(self, instance, owner):
        return self.value


class Triangle:
    """ Class that represents triangle.

    Attributes
    ----------
    a, b, c -  triangle sides (TriangleSide descriptor)

    Methods
    -------
    len(self) - return int(perimetr)
    self() - return approximate area or triangle (due to ~perimetr)

    Raises
    ------
    ValueError
        if there is a combination in which one of the sides
        is bigger than the other two combined
    Errors from TriangleSide descriptor
    """

    a = TriangleSide()
    b = TriangleSide()
    c = TriangleSide()

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        current_sides = ['a', 'b', 'c']
        current_sides.remove(key)

        if hasattr(self, current_sides[0]) and hasattr(self, current_sides[1]):
            first = getattr(self, current_sides[0])
            second = getattr(self, current_sides[1])
            new = value

            if (first > second + new or second > new + first
                    or new > first + second):
                raise ValueError('с указанными длинами нельзя '
                                 'образовать треугольник')

        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs) -> float:
        a, b, c, p = self.a, self.b, self.c, len(self) / 2
        area = sqrt((p * (p - a) * (p - b) * (p - c)))
        return area


if __name__ == '__main__':
    triangle = Triangle(3, 2, 3)
    print(triangle())
    print(len(triangle))
