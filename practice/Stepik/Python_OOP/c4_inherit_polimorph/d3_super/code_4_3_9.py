class StringDigit(str):
    def __init__(self, string: str):
        self._validate_string(string)

    def __add__(self, other: str) -> 'StringDigit':
        self._validate_string(other)
        str_result = super(StringDigit, self).__add__(other)
        string_digit_result = self.__class__(str_result)
        return string_digit_result

    def __radd__(self, other: str) -> 'StringDigit':
        return self.__class__(other) + self

    def _validate_string(self, string: str):
        self._check_if_string(string)
        self._check_if_only_digits(string)

    @staticmethod
    def _check_if_only_digits(string: str):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")

    @staticmethod
    def _check_if_string(value: str):
        if not isinstance(value, str):
            raise TypeError('входные данные должны быть строкой')
