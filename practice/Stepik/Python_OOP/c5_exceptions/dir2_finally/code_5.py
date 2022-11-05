def main():

    input_values = input().split()
    pt = Point()

    try:
        a, b = [int(x) for x in input_values]
        pt = Point(a, b)
    except ValueError:
        try:
            a, b = [float(x) for x in input_values]
        except ValueError:
            pass
    finally:
        print(f"Point: x = {pt.x}, y = {pt.y}")


class Point:
    _x: float
    _y: float

    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y


if __name__ == '__main__':
    main()
