from typing import Iterable


class MyTuple(tuple):
    def __add__(self, other: Iterable):
        return MyTuple(super().__add__(tuple(other)))


if __name__ == '__main__':
    tp = MyTuple()
    print(type(tp))
    print(type(tp + "sldkfjj"))

