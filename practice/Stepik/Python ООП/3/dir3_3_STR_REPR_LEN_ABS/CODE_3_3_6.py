class Complex:
    _real: float
    _img: float

    def __init__(self, real: float, img: float):
        self._real = real
        self._img = img

    def __abs__(self) -> float:
        return (self.real ** 2 + self.img ** 2) ** 0.5

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        super().__setattr__(key, value)

    @property
    def real(self) -> float:
        return self._real

    @real.setter
    def real(self, real: float) -> None:
        self._real = real

    @property
    def img(self) -> float:
        return self._img

    @img.setter
    def img(self, img: float) -> None:
        self._img = img


if __name__ == '__main__':
    cmp = Complex(7, 8)
    cmp.real = 3
    cmp.img = 4
    c_abs = abs(cmp)
