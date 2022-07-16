from typing import Union


class Point:
    _x: int | str
    _y: int | str

    def __init__(self, x, y):
        print(type(self.__annotations__.get("_x")))
        self._x = x
        self._y = y

    def __setattr__(self, key, value):
        if type(value) not in self.__annotations__.get(key):
            raise TypeError("You are so wrong now, you can't even imagine..")


if __name__ == '__main__':
    point = Point(1, 2)
    print(point.__annotations__)

