from typing import List


class Telecast:
    __id: int
    __name: str
    __duration: int

    def __init__(self, id: int, name: str, duration: int):
        self.uid = id
        self.name = name
        self.duration = duration

    @property
    def uid(self) -> int:
        return self.__id

    @uid.setter
    def uid(self, id: int) -> None:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int) -> None:
        self.__duration = duration


class TVProgram:
    name: str
    items: List[Telecast]

    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add_telecast(self, tl: Telecast) -> None:
        self.items.append(tl)

    def remove_telecast(self, indx: int) -> None:
        for telecast in self.items:
            if telecast.uid == indx:
                self.items.remove(telecast)
                return


if __name__ == '__main__':
    pr = TVProgram("Первый канал")
    pr.add_telecast(Telecast(1, "Доброе утро", 10000))
    pr.add_telecast(Telecast(2, "Новости", 2000))
    pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
    for t in pr.items:
        print(f"{t.name}: {t.duration}")
