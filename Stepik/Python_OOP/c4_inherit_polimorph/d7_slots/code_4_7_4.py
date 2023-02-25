class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio: str, old: int, job: str):
        self._fio = fio
        self._old = old
        self._job = job


if __name__ == '__main__':
    persons = [
        Person('Суворов', 52, 'полководец'),
        Person('Рахманинов', 50, 'пианист, композитор'),
        Person('Балакирев', 34, 'программист и преподаватель'),
        Person('Пушкин', 32, 'поэт и писатель'),
    ]
