from typing import List


class LessonItem:
    """ Lesson in module"""

    title: str
    practices: int
    duration: int

    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if (not isinstance(value, self.__annotations__[key])
                or isinstance(value, bool)):
            raise TypeError("Неверный тип присваиваемых данных.")

        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ("title", "practices", "duration"):
            pass


class Module:
    """ Module of lessons in course"""

    name: str
    lessons: List[LessonItem]

    def __init__(self, name: str):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: LessonItem) -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        self.lessons.pop(indx)


class Course:
    """ Educational course containing modules of lessons """

    name: str
    modules: List[Module]

    def __init__(self, name: str):
        self.name = name
        self.modules = []

    def add_module(self, module: Module) -> None:
        self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        self.modules.pop(indx)


if __name__ == '__main__':
    course = Course("Python ООП")
    module_1 = Module("Часть первая")
    module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
    module_1.add_lesson(LessonItem("Урок 3", 5, 800))
    course.add_module(module_1)
    module_2 = Module("Часть вторая")
    module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
    course.add_module(module_2)

    print(course.__dict__)