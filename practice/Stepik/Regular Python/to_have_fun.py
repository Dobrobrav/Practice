from random import randint, choice
from typing import Callable, TypeAlias


Password: TypeAlias = str


def random_password(psw_chars: str, min_length: int,
                    max_length: int) -> Callable[[], Password]:
    def wrapper():
        psw_length = randint(min_length, max_length)
        generated_psw = ''.join(
            choice(psw_chars) for _ in range(psw_length)
        )
        return generated_psw

    return wrapper


if __name__ == '__main__':
    min_length = 5
    max_length = 20
    psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

    rnd = random_password(psw_chars, min_length, max_length)
    lst_pass = [rnd() for _ in range(3)]
    print(lst_pass)
