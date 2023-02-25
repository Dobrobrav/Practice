def main():
    circle = Circle(10.5, 7, 22)
    circle.radius = ---10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
    x, y = circle.x, circle.y
    res = circle.name  # False, т.к. атрибут name не существует
    print(res)
    print(x, y, circle.radius)


class Circle:
    __x: float
    __y: float
    __radius: float

    def __init__(self, x: float, y: float, radius: float) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        print(self.__annotations__)

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float) -> None:
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float) -> None:
        self.__y = y

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float) -> None:
        if radius <= 0:
            return
        self.__radius = radius

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        super(Circle, self).__setattr__(key, value)

    def __getattr__(self, item) -> False:
        return False


if __name__ == '__main__':
    main()
