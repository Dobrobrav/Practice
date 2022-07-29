from math import sqrt


class Line:
    x1: float
    y1: float
    x2: float
    y2: float
    _length: float

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        if sqrt((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) < 1:
            return 0
        return 1
