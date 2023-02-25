from typing import List


class Student:
    _fio: str
    _group: str
    _lect_marks: List[int]
    _house_marks: List[int]

    def __init__(self, fio: str, group: str):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark: int):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark: int):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; " \
               f"оценки за д/з: {str(self._house_marks)}"


class Mentor:
    _fio: str
    _subject: str

    def __init__(self, fio: str, subject: str):
        self._fio = fio
        self._subject = subject


# здесь продолжайте программу
class Lector(Mentor):
    def __init__(self, fio: str, subject: str):
        super().__init__(fio, subject)

    def __str__(self):
        return f"Лектор {self._fio}: предмет {self._subject}"

    @staticmethod
    def set_mark(student: Student, mark: int):
        student.add_lect_marks(mark)


class Reviewer(Mentor):
    def __init__(self, fio: str, subject: str):
        super().__init__(fio, subject)

    @staticmethod
    def set_mark(student: Student, mark: int):
        student.add_house_marks(mark)

    def __str__(self):
        return f"Эксперт {self._fio}: предмет {self._subject}"
