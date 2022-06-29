from random import randint, choice
from typing import TypeAlias


Password: TypeAlias = str


class RandomPassword:
    """ Class for generating passwords """

    _psw_chars: str
    _min_length: int
    _max_length: int

    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self._psw_chars = psw_chars
        self._min_length = min_length
        self._max_length = max_length

    def __call__(self, *args, **kwargs) -> Password:
        psw_length = randint(self._min_length, self._max_length)
        generated_psw = ''.join(
            choice(self._psw_chars) for _ in range(psw_length)
        )
        return generated_psw


if __name__ == '__main__':
    min_length = 5
    max_length = 20
    psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

    rnd = RandomPassword(psw_chars, min_length, max_length)
    lst_pass = [rnd() for _ in range(3)]
    print(lst_pass)

