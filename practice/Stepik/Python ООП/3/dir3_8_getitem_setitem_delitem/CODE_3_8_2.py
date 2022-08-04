from typing import Tuple


class Record:
    _key_by_id: Tuple[str, ...]

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._key_by_id = tuple(kwargs)

    def __getitem__(self, item: int):
        self._check_index(item)
        return getattr(self, self._key_by_id[item])

    def __setitem__(self, key: int, value: str):
        self._check_index(key)
        setattr(self, self._key_by_id[key], value)

    def _check_index(self, index: int):
        if not ((isinstance(index, int)
                 and 0 <= index <= len(self._key_by_id) - 1)):
            raise IndexError('неверный индекс поля')
