from abc import ABC, abstractmethod
from itertools import count


class Model(ABC):
    @abstractmethod
    def get_pk(self) -> int:
        ...

    @staticmethod
    def get_info() -> str:
        return "Базовый класс Model"


class ModelForm(Model):
    _login: str
    _password: str
    _current_id = count(1)

    def __init__(self, login: str, password: str):
        self._id = next(self._current_id)
        self._login = login
        self._password = password

    def get_pk(self) -> int:
        return self._id


if __name__ == '__main__':
    form = ModelForm("Логин", "Пароль")
    print(form.get_pk())
