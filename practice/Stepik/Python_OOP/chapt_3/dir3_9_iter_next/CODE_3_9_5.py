from typing import Union


class Person:
    fio: str
    job: str
    old: int
    salary: float
    year_job: int
    _attr_name_by_index = ('fio', 'job', 'old', 'salary', 'year_job')
    _current_iter_index = 0

    def __init__(self, fio: str, job: str, old: int,
                 salary: float, year_job: int):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __setitem__(self, key: int, value: Union[float, str]):
        self._check_index(key)
        setattr(self, self._attr_name_by_index[key], value)

    def __getitem__(self, item: int) -> Union[float, str]:
        self._check_index(item)
        return getattr(self, self._attr_name_by_index[item])

    def __iter__(self) -> 'Person':
        self._current_iter_index = 0
        return self

    def __next__(self):
        try:
            self._check_index(self._current_iter_index)
        except IndexError:
            raise StopIteration

        attr_name = self._attr_name_by_index[self._current_iter_index]
        ret_value = getattr(self, attr_name)
        self._current_iter_index += 1

        return ret_value

    def _check_index(self, index: int):
        if not (type(index) is int
                and 0 <= index < len(self._attr_name_by_index)):
            raise IndexError('неверный индекс')
