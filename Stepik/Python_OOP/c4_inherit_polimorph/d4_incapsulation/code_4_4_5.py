class Animal:
    __name: str
    __kind: str
    __old: int

    def __init__(self, name: str, kind: str, old: int):
        self.name = name
        self.kind = kind
        self.old = old

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def old(self) -> int:
        return self.__old

    @old.setter
    def old(self, old: int):
        self.__old = old


if __name__ == '__main__':
    animals = [
        Animal('Васька', 'дворовый кот', 5),
        Animal('Рекс', 'немецкая овчарка', 8),
        Animal('Кеша', 'попугай', 5),
    ]
