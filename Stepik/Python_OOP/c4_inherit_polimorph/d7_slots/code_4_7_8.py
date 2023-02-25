class Function:
    def __init__(self):
        self._amplitude = 1.0  # амплитуда функции
        self._bias = 0.0  # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть '
                                  'переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj

    # здесь добавляйте еще один магический метод для умножения


# здесь объявляйте класс Linear
class Linear(Function):
    _k: float
    _b: float

    def __init__(self, *args):
        super().__init__()
        try:
            self._k = args[0]._k
            self._b = args[0]._b
        except AttributeError:
            self._k, self._b = args

    def _get_function(self, x):
        return self._k * x + self._b
