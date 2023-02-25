from typing import Iterator


def main():
    ceiling = int(input())
    get_sum_up_to = gen_sum_up_to(ceiling)
    for num in get_sum_up_to:
        print(num, end=' ')
    print()


def gen_sum_up_to(ceiling: int) -> Iterator[int]:
    """
    yield sum up to ceiling value.
    Example: ceiling = 5 => yield: 1; 3; 6; 10; 15
    """
    _validate_n(ceiling)

    sum_ = 0
    for natural in range(1, ceiling + 1):
        sum_ += natural
        yield sum_


def _validate_n(n: int):
    if type(n) is not int:
        raise TypeError('ceiling value must be int.')
    if n < 1:
        raise ValueError('ceiling value must be >= 1.')


if __name__ == '__main__':
    main()
