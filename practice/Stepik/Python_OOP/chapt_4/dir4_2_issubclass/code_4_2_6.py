from typing import Iterable


class Tuple(tuple):
    def __add__(self, other: Iterable):
        return Tuple(super().__add__(tuple(other)))


if __name__ == '__main__':
    tp = Tuple()
    print(type(tp))
    print(type(tp + "sldkfjj"))

