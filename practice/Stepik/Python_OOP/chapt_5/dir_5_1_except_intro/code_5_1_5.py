def main():
    pt = Point(1, 2)

    try:
        print(pt.z)
    except AttributeError:
        print("Атрибут с именем z не существует")


class Point:
    _x: float
    _y: float

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y


if __name__ == '__main__':
    main()
