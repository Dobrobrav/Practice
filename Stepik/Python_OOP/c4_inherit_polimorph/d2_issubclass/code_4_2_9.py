from typing import Tuple


class IteratorAttrs:
    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value


class SmartPhone(IteratorAttrs):
    model: str
    size: Tuple[float, float]
    memory: int

    def __init__(self, model: str, size: Tuple[float, float], memory: int):
        self.model = model
        self.size = size
        self.memory = memory


if __name__ == '__main__':
    print(SmartPhone.__mro__)
