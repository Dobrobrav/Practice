class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000
    __a: float
    __b: float
    __c: float

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        super().__setattr__(key, value)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: float) -> None:
        if self._check_num(a):
            self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: float) -> None:
        if self._check_num(b):
            self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c: float) -> None:
        if self._check_num(c):
            self.__c = c

    @classmethod
    def _check_num(cls, value: float) -> bool:
        return (type(value) in (int, float)
                and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION)


if __name__ == '__main__':
    d = Dimensions(True, 20.1, 30)
    d.a = 11
    d.b = 15
    a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
    print(a, b, c)
    # d.MAX_DIMENSION = 10  # исключение AttributeError
