class Dimensions:
    """ Class that represents dimensions of physical bodies.

    Attributes
    ----------
    a, b, c: dimensions - must be positive (if not, ValueError is raised)

    Instances of the class with the same a, b, c have the same hash.
    """

    a: float
    b: float
    c: float

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ('a', 'b', 'c') and value <= 0:
            raise ValueError('габаритные размеры должны быть положительными числами')
        super().__setattr__(key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __repr__(self):
        return f"{self.a}-{self.b}-{self.c}"


if __name__ == '__main__':
    str_in = input()
    lst_dims = [Dimensions(*(float(dimension) for dimension in line.split()))
                for line in str_in.split('; ')]

    print(sorted(lst_dims, key=hash))


